import os
import hubspot
from datetime import datetime
import json
import requests as rq
import logging
from packages.schema import Schema
from packages.config import Config
from packages.s3_resource import S3
from packages.redshift_resource import Redshift
from dateutil import parser


logging.basicConfig(level=logging.INFO)  # verbose logging
logger = logging.getLogger(__name__)

class Hubspot:
    def __init__(self, api_key):
        self.client = hubspot.HubSpot(api_key=api_key)
        self.api_key = api_key
        self.params = {
            "hapikey": self.api_key,
            "limit": 100
        }
        self.headers = {"Content-Type": "application/json"}

    def check_limits(self, call):
        daily_limit = 500000
        headers = call.headers
        daily_calls_left = int(headers['X-HubSpot-RateLimit-Daily-Remaining'])
        if daily_calls_left <= 200000:
            raise ValueError('Reached our 200,000 call limit.')

    def _flatten_properties(self, data, sdk_pulled=True):
        new_data = []
        for record in data:
            if sdk_pulled:
                dict_record = record.to_dict()
            else:
                dict_record = record

            for k, v in dict_record['properties'].items():
                dict_record[k] = v
            del dict_record['properties']
            new_data.append(dict_record)
        return new_data

    def get_filter(self, last_updated, properties, audit_col):
        filter_groups = {
            
            "filterGroups":[
            {
                "filters":[
                {
                    "propertyName": audit_col,
                    "operator": "GT",
                    "value": last_updated
                }
                ]
            }
            ],
            "sorts": [
                {
                    "propertyName": audit_col,
                    "direction": "ASCENDING"
                }
            ],
            "properties": properties,
            "limit": 100,
        }

        return filter_groups
        
    def get_engagements(self, table, filter_ms, audit_col):
        additional_data = False
        all_records = []
        properties = [x['name'] for x in self.get_object_properties(table)]
        filter_data = self.get_filter(filter_ms, properties, audit_col[0])

        filter_json = json.dumps(filter_data)
        url = f'https://api.hubspot.com/crm/v3/objects/{table}' + '/search'
        data = rq.post(url, params=self.params, data=filter_json, headers=self.headers)

        data.raise_for_status()
        records = json.loads(data.content)
        all_records.append(self._flatten_properties(records['results'], sdk_pulled=False))
        while 'paging' in records.keys():
            filter_data['after'] = records['paging']['next']['after']
            if filter_data['after'] == '10000':
                logger.info(f"Can only pull 10000 pages at a time. Run again to get next batch for {table}")
                additional_data=True
                break
            logger.info(f"Pulling data after: {filter_data['after']}")
            filter_json = json.dumps(filter_data)
            data = rq.post(url, params=self.params, data=filter_json, headers=self.headers)
            data.raise_for_status()
            self.check_limits(data)
            records = json.loads(data.content)
            all_records.append(self._flatten_properties(records['results'], sdk_pulled=False))

        return [item for sublist in all_records for item in sublist], additional_data

    def get_pipelines(self):
        return self.client.crm.pipelines.pipelines_api.get_all('deals').to_dict()['results']

    def get_contacts(self):
        properties = [x['name'] for x in self.get_object_properties('contacts')]
        return self._flatten_properties(self.client.crm.contacts.get_all(properties=properties))

    def get_deals(self):
        properties = [x['name'] for x in self.get_object_properties('deals')]
        return self._flatten_properties(self.client.crm.deals.get_all(properties=properties))

    def get_companies(self):
        return self.client.crm.companies.get_all()

    def get_object_properties(self, object_name):
        return self.client.crm.properties.core_api.get_all(object_name).to_dict()['results']

    def get_object_data(self, object_name):
        object_map = {
            'contacts': self.get_engagements,
            'deals': self.get_engagements
        }
        if object_map.get(object_name):
            return object_map[object_name](object_name)
        else:
            raise ValueError(f"unsupported object {object_name}")


class RedshiftHubspotSyncer:
    def __init__(self, s3, redshift, hubspot, target_schema):
        self.s3 = s3
        self.redshift = redshift
        self.hubspot = hubspot
        self.schema = Schema(target_schema)
        self.extract_ts = datetime.utcnow()
        self.s3_prefix = target_schema
        self.objects = [
            'contacts',
            'deals'
        ]
        self.redshift.createSchema(self.schema)

    def get_latest_extract(self, table_name, init=False):
        audit_cols = self.schema.schema_def[table_name].get('audit_cols')
        if not audit_cols:
            return None

        if init:
            ts = datetime(2019, 1, 1).timestamp()
            return str(ts).split('.')[0] + '000', audit_cols

        audit_col_str = audit_cols[0] if len(audit_cols) == 1 else f'GREATEST({",".join(audit_cols)})'
        query = """
            SELECT MAX({})
            FROM {}.{}
        """.format(
            audit_col_str,
            self.schema.name,
            table_name
        )
        max_extract = self.redshift.executeQuery(query)[0]
        
        if max_extract[0]:
            ts = max_extract[0].timestamp()
        else:
            ts = datetime(2019, 1, 1).timestamp()
        return str(ts).split('.')[0] + '000', audit_cols


    def get_data(self, table_name, filter_ms, audit_col):
        all_data = []
        data, additional_data = self.hubspot.get_engagements(table_name, filter_ms, audit_col)
        all_data.append(data)

        while additional_data:
            audit_dates = [parser.parse(x[audit_col[0]]) for x in data]
            logger.info(f"Pulling new data as of: {max(audit_dates)}")
            filter_ms = str(max(audit_dates).timestamp() * 1000).split('.')[0]
            data, additional_data = self.hubspot.get_engagements(table_name, filter_ms, audit_col)
            all_data.append(data)

        return [item for sublist in all_data for item in sublist]

    def sync_table(self, table_name, init=False):
        s3_path = f"{self.s3_prefix}/{table_name}/{datetime.utcnow().isoformat()}"
        field_names = self.schema.getTableFields(table_name)
        filter_ms, audit_col = self.get_latest_extract(table_name, init)
        data = self.get_data(table_name, filter_ms, audit_col)

        clean_data = [{k: v for k, v in row.items() if k in field_names} for row in data]

        self.s3.stream_dict_writer(clean_data, field_names, s3_path)
        # # TODO: Just doing fulls for now
        if init:
            self.redshift.createTable(self.schema, table_name)
            self.redshift.truncate(self.schema, table_name)
            self.redshift.appendFromS3(self.schema, table_name, 's3://' + self.s3.bucket + '/' + s3_path)

        else:
            self.redshift.upsertFromS3(self.schema, table_name, 's3://' + self.s3.bucket + '/' + s3_path)

    def sync(self):
        for object in self.objects:
            self.sync_table(object)


if __name__ == '__main__':
    TARGET_SCHEMA = 'hubspot'
    config = Config('config/config.yaml').getConfigObject()
    redshift_client = Redshift(**config['Resources']['redshift'])
    s3_client = S3(**config['Resources']['s3'])
    hubspot_client = Hubspot(**config['Resources']['hubspot'])
    syncer = RedshiftHubspotSyncer(s3_client, redshift_client, hubspot_client, TARGET_SCHEMA)
    syncer.sync()

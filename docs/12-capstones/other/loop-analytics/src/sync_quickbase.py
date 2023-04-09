from asyncio import create_subprocess_shell
import json
import logging
# from turtle import update
import requests as rq
import json
import pandas as pd
import os
import re

from jinja2 import Template
from datetime import datetime

from packages.schema import Schema
from packages.s3_resource import S3
from packages.config import Config
from packages.redshift_resource import Redshift
from pandas.api.types import is_datetime64_any_dtype as is_datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Quickbase:
    def __init__(self, config):
        self.quick_config = config['Resources']['quickbase']
        self.headers = {
            "Authorization": "QB-USER-TOKEN " + self.quick_config['access_token'],
            "QB-Realm-Hostname": self.quick_config['QB-Realm-Hostname'],
            "User-Agent": "zach.bolian@dvx.ventures",
            "Content-Type": "application/json"
        }
        self.params = {
            'appId': self.quick_config['appId']
        }

        self.base_table_url = 'https://api.quickbase.com/v1/tables/'

    def pull_table_fields(self, table_name):
        """
        Pull Table from quickbase
        """
        table_id = self.quick_config['tables'][table_name]['table_id']
        url = 'https://api.quickbase.com/v1/fields'
        self.params['tableId'] = table_id

        response = rq.get(
            url=url, 
            params = self.params, 
            headers = self.headers
        )
        
        assert response.status_code == 200  # errors give 207
        
        fields = json.loads(response.content)

        return fields, table_id

    def gen_qb_yaml(self, table_name):
        fields, _ = self.pull_table_fields(table_name)
        field_type = {re.sub(r'[^\w\s]', '', i['label']).lower().replace(' ', '_'): i['fieldType'] for i in fields}
        field_type_final = {}
        for key in field_type.keys():
            new_key = key.replace('__', '_')
            field_type_final[new_key] = field_type[key]

        for i in field_type_final.keys():
            print(f"- name: {i}")

            if field_type_final[i] in ('text', 'timestamp'):
                print(f"  type: {field_type_final[i]}")
            else:
                print("  type: text")

    def pull_table_data(self, table_name):
        url = 'https://api.quickbase.com/v1/records/query'
        fields, table_id = self.pull_table_fields(table_name)
        field_map = {i['id']: re.sub(r'[^\w\s]', '', i['label']).lower().replace(' ', '_') for i in fields}
        field_type = {re.sub(r'[^\w\s]', '', i['label']).lower().replace(' ', '_'): i['fieldType'] for i in fields}

        query = self.gen_query(table_id, field_map)

        response = rq.post(
            url=url, 
            data = query, 
            headers = self.headers
        )
        response.raise_for_status()

        records = json.loads(response.content)
        data = records['data']
        parsed_data = self.parse_data(data, field_map, field_type)

        return parsed_data

    def parse_data(self, data, field_map, field_type):
        parsed_data = []
        for rec in data:
            new_rec = {}
            for key_id in rec.keys():
                if isinstance(rec[key_id]['value'], dict):
                    field = field_map[int(key_id)]
                    if field_type[field] == 'file':
                        new_rec[field_map[int(key_id)].replace('__', '_')] = rec[key_id]['value']['url']
                    else:
                        new_rec[field_map[int(key_id)].replace('__', '_')] = rec[key_id]['value']['id']
                else:
                    new_rec[field_map[int(key_id)].replace('__', '_')] = rec[key_id]['value']

            parsed_data.append(new_rec)

        return parsed_data

    def gen_query(self, table_id, field_map):
        query = {
            "from": table_id,
            "select": list(field_map.keys())
        }

        query = json.dumps(query)

        return query

    def write_to_table(self, table_name, df):
        mode = self.quick_config['tables'][table_name]['mode']

        if mode == 'full':
            self.full_replace(table_name, df)
        elif mode == 'upsert':
            self.insert_records(table_name, df)
        else:
            raise ValueError(f"invalid mode {mode}")

    def get_table_metadata(self, table_name):
        url = 'https://api.quickbase.com/v1/records'
        fields, table_id = self.pull_table_fields(table_name)

        field_map = {re.sub(r'[^\w\s]', '', i['label']).lower().replace(' ', '_').replace('__', '_'): i['id'] for i in fields}
        return url, fields, table_id, field_map

    def insert_records(self, table_name, df):
        url, fields, table_id, field_map = self.get_table_metadata(table_name)

        # fix timestamps
        for dcol in ['created_at', 'updated_at']:
            if dcol in df.columns:
                try:
                    df[dcol] = pd.to_datetime(df[dcol]).dt.strftime('%Y-%m-%dT%H:%M:%SZ')
                except:
                    pass

        # fix booleans
        mask = df.applymap(type) != bool
        d = {True: 'true', False: 'false'}
        df = df.where(mask, df.replace(d))

        upload_data = self.prep_qb_upload(table_name, field_map, df)

        response = rq.post(
            url=url, 
            data = upload_data, 
            headers = self.headers
        )
       
        assert response.status_code == 200  # errors give 207

    def truncate_table(self, table_name):
        url, fields, table_id, field_map = self.get_table_metadata(table_name)

        record_id = field_map['record_id']

        delete_response = rq.delete(
            url=url,
            data = json.dumps({
                "from": table_id,
                "where": "{" + f"{record_id}" + ".GT.0}"
            }), 
            headers = self.headers
        )

        assert delete_response.status_code == 200  # errors give 207

    def full_replace(self, table_name, df):
        url, fields, table_id, field_map = self.get_table_metadata(table_name)
        self.truncate_table(table_name)
        self.insert_records(table_name, df)

    def prep_qb_upload(self, table_name, field_map, df):
        fields, table_id = self.pull_table_fields(table_name)
        upload_data = {"to": table_id, "data": []}
        qb_default_fields = set(['Date Created', 'Date Modified', 'Record ID#', 'Record Owner', 'Last Modified By'])
        df = df[[x['label'] for x in fields if x['label'] not in qb_default_fields and x['label'] in df.columns]]  # subset to dest fields - note, requires that names match

        df_dict = df.to_dict(orient='records')
        for row in df_dict:
            new_row = {}
            for col in row.keys():
                new_row[field_map[col]] = {"value": str(row[col])}

            upload_data['data'].append(new_row)

        upload_data = json.dumps(upload_data)
        upload_data = upload_data.replace('"None"', '""').replace('"NaT"', '""').replace('"NaN"', '""')

        return upload_data 
            

class RedshiftQuickbaseSyncer:
    def __init__(self, s3, redshift, quickbase, target_schema):
        self.s3 = s3
        self.redshift = redshift
        self.quickbase = quickbase
        self.schema = Schema(target_schema)
        self.extract_ts = datetime.utcnow()
        self.s3_prefix = target_schema

        self.redshift.createSchema(self.schema)

    def sync_table(self, table_name):
        if table_name:
            table_name = [table_name]
        else:
            table_name = list(self.schema.schema_def.keys())

        for tn in table_name:
            logger.info(f"Loading data into: {tn}")
            s3_path = f"{self.s3_prefix}/{tn}/{datetime.utcnow().isoformat()}"
            field_names = self.schema.getTableFields(tn)
            data = self.quickbase.pull_table_data(tn)
            if data: 
                qb_fields = set(data[0].keys())
                clean_data =  [{k: v for k, v in row.items() if k in field_names} for row in data]
                if len(qb_fields - set(field_names)) > 0:
                    logger.info(f"Missing qb field(s): {qb_fields - set(field_names)} from: {tn}.yaml")

                self.s3.stream_dict_writer(clean_data, field_names, s3_path)
                # Fulls only for QB
                self.redshift.createTable(self.schema, tn)
                self.redshift.truncate(self.schema, tn)
                self.redshift.appendFromS3(self.schema, tn, 's3://' + self.s3.bucket + '/' + s3_path)

    def dw_to_quickbase(self, schema_name, dw_table_name, qb_table_name):
        df = self.redshift.table_to_df(schema_name, dw_table_name)
        self.quickbase.write_to_table(qb_table_name, df)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--qb_table_name", "-qbtb", help="Table name")
    parser.add_argument("--to_dw", "-dw", action='store_true', help="Table name")
    parser.add_argument("--to_quickbase", "-qb", action='store_true', help="Table name")
    parser.add_argument("--schema_name", "-sc", help="Table name")
    parser.add_argument("--dw_table_name", "-dwtb", help="Table name")

    args = parser.parse_args()

    qb_table_name = args.qb_table_name if args.qb_table_name else None

    TARGET_SCHEMA = 'quickbase'
    config = Config('config/config.yaml').getConfigObject()
    redshift_client = Redshift(**config['Resources']['redshift'])
    s3_client = S3(**config['Resources']['s3'])
    quickbase_client = Quickbase(config)
    syncer = RedshiftQuickbaseSyncer(s3_client, redshift_client, quickbase_client, TARGET_SCHEMA)

    if args.to_dw:
        syncer.sync_table(qb_table_name)

    if args.to_quickbase:
        syncer.dw_to_quickbase(args.schema_name, args.dw_table_name, qb_table_name)

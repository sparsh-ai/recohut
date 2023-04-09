import json
import logging
import requests as rq
import time
import json
import pandas as pd

import datetime

from packages.schema import Schema
from packages.config import Config
from packages.s3_resource import S3
from packages.redshift_resource import Redshift


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Ip_Extractor:
    def __init__(self):
        config = Config('config/config.yaml').getConfigObject()
        self.schema = Schema('ip_api')
        self.table_name = 'ip_location'
        ip_config = config['Resources']['ip_api']
        self.table_cols = self.schema.getTableFields('ip_location')
        

        self.bucket = config['Resources']['s3']['bucket']
        self.s3_prefix = ip_config['s3_prefix']


        rs_config = config['Resources']['redshift']
        self.rs = Redshift(
                user=rs_config['user'],
                password=rs_config['password'],
                host=rs_config['host'],
                port=rs_config['port'],
                database=rs_config['database']
            )

        self.endpoint = "http://ip-api.com/batch?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query"

    def pull_missing_ips(self):
        query = """
            select distinct 
                context_ip
            from dw.fact_web_activity fwa 
            left join ip_api.ip_location il
                on il.ip_id = fwa.context_ip
            where fwa.session_start_ts >= CURRENT_DATE + INTERVAL '-1 day'
            AND il.ip_id is null;
        """
        ips = [rec[0] for rec in self.rs.executeQuery(query)]
        data = [
            {
                "query": ip,
                "fields": 'status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query',
                "lang": 'en'
            } for ip in ips
        ]

        logger.info(f"Found {len(data)} IP records without region data")

        return data

    def pull_ip_info(self, ips_batch_json):
        response_cols = self.table_cols

        # need to rename ID field to match call json
        response_cols[0] = 'query'
        response_cols[-1] = 'as'
        
        req = rq.post(self.endpoint, data = ips_batch_json)
        req.raise_for_status()

        sucessful_pulls = []
        errors = []

        for r in req.json():
            if r['status'] == 'success':
                good_pull = {}
                for col in response_cols:
                    good_pull[col] = r[col] if col in r.keys() else ''
                sucessful_pulls.append(good_pull)
            else:
                errors.append(r)

        logger.info(f"Pulled {len(sucessful_pulls)} successful records and {len(errors)} failed records")

        return sucessful_pulls

    def process_missing_ips(self, ip_list):
        all_ip_info = []
        for i in range(0, len(ip_list), 100):
            logger.info(f"Pulling IPs from {i} to {i + 100} our of {len(ip_list)} total records")
            ip_group = self.pull_ip_info(json.dumps(ip_list[i:i+100]))
            all_ip_info.append(ip_group)

            time.sleep(10)

        flat_ip_list = [list(item.values()) for sublist in all_ip_info for item in sublist]
        logger.info(f"Total successful records pulled: {len(flat_ip_list)}")

        return flat_ip_list

    def create_ip_table(self, table_name):
        self.rs.createSchema(self.schema)
        self.rs.createTable(self.schema, table_name)

    def load_data(self, data, table_name):
        extract_ts = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        out_prefix = '{}/{}'.format(self.s3_prefix, extract_ts)
        s3 = S3(self.bucket)
        s3.stream_writer(data, out_prefix)

        s3_path = 's3://{}/{}/part'.format(self.bucket, out_prefix)
        self.rs.upsertFromS3(self.schema, table_name, s3_path)

    def update_ip_table(self, init=False):
        self.create_ip_table(self.table_name)
        ips = self.pull_missing_ips()
        data = self.process_missing_ips(ips)
        self.load_data(data, self.table_name)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    ip_load = Ip_Extractor()
    ip_load.update_ip_table()
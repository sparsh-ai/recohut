import os
import pandas as pd
import requests as rq
from retrying import retry
from datetime import datetime

from packages.schema import Schema
from packages.s3_resource import S3
from packages.redshift_resource import Redshift
from packages.config import Config


class reviewsio:
    def __init__(self, store, apikey):
        self.url = 'https://api.reviews.io'
        self.apikey = apikey
        self.store = store

    def _make_request_params(self, page, res_per_page):
        return {
            'store': self.store,
            'apikey': self.apikey,
            'page': page,
            'per_page': res_per_page
        }

    @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
    def _make_request(self, endpoint, params):
        req = rq.get(self.url + endpoint, params=params)
        req.raise_for_status()
        return req.json()

    def get_merchant_reviews(self):
        res_per_page = 1000
        page = 0
        all_data = []
        while True:
            params = self._make_request_params(page, res_per_page)
            req_data = self._make_request('/merchant/reviews', params)
            current_page = int(req_data['page'])
            total_pages = req_data['total_pages']
            all_data += req_data['reviews']
            if current_page == (total_pages - 1):
                break
            else:
                page += 1
        return all_data


class RedshiftLoader:

    def __init__(self, s3_bucket, s3_prefix, rs_user, rs_password, rs_host, rs_db, rs_port=5439):
        self.db = Redshift(
            user=rs_user,
            password=rs_password,
            host=rs_host,
            port=rs_port,
            database=rs_db
        )

        self.schema = Schema('reviewsio')
        self.db.createSchema(self.schema)
        self.bucket = s3_bucket
        self.s3_prefix = s3_prefix
        self.s3 = S3(self.bucket)
        self.extract_ts = datetime.utcnow()

    def load_data(self, data, table_name):
        self.db.createTable(self.schema, table_name)
        s3_key = '{0}/{1}.gz'.format(self.s3_prefix, self.extract_ts)
        self.s3.upload_df(data, s3_key)
        self.db.truncate(self.schema, table_name)
        self.db.appendFromS3(self.schema, table_name, 's3://{}/{}'.format(self.bucket, s3_key))


def convert_to_df(data: list) -> pd.DataFrame:
    # convert reviews.io payload to a dataframe to
    for record in data:
        for k in ('first_name', 'last_name', 'verified_buyer', 'address', 'email'):
            record["reviewer_" + k] = record['reviewer'].get(k)
        del record['reviewer']
        del record['ratings']
        del record['images']
        del record['tags']
        del record['replies']
    return pd.DataFrame(data)


if __name__ == '__main__':
    TARGET_TABLE = 'reviewsio.merchant_reviews'
    config = Config('config/config.yaml').getConfigObject()

    reviewsio_config = config['Resources']['reviewsio']
    client = reviewsio(reviewsio_config['reviewsio_store'], reviewsio_config['reviewsio_key'])
    merchant_reviews = client.get_merchant_reviews()
    df = convert_to_df(merchant_reviews)

    rs_config = config['Resources']['redshift']
    s3_bucket = config['Resources']['s3']['bucket']
    s3_prefix = 'reviewsio'
    rs = RedshiftLoader(s3_bucket, s3_prefix, rs_config['user'], rs_config['password'], rs_config['host'], rs_config['database'])
    col_order = rs.schema.getTableFields(TARGET_TABLE.split('.')[1])

    rs.load_data(df[col_order], TARGET_TABLE.split('.')[1])

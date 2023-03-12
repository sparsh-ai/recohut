import json
import requests as rq
from retrying import retry
from datetime import datetime

from packages.schema import Schema
from packages.config import Config
from packages.s3_resource import S3
from packages.redshift_resource import Redshift


# TODO: timestamps aren't happy going into redshift like this
# '2021-06-30T14:02:24-07:00'
# putting in as string now and casting later (which doesn't fix for timezone)

class Shopify:
    def __init__(self, shop, api_password) :
        self.shop = shop
        self.header = { 'X-Shopify-Access-Token': api_password }

    # @retry(wait_exponential_multiplier=1000, wait_exponential_max=5000)
    def _get_data(self, object, params={}):
        combined_data = []
        base_url = f"https://{self.shop}.myshopify.com/admin/api/2021-04/{object}.json"
        print(f"fetching data from {base_url}")
        req = rq.get(base_url, headers=self.header, params=params)
        req.raise_for_status()
        combined_data += req.json()[object]
        request_headers = req.headers

        # pagination
        while True:
            url = self._get_next_url(request_headers)
            if url:
                print(f"fetching data from {url}")
                req = rq.get(url, headers=self.header)
                req.raise_for_status()
                combined_data += req.json()[object]
                request_headers = req.headers
            else:
                break

        return combined_data

    def _get_next_url(self, response_header):
        if response_header.get('Link'):
            links = response_header['Link'].split(',')
            raw_link_str = None
            for link in links:
                link_str, rel_str = link.split(';')
                if rel_str.strip() == 'rel="next"':
                    raw_link_str = link_str
            if raw_link_str:
                return raw_link_str[raw_link_str.index('<') + 1:raw_link_str.index('>')]
            else:
                return None
        else:
            return None

    def get_orders(self, last_ts=None):
        return self._get_data('orders', {'status': 'any', 'limit': 250})

    def get_customers(self, last_ts=None):
        return self._get_data('customers', {'status': 'any', 'limit': 250})

    def get_products(self, last_ts=None):
        return self._get_data('products', {'limit': 250})

    def get_line_items(self):
        orders = self.get_orders()
        line_items = []
        for order in orders:
            if order.get('line_items'):
                tmp = order.get('line_items')
                for x in tmp:
                    x['order_id'] = order['id']
                    line_items.append(x)
        return line_items

    def get_variants(self):
        products = self.get_products()
        variants = []
        for product in products:
            if product.get('variants'):
                variants += product.get('variants')
        return variants

    def get_object_data(self, object_name):
        object_map = {
            'customers': self.get_customers,
            'orders': self.get_orders,
            'line_items': self.get_line_items,
            'variants': self.get_variants,
            'products': self.get_products
        }
        if object_map.get(object_name):
            return object_map[object_name]()
        else:
            raise ValueError(f"unsupported object {object_name}")


class RedshiftShopifySyncer:
    def __init__(self, s3, redshift, shopify, target_schema):
        self.s3 = s3
        self.redshift = redshift
        self.shopify = shopify
        self.schema = Schema(target_schema)
        self.extract_ts = datetime.utcnow()
        self.s3_prefix = target_schema
        self.objects = [
            'orders',
            'customers',
            'line_items',
            'products',
            'variants'
        ]
        self.redshift.createSchema(self.schema)

    def get_last_ts(self, table_name):
        ...

    def sync_table(self, table_name):
        s3_path = f"{self.s3_prefix}/{table_name}/{datetime.utcnow().isoformat()}"
        field_names = self.schema.getTableFields(table_name)
        data = self.shopify.get_object_data(table_name)
        clean_data = [{k: json.dumps(v) if isinstance(v, dict) or isinstance(v, list) else v for k, v in row.items() if k in field_names} for row in data]
        self.s3.stream_dict_writer(clean_data, field_names, s3_path)
        # TODO: Just doing fulls for now
        self.redshift.createTable(self.schema, table_name)
        self.redshift.truncate(self.schema, table_name)
        self.redshift.appendFromS3(self.schema, table_name, 's3://' + self.s3.bucket + '/' + s3_path)

    def sync(self):
        for object in self.objects:
            self.sync_table(object)


if __name__ == '__main__':
    TARGET_SCHEMA = 'shopify'
    config = Config('config/config.yaml').getConfigObject()
    redshift_client = Redshift(**config['Resources']['redshift'])
    s3_client = S3(**config['Resources']['s3'])
    shopify_client = Shopify(**config['Resources']['shopify'])
    syncer = RedshiftShopifySyncer(s3_client, redshift_client, shopify_client, TARGET_SCHEMA)
    syncer.sync()

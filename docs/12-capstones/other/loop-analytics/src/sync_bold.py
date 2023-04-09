import os
import csv
import json
import requests as rq
from datetime import datetime

from packages.schema import Schema
from packages.config import Config
from packages.s3_resource import S3
from packages.redshift_resource import Redshift


# TODO: timestamps aren't happy going into redshift like this
# '2021-06-30T14:02:24-07:00'
# putting in as string now and casting later (which doesn't fix for timezone)

class Bold:
    CONFIG = {
        'base_url': 'https://api.boldcommerce.com',
        'endpoints': {
            'shops': {
                'get_shop_info': '/shops/v1/info',
            },
            'products': {
                'list_products': '/products/v2/shops/{shop_identifier}/products',
            },
            'subscriptions': {
                'list_subscriptions': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions',
                'get_subscription': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions/{subscriptionId}',
                'list_subscription_intervals': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions/{subscriptionId}/interval',
                'get_subscription_payment_method': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions/{subscriptionId}/payment_method',
                'list_subscription_payment_methods': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions/{subscriptionId}/payment_methods',
                'list_alternative_payment_methods': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions/{subscriptionId}/alternative_payments',
                'list_subscription_groups': '/subscriptions/v1/shops/{shopIdentifier}/subscription_groups',
            },
            'orders': {
                'list_subscription_orders': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions/{subscriptionId}/orders',
                'get_subscription_order': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions/{subscriptionId}/orders/{orderId}',
                'list_subscription_future_orders': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions/{subscriptionId}/future_orders',
            },
            'subscription_line_items': {
                'get_subscription_swapable_products': '/subscriptions/v1/shops/{shopIdentifier}/subscriptions/{subscriptionId}/line_items/{lineItemId}/products_swap',
            },
            'customers': {
                'list_customer_subscriptions': '/subscriptions/v1/shops/{shopIdentifier}/customers/{customerId}/subscriptions',
                'list_customers': '/subscriptions/v1/shops/{shopIdentifier}/customers',
                'get_customer': '/subscriptions/v1/shops/{shopIdentifier}/customers/{customerId}'
            }
        }
    }

    def __init__(self, access_token, shop_identifier: None):
        self.header = {'Authorization':  'bearer {access_token!s}'.format(access_token=access_token)}
        self.object_map = {
            'line_items': self.get_line_items,
            'subscriptions': self.call_get_subscriptions,
            'customers': self.get_subscription_customers,
            'addresses': self.get_subscription_addresses,
        }
        self.data = {}
        self.shop_id = shop_identifier

    def get_content(self, url, headers, params={}):
        content = {}
        response = rq.get(url, headers=headers, params=params)
        if response.status_code == 200:
            content = response.json() or {}
        else:
            print("Couldn't get content. Status returned was %s" % response.status_code)
            return None

        return content

    def get_url(self, *args, **kwargs):
        base_url = self.CONFIG.get('base_url')
        endpoint = self.CONFIG.get('endpoints', {})
        for arg in args:
            endpoint = endpoint.get(arg, {})
        url_temp = "%(base_url)s%(endpoint)s" % {'base_url': base_url, 'endpoint': endpoint}
        url = url_temp.format(**kwargs) if kwargs else url_temp
        return url

    def get_shop_id(self, url: str = None):
        if self.shop_id:
            return self.shop_id

        url = url or self.get_url('shops', 'get_shop_info')

        content = self.get_content(url, self.header)
        return content.get('shop_identifier')

    def next_page(self, content):
        pagination = content.get('pagination', {})
        if pagination:
            total_pages = pagination.get('total_pages', 0)
            page = pagination.get('current_page', total_pages)
            if page < total_pages:
                return {'page': page + 1}
            else:
                return None
        else:
            return None

    def get_batched_records(self, url: str, object_name: str,  params: dict = {}, batch_size: int = 100, max: int = -1):

        subscriptions = []
        total = 0
        local_params = {'limit': batch_size}
        local_params.update(params)
        content = self.get_content(url, self.header, local_params)
        batch = content.get(object_name, [])

        while batch and (max <= 0 or total + len(batch) <= max):
            subscriptions.extend(batch)
            total = len(subscriptions)
            watermark = batch[-1].get('id', 0)
            local_params.update({'since_id': watermark})
            content = self.get_content(url, self.header, local_params)
            batch = content.get(object_name, [])

        return subscriptions

    def call_get_subscriptions(self):
        if self.data.get('subscriptions', []):
            return self.data.get('subscriptions')

        shop_id = self.get_shop_id()
        url = self.get_url('subscriptions', 'list_subscriptions', shopIdentifier=shop_id)

        self.data['subscriptions'] = self.get_batched_records(url, 'subscriptions', params={'expand': 'customer'})
        return self.data.get('subscriptions', [])

    def get_subscription_customers(self):
        subscriptions = self.call_get_subscriptions()
        customers = []
        customer_ids = []
        for subscription in subscriptions:
            customer = subscription.get('customer')
            if customer and not customer.get('id') in customer_ids:
                customers.append(customer)
                customer_ids.append(customer.get('id'))
        return customers

    def get_subscription_addresses(self):
        subscriptions = self.call_get_subscriptions()
        addresses = []
        address_functions = ['billing_address', 'shipping_address']
        address_ids = {}
        for subscription in subscriptions:
            for address_function in address_functions:
                addr_ids = address_ids.get(address_function, [])
                address_ids[address_function] = addr_ids
                addr = subscription.get(address_function)
                if addr and not addr.get('id', '0') in addr_ids:
                    addr['address_function'] = address_function
                    addresses.append(addr)
                    addr_ids.append(addr.get('id', '0'))
                else:
                    continue
        return addresses

    def get_line_items(self):
        subscriptions = self.call_get_subscriptions()
        line_items = []
        for subscription in subscriptions:
            line_items.extend(subscription.get('line_items', []))
        return line_items

    def get_object_data(self, object_name):
        if self.object_map.get(object_name):
            return self.object_map[object_name]()
        else:
            raise ValueError(f"unsupported object {object_name}")

    def get_mapped_objects(self):
        return [key for key in self.object_map]


class RedshiftBoldSyncer:
    def __init__(self, s3, redshift, bold_client, target_schema):
        self.s3 = s3
        self.redshift = redshift
        self.client = bold_client
        self.schema = Schema(target_schema)
        self.extract_ts = datetime.utcnow()
        self.s3_prefix = target_schema
        self.objects = self.client.get_mapped_objects()
        self.redshift.createSchema(self.schema)

    def get_last_ts(self, table_name):
        ...

    def sync_table(self, table_name):
        s3_path = f"{self.s3_prefix}/{table_name}/{datetime.utcnow().isoformat()}"
        field_names = self.schema.getTableFields(table_name)
        data = self.client.get_object_data(table_name)
        clean_data = [
            {
                k: json.dumps(v) if isinstance(v, dict) or isinstance(v, list) else v
                for k, v in row.items() if k in field_names
            } for row in data
        ]

        self.s3.stream_dict_writer(clean_data, field_names, s3_path)
        # # TODO: Just doing fulls for now
        self.redshift.createTable(self.schema, table_name)
        self.redshift.truncate(self.schema, table_name)
        self.redshift.appendFromS3(self.schema, table_name, 's3://' + self.s3.bucket + '/' + s3_path)

    def sync(self):
        for object in self.objects:
            self.sync_table(object)

if __name__ == '__main__':
    TARGET_SCHEMA = 'bold'
    config = Config('config/config.yaml').getConfigObject()
    redshift_client = Redshift(**config['Resources']['redshift'])
    s3_client = S3(**config['Resources']['s3'])
    bold_client = Bold(**config['Resources']['bold'])
    syncer = RedshiftBoldSyncer(s3_client, redshift_client, bold_client, TARGET_SCHEMA)
    syncer.sync()
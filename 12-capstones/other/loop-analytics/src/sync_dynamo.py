from packages.schema import Schema
from packages.s3_resource import S3
from packages.config import Config
from packages.redshift_resource import Redshift
from datetime import datetime

import logging
import boto3


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


PROD_TABLES = [
    'accounts-prod', 
    'accounts-sequence-prod', 
    'bold-subscription-notification-prod', 
    'carts-prod', 
    'customer-migration-messages-prod', 
    'customer-migrations-prod', 
    'customers-prod', 
    'registries-prod'
]

DEV_TABLES = [
    'accounts-dev', 
    'accounts-sequence-dev', 
    'bold-subscription-notification-dev', 
    'carts-dev', 
    'customer-migration-messages-dev', 
    'customer-migrations-dev', 
    'customers-dev', 
    'registries-dev'
]



class RedshiftDynamoSyncer:
    def __init__(self, s3, redshift, target_schema):
        self.s3 = s3
        self.redshift = redshift
        self.schema = Schema(target_schema)
        self.extract_ts = datetime.utcnow()
        self.s3_prefix = target_schema
        self.client = boto3.client('dynamodb', region_name='us-west-2')

        self.tables = DEV_TABLES

        self.redshift.createSchema(self.schema)

    def copy_data(self):
        # rs_tables = [i.replace('_', '-') for i in self.schema.getSchemaTables]
        for table in self.tables:
            rs_table = table.replace('-', '_')
            self.redshift.createTable(self.schema, rs_table)
            self.redshift.truncate(self.schema, rs_table)
            self.redshift.load_dynamo(self.schema.name, table, rs_table)


    ### This is just to generate the yamls of the tables we want to pull over
    def pull_dynamo_tables(self):
        data = []
        for table in self.tables:
            td = {}
            td['table_name'] = table

            table_data = self.client.describe_table(TableName=table)
            cols = []

            for attribute in table_data['Table']['AttributeDefinitions']:
                col = {
                    "col_name": attribute['AttributeName'],
                    "col_type": attribute['AttributeType']
                }

                cols.append(col)

            td['Columns'] = cols

            data.append(td)

        return data

    def gen_yamls(self):
        table_data = self.pull_dynamo_tables()
        for tab in table_data:
            print(f"{tab['table_name'].replace('-', '_')}:")
            print(f"  fields:")
            for col in tab['Columns']:
                print(f"    - name: {col['col_name']}")
                if col['col_type'] == 'S':
                    print(f"      type: TEXT")
                elif col['col_type'] == 'N':
                    print(f"      type: FLOAT")
                else:
                    print(f"      type: {col['col_type']}")

        

if __name__ == "__main__":
    TARGET_SCHEMA = 'dynamo'
    config = Config('config/config.yaml').getConfigObject()
    redshift_client = Redshift(**config['Resources']['redshift'])
    s3_client = S3(**config['Resources']['s3'])
    syncer = RedshiftDynamoSyncer(s3_client, redshift_client, TARGET_SCHEMA)
    syncer.copy_data()
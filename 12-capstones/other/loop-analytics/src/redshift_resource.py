import logging
import pandas as pd
import os
import boto3
from jinja2 import Template
from sqlalchemy import create_engine, exc, MetaData, Table, text

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class Redshift:
    def __init__(self, **kwargs):
        self.engine = create_engine(
                'redshift+psycopg2://{db_user}:{db_password}@{db_host}:5439/{db_name}'.format(
                    db_user=kwargs.get('user', os.environ.get('RS_USER')),
                    db_password=kwargs.get('password', os.environ.get('RS_PASSWORD')),
                    db_host=kwargs.get('host', os.environ.get('RS_HOST')),
                    db_name=kwargs.get('database', os.environ.get('RS_DB'))
                ),
                pool_recycle=3600
            )
        self.aws_iam_role = kwargs.get('aws_iam_role', os.environ.get('AWS_IAM_ROLE'))
        self.aws_key = kwargs.get('aws_key', os.environ.get('AWS_ACCESS_KEY_ID'))
        if not self.aws_key:
            session = boto3.Session()
            credentials = session.get_credentials()
            self.aws_key = credentials.access_key
        self.aws_secret = kwargs.get('aws_secret', os.environ.get('AWS_SECRET_ACCESS_KEY'))
        if not self.aws_secret:
            session = boto3.Session()
            credentials = session.get_credentials()
            self.aws_secret = credentials.secret_key
        self.conn = self.engine.connect()

    def load(self, schema, table, s3_path, **kwargs):
        logger.info('loading data to {}.{}'.format(schema, table))
        copy_str = """
            COPY {schema}.{table}
            FROM '{s3path}'
            credentials 'aws_access_key_id={aws_key};aws_secret_access_key={aws_secret}'
            CSV GZIP
            TIMEFORMAT 'auto'
            TRUNCATECOLUMNS
            --REGION 'us-west-2';
        """.format(
            schema=schema,
            table=table,
            s3path=s3_path,
            aws_key=self.aws_key,
            aws_secret=self.aws_secret
        )
        self.engine.execute(text(copy_str).execution_options(autocommit=True))

    def load_dynamo(self, schema, from_table, to_table, **kwargs):
        logger.info('loading data to {}.{}'.format(schema, to_table))
        copy_str = f"""
            COPY {schema}.{to_table}
            FROM 'dynamodb://{from_table}'
            credentials 'aws_access_key_id={self.aws_key};aws_secret_access_key={self.aws_secret}'
            readratio 25;
        """
        self.engine.execute(text(copy_str).execution_options(autocommit=True))

    def truncate(self, schema, table):
        logger.info('truncating table {}.{}'.format(schema, table))
        truncate_str = """
            TRUNCATE {}.{};
        """.format(schema.name, table)
        self.engine.execute(text(truncate_str).execution_options(autocommit=True))

    def dropTable(self, schema, table_name):
        logger.info("Dropping table {}.{}".format(schema.name, table_name))
        query_str = """
            DROP TABLE IF EXISTS {}.{};
        """.format(schema.name, table_name)
        self.engine.execute(text(query_str).execution_options(autocommit=True))

    def dropView(self, schema, table_name, cascade=False):
        cascade_str = '' if not cascade else 'CASCADE'
        query_str = """
            DROP VIEW IF EXISTS {}.{} {};
        """.format(schema.name, table_name, cascade_str)
        self.engine.execute(text(query_str).execution_options(autocommit=True))

    def makeCreateTableQuery(self, schema, table_name):
        query_str = ""
        field_list = []
        table_obj = schema.schema_def[table_name]
        for field in table_obj.get('fields'):
            field_list.append('{0} {1}'.format(field.get('name'), field.get('type')))
        query_str += 'CREATE TABLE IF NOT EXISTS {0}.{1} ('.format(schema.name, table_name) + ','.join(field_list) + ')'
        if table_obj.get('distkeys'):
            if len(table_obj.get('distkeys')) > 1:
                raise Exception("More than one distkey for {0}. Only 1 supported.".format(table_name))
            query_str += ' distkey(' + ','.join(table_obj.get('distkeys')) + ')'
        if table_obj.get('diststyle'):
            query_str += ' diststyle ' + table_obj.get('diststyle')
        if table_obj.get('sortkeys'):
            query_str += ' sortkey(' + ','.join(table_obj.get('sortkeys')) + ')'
        query_str += ';'
        return query_str

    def grantTablePerms(self, schema, table_name):
        # update perms
        for user in schema.schema_perms:
            self.engine.execute(text("GRANT USAGE ON SCHEMA {} TO {}".format(schema.name, user)).execution_options(autocommit=True))
            for permission_type in schema.schema_perms[user]:
                if table_name in schema.schema_perms[user][permission_type]['tables'] or schema.schema_perms[user][permission_type]['tables'] == ['*']:
                    if schema.schema_perms[user][permission_type]['tables'] == ['*']:
                        self.engine.execute(
                            text("GRANT {} ON ALL TABLES IN SCHEMA {} TO {}".format(permission_type, schema.name, user)).execution_options(autocommit=True)
                        )
                    else:
                        self.engine.execute(
                            text("GRANT {} ON {} IN SCHEMA {} TO {}".format(permission_type, table_name, schema.name, user)).execution_options(autocommit=True)
                        )
    def createSchema(self, schema):
        logger.info("Creating schema {} if it doesn't already exist.".format(schema.getSchemaName()))
        query_str = "CREATE SCHEMA IF NOT EXISTS {}".format(schema.getSchemaName())
        self.engine.execute(text(query_str).execution_options(autocommit=True))

    def createTable(self, schema, table_name):
        logger.info("Creating table {}.{}".format(schema.name, table_name))
        query_str = self.makeCreateTableQuery(schema, table_name)
        self.engine.execute(text(query_str).execution_options(autocommit=True))
        self.grantTablePerms(schema, table_name)

    def createTableLike(self, schema, table_name, copy_table_name):
        query = """
            CREATE TABLE {0}.{1} (LIKE {0}.{2});
        """.format(schema.name, table_name, copy_table_name)
        self.engine.execute(text(query).execution_options(autocommit=True))

    def upsertTable(self, schema, table_name, update_table_name):
        table_obj = schema.schema_def[table_name]
        pks = table_obj.get('pk')
        parent_keys = table_obj.get('parent_key')

        if parent_keys:
            parent_keys_where = " AND ".join(["{0}.{2} = {1}.{2}".format(table_name, update_table_name, parent_key) for parent_key in parent_keys if parent_keys])
            where_clause = "WHERE " + parent_keys_where
        elif pks:
            pks_where = " AND ".join(["{0}.{2} = {1}.{2}".format(table_name, update_table_name, pk) for pk in pks if pks])
            where_clause = "WHERE " + pks_where
        else:
            where_clause = ""

        query = """
            BEGIN TRANSACTION;
            DELETE FROM {0}.{1}
            USING {0}.{2}
            {3};

            INSERT INTO {0}.{1}
            SELECT * FROM {0}.{2};
    
            END TRANSACTION;
        """.format(schema.name, table_name, update_table_name, where_clause)
        logger.info("QUERY {}".format(query))
        self.engine.execute(text(query).execution_options(autocommit=True))

    def upsertFromS3(self, schema, table_name, s3_path):
        update_table_name = self.loadToStagingTable(schema, table_name, s3_path)
        self.upsertTable(schema, table_name, update_table_name)
        self.dropTable(schema, update_table_name)

    def loadToStagingTable(self, schema, table_name, s3_path):
        update_table_name = table_name + '_stage'
        self.dropTable(schema, update_table_name)  # drop if there's one lingering from a previous failure
        self.createTableLike(schema, update_table_name, table_name)
        self.load(schema.name, update_table_name, s3_path)
        return update_table_name

    def appendFromS3(self, schema, table_name, s3_path):
        self.load(schema.name, table_name, s3_path)

    def buildTable(self, schema, table_name, mode='full'):
        # TODO: This doesn't work if the table doesn't exist yet
        self.createTable(schema, table_name)
        # This wasn't working if the table didn't have a schema obj
        if schema.schema_def.get(table_name) and schema.schema_def[table_name].get('mode'):  # override if in table yaml
            mode = schema.schema_def[table_name].get('mode')

        query_path = "/".join([os.path.dirname(__file__).replace('packages', 'schema'), schema.name, table_name]) + '.sql'
        with open(query_path, 'r') as f:
            query_string = f.read()
            query_string = Template(query_string).render(mode=mode)

            # todo - this is ugly, but needed build w/in txn now
            drop_str = ""
            create_str = ""
            if mode == 'full':
                drop_str = "DROP TABLE {}.{};".format(schema.name, table_name)
                create_str = self.makeCreateTableQuery(schema, table_name)
            # elif mode == 'incremental':
            #     max_dt = self.executeQuery("SELECT GREATEST(MAX({})) FROM {}.{}".format(
            #             ','.join(schema[table_name]['audit_cols']),
            #             schema.name,
            #             table_name
            #         )
            #     )

            query = """
                BEGIN TRANSACTION;

                {drop}

                {create}

                INSERT INTO {schema}.{table}
                {query};

                END TRANSACTION;
            """.format(
                drop=drop_str,
                create=create_str,
                schema=schema.name,
                table=table_name,
                query=query_string
            )
            logger.info("QUERY {}".format(query))
            self.engine.execute(text(query).execution_options(autocommit=True))
            self.grantTablePerms(schema, table_name)

    def buildView(self, schema, view_name):
        query_path = "/".join([os.path.dirname(__file__).replace('packages', 'schema'), schema.name, view_name]) + '.sql'

        self.dropView(schema, view_name)

        with open(query_path, 'r') as f:
            query_string = f.read()

            query = """
                CREATE OR REPLACE VIEW {0}.{1} AS
                {2}
            """.format(schema.name, view_name, query_string)
            logger.info("QUERY {}".format(query))
            self.engine.execute(text(query).execution_options(autocommit=True))

    def executeQuery(self, query):
        result = self.engine.execute(text(query).execution_options(autocommit=True))
        return result.fetchall()

    def delete_after_date(self, schema, table_name, delete_date, date_field):
        """
        This method can be useful when pulling from an data source this provides
        responses by day. To ensure there is no overlap on multiple runs intraday,
        we delete existing records for that day.
        """
        date = delete_date.strftime('%Y-%m-%d')
        logger.info('Deleting rows on and after {}'.format(date))
        query = """
            DELETE FROM {}.{}
            WHERE {} >= '{}'
        """.format(
            schema.name,
            table_name,
            date_field,
            date
        )
        self.engine.execute(text(query))

    def table_to_df(self, schema_name, table_name, order_by=[], where_clause=''):
        if len(order_by) > 0:
            order_by_clause = f" ORDER BY {','.join(order_by)}"
        else:
            order_by_clause = ''

        df = pd.read_sql(
            f"""
            SELECT *
            FROM {schema_name}.{table_name}
            {where_clause}
            {order_by_clause}
            """,
            self.engine
        )

        return df

    def query_to_df(self, query):
        df = pd.read_sql(query)
        return df
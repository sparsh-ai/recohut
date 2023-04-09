import psycopg2
import os


class Postgres:
    def __init__(self, user, password, server_name='localhost', db_name='template1', port=5432):
        self.conn = psycopg2.connect("dbname={0} user={1} host={2} password={3} port={4}".format(
            db_name,
            user,
            server_name,
            password,
            port
        ))
        self.cursor = self.conn.cursor()

    def executeQuery(self, query_string):
        self.cursor.execute(query_string)
        try:
            return self.cursor.fetchall()
        except:
            # TODO: Future optimizations around commiting within a transaction and such here
            self.conn.commit()
            print("No results. Commited transaction.")

    def dropTable(self, table_name):
        schema_name, table_name = table_name.split('.')
        query_string = "DROP TABLE IF EXISTS {0}.{1} ".format(schema_name, table_name)
        self.executeQuery(query_string)

    def buildTable(self, table_name):
        query_path = os.path.dirname(__file__).replace('packages', 'schema') + '/' + table_name.replace('.', '/') + '.sql'
        f = open(query_path, 'rb')
        query_string = f.read()
        f.close()

        schema_name, table_name = table_name.split('.')
        query_string = "INSERT INTO {0}.{1} ".format(schema_name, table_name) + query_string

        self.emptyTable(schema_name, table_name)  # drop data
        self.executeQuery(query_string)

    def emptyTable(self, schema_name, table_name):
        tables = self.executeQuery('SELECT * FROM pg_catalog.pg_tables')
        if table_name in set([x[1] for x in tables]):
            self.executeQuery('DELETE FROM {0}.{1}'.format(schema_name, table_name))  # drop data

    def loadTable(self, path_to_file, schema_name, table_name,
            aws_access_key_id=None, aws_secret_access_key=None):
        # TODO: Can make this function more flexible for other delimiters, encoding options, etc
        if path_to_file[0:3] == 's3:':
            query_string = "COPY {0}.{1} FROM '{2}' credentials 'aws_access_key_id={3};aws_secret_access_key={4}' CSV DELIMITER ','\
                IGNOREHEADER 1 ACCEPTINVCHARS".format(
                    schema_name,
                    table_name,
                    path_to_file,
                    aws_access_key_id,
                    aws_secret_access_key
                )
        else:
            query_string = "COPY {0}.{1} FROM '{2}' HEADER DELIMITER ',' CSV ENCODING 'LATIN1'".format(
                schema_name,
                table_name,
                path_to_file
            )
        self.executeQuery(query_string)

    def createTable(self, schema, table_name):
        query_str = ""
        field_list = []
        table_obj = schema.schema_def[table_name]
        for field in table_obj.get('fields'):
            field_list.append('{0} {1}'.format(field.get('name'), field.get('type')))
        query_str += 'CREATE TABLE IF NOT EXISTS {0}.{1} ('.format(self.name, table_name) + ','.join(field_list) + ')'
        if table_obj.get('distkeys'):
            if len(table_obj.get('distkeys')) > 1:
                raise Exception("More than one distkey for {0}. Only 1 supported.".format(table_name))
            query_str += ' distkey(' + ','.join(table_obj.get('distkeys')) + ')'
        if table_obj.get('diststyle'):
            query_str += ' diststyle ' + table_obj.get('diststyle')
        if table_obj.get('sortkeys'):
            query_str += ' sortkey(' + ','.join(table_obj.get('sortkeys')) + ')'
        query_str += ';'
        self.executeQuery(query_str)

    def createSchema(self, schema, create_tables=False):
        query_str = 'CREATE SCHEMA IF NOT EXISTS {0};'.format(schema.name)
        if create_tables:
            for table in schema.schema_def:
                query_str += self.CreateTable(schema, table)
        self.executeQuery(query_str)

    def dropSchema(self, schema):
        self.executeQuery('DROP SCHEMA {0} CASCADE;'.format(schema.name))

    def windowUpdate(self, paths_to_files, schema_name, table_name, window_fields,
            aws_access_key_id=None, aws_secret_access_key=None):
        if paths_to_files:
            fqn = '.'.join([schema_name, table_name])
            stg_tbl_name = fqn.replace('.', '.stg_')
            self.executeQuery('create table {0} (like {1})'.format(stg_tbl_name, fqn))
            for path_to_file in paths_to_files:
                self.loadTable(path_to_file, stg_tbl_name.split('.')[0], stg_tbl_name.split('.')[1], aws_access_key_id, aws_secret_access_key)
            drop_query = """
                DELETE FROM {0} USING {1} WHERE {2}
                """.format(fqn, stg_tbl_name, ' and '.join([table_name + '.' + x + '=' + stg_tbl_name.split('.')[1] + '.' + x for x in window_fields]))
            self.executeQuery(drop_query)
            insert_query = """
                INSERT INTO {0} SELECT * FROM {1}
                """.format(fqn, stg_tbl_name)
            self.executeQuery(insert_query)
            self.executeQuery('drop table {0}'.format(stg_tbl_name))

    def fullUpdate(self, paths_to_files, schema_name, table_name,
            aws_access_key_id=None, aws_secret_access_key=None):
        """
        This method blows away existing data and loads data from files
        """
        if paths_to_files:
            self.emptyTable(schema_name, table_name)
            for path_to_file in paths_to_files:
                self.loadTable(path_to_file, schema_name, table_name, aws_access_key_id, aws_secret_access_key)

    def appendUpdate(self, paths_to_files, schema_name, table_name,
            aws_access_key_id=None, aws_secret_access_key=None):
        """
        This table loads data into table from files without blowing away data first
        This is the same as fullUpdate(), just it doesn't empty the table first.
        """
        if paths_to_files:
            for path_to_file in paths_to_files:
                self.loadTable(path_to_file, schema_name, table_name, aws_access_key_id, aws_secret_access_key)

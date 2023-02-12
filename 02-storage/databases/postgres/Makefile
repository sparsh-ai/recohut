connect:
	psql --host=<> --port=5432 --username=<> --dbname=<>
	psql -h localhost -p 5432 -d <db_name> -U <user_name> -W

connect_database:
	\connect <database_name>;

create_dump:
	pg_dump --host=<hostname> --port=3306  --user=<username> --password --dbname=database_name --table=table_name --format=plain > data-to-be-loaded.sql
	pg_dump --host=<hostname> --port=3306  --user=<username> --password --dbname=database_name --table=table_name --format=tar > data-to-be-loaded.tar

restore_dump:
	\include data-to-be-loaded.sql;
	pg_restore --user=<username> --host=<hostname> --password --dbname=<database_name> < data-to-be-loaded.tar

describe_table:
	\d <table_name>

show_talbe:
	\d <table_name>

restart_service_mac:
	brew services restart postgresql

import_data_from_sql:
	\i path_of_your_dump_file.sql

import_data_from_csv:
	\copy drivers(id, first_name, last_name)
	from './data/drivers.csv'
	with delimiter ','
	csv header;

psql_general:
	CREATE DATABASE <db_name>;
	CREATE USER <user_name> WITH ENCRYPTED PASSWORD '<password>';
	GRANT ALL ON DATABASE <db_name> TO <user_name>;
	GRANT pg_read_server_files TO <user_name>;
	\q

connect_py:
	import boto3
	import json

	def get_secret(secret_name, region_name="us-east-1"):
		session = boto3.session.Session()
		client = session.client(
			service_name='secretsmanager',
			region_name=region_name)
		get_secret_value_response = client.get_secret_value(SecretId=secret_name)
		get_secret_value_response = json.loads(get_secret_value_response['SecretString'])
		return get_secret_value_response

	creds = get_secret("wysde")
	USERNAME = creds["RDS_POSTGRES_USERNAME"]
	PASSWORD = creds["RDS_POSTGRES_PASSWORD"]
	HOST = creds["RDS_POSTGRES_HOST"]
	DATABASE = 'sparsh'

	conn_str = 'postgresql://{0}:{1}@{2}/{3}'.format(USERNAME, PASSWORD, HOST, DATABASE)

	%config SqlMagic.autopandas=True
	%config SqlMagic.displaycon=False
	%config SqlMagic.feedback=False
	%config SqlMagic.displaylimit=5
	%reload_ext sql
	%sql {conn_str}
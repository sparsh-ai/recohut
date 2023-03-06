connect:
	psql --host=<> --port=5432 --username=<> --dbname=<>
	psql -h localhost -p 5432 -d <db_name> -U <user_name> -W
	PGPASSWORD=student createdb -h 127.0.0.1 -U student pagila
	PGPASSWORD=student psql -q -h 127.0.0.1 -U student -d pagila -f Data/pagila-schema.sql

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

connect_and_create_db_py:
	import os
	import pandas as pd
	from sqlalchemy import create_engine

	POSTGRES_USERNAME = ''
	POSTGRES_PASSWORD = ''
	POSTGRES_ENDPOINT = ''
	POSTGRES_DATABASE = ''

	CONN = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@{POSTGRES_ENDPOINT}:5432/{POSTGRES_DATABASE}"
	engine = create_engine(CONN)
	conn = engine.connect()

	try: 
		conn.execution_options(isolation_level="AUTOCOMMIT").execute("CREATE DATABASE mydb")
	except Exception as e:
		print(e)
	finally:
		conn.close()

load_data_py:
	import psycopg2
	import pandas as pd
	import sqlalchemy as sa

	conn = psycopg2.connect(f"host=database-1.us-east-1.rds.amazonaws.com dbname=template1 user=postgres password=")
	conn.set_session(autocommit=True)
	cur = conn.cursor()
	cur.execute("DROP DATABASE IF EXISTS stations WITH (FORCE)")
	cur.execute("CREATE DATABASE stations WITH ENCODING 'utf8' TEMPLATE template0")
	conn.close()   

	conn = psycopg2.connect(f"host=database-1.us-east-1.rds.amazonaws.com dbname=stations user=postgres password=")
	DDL = """
	CREATE TABLE stations (
	stop_id INTEGER PRIMARY KEY,
	direction_id VARCHAR(1) NOT NULL,
	stop_name VARCHAR(70) NOT NULL,
	station_name VARCHAR(70) NOT NULL,
	station_descriptive_name VARCHAR(200) NOT NULL,
	station_id INTEGER NOT NULL,
	"order" INTEGER,
	red BOOLEAN NOT NULL,
	blue BOOLEAN NOT NULL,
	green BOOLEAN NOT NULL
	);
	"""
	cur = conn.cursor()
	cur.execute(DDL)
	conn.commit()
	conn.close()

	df = pd.read_csv("data.csv")
	db_url = 'postgresql://<username>:<password>@database-1.us-east-1.rds.amazonaws.com:5432/stations'
	engine = sa.create_engine(db_url)
	df.to_sql('stations', engine, method='multi', index=False, if_exists='append')
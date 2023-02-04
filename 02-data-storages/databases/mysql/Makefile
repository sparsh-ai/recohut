start:
	start_mysql

connect:
	mysql --host=<hostname> --port=3306  --user=<username> --password

create_database:
	create database <dbname>;

create_table:
	create table mytbl(ts datetime, vid int, type char(15), pid smallint);

disconnect:
	exit

create_dump:
	mysqldump --host=<hostname> --port=3306  --user=<username> --password <database_name> <table_name> > data-to-be-loaded.sql

restore_dump:
	source data-to-be-loaded.sql;
	mysql --host=<hostname> --port=3306  --user=<username> --password <database_name> < data-to-be-loaded.sql

show_tables:
	SHOW FULL TABLES WHERE table_type = 'BASE TABLE';

describe_table:
	describe <table_name>

connect_python:
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
	USERNAME = creds["RDS_MYSQL_USERNAME"]
	PASSWORD = creds["RDS_MYSQL_PASSWORD"]
	HOST = creds["RDS_MYSQL_HOST"]
	DATABASE = 'sparsh'
	conn_str = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(USERNAME, PASSWORD, HOST, DATABASE)
	%config SqlMagic.autopandas=True
	%config SqlMagic.displaycon=False
	%config SqlMagic.feedback=False
	%config SqlMagic.displaylimit=5
	%reload_ext sql
	%sql {conn_str}

ddl_ingest_python:
	TABLE = "table_to_be_loaded"
	df = pd.read_csv(f"./data/{TABLE}.csv")
	print(pd.io.sql.get_schema(df, name=TABLE, con=conn))
	df.to_csv(f"./data/{TABLE}.csv", index=False)
	echo mysqlimport --local \
		--compress \
		--user={USERNAME} \
		--password \
		--host={HOST} \
		--ignore-lines=1 \
		--fields-terminated-by=\',\' {DATABASE} data/{TABLE}.csv
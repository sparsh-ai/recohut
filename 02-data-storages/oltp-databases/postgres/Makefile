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
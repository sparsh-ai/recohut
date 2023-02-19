# Airflow Forex ETL

The ETL process will extract data from fixer.io API, transform it, and load it to a PostgreSQL database. This project aims to have an automated process that constantly feeds the PostgreSQL database with data.

Process steps:

1. Create a free accout on fixer.io
2. Get the API key and add in the DAG
3. Add connection: {'connection_id':'is_api_available', 'connection_type':'http', 'host':'https://api.apilayer.com/fixer'}
4. Add connection: {'connection_id':'postgres', 'connection_type':'postgres', 'host':{HOST}, 'port':{PORT}, 'schema':{DATABASE}, 'login':{USER}, 'password':{PASSWORD}}
5. Run the DAG
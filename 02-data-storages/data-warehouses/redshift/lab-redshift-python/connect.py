import pandas as pd
import psycopg2
import boto3
import json
from sqlalchemy import create_engine
from sqlalchemy import text

def get_secret(secret_name='wysde'):
    region_name = "us-east-1"
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name)
    get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    get_secret_value_response = json.loads(get_secret_value_response['SecretString'])
    return get_secret_value_response

secret_vals = get_secret()

redshift_endpoint = secret_vals['REDSHIFT_HOST']
redshift_user = secret_vals['REDSHIFT_USERNAME']
redshift_pass = secret_vals['REDSHIFT_PASSWORD']
port = 5439
dbname = "dev"

engine_string = "postgresql+psycopg2://%s:%s@%s:%d/%s" \
% (redshift_user, redshift_pass, redshift_endpoint, port, dbname)
engine = create_engine(engine_string)

query = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog' AND 
    schemaname != 'information_schema';
"""
df = pd.read_sql_query(text(query), engine)

query = """
SELECT * FROM "dev"."public"."users";
"""
df = pd.read_sql_query(text(query), engine)
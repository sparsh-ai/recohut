from datetime import datetime
import json

from airflow import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator

default_args = {
  'start_date': datetime(2021, 1, 1),
}

with DAG(dag_id='nft-pipeline',
         schedule_interval='@daily',
         default_args=default_args,
         tags=['nft'],
         catchup=False) as dag:
  
  creating_table = SqliteOperator(
    task_id='creating_table',
    sqlite_conn_id='db_sqlite',
    sql='''
      CREATE TABLE IF NOT EXISTS nfts (
        token_id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        image_url TEXT NOT NULL
      )
    '''
  )

  is_api_available = HttpSensor(
    task_id='is_api_available',
    http_conn_id='opensea_api',
    endpoint='api/v1/assets?collection=doodles-official&limit=1'
  )

  extract_nft = SimpleHttpOperator(
    task_id='extract_nft',
    http_conn_id='opensea_api',
    endpoint='api/v1/assets?collection=doodles-official&limit=1',
    method='GET',
    response_filter=lambda res: json.loads(res.text),
    log_response=True
  )
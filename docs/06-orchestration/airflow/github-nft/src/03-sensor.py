from datetime import datetime

from airflow import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor

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

# UI 가서 그래프 확인
# create http connection
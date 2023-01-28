from datetime import datetime
import json

from airflow import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from pandas import json_normalize

default_args = {
  'start_date': datetime(2021, 1, 1),
}

def _processing_nft(ti):
  assets = ti.xcom_pull(task_ids=['extract_nft']) 
  if not len(assets):
    raise ValueError("assets is empty")
  nft = assets[0]['assets'][0]

  processed_nft = json_normalize({
    'token_id': nft['token_id'],
    'name': nft['name'],
    'image_url': nft['image_url'],
  })
  processed_nft.to_csv('/tmp/processed_nft.csv', index=None, header=False)


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

  process_nft = PythonOperator(
    task_id='process_nft',
    python_callable=_processing_nft
  )

  storing_user = BashOperator(
    task_id='storing_user',
    bash_command='echo -e ".separator ","\n.import /tmp/processed_user.csv users" | sqlite3 /Users/keon/airflow/airflow.db'
  )

# UI 가서 그래프 확인
# create http connection
#  airflow tasks test example_sqlite creating_table 2021-01-01

# sqlite3 airflow.db
# .tables
# select * from users;
# sqlite> .schema users
# CREATE TABLE users (
#         firstname TEXT NOT NULL,
#         lastname TEXT NOT NULL,
#         country TEXT NOT NULL,
#         username TEXT NOT NULL,
#         password TEXT NOT NULL,
#         email TEXT NOT NULL PRIMARY KEY
#       );

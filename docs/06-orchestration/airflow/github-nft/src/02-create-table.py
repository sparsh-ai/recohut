from datetime import datetime

from airflow import DAG
from airflow.providers.sqlite.operators.sqlite import SqliteOperator

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

#  airflow tasks test example_sqlite creating_table 2021-01-01

# sqlite3 airflow.db
# .tables
# select * from nfts;
# sqlite> .schema nfts
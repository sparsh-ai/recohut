from datetime import datetime

from airflow import DAG

default_args = {
  'start_date': datetime(2021, 1, 1),
}

with DAG(dag_id='nft-pipeline',
         schedule_interval='@daily',
         default_args=default_args,
         tags=['nft'],
         catchup=False) as dag:
  pass
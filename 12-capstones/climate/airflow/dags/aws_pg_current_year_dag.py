import os
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine
import pyarrow.csv as pv
import pyarrow.parquet as pq
import pyarrow.compute as pc
import pandas as pd

URL_PREFIX = 'https://noaa-ghcn-pds.s3.amazonaws.com'
TEMP_STORAGE_PATH = os.getenv('TEMP_STORAGE_PATH', 'not-found')
START_YEAR = int(os.getenv("START_YEAR", "1760"))
PG_SCHEMA = 'ghcnd'

csv_schema = {
    'id': 'string',
    'date': 'string',
    'element': 'string',
    'value': 'int32',
    'm_flag': 'string',
    'q_flag': 'string',
    's_flag': 'string',
    'obs_time': 'int16',
}

def format_to_parquet(**kwargs):
    year = kwargs['year']
    src_file = kwargs['src_file']
    header = kwargs['column_names']
    column_types = kwargs['column_types']
    if not src_file.endswith('.csv'):
        logging.error("Can only accept source files in CSV format, for the moment")
        return
    table = pv.read_csv(
      src_file,
      read_options = pv.ReadOptions(column_names=column_names),
      convert_options = pv.ConvertOptions(column_types=column_types)
    )
    table = table \
        .append_column('parsed_date', pc.strptime(table.column("date"), format='%Y%m%d', unit='s').cast('date32')) \
        .drop(['date']) \
        .rename_columns(['id','element','value','m_flag','q_flag','s_flag','obs_time','date'])
    pq.write_table(table, src_file.replace('.csv', '.parquet'))

def parquet_to_pg(**kwargs):

    src_file = kwargs['src_file']
    table_name = kwargs['table_name']
    # df = pq.read_table(src_file).to_pandas()
    df = pd.read_parquet(src_file) # use pandas directly, since pandas uses pyarrow by default.

    dbschema = PG_SCHEMA
    user = "root"
    password = "root"
    host = "postgres-service-ghcnd"
    port = 5432
    db = "ghcn-d"
    cmd = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    engine = create_engine(cmd, connect_args={'options': f'-csearch_path={dbschema}'})
    engine.connect()
    df.to_sql(table_name, engine, if_exists='append', index=False)

default_args = {
    "owner": "airflow",
    "start_date": datetime.now() - timedelta(days=2),
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="aws_pg_current_year",
    schedule_interval="0 0 * * *",
    default_args=default_args,
    catchup=True,
    max_active_runs=1,
    tags=['ghcnd'],
) as dag:

    year = '{{dag_run.logical_date.strftime("%Y")}}'
    column_names = ['id','date','element','value','m_flag','q_flag','s_flag','obs_time']
    csv_file_name = f'/{year}.csv'
    dataset_url = URL_PREFIX + '/csv' + csv_file_name
    csv_file_path = TEMP_STORAGE_PATH + csv_file_name
    parquet_file_name = csv_file_name.replace('.csv', '.parquet')
    parquet_file_path = TEMP_STORAGE_PATH + parquet_file_name
    table_name = f"{year}"

    download_dataset_task = BashOperator(
        task_id="download_dataset_task",
        bash_command=f"""
          if ! [ -f {csv_file_path} ] ; then
            curl -sS {dataset_url} > {csv_file_path};
          fi
        """
    )

    format_to_parquet_task = PythonOperator(
        task_id="format_to_parquet_task",
        python_callable=format_to_parquet,
        op_kwargs={
            "src_file": csv_file_path,
            "column_names": column_names,
            "column_types": csv_schema,
            "year": year
        },
    )

    clear_local_files_task = BashOperator(
        task_id="clear_local_files_task",
        bash_command=f"rm {csv_file_path}"
    )

    CREATE_TABLE_QUERY = f"""
      CREATE UNLOGGED TABLE IF NOT EXISTS "{PG_SCHEMA}"."{table_name}" (
        index SERIAL PRIMARY KEY,
        id CHAR(11),
        date DATE,
        element CHAR(4),
        value INTEGER,
        m_flag CHAR(1),
        q_flag CHAR(1),
        s_flag CHAR(1),
        obs_time SMALLINT
      )
      """
    create_table_task = PostgresOperator(
            task_id= "create_pg_table_task",
            sql=CREATE_TABLE_QUERY,
        )

    parquet_to_pg_task = PythonOperator(
      task_id="parquet_to_pg_task",
      python_callable=parquet_to_pg,
      op_kwargs={
          "src_file": parquet_file_path,
          "table_name": table_name
      },
    )

    download_dataset_task >> format_to_parquet_task >> create_table_task >> parquet_to_pg_task >> clear_local_files_task

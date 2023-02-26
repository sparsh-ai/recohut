import os
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from sqlalchemy import create_engine
import pyarrow.csv as pv
import pyarrow.parquet as pq
import pandas as pd

URL_PREFIX = 'https://noaa-ghcn-pds.s3.amazonaws.com'
TEMP_STORAGE_PATH = os.getenv('TEMP_STORAGE_PATH', 'not-found')

origin_file_ids = ['stations', 'countries']
headers = {
    "stations": ['id','latitude','longitude','elevation','state','name','gsn_flag','hcn_crn_flag','wmo_id'],
    "countries": ['code','name']
}
column_indexes = {
    'stations': [[0,11],[12,20],[21,30], [31,37], [38,40], [41,71], [72,75], [76,79], [80,85]],
    'countries': [[0,2],[3,50]]
}
is_text_column = {
    'stations': [True,False,False,False,True,True,True,True,True],
    'countries': [True,True]
}

CREATE_TABLE_QUERY = {
    'stations':  """CREATE TABLE IF NOT EXISTS ghcnd.stations (
            id CHAR(11) PRIMARY KEY,
            latitude DOUBLE PRECISION,
            longitude DOUBLE PRECISION,
            elevation DOUBLE PRECISION,
            state CHAR(2),
            name CHAR(30),
            gsn_flag CHAR(3),
            hcn_crn_flag CHAR(3),
            wmo_id CHAR(5)
            );""",
    'countries': """CREATE TABLE IF NOT EXISTS ghcnd.countries (
            code CHAR(2) PRIMARY KEY,
            name CHAR(46)
            );"""}

def convert_to_csv(**kwargs):

    src_file = kwargs['src_file']
    header = kwargs['header']
    column_indexes = kwargs['column_indexes']
    is_text_column = kwargs['is_text_column']
    with open(src_file) as f_t:
        with open(src_file.replace('txt','csv'), "w") as f_c:
            f_c.writelines([','.join(header)+'\n'])
            for line in f_t:
                columns = []
                for i, index in enumerate(column_indexes):
                    text = line[index[0]:index[1]].strip()
                    if is_text_column:
                        columns.append('"'+text+'"')
                    else:
                        columns.append(line[index[0]:index[1]])
                f_c.writelines([','.join(columns) + '\n'])

def format_to_parquet(**kwargs):

    src_file = kwargs['src_file']
    if not src_file.endswith('.csv'):
        logging.error("Can only accept source files in CSV format, for the moment")
        return
    table = pv.read_csv(src_file)
    pq.write_table(table, src_file.replace('.csv', '.parquet'))


def parquet_to_pg(**kwargs):

    src_file = kwargs['src_file']
    table_name = kwargs['table_name']
    # df = pq.read_table(src_file).to_pandas()
    df = pq.read_table(src_file).to_pandas() # use pandas directly, since pandas uses pyarrow by default.

    dbschema='ghcnd'
    user = "root"
    password = "root"
    host = "postgres-service-ghcnd"
    port = 5432
    db = "ghcn-d"
    cmd = f'postgresql://{user}:{password}@{host}:{port}/{db}'
    engine = create_engine(cmd, connect_args={'options': f'-csearch_path={dbschema}'})
    df.to_sql(table_name, engine, if_exists='append')

default_args = {
    "owner": "airflow",
    "start_date": datetime.now(),
    "end_date": datetime.now() + timedelta(days=1),
    "depends_on_past": False,
    "retries": 0,
}


# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="aws_pg_other_datasets_job",
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['ghcnd'],
) as dag:

    for file_id in origin_file_ids:
        
        txt_file_name = f'/ghcnd-{file_id}.txt'
        dataset_url = URL_PREFIX + txt_file_name
        txt_file_path = TEMP_STORAGE_PATH + txt_file_name
        csv_file_name = txt_file_name.replace('.txt', '.csv')
        csv_file_path = TEMP_STORAGE_PATH + csv_file_name
        parquet_file_name = txt_file_name.replace('.txt', '.parquet')
        parquet_file_path = TEMP_STORAGE_PATH + parquet_file_name
        table_name = f"{file_id}"

        download_dataset_task = BashOperator(
            task_id=f"download_dataset_{file_id}_task",
            bash_command=f"curl -sS {dataset_url} > {txt_file_path}"
        )

        convert_to_csv_task = PythonOperator(
            task_id=f"convert_to_csv_{file_id}_task",
            python_callable=convert_to_csv,
            op_kwargs={
                'src_file': txt_file_path,
                'header': headers[file_id],
                'column_indexes': column_indexes[file_id],
                'is_text_column': is_text_column[file_id]
            }
        )

        format_to_parquet_task = PythonOperator(
            task_id=f"format_to_parquet_{file_id}_task",
            python_callable=format_to_parquet,
            op_kwargs={
                "src_file": csv_file_path
            },
        )

        clear_local_files_task = BashOperator(
            task_id=f"clear_local_{file_id}_files",
            bash_command=f"rm {csv_file_path} {txt_file_path}"
        )

        create_table_task = PostgresOperator(
                task_id= f"create_pg_table_{file_id}_task",
                sql=CREATE_TABLE_QUERY[file_id],
            )

        parquet_to_pg_task = PythonOperator(
            task_id=f"parquet_to_pg_{file_id}_task",
            python_callable=parquet_to_pg,
            op_kwargs={
                "src_file": parquet_file_path,
                "table_name": table_name
            },
        )


        download_dataset_task >> convert_to_csv_task >> format_to_parquet_task >> clear_local_files_task >> create_table_task >> parquet_to_pg_task

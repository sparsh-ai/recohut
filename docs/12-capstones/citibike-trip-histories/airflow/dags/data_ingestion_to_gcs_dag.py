import os
from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from utils import format_to_parquet, upload_to_gcs


PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

csv_file = '{{ execution_date.strftime(\'%Y%m\') }}-citibike-tripdata.csv'
zip_file = f'{csv_file}.zip'
dataset_url = f'https://s3.amazonaws.com/tripdata/{zip_file}'
path_to_local_home = os.environ.get('AIRFLOW_HOME', '/opt/airflow/')
parquet_file = csv_file.replace('.csv', '.parquet')


default_args = {
    "owner": "airflow",
    "start_date": datetime(2018, 1, 1),
    "end_date": datetime(2020, 12, 31),
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="data_ingestion_to_gcs_dag",
    schedule_interval="@monthly",
    default_args=default_args,
    catchup=True,
    max_active_runs=3,
    tags=['city-bikes'],
) as dag:

    download_zip_file_task = BashOperator(
        task_id="download_zip_file_task",
        bash_command=f"curl -sSLf {dataset_url} > {path_to_local_home}/{zip_file}"
    )

    unzip_dataset_task = BashOperator(
        task_id="unzip_dataset_task",
        bash_command=f"unzip -o {path_to_local_home}/{zip_file} -d {path_to_local_home}"
    )

    format_to_parquet_task = PythonOperator(
        task_id="format_to_parquet_task",
        python_callable=format_to_parquet,
        op_kwargs={
            "src_file": f"{path_to_local_home}/{csv_file}",
        },
    )

    local_to_gcs_task = PythonOperator(
        task_id="local_to_gcs_task",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": f"city_bikes_trips/{{{{ execution_date.strftime(\'%Y\') }}}}/{parquet_file}",
            "local_file": f"{path_to_local_home}/{parquet_file}",
        },
    )

    clean_up_data_task = BashOperator(
        task_id="clean_up_data_task",
        bash_command=f"rm {path_to_local_home}/{zip_file} {path_to_local_home}/{csv_file}"
                     f" {path_to_local_home}/{parquet_file}"
    )

    download_zip_file_task >> unzip_dataset_task >> format_to_parquet_task >> local_to_gcs_task >> clean_up_data_task

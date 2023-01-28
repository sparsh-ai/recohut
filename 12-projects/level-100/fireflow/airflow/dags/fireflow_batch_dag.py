import os
import logging
import requests
import json
import pandas as pd

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from google.cloud import storage
from airflow.contrib.operators.gcs_to_bq import GCSToBigQueryOperator
import pyarrow.csv as pv
import pyarrow.parquet as pq
from datetime import date as dt

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= '../../credentials/fireflow-creds.json'

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
# path_to_local_home = "/opt/airflow/"
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", 'fireflow_dataset')

# GITHUB DATA URL
date = dt.today().strftime("%d")

customer = 'https://raw.githubusercontent.com/billiechristian/data-fellowship-fireflow/main/data/customer.csv'
education = 'https://raw.githubusercontent.com/billiechristian/data-fellowship-fireflow/main/data/education.csv'
job = 'https://raw.githubusercontent.com/billiechristian/data-fellowship-fireflow/main/data/job.csv'
salesperson = 'https://raw.githubusercontent.com/billiechristian/data-fellowship-fireflow/main/data/salesperson.csv'
sales_training = 'https://raw.githubusercontent.com/billiechristian/data-fellowship-fireflow/main/data/salesperson_training.csv'
training_course = 'https://raw.githubusercontent.com/billiechristian/data-fellowship-fireflow/main/data/training_course.csv'
fact = f'https://raw.githubusercontent.com/billiechristian/data-fellowship-fireflow/main/data/data_split/2022-01-{date}.csv'


url_list = [customer, education, job, salesperson, sales_training, training_course, fact]
local_file_name = ['customer.csv', 'education.csv', 'job.csv', 'salesperson.csv', 'sales_training.csv', 'training_course.csv', f'fact_table_{date}.csv']

def download_github_data (URL_LIST, LOCAL_FILE_NAME):
    for url, filename in zip(URL_LIST, LOCAL_FILE_NAME):
        os.system(f"curl -sSL {url} > {path_to_local_home}/{filename}")

def load_data_to_gcs(bucket, object_name, local_file_name):
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client()
    bucket = client.bucket(bucket)

    for filename, object in zip(local_file_name, object_name) :
        blob = bucket.blob(object)
        blob.upload_from_filename(f'{path_to_local_home}/{filename}')


default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="fireflow_dag",
    schedule_interval="0 10 * * *",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['data-fellowship-8'],
) as dag:

    download_github_data_task = PythonOperator(
        task_id="download_github_data_task",
        python_callable=download_github_data,
        op_kwargs={
            'URL_LIST': url_list,
            'LOCAL_FILE_NAME': local_file_name},
    )

    load_to_gcs_task = PythonOperator(
            task_id="load_to_gcs_task",
            python_callable=load_data_to_gcs,
            op_kwargs={
                "bucket": BUCKET,
                "object_name": list(map(lambda x: 'data/' + x, local_file_name)),
                "local_file_name": local_file_name,
            },
    )

    fact_table_gcs_to_bigquery_task = GCSToBigQueryOperator(
        task_id="fact_table_gcs_to_bigquery_task",
        bucket= BUCKET,
        source_objects=[f"data/fact_table_{date}.csv"],
        destination_project_dataset_table= "{}.{}.{}".format(PROJECT_ID,BIGQUERY_DATASET,"Fact_Table"),
        source_format='csv',
        skip_leading_rows=1,
        field_delimiter=',',
        schema_fields=[
        {'name': 'date', 'type': 'DATE', 'mode': 'NULLABLE'},
        {'name': 'customer_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'contact', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'duration', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'campaign', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'pdays', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'previous', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'poutcome', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'emp_var_rate', 'type': 'FLOAT', 'mode': 'NULLABLE'},
        {'name': 'cons_price_idx', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'cons_conf_idx', 'type': 'FLOAT', 'mode': 'NULLABLE'},
        {'name': 'euribor3m', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'nr_employed', 'type': 'FLOAT', 'mode': 'NULLABLE'},
        {'name': 'y', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'sales_id', 'type': 'STRING', 'mode': 'NULLABLE'},
    ],
    create_disposition='CREATE_IF_NEEDED',
    write_disposition='WRITE_APPEND',
    time_partitioning={
                        "type": "DAY",
                        # "expirationMs": string,
                        "field": "date"
                        # "requirePartitionFilter": boolean
                      })

    customer_gcs_to_biqquery= GCSToBigQueryOperator(
        task_id="customer_gcs_to_bigquery_task",
        bucket= BUCKET,
        source_objects=["data/{}.csv".format('customer')],
        destination_project_dataset_table= "{}.{}.{}".format(PROJECT_ID,BIGQUERY_DATASET,'customer'),
        source_format='csv',
        skip_leading_rows=1,
        field_delimiter=',',
        schema_fields=[
        {'name': 'id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'age', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'sex', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'job_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'marital', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'education_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'default', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'housing', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'loan', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'city', 'type': 'STRING', 'mode': 'NULLABLE'},
    ],
    create_disposition='CREATE_IF_NEEDED',
    write_disposition='WRITE_TRUNCATE')

    education_gcs_to_biqquery= GCSToBigQueryOperator(
        task_id="education_gcs_to_bigquery_task",
        bucket= BUCKET,
        source_objects=["data/{}.csv".format('education')],
        destination_project_dataset_table= "{}.{}.{}".format(PROJECT_ID,BIGQUERY_DATASET,'education'),
        source_format='csv',
        skip_leading_rows=1,
        field_delimiter=',',
        schema_fields=[
        {'name': 'education_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'education_level', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'description', 'type': 'STRING', 'mode': 'NULLABLE'},
    ],
    create_disposition='CREATE_IF_NEEDED',
    write_disposition='WRITE_TRUNCATE')

    job_gcs_to_biqquery= GCSToBigQueryOperator(
        task_id="job_gcs_to_bigquery_task",
        bucket= BUCKET,
        source_objects=["data/{}.csv".format('job')],
        destination_project_dataset_table= "{}.{}.{}".format(PROJECT_ID,BIGQUERY_DATASET,'job'),
        source_format='csv',
        skip_leading_rows=1,
        field_delimiter=',',
        schema_fields=[
        {'name': 'job_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'description', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'average_annual_salary', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'average_age', 'type': 'FLOAT', 'mode': 'NULLABLE'},
    ],
    create_disposition='CREATE_IF_NEEDED',
    write_disposition='WRITE_TRUNCATE')

    salesperson_gcs_to_biqquery= GCSToBigQueryOperator(
        task_id="salesperson_gcs_to_bigquery_task",
        bucket= BUCKET,
        source_objects=["data/{}.csv".format('salesperson')],
        destination_project_dataset_table= "{}.{}.{}".format(PROJECT_ID,BIGQUERY_DATASET,'salesperson'),
        source_format='csv',
        skip_leading_rows=1,
        field_delimiter=',',
        schema_fields=[
        {'name': 'id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'name', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'age', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'city', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'sex', 'type': 'INTEGER', 'mode': 'NULLABLE'},
    ],
    create_disposition='CREATE_IF_NEEDED',
    write_disposition='WRITE_TRUNCATE')

    sales_training_gcs_to_biqquery= GCSToBigQueryOperator(
        task_id="sales_training_gcs_to_bigquery_task",
        bucket= BUCKET,
        source_objects=["data/{}.csv".format('sales_training')],
        destination_project_dataset_table= "{}.{}.{}".format(PROJECT_ID,BIGQUERY_DATASET,'sales_training'),
        source_format='csv',
        skip_leading_rows=1,
        field_delimiter=',',
        schema_fields=[
        {'name': 'sales_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'training_id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'status', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'start_date', 'type': 'DATE', 'mode': 'NULLABLE'},
        {'name': 'end_date', 'type': 'DATE', 'mode': 'NULLABLE'},
    ],
    create_disposition='CREATE_IF_NEEDED',
    write_disposition='WRITE_TRUNCATE')

    training_course_gcs_to_biqquery= GCSToBigQueryOperator(
        task_id="training_course_gcs_to_bigquery_task",
        bucket= BUCKET,
        source_objects=["data/{}.csv".format('training_course')],
        destination_project_dataset_table= "{}.{}.{}".format(PROJECT_ID,BIGQUERY_DATASET,'training_course'),
        source_format='csv',
        skip_leading_rows=1,
        field_delimiter=',',
        schema_fields=[
        {'name': 'id', 'type': 'INTEGER', 'mode': 'NULLABLE'},
        {'name': 'training_course', 'type': 'STRING', 'mode': 'NULLABLE'},
        {'name': 'description', 'type': 'STRING', 'mode': 'NULLABLE'},
    ],
    create_disposition='CREATE_IF_NEEDED',
    write_disposition='WRITE_TRUNCATE')
    

    download_github_data_task >> load_to_gcs_task >> fact_table_gcs_to_bigquery_task\
    >> customer_gcs_to_biqquery >> education_gcs_to_biqquery >> job_gcs_to_biqquery\
    >> salesperson_gcs_to_biqquery >> sales_training_gcs_to_biqquery >> training_course_gcs_to_biqquery
    





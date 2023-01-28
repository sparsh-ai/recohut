import os
import logging
from datetime import datetime, timedelta

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from google.cloud import storage
from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator, BigQueryInsertJobOperator
import pyarrow.csv as pv
import pyarrow.parquet as pq

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
BIGQUERY_DATASET = os.environ.get("GCP_BQ_DATASET")
TEMP_STORAGE_PATH = os.getenv('TEMP_STORAGE_PATH', 'not-found')
URL_PREFIX = 'https://noaa-ghcn-pds.s3.amazonaws.com'

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


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    :param bucket: GCS bucket name
    :param object_name: target path & file-name
    :param local_file: source path & file-name
    :return:
    """
    # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # (Ref: https://github.com/googleapis/python-storage/issues/74)
    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB
    # End of Workaround

    client = storage.Client()
    bucket = client.bucket(bucket)

    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)

default_args = {
    "owner": "airflow",
    "start_date": datetime.now(),
    "end_date": datetime.now() + timedelta(days=1),
    "depends_on_past": False,
    "retries": 1,
}


# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="data_ingestion_other_datasets",
    schedule_interval="@once",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['ghcnd'],
) as dag:

    for id in origin_file_ids:
        
        txt_file_name = f'/ghcnd-{id}.txt'
        dataset_url = URL_PREFIX + txt_file_name
        txt_file_path = TEMP_STORAGE_PATH + txt_file_name
        csv_file_name = txt_file_name.replace('.txt', '.csv')
        csv_file_path = TEMP_STORAGE_PATH + csv_file_name
        parquet_file_name = txt_file_name.replace('.txt', '.parquet')
        parquet_file_path = TEMP_STORAGE_PATH + parquet_file_name
        parquet_object_path = f"{parquet_file_name[1:]}"
        parquet_uri = f"gs://{BUCKET}/{parquet_object_path}"
        external_table_name = f"external_table_{id}"
        table_name = f"{id}"

        download_dataset_task = BashOperator(
            task_id=f"download_dataset_{id}_task",
            bash_command=f"curl -sS {dataset_url} > {txt_file_path}"
        )

        convert_to_csv_task = PythonOperator(
            task_id=f"convert_to_csv_{id}_task",
            python_callable=convert_to_csv,
            op_kwargs={
                'src_file': txt_file_path,
                'header': headers[id],
                'column_indexes': column_indexes[id],
                'is_text_column': is_text_column[id]
            }
        )

        format_to_parquet_task = PythonOperator(
            task_id=f"format_to_parquet_{id}_task",
            python_callable=format_to_parquet,
            op_kwargs={
                "src_file": csv_file_path
            },
        )

        local_to_gcs_task = PythonOperator(
            task_id=f"local_to_gcs_{id}_task",
            python_callable=upload_to_gcs,
            op_kwargs={
                "bucket": BUCKET,
                "object_name": parquet_object_path,
                "local_file": parquet_file_path
            },
        )

        clear_local_files = BashOperator(
            task_id=f"clear_local_{id}_files",
            bash_command=f"rm {csv_file_path} {parquet_file_path} {txt_file_path}"
        )

        gcs_to_bq_ext = BigQueryCreateExternalTableOperator(
            task_id=f"gcs_to_bq_ext_{id}_task",
            table_resource={
                "tableReference": {
                    "projectId": PROJECT_ID,
                    "datasetId": BIGQUERY_DATASET,
                    "tableId": external_table_name,
                },
                "externalDataConfiguration": {
                    "sourceFormat": "PARQUET",
                    "sourceUris": [parquet_uri],
                },
            },
        )

        CREATE_TABLE_QUERY = f"CREATE OR REPLACE TABLE {PROJECT_ID}.{BIGQUERY_DATASET}.{table_name} \
            AS SELECT * FROM {PROJECT_ID}.{BIGQUERY_DATASET}.{external_table_name};"

        bq_ext_to_part = BigQueryInsertJobOperator(
            task_id=f"bq_ext_to_table_{id}_task",
            configuration={
                "query": {
                    "query": CREATE_TABLE_QUERY,
                    "useLegacySql": False,
                }
            }
        )

        download_dataset_task >> convert_to_csv_task >> format_to_parquet_task >> local_to_gcs_task >> clear_local_files >> gcs_to_bq_ext >> bq_ext_to_part

import os
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.operators.dataproc \
    import  \
        DataprocSubmitPySparkJobOperator, \
        DataprocDeleteClusterOperator, \
        DataprocCreateClusterOperator
from google.cloud import storage

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
BIGQUERY_DATASET = os.environ.get("GCP_BQ_DATASET")
REGION=os.environ.get("GCP_REGION")
START_YEAR = os.getenv("START_YEAR", "2022")
DATAPROC_CLUSTER = os.getenv("GCP_DATAPROC_CLUSTER", "ghcnd")
TEMP_STORAGE_PATH = os.getenv('TEMP_STORAGE_PATH', 'not-found')
SOURCES_PATH = os.getenv('SOURCES_PATH', 'not-found')
source_file_name = '/process_year_tables.py'
source_path_file = SOURCES_PATH + source_file_name
gcs_path_file = f'sources{source_file_name}'
gcs_source_uri = f'gs://{BUCKET}/{gcs_path_file}'

default_args = {
    "owner": "airflow",
    "start_date": datetime.now() - timedelta(days=2),
    "depends_on_past": False,
    "retries": 0,
}

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

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="data_transformation_dataproc_spark_job",
    schedule_interval="0 6 * * *",
    default_args=default_args,
    catchup=True,
    max_active_runs=1,
    tags=['ghcnd'],
) as dag:

    END_YEAR = '{{dag_run.logical_date.strftime("%Y")}}'

    """
    # Not working because of permissions error from container calling gcloud
    submit_dataproc_spark_job_task = BashOperator(
        task_id="submit_dataproc_spark_job_task",
        bash_command= ( f"gcloud dataproc jobs submit pyspark "
        "../spark/process_year_tables.py "
        f"--cluster={DATAPROC_CLUSTER} "
        f"--region={REGION} "
        f"--jars '../spark/spark-bigquery-with-dependencies_2.12-0.24.0.jar' "
        f"-- {START_YEAR} {END_YEAR}" 
        )
    )
    """

    create_dataproc_cluster_task=DataprocCreateClusterOperator(
        task_id = 'create_dataproc_cluster_task',
        project_id = PROJECT_ID,
        cluster_name = DATAPROC_CLUSTER,
        num_workers = 2,
        worker_machine_type = 'n1-standard-4',
        region = REGION,
    )

    upload_main_to_gcs_task = PythonOperator(
        task_id=f"upload_main_to_gcs_task",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": gcs_path_file,
            "local_file": source_path_file,
        },
    )

    submit_dataproc_spark_job_task = DataprocSubmitPySparkJobOperator(
        task_id = "submit_dataproc_spark_job_task",
        main = gcs_source_uri,
        arguments = [START_YEAR, f'{END_YEAR}'],
        region = REGION,
        cluster_name = DATAPROC_CLUSTER,
        dataproc_jars = ["gs://spark-lib/bigquery/spark-bigquery-with-dependencies_2.12-0.24.0.jar"]
    )

    delete_dataproc_cluster_task = DataprocDeleteClusterOperator(
        task_id = "delete_dataproc_cluster_task",
        project_id = PROJECT_ID,
        cluster_name = DATAPROC_CLUSTER,
        region = REGION,
        trigger_rule = "all_done",
    )

    create_dataproc_cluster_task >> upload_main_to_gcs_task >> submit_dataproc_spark_job_task >> delete_dataproc_cluster_task

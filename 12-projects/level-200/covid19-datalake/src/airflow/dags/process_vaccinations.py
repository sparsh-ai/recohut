from datetime import datetime

import boto3
from airflow.models.dag import DAG
from tasks import ingestion, processing

ENV = "staging"
_bucket = f"s3://data-pipeline-s3-bucket-{ENV}"

boto3_session = boto3.Session(profile_name="RedshiftIngestRole")

with DAG(
    dag_id=f"vaccinations-{ENV}",
    schedule_interval="0 9 * * *",
    catchup=False,
    start_date=datetime(2022, 12, 17),
) as dag:
    process_vacciations_task = processing.process_vaccinations(
        bucket=_bucket,
        boto3_session=boto3_session,
    )
    ingest_vaccinations_task = ingestion.ingest_into_redshift(
        bucket=_bucket,
        boto3_session=boto3_session,
    )

process_vacciations_task >> ingest_vaccinations_task

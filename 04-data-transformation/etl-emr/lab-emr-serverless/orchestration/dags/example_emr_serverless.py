import os
from datetime import datetime

from airflow import DAG
from emr_serverless.operators.emr import EmrServerlessStartJobOperator

# Replace these with your correct values
APPLICATION_ID = os.getenv("APPLICATION_ID")
JOB_ROLE_ARN = os.getenv("JOB_ROLE_ARN")
S3_BUCKET = os.getenv("S3_BUCKET")

JOB_DRIVER_ARG = {
    "sparkSubmit": {
        "entryPoint": f"s3://{S3_BUCKET}/src/py/pi.py",
    }
}

CONFIGURATION_OVERRIDES_ARG = {
    "monitoringConfiguration": {
        "s3MonitoringConfiguration": {
            "logUri": f"s3://{S3_BUCKET}/logs/"
        }
    },
}

with DAG(
    dag_id='example_emr_serverless_job',
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    tags=['example'],
    catchup=False,
) as dag:

    job_starter = EmrServerlessStartJobOperator(
        task_id="start_job",
        application_id=APPLICATION_ID,
        execution_role_arn=JOB_ROLE_ARN,
        job_driver=JOB_DRIVER_ARG,
        configuration_overrides=CONFIGURATION_OVERRIDES_ARG,
    )
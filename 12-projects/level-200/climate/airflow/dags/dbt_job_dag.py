import os
import logging
from datetime import datetime, timedelta
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from dbt_cloud_utils import dbt_cloud_job_runner

DBT_ACCOUNT_ID = int(os.environ.get("DBT_ACCOUNT_ID"))
DBT_PROJECT_ID = int(os.environ.get("DBT_PROJECT_ID"))
DBT_JOB_ID = int(os.environ.get("DBT_JOB_ID"))
DBT_API_KEY_FILE = str(os.environ.get("DBT_API_KEY_FILE"))

with open(DBT_API_KEY_FILE, 'r') as f:
    DBT_API_KEY = f.readline()

default_args = {
    "owner": "airflow",
    "start_date": datetime.now() - timedelta(days=2),
    "depends_on_past": False,
    "retries": 0,
}

dbt_cloud_job_runner_config = dbt_cloud_job_runner(
    account_id=DBT_ACCOUNT_ID,
    project_id=DBT_PROJECT_ID, 
    job_id=DBT_JOB_ID, 
    cause="run_job", 
    dbt_cloud_api_key=DBT_API_KEY
)

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="data_transformation_dbt_job",
    schedule_interval="0 6 * * *",
    default_args=default_args,
    catchup=True,
    max_active_runs=1,
    tags=['ghcnd'],
) as dag:

    run_dbt_cloud_job_task = PythonOperator(
        task_id=f"run_dbt_cloud_job_task",
        python_callable=dbt_cloud_job_runner_config.run_job,
        provide_context=True,
    )

    run_dbt_cloud_job_task   


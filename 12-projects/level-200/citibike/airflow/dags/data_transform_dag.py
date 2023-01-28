from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="data_transform_dag",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['city-bikes'],
) as dag:

    run_dbt_task = BashOperator(
        task_id="run_dbt_task",
        bash_command="cd /dbt && dbt deps && dbt build --profiles-dir ."
    )

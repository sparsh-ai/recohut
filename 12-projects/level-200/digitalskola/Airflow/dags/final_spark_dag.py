from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago 


# DAG Definition
default_args = {
	'owner': 'athoillah',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='etl_spark',
    description='Final-Project : extract from csv using spark transform and load to PostgreSQL',
    start_date = days_ago(1),
    schedule_interval = None,
) as dag:

    # Start job
    job_start = DummyOperator(
        task_id = "job_start"
        )

    
    # ETL TestData from csv to postgres
    TestData_to_postgres = BashOperator(
    	task_id = 'TestData_to_Postgres',
    	bash_command='python3 /home/athoillah/Final/Local/Extract_Spark/etl_test.py '
        )

    # ETL TrainData from csv to postgres
    TrainData_to_postgres = BashOperator(
    	task_id = 'TrainData_to_Postgres',
    	bash_command='python3 /home/athoillah/Final/Local/Extract_Spark/etl_train.py '
        )


    # Finish job
    job_finish = DummyOperator(
        task_id = "job_finish"
        )


    # Orchestration
    (
        job_start
        >> [TrainData_to_postgres, TestData_to_postgres]
        >> job_finish
    )
from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.postgres_operator import PostgresOperator
# from airflow.operators.sensors import ExternalTaskSensor
from airflow.sensors.base import BaseSensorOperator
from airflow.utils.task_group import TaskGroup
from airflow.utils.dates import days_ago 

# DAG Definition
default_args = {
	'owner': 'athoillah',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    default_args=default_args,
    dag_id='etl_dimension_table',
    description='Final-Project : Making Dimension Table, Depend on other work',
    start_date = days_ago(1),
    schedule_interval = None,
) as dag:

    # Start job
    job_start = DummyOperator(
        task_id = "job_start"
        )

    # ext1 = ExternalTaskSensor(
    #     task_id='mongodb_dag_complete',
    #     external_dag_id='etl_mongodb',
    #     external_task_id=None,  # wait for whole DAG to complete
    #     check_existence=True
    # )

    # ext2 = ExternalTaskSensor(
    #     task_id='spark_dag_complete',
    #     external_dag_id='etl_spark',
    #     external_task_id=None,  # wait for whole DAG to complete
    #     check_existence=True
    # )

    # Extract data from MongoDB
    mongodb_etl_zips = BashOperator(
    	task_id = 'mongodb_etl_zips',
    	bash_command='python3 /home/athoillah/Final/Local/Extract_MongoDB/etl-zips-mongodb.py'
        )

    mongodb_etl_companies = BashOperator(
    	task_id = 'mongodb_etl_companies',
    	bash_command='python3 /home/athoillah/Final/Local/Extract_MongoDB/etl-companies-mongodb.py'
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

    # Dim Tables
    dim_country = BashOperator(
        task_id="dim_country",
        bash_command="python3 /home/athoillah/Final/Local/Datawarehouse/Dimension_table/dim_country.py",
        dag=dag
    )

    dim_state = BashOperator(
        task_id="dim_state",
        bash_command="python3 /home/athoillah/Final/Local/Datawarehouse/Dimension_table/dim_state.py",
        dag=dag
    )

    dim_city = BashOperator(
        task_id="dim_city",
        bash_command="python3 /home/athoillah/Final/Local/Datawarehouse/Dimension_table/dim_city.py",
        dag=dag
    )

    dim_currency = BashOperator(
        task_id="dim_currency",
        bash_command="python3 /home/athoillah/Final/Local/Datawarehouse/Dimension_table/dim_currency.py",
        dag=dag
    )

    # Finish job
    job_finish = DummyOperator(
        task_id = "job_finish"
        )

    # dummy job
    breathing = DummyOperator(
        task_id = "breathing"
        )


    # Orchestration
    depend_on = (job_start >> [mongodb_etl_companies, mongodb_etl_zips] >> breathing >> [TrainData_to_postgres, TestData_to_postgres])
    (
        depend_on
        >> dim_country
        >> dim_state
        >> dim_city
        >> dim_currency
        >> job_finish
    )
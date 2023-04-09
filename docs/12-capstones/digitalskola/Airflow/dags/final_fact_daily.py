from datetime import datetime
from datetime import timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.bash_operator import BashOperator
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
    dag_id='etl_fact_table_daily',
    description='Final-Project : Making Fact Table, Depend on other work',
    start_date = days_ago(1),
    schedule_interval = '@daily',
) as dag:
    # Start job
    job_start = DummyOperator(
        task_id = "job_start"
        )

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

    office_per_state = PostgresOperator(
        task_id='Count_Office_per_State',
        postgres_conn_id='twitter_etl_conn',
        sql="/home/athoillah/Final/Local/Datawarehouse/Fact_table/fact_office_per_state.sql"
    )

    currency_daily = PostgresOperator(
        task_id="average_currency",
        postgres_conn_id='twitter_etl_conn',
        sql="/home/athoillah/Final/Local/Datawarehouse/Fact_table/fact_avg_curr_daily.sql"
    )

    #Orchestration
    depend_on = (job_start >> [mongodb_etl_companies, mongodb_etl_zips] >> breathing >> [TrainData_to_postgres, TestData_to_postgres] >> dim_country >> dim_state >> dim_city >> dim_currency)
    
    (
        depend_on
        >> office_per_state
        >> currency_daily
        >> job_finish
    )
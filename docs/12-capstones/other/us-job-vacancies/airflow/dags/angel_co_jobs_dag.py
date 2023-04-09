from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from helpers import SqlQueries
from crawlers.angel_co import main as angel_co_scraper
from crawlers.angel_co_parser import main as angel_co_crawler

default_args = {
    'owner': 'gabriel',
    'start_date': datetime(2019, 10, 19),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=300)
}

dag = DAG('angel_co_jobs_dag',
          default_args=default_args,
          description='Load the jobs dataset and insert into PostgreSQL',
          schedule_interval='@daily',
          catchup=False
        )

# 1st step - download all htmls

run_selenium_scraper = PythonOperator(
    dag=dag,
    task_id='run_selenium_scraper',
    provide_context=False,
    python_callable=angel_co_scraper
)

# 2nd step - Parse all HTMLs into simple python data structures and insert into the jobs, companies and tags tables
# Mostly another python operator
run_crawler_on_scraped_data = PythonOperator(
    dag=dag,
    task_id='run_crawler_on_scraped_data',
    provide_context=False,
    python_callable=angel_co_crawler
)

# 3rd step - Delete all the HTML page files
# Yet Another python operator

run_selenium_scraper >> run_crawler_on_scraped_data

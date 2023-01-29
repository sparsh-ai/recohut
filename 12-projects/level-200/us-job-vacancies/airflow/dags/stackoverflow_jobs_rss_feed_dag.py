from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (StageStackoverflowJobsOperator, LoadFactOperator,
                                LoadDimensionOperator, DataQualityOperator)
from helpers import SqlQueries

default_args = {
    'owner': 'gabriel',
    'start_date': datetime(2019, 10, 19),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=300)
}

dag = DAG('stackoverflow_jobs_rss_feed_dag',
          default_args=default_args,
          description='Load the jobs dataset and insert into PostgreSQL',
          schedule_interval='@daily',
          catchup=False
        )

stage_stackoverflow_jobs = StageStackoverflowJobsOperator(
    task_id='stage_stackoverflow_jobs',
    dag=dag,
    pgsql_conn_id="pgsql",
    http_conn_id="stackoverflow_jobs",
)

check_staging_stackoverflow_jobs_table = DataQualityOperator(
    task_id='check_staging_stackoverflow_jobs_table',
    dag=dag,
    pgsql_conn_id="pgsql",
    tables=['staging_stackoverflow_jobs']
)

upsert_companies_dimension_table = LoadDimensionOperator(
    task_id='upsert_companies_dimension_table',
    dag=dag,
    table='companies',
    pgsql_conn_id="pgsql",
    select_query=SqlQueries.select_companies_from_stackoverflow_jobs
)

upsert_tags_dimension_table = LoadDimensionOperator(
    task_id='upsert_tags_dimension_table',
    dag=dag,
    table='tags',
    pgsql_conn_id="pgsql",
    select_query=SqlQueries.select_tags_from_stackoverflow_jobs
)

upsert_job_vacancies_fact_table = LoadFactOperator(
    task_id='upsert_job_vacancies_fact_table',
    dag=dag,
    table='job_vacancies',
    pgsql_conn_id="pgsql",
    select_query=SqlQueries.select_job_vacancies_from_stackoverflow_jobs
)

check_dimensions_tables = DataQualityOperator(
    task_id='check_dimensions_tables',
    dag=dag,
    pgsql_conn_id="pgsql",
    tables=['companies', 'tags']
)

check_fact_table = DataQualityOperator(
    task_id='check_fact_table',
    dag=dag,
    pgsql_conn_id="pgsql",
    tables=['job_vacancies'],
    where_parameters="provider_id = 'stackoverflow_jobs'"
)

stage_stackoverflow_jobs >> check_staging_stackoverflow_jobs_table

check_staging_stackoverflow_jobs_table >> upsert_companies_dimension_table
check_staging_stackoverflow_jobs_table >> upsert_tags_dimension_table
check_staging_stackoverflow_jobs_table >> upsert_job_vacancies_fact_table

upsert_companies_dimension_table >> check_dimensions_tables
upsert_tags_dimension_table >> check_dimensions_tables

upsert_job_vacancies_fact_table >> check_fact_table
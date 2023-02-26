from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators import (
    StageCsvToRedshiftOperator, PostgresOperator, StageJsonToRedshiftOperator,
    LoadDimensionOperator, LoadFactOperator, DataQualityOperator
)
from helpers import SqlQueries

default_args = {
    'owner': 'gabriel',
    'start_date': datetime(2006, 1, 1),
    'end_date': datetime(2017, 1, 1),
    'depends_on_past': True,
    'retries': 1,
    'retry_delay': timedelta(seconds=300)
}

dag = DAG('jobtechdev_se_historical_jobs_dag',
          default_args=default_args,
          description='Load the jobs dataset and insert into Redshift',
          schedule_interval='@yearly',
          max_active_runs=1,
          catchup=False
        )

recreate_staging_jobtechdev_jobs_table = PostgresOperator(
    task_id="recreate_staging_jobtechdev_jobs_table",
    dag=dag,
    postgres_conn_id="redshift",
    sql=SqlQueries.recreate_staging_jobtechdev_jobs_table
)

staging_jobtechdev_jobs = StageJsonToRedshiftOperator(
    task_id='staging_jobtechdev_jobs',
    dag=dag,
    table="staging_jobtechdev_jobs",
    redshift_conn_id="redshift",
    aws_credentials_id="aws_credentials",
    s3_bucket="social-wiki-datalake",
    s3_key="capstone/jobtechdev-historical/{ds_year}.json",
    json_path="s3://social-wiki-datalake/capstone/jobtechdev_se_historical_json_path.json",
    extra_copy_parameters="DATEFORMAT AS 'YYYY-MM-DD'"
)

check_staging_jobtechdev_jobs_table = DataQualityOperator(
    task_id='check_staging_jobtechdev_jobs_table',
    dag=dag,
    redshift_conn_id="redshift",
    tables=['staging_jobtechdev_jobs']
)

upsert_companies_dimension_table = LoadDimensionOperator(
    task_id='upsert_companies_dimension_table',
    dag=dag,
    table='companies',
    redshift_conn_id="redshift",
    select_query=SqlQueries.select_jobtechdev_companies_from_staging
)

upsert_job_vacancies_fact_table = LoadFactOperator(
    task_id='upsert_job_vacancies_fact_table',
    dag=dag,
    table='job_vacancies',
    redshift_conn_id="redshift",
    select_query=SqlQueries.select_jobtechdev_jobs_from_staging
)

check_dimensions_tables = DataQualityOperator(
    task_id='check_dimensions_tables',
    dag=dag,
    redshift_conn_id="redshift",
    tables=['companies']
)

check_fact_table = DataQualityOperator(
    task_id='check_fact_table',
    dag=dag,
    redshift_conn_id="redshift",
    tables=['job_vacancies'],
    where_parameters="provider_id = 'jobtechdevse'"
)

# Re-Create the staging table
# Stage all the JSON data from diverses years with a COPY command (paralellize the years? Yes!)
# Run the query to copy the data from the staging table to the fact/dimensions table
#   | -> First the dimensions (tags and companies)
#   | -> Then the fact (job_vacancies)

recreate_staging_jobtechdev_jobs_table >> staging_jobtechdev_jobs

staging_jobtechdev_jobs >> check_staging_jobtechdev_jobs_table

check_staging_jobtechdev_jobs_table >> upsert_companies_dimension_table
check_staging_jobtechdev_jobs_table >> upsert_job_vacancies_fact_table

upsert_companies_dimension_table >> check_dimensions_tables
upsert_job_vacancies_fact_table >> check_fact_table

from datetime import datetime, timedelta
import os
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.base_hook import BaseHook
from airflow.hooks.postgres_hook import PostgresHook
from algoliasearch.search_client import SearchClient
from airflow.sensors.external_task_sensor import ExternalTaskSensor

def index_jobs(**context):
    global algolia_conn_id

    pgsql = PostgresHook(postgres_conn_id="pgsql")
    cur = pgsql.get_cursor()

    algolia_conn = BaseHook.get_connection('algolia')
    client = SearchClient.create(algolia_conn.login, algolia_conn.password)
    index = client.init_index('jobs')
    
    jobs_sql_query = """
      SELECT 
        j.id AS objectID,
        j.provider_id AS provider_id,
        j.remote_id_on_provider AS remote_id_on_provider,
        j.remote_url AS remote_url,
        j.location AS location,
        j.currency_code AS currency_code,
        j.company_id AS company_id,
        j.company_name AS company_name,
        j.title AS title,
        j.description AS description,
        j.tags AS tags,
        j.salary AS salary,
        j.salary_max AS salary_max,
        j.salary_frequency AS salary_frequency,
        j.has_relocation_package AS has_relocation_package,
        j.expires_at AS expires_at,
        j.published_at AS published_at,
        c.id AS child_company_id,
        c.name AS child_company_name,
        c.remote_url AS child_company_remote_url,
      FROM job_vacancies j
        LEFT JOIN companies c ON (c.id = j.company_id)
      WHERE
        CAST(j.published_at AS DATE) = '{}'::DATE
    """.format(context['execution_date'])

    cur.execute(jobs_sql_query)
    rows = cur.fetchall()
    index.save_objects(rows)

def sensor_date(dt):
    return dt.replace(hour=0, minute=0, second=0)

default_args = {
    'owner': 'gabriel',
    'start_date': datetime(2019, 10, 19),
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=300)
}


dag = DAG('algoliasearch_index_jobs_dag',
          default_args=default_args,
          description='Index all jobs from our PostgreSQL database',
          schedule_interval='@daily',
          catchup=False
        )

wait_stackoverflow_jobs_rss_feed_dag = ExternalTaskSensor(
    task_id='wait_stackoverflow_jobs_rss_feed_dag',
    external_dag_id='stackoverflow_jobs_rss_feed_dag',
    external_task_id=None,
    execution_date_fn=sensor_date,
    dag=dag, mode='reschedule'
)

wait_landing_jobs_api_dag = ExternalTaskSensor(
    task_id='wait_landing_jobs_api_dag',
    external_dag_id='landing_jobs_api_dag',
    external_task_id=None,
    execution_date_fn=sensor_date,
    dag=dag, mode='reschedule'
)

wait_github_jobs_api_dag = ExternalTaskSensor(
    task_id='wait_github_jobs_api_dag',
    external_dag_id='github_jobs_api_dag',
    external_task_id=None,
    execution_date_fn=sensor_date,
    dag=dag, mode='reschedule'
)

wait_angel_co_jobs_dag = ExternalTaskSensor(
    task_id='wait_angel_co_jobs_dag',
    external_dag_id='angel_co_jobs_dag',
    external_task_id=None,
    execution_date_fn=sensor_date,
    dag=dag, mode='reschedule'
)

index_jobs_task = PythonOperator(
    dag=dag,
    task_id='index_jobs_task',
    provide_context=True,
    python_callable=index_jobs
)

wait_stackoverflow_jobs_rss_feed_dag >> index_jobs_task
wait_landing_jobs_api_dag >> index_jobs_task
wait_github_jobs_api_dag >> index_jobs_task
wait_angel_co_jobs_dag >> index_jobs_task

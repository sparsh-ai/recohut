from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
import datetime

DAG_ID = "patent_analytics_drop_create_table_dag"
with DAG(
    dag_id=DAG_ID,
    start_date=datetime.datetime(2022, 9, 1),
    catchup=False,
) as dag:
    create_tables = PostgresOperator(
        task_id="create_tables",
        postgres_conn_id="redshift",
        sql="sql/drop_create_tables.sql",
    )

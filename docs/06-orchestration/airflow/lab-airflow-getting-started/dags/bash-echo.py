# Building a simple Bash command echo pipeline with Airflow

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
        'depends_on_past': False,
        'email': ['sprsag@gmail.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes=5),
        'owner': 'sparsh'
        }

with DAG(
    'Training-DAG-1',
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
    default_args=default_args,
) as dag:

    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )

    t3 = BashOperator(
        task_id='templated',
        depends_on_past=False,
        bash_command='echo "Hello World!"',
    )

    t1 >> [t2, t3]
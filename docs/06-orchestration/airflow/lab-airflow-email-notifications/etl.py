import os
import datetime as dt

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator


with DAG('etl',
    description='An Airflow DAG running dbt and Great Expectations tasks',
    schedule_interval=None,
    start_date=dt.datetime(2021, 1, 1),
    catchup=False,
    render_template_as_native_obj=True
    ) as dag:
    
    root_path="{{ dag_run.conf['root_path'] }}"
    profiles_dir = os.path.join(root_path, "dbt")
    data_context_root_dir = os.path.join(root_path, "great_expectations")
    
    ge_validate = BashOperator(
        task_id="ge_validate",
        bash_command=f"""
        cd {data_context_root_dir} && \
        great_expectations checkpoint run \
        yellow_tripdata_sample_2019_01
        """,
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command=f"""
        dbt run \
        --profiles-dir {profiles_dir} --project-dir {profiles_dir}
        """,
    )
    
    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")
    
    send_email = EmailOperator(
        task_id='send_email',
        to='user1@gmail.com',
        subject='Airflow Alert',
        html_content=f"""<h3>Data Validated and Transformed Successfully!</h3> """,
        dag=dag
        )
    
    send_email_1 = EmailOperator(
        task_id='send_email_1',
        to='user2@gmail.com',
        subject='Airflow Alert',
        html_content=f"""<h3>Hi user2, <br>Data Validated and Transformed Successfully!</h3> """,
        dag=dag
        )
    
    send_email_2 = EmailOperator(
        task_id='send_email_2',
        to='user3@gmail.com',
        subject='Airflow Alert',
        html_content=f"""<h3>Hi user3, <br>Data Validated and Transformed Successfully!</h3> """,
        dag=dag
        )
    
    send_email_3 = EmailOperator(
        task_id='send_email_3',
        to='user4@gmail.com',
        subject='Airflow Alert',
        html_content=f"""Hi user4, <br>Data Validated and Transformed Successfully!""",
        dag=dag
        )

    chain(
        begin,
        ge_validate,
        dbt_run,
        send_email,
        send_email_1,
        send_email_2,
        send_email_3,
        end,
    )

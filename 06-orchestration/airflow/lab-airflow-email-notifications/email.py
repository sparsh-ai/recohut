import datetime as dt
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.email_operator import EmailOperator
from airflow.models.baseoperator import chain


with DAG('dummy_dag',
    description='An Airflow DAG running dbt and Great Expectations tasks',
    schedule_interval=None,
    start_date=dt.datetime(2022, 7, 21),
    catchup=False,
    render_template_as_native_obj=True
    ) as dag:
    
    send_email_1 = EmailOperator(
        task_id='send_email_1',
        to='user1@gmail.com',
        subject='Airflow Alert',
        html_content=f"""<h3>Hi user1, \nData Validated and Transformed Successfully!</h3> """,
        dag=dag
        )
    
    send_email_2 = EmailOperator(
        task_id='send_email_2',
        to='user2@gmail.com',
        subject='Airflow Alert',
        html_content=f"""<h3>Hi user2, \nData Validated and Transformed Successfully!</h3> """,
        dag=dag
        )
    
    send_email_3 = EmailOperator(
        task_id='send_email_3',
        to='user3@gmail.com',
        subject='Airflow Alert',
        html_content=f"""<h3>Hi user3, \nData Validated and Transformed Successfully!</h3> """,
        dag=dag
        )
    
    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")


    chain(
        begin,
        send_email_1,
        send_email_2,
        send_email_3,
        end,
    )

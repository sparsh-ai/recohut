import datetime as dt
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from airflow.models.baseoperator import chain
from airflow.utils.email import send_email

email_to = 'sparsh.cloud@gmail.com'

def failure_function(context):
    dag_run = context.get('dag_run')
    msg = "The folder you are trying to open doesn't exist hence the task has Failed."
    subject = f"DAG {dag_run} Failed"
    send_email(to=email_to, subject=subject, html_content=msg)

def success_function(context):
    dag_run = context.get('dag_run')
    msg = "Echoed Hello hence the task has executed successfully."
    subject = f"DAG {dag_run} has completed"
    send_email(to=email_to, subject=subject, html_content=msg)
    
# def success_function_folderavailable(context):
#     dag_run = context.get('dag_run')
#     msg = "Folder opened successfully."
#     subject = f"DAG {dag_run} has completed"
#     send_email(to=email_to, subject=subject, html_content=msg)


with DAG('SPR_EMAIL_NOTIFICATION',
         description='A simple job to nofity user about the execution status of their specified tasks.',
         schedule_interval=None,
         start_date=dt.datetime(2022, 10, 21),
         catchup=False) as dag:

    begin = DummyOperator(task_id="begin")
    
    say_hello = BashOperator(
        task_id='say_hello',
        on_failure_callback=failure_function,
        on_success_callback=success_function,
        bash_command='echo Hello' 
    )

    open_temp_folder = BashOperator(
        task_id='open_temp_folder',
        on_failure_callback=failure_function,
        on_success_callback=success_function_folderavailable,
        bash_command='cd temp_folder'
    )

    end = DummyOperator(task_id="end")
    
    chain(
        begin,
        say_hello,
        open_temp_folder,
        end)


# with DAG('SPR_EMAIL_NOTIFICATION',
#     description='An Airflow DAG to send the dag status over email',
#     schedule_interval=None,
#     start_date=dt.datetime(2022, 10, 21),
#     catchup=False,
#     render_template_as_native_obj=True,
#     on_failure_callback=send_email
#     ) as dag:
    
#     send_email_1 = EmailOperator(
#         task_id='send_email_1',
#         to='sparsh.cloud@gmail.com',
#         subject='Airflow Alert',
#         html_content=f"""<h3>Hi Sparsh, \nData Validated and Transformed Successfully!</h3> """,
#         dag=dag
#         )
    
#     begin = DummyOperator(task_id="begin")
#     end = DummyOperator(task_id="end")

#     chain(
#         begin,
#         send_email_1,
#         end,
#     )

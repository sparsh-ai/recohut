import os
from datetime import timedelta

from airflow import DAG
from airflow.models import Variable
from airflow.models.baseoperator import chain
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.providers.amazon.aws.operators.sns import SnsPublishOperator
from airflow.providers.slack.operators.slack_webhook import SlackWebhookOperator
from airflow.utils.dates import days_ago

DAG_ID = os.path.basename(__file__).replace(".py", "")

DEFAULT_ARGS = {
    "owner": "sparsh",
    "depends_on_past": False,
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}


def _slack_failure_notification(context):
    slack_msg = f"""
            :red_circle: DAG Failed.
            *Task*: {context.get('task_instance').task_id}
            *Dag*: {context.get('task_instance').dag_id}
            *Execution Time*: {context.get('execution_date')}
            *Log Url*: {context.get('task_instance').log_url}
            """
    # find the slack_webhook with "airflow connections list"
    failed_alert = SlackWebhookOperator(
        task_id="slack_notification", http_conn_id="slack_webhook", message=slack_msg
    )

    return failed_alert.execute(context=context)


def _slack_success_notification(context):
    slack_msg = f"""
            :large_green_circle: DAG Succeeded.
            *Task*: {context.get('task_instance').task_id}
            *Dag*: {context.get('task_instance').dag_id}
            *Execution Time*: {context.get('execution_date')}
            *Log Url*: {context.get('task_instance').log_url}
            """
    # find the slack_webhook with "airflow connections list"
    success_alert = SlackWebhookOperator(
        task_id="slack_notification", http_conn_id="slack_webhook", message=slack_msg
    )

    return success_alert.execute(context=context)


with DAG(
    dag_id=DAG_ID,
    description="Run all DAGs",
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=45),
    start_date=datetime(2023, 3, 1),
    schedule_interval=None,
    on_failure_callback=_slack_failure_notification,
    on_success_callback=_slack_success_notification,
    tags=["spotify table"],
) as dag:

    trigger_task1 = TriggerDagRunOperator(
        task_id="trigger_task1",
        trigger_dag_id="t1_create_tables",
        wait_for_completion=True,
    )

    trigger_task2 = TriggerDagRunOperator(
        task_id="trigger_task2",
        trigger_dag_id="t2_data_ingestion",
        wait_for_completion=True,
    )

    trigger_task3 = TriggerDagRunOperator(
        task_id="trigger_task3",
        trigger_dag_id="t3_unload_data",
        wait_for_completion=True,
    )

    trigger_task4 = TriggerDagRunOperator(
        task_id="trigger_task4",
        trigger_dag_id="t4_glue_catelog_query",
        wait_for_completion=True,
    )
    (trigger_task1 >> trigger_task2 >> trigger_task3 >>trigger_task4)

"""
Validate the data from the fetched json files - assert data for all relevant days has been collected (excluding bank holidays and weekends).
"""
import glob
import logging
import re
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

import pandas as pd
from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.email import EmailOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.sensors.external_task import ExternalTaskSensor


dag_id = "exchange_rates_validate"
currencies = ["eur", "usd"]
project_directory = "/home/user/exchange_rates/"
year = "{{ macros.ds_format(ds, '%Y-%m-%d', '%Y') }}"
bank_holidays_file_path = f"{project_directory}bank_holidays/bank_holidays_poland_{year}.csv"
sensor_tasks = []


def _fetch_last_day_of_year(execution_date):
    """Returns 31 Decemeber of the current year as a datetime object."""
    return execution_date + relativedelta(years=1, days=-1)


def all_days(year):
    date_list = []
    start = date(year, 1, 1)
    while start.year == year:
        date_list.append(start)
        start += timedelta(days=1)
    return set(date.strftime("%Y-%m-%d") for date in date_list)


def all_bank_holidays(file_path):
    holidays = pd.read_csv(file_path)
    return set(holidays["Date"])


def all_weekends(year):
    date_list = []
    d_sat = date(year, 1, 1)
    d_sat += timedelta(days=5 - d_sat.weekday())
    while d_sat.year == year:
        date_list.append(d_sat)
        d_sun = d_sat + timedelta(days=1)
        if d_sun.year == year:
            date_list.append(d_sun)
        else:
            break
        d_sat += timedelta(days=7)
    return set(date.strftime("%Y-%m-%d") for date in date_list)


def all_working_days(year, file_path):
    return all_days(year) - all_weekends(year) - all_bank_holidays(file_path)


def all_file_dates(project_directory, year, currency):
    files = glob.glob(f"{project_directory}{year}/{currency}/*-*-*")
    return set(re.findall("\d{4}-\d{2}-\d{2}$",file)[-1] for file in files)


def _validate_data(project_directory, year, currencies, file_path):
    checks_passed = 0
    year = int(year)
    for currency in currencies:
        if all_file_dates(project_directory, year, currency) == all_working_days(year, file_path):
            checks_passed += 1
        else:
            logging.warning(f"Check for currency {currency} has not passed.")
    if checks_passed == len(currencies):
        return "trigger_downstream_dag"
    else:
        return "send_email"


default_args = {
    "email": ["first.last@example.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 5,
    "retry_delay": timedelta(minutes=15),
}

dag = DAG(                                                     
    dag_id=dag_id,                          
    start_date=datetime(2022, 1, 1),
    schedule_interval="@yearly",
    default_args=default_args,
    max_active_runs=5,
    tags=["exchange_rates", "validate"],
)

dag.doc_md = __doc__

for currency in currencies:
    sense_last_day = ExternalTaskSensor(
        task_id=f"sense_last_day_{currency}",
        external_dag_id="exchange_rates_collect",
        external_task_id=f"download_data_{currency}",
        allowed_states=["success", "skipped"],
        execution_date_fn=_fetch_last_day_of_year,
        dag=dag,
    )

    sensor_tasks.append(sense_last_day)

sense_holidays_file = FileSensor(
    task_id="holidays_file_sensor",
    filepath=bank_holidays_file_path,
    dag=dag,
)

validate_data = BranchPythonOperator(
    task_id="validate_data",
    python_callable=_validate_data,
    op_kwargs={
        "project_directory": project_directory,
        "year": year,
        "currencies": currencies,
        "file_path": bank_holidays_file_path,
    },
    dag=dag,
)

trigger_downstream_dag = TriggerDagRunOperator(
    task_id="trigger_downstream_dag",
    trigger_dag_id="exchange_rates_transform",
    execution_date="{{ ds }}",
    reset_dag_run=True,
    dag=dag,
)

send_email = EmailOperator(
    task_id="send_email",
    subject=f"Missing exchange rates data {year}",
    to="first.last@example.com",
    html_content="Please make sure no exchange rate data is missing.",
    dag=dag,
)

sensor_tasks >> sense_holidays_file >> validate_data >> [trigger_downstream_dag, send_email]

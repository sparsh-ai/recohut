"""
Extract - Fetch exchange rates from the National Bank of Poland.
Validate - Validate the data from the fetched json files - assert data for all relevant days has been collected (excluding bank holidays and weekends).
Transform - Collect the data from the fetched json files on an annual basis.
"""

import glob
import json
import os
import logging
import re
import pandas as pd
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.providers.http.sensors.http import HttpSensor
from airflow.operators.email import EmailOperator
from airflow.operators.python import BranchPythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.sensors.external_task import ExternalTaskSensor


dag_id = "exchange_rates_etl"
http_conn_id = "http_nbp"
currencies = ["eur", "usd"]
project_directory = "/Users/sparshagarwal/Desktop/projects/de/_tmp/airflow-forex/data/exchange_rates/"
file_path = os.path.join(project_directory, "{{ macros.ds_format(ds, '%Y-%m-%d', '%Y') }}/")
file_path_current_year = f"{project_directory}{{{{ macros.ds_format(ds, '%Y-%m-%d', '%Y') }}}}/"
file_path_prev_year = f"{project_directory}{{{{ macros.ds_format(macros.ds_add(ds, -1), '%Y-%m-%d', '%Y') }}}}/"
year = "{{ macros.ds_format(ds, '%Y-%m-%d', '%Y') }}"
bank_holidays_file_path = f"{project_directory}bank_holidays/bank_holidays_poland_{year}.csv"
sensor_tasks = []


def _get_endpoint(currency):
    """Returns a currency-specific endpoint."""
    return f"a/{currency}/{{{{ ds }}}}/?format=json"


def _clean_directory(current_year_path):
    """Removes all jsons from the year folder except for the last one."""
    files = glob.glob(f"{current_year_path}/*")
    files = sorted(files)[:-2]
    for f in files:
        os.unlink(f)      


def _merge_jsons_and_save_csv(current_year_path, prev_year_path, currency, **context):
    """Merge all relevant jsons in a pandas data frame, removes unnecessary columns, and saves as a csv file."""
    file_list = glob.glob(f"{current_year_path}/*-*-*")
    file_list.extend(glob.glob(f"{prev_year_path}/*-*-*"))
    assert len(file_list) < 365, "Make sure you have no more than 365 files in the source directory."
    dfs = []
    for file in file_list:
        f = open(file)
        data = json.load(f)
        f.close()
        df = pd.json_normalize(data, meta=["code"], record_path=["rates"])
        dfs.append(df)
    output = pd.concat(dfs).sort_values("effectiveDate", ignore_index=True)
    output.rename(
        columns={
            "effectiveDate": "effective_date", 
            "mid": "current_rate",
            "code": "currency"    
        }, 
        inplace = True
    )
    output["prev_day_date"] = output["effective_date"].shift(1)
    output["prev_day_rate"] = output["current_rate"].shift(1)
    output.drop(labels=0, axis=0, inplace=True)
    output = output[["no", "currency", "effective_date", "current_rate", "prev_day_date", "prev_day_rate"]]
    output.to_csv(f"{current_year_path}/{context['dag'].dag_id}_{currency}.csv", index=False)


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
   start_date=datetime(2022, 12, 31),
   schedule_interval="@daily",
   default_args=default_args,
   max_active_runs=5,
   tags=["exchange_rates"],
)

dag.doc_md = __doc__

for currency in currencies:
    sense_data = HttpSensor(
        task_id=f"sense_data_{currency}",
        http_conn_id=http_conn_id,
        endpoint=_get_endpoint(currency),
        poke_interval=5,
        timeout=20,
        soft_fail=True,
        dag=dag,
    )

    download_data = BashOperator(
        task_id=f"download_data_{currency}",
        bash_command=\
            f"""
            mkdir -p {file_path}{currency}/ && 
                touch '{file_path}{currency}/{{{{ ds }}}}' && 
                wget {{{{ conn.http_nbp.host }}}}{_get_endpoint(currency)} -O '{file_path}{currency}/{{{{ ds }}}}'
            """,
        depends_on_past=True,
        dag=dag,
    )

    sense_data >> download_data
    

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


for currency in currencies:    
    process_data = PythonOperator(
        task_id=f"process_data_{currency}",
        python_callable=_merge_jsons_and_save_csv,
        op_kwargs={
            "current_year_path": f"{file_path_current_year}{currency}",
            "prev_year_path": f"{file_path_prev_year}{currency}",
            "currency": currency,
        },
        provide_context=True,
        dag=dag,
    )

    clean_directory = PythonOperator(
        task_id=f"clean_directory_{currency}",
        python_callable=_clean_directory,
        op_kwargs={
            "current_year_path": f"{file_path_current_year}{currency}",
        },
        dag=dag,
    )
                     
    process_data >> clean_directory
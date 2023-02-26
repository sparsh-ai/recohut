"""
Collect the data from the fetched json files on an annual basis.
"""
import glob
import json
import os
import pandas as pd
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


dag_id = "exchange_rates_transform"
currencies = ["eur", "usd"]
project_directory = "/home/yegor/projects/exchange_rates/"
file_path_current_year = f"{project_directory}{{{{ macros.ds_format(ds, '%Y-%m-%d', '%Y') }}}}/"
file_path_prev_year = f"{project_directory}{{{{ macros.ds_format(macros.ds_add(ds, -1), '%Y-%m-%d', '%Y') }}}}/"


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
   schedule_interval=None,
   default_args=default_args,
   max_active_runs=5,
   tags=["exchange_rates", "transform", "load"],
)

dag.doc_md = __doc__

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

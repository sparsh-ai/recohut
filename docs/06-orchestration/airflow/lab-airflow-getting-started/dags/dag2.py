import os
import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.empty import EmptyOperator

import pandas as pd

from faker import Faker
import csv


def generate_csv(save_path):
    print("Generating CSV file...")
    os.makedirs(save_path, exist_ok=True)
    output=open(os.path.join(save_path, 'data2.csv'), 'w')
    fake=Faker()
    header=['name','age','street','city','state','zip','lng','lat']
    mywriter=csv.writer(output)
    mywriter.writerow(header)
    for r in range(10):
        mywriter.writerow([fake.name(),fake.random_int(min=18, max=80, step=1), fake.street_address(), fake.city(),fake.state(),fake.zipcode(),fake.longitude(),fake.latitude()])
    output.close()


def csv_to_json(read_path, save_path):
    print("Converting CSV to JSON...")
    os.makedirs(read_path, exist_ok=True)
    os.makedirs(save_path, exist_ok=True)
    df = pd.read_csv(os.path.join(read_path, "data.csv"))
    for i, r in df.iterrows():
        print(r['name'])
    df.head().to_json(os.path.join(save_path, "fromAirflow.json"), orient='split')
    

default_args = {
    'owner': 'sparsh',
    'start_date': dt.datetime(2022, 7, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=50),
}


with DAG('CSV-to-JSON-Pipeline',
         default_args=default_args,
         schedule_interval=None,      # '0 * * * *',
         catchup=False,
         ) as dag:
    
    raw_path="{{ dag_run.conf['raw_path'] }}"
    refined_path="{{ dag_run.conf['refined_path'] }}"
    
    start_task = EmptyOperator(task_id="start")
    end_task = EmptyOperator(task_id="end")
    
    generateCSV = PythonOperator(task_id='generateCSV',
                                      python_callable=generate_csv,
                                      op_kwargs={"save_path": raw_path})
    
    convertCSVtoJson = PythonOperator(task_id='convertCSVtoJson',
                                      python_callable=csv_to_json,
                                      op_kwargs={"read_path": raw_path,
                                                 "save_path": refined_path})


start_task >> generateCSV >> convertCSVtoJson >> end_task
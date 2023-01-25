"""
# CSV To JSON ETL Pipeline

Building data pipeline to generate synthetic data and convert it to json.

1. Extract - Generate synthetic data using faker and save as csv
1. Transform - Convert csv to json
1. Load - Save the transformed data as json file at the given path
"""

import os
import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import pandas as pd

from faker import Faker
import csv


def generate_csv(save_path):
    print("Generating CSV file...")
    os.makedirs(save_path, exist_ok=True)
    output=open(os.path.join(save_path, 'data.csv'), 'w')
    fake=Faker()
    header=['name','age','street','city','state','zip','lng','lat']
    mywriter=csv.writer(output)
    mywriter.writerow(header)
    for r in range(1000):
        mywriter.writerow([fake.name(),fake.random_int(min=18, max=80, step=1), fake.street_address(), fake.city(),fake.state(),fake.zipcode(),fake.longitude(),fake.latitude()])
    output.close()


def csv_to_json(read_path, save_path):
    print("Converting CSV to JSON...")
    os.makedirs(read_path, exist_ok=True)
    os.makedirs(save_path, exist_ok=True)
    df = pd.read_csv(os.path.join(read_path, "data.csv"))
    for i, r in df.iterrows():
        print(r['name'])
    df.to_json(os.path.join(save_path, "fromAirflow.json"), orient='records')
    

default_args = {
    'owner': 'sparsh',
    'start_date': dt.datetime(2022, 7, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=50),
}


with DAG('MyCSVDAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=50),      # '0 * * * *',
         ) as dag:
    
    raw_path="{{ dag_run.conf['raw_path'] }}"
    refined_path="{{ dag_run.conf['refined_path'] }}"
    
    generateCSV = PythonOperator(task_id='generateCSV',
                                      python_callable=generate_csv,
                                      op_kwargs={"save_path": raw_path})
    
    convertCSVtoJson = PythonOperator(task_id='convertCSVtoJson',
                                      python_callable=csv_to_json,
                                      op_kwargs={"read_path": raw_path,
                                                 "save_path": refined_path})


generateCSV >> convertCSVtoJson

# config in gcs composer
# {"raw_path":"/home/airflow/gcs/data/raw", "refined_path":"/home/airflow/gcs/data/refined"}
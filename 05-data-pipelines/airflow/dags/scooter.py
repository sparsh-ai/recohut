"""
# Airflow Scooter ETL

Build an Airflow ETL pipeline using Scooter dataset
"""

import os
import datetime as dt
from datetime import timedelta

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

import pandas as pd


def clean_scooter(read_path, save_path):
    print("Cleaning Scooter data...")
    os.makedirs(read_path, exist_ok=True)
    os.makedirs(save_path, exist_ok=True)
    df=pd.read_csv(os.path.join(read_path, 'scooter.csv'))
    df.drop(columns=['region_id'], inplace=True)
    df.columns=[x.lower() for x in df.columns]
    df['started_at']=pd.to_datetime(df['started_at'],format='%m/%d/%Y %H:%M')
    df.to_csv(os.path.join(save_path, 'cleanscooter.csv'))


def filter_data(read_path, save_path):
    print("Filtering data...")
    os.makedirs(read_path, exist_ok=True)
    os.makedirs(save_path, exist_ok=True)
    df=pd.read_csv(os.path.join(read_path, 'cleanscooter.csv'))
    fromd = '2019-05-23'
    tod='2019-06-03'
    tofrom = df[(df['started_at']>fromd)&(df['started_at']<tod)]
    tofrom.to_csv(os.path.join(save_path, 'may23-june3.csv'))
    

default_args = {
    'owner': 'sparsh',
    'start_date': dt.datetime(2022, 7, 11),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=50),
}


with DAG('ScooterDAG',
         default_args=default_args,
         schedule_interval=timedelta(minutes=50),      # '0 * * * *',
         ) as dag:
    
    raw_path="{{ dag_run.conf['raw_path'] }}"
    refined_path="{{ dag_run.conf['refined_path'] }}"
    consumption_path="{{ dag_run.conf['consumption_path'] }}"
    
    cleanScooter = PythonOperator(task_id='cleanScooter',
                                      python_callable=clean_scooter,
                                        op_kwargs={"read_path": raw_path,
                                                 "save_path": refined_path})
    
    filterData = PythonOperator(task_id='filterData',
                                      python_callable=filter_data,
                                      op_kwargs={"read_path": refined_path,
                                                 "save_path": consumption_path})


cleanScooter >> filterData

# config in local airflow
# {"raw_path":"/Users/sparshagarwal/Desktop/de-ac/airflow/data/raw",
#  "refined_path":"/Users/sparshagarwal/Desktop/de-ac/airflow/data/refined",
#  "consumption_path":"/Users/sparshagarwal/Desktop/de-ac/airflow/data/consumption"}

# config in gcs composer
# {"raw_path":"/home/airflow/gcs/data/raw",
#  "refined_path":"/home/airflow/gcs/data/refined",
#  "consumption_path":"/home/airflow/gcs/data/consumption"}
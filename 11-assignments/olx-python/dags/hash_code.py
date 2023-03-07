"""
This DAG has the functionality of extracting the raw file with
the cities of the world, filter by one country, make some transformations
and upload a JSON file into a AWS S3 Bucket
"""
import os
from zipfile import ZipFile
import json
from datetime import datetime
import pandas as pd
import geohash2 as gh
import boto3

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable

COUNTRY = Variable.get("COUNTRY")
BUCKET = Variable.get("BUCKET")
AWS_ACCESS_KEY = Variable.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = Variable.get("AWS_SECRET_KEY")
path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")


def dataframe_transformation(local_zip_path, filename, json_filename):
    """
    Function to perform data transformation.
    It performs the following steps:
    - Extracts the .csv into a pandas dataframe
    - Filters by one country
    - Extracts only some columns from the dataframe
    - Adds a Geohash Code column to the dataframe
    - Converts the dataframe into a JSON file
    :param local_zip_path:
    :param filename:
    :param json_filename:
    :return: NONE
    """
    # Get full dataframe
    with ZipFile(local_zip_path) as zip_file:
        with zip_file.open(filename) as csv_file:
            dataframe = pd.read_csv(csv_file)

    # Filter dataframe by country
    # If there is no country to filter it will return all the dataset
    if COUNTRY is None:
        print('LOG: No country to filter. Returning all the World')
        output_dataframe = dataframe
    else:
        print(f'LOG: Getting cities from {COUNTRY}..')
        output_dataframe = dataframe[dataframe.country == COUNTRY]

    # Selecting columns
    print('LOG: Selecting columns...')
    argv = ['city', 'lat', 'lng', 'population']
    out_dataframe = pd.DataFrame()
    for arg in argv:
        out_dataframe[arg] = output_dataframe[[arg]]

    # Building extra column
    print('LOG: Adding GeoHash column...')
    out_dataframe["geohash"] = out_dataframe.apply(lambda x: gh.encode(x.lat, x.lng, precision=12)
                                                   , axis=1)

    result = out_dataframe.to_json(orient="records")
    parsed = json.loads(result)
    with open(json_filename, 'w', encoding='utf-8') as file_open:
        json.dump(parsed, file_open, ensure_ascii=False, indent=4)

    print(out_dataframe.head())


def upload_to_s3(s3_path, json_filename,):
    """
    Function to upload a file into AWS S3
    :param json_filename: string with the name of the file to upload
    :param s3_path: string with the name of a s3 path without the file name
    :return: None
    """
    region_name = 'eu-west-1'
    s3_client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY
                             , aws_secret_access_key=AWS_SECRET_KEY
                             , region_name=region_name)
    try:
        s3_client.upload_file(json_filename, BUCKET, f'{s3_path}{json_filename}')
        print(f'LOG: The file {json_filename} was inserted in '
              f's3://{BUCKET}/{s3_path} with success !')
    except Exception as err:
        print(f"LOG: Some ERROR occur when inserting the file "
              f"{json_filename} in s3://{BUCKET}/{s3_path} "
              f"({err})")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id=f"Ingest_cities_from_{COUNTRY}",
    schedule_interval=None,
    default_args=default_args,
    catchup=True,
    max_active_runs=1,
    tags=['OLX'],
    start_date=datetime(2019, 1, 1)
) as dag:

    dataset_file = 'worldcities.zip'
    dataset_url = f"https://simplemaps.com/static/data/" \
                  f"world-cities/basic/simplemaps_worldcities_basicv1.75.zip"
    download_dataset_task = BashOperator(
        task_id="download_dataset_task",
        bash_command=f"curl -sSLf {dataset_url} > {path_to_local_home}/{dataset_file}"
    )

    dataframe_transformation = PythonOperator(
        task_id=f'dataframe_transformation',
        python_callable=dataframe_transformation,
        op_kwargs={
            "local_zip_path": f'{path_to_local_home}/{dataset_file}',
            "filename": f'{dataset_file.replace(".zip", ".csv")}',
            "json_filename": f'cites_from_{COUNTRY}.json',}
    )

    upload_to_s3 = PythonOperator(
        task_id=f'upload_to_s3',
        python_callable=upload_to_s3,
        op_kwargs={
            "json_filename": f'cites_from_{COUNTRY}.json',
            "s3_path": f'refined/{COUNTRY}/',
        }
    )

    remove_dataset_task = BashOperator(
        task_id=f"remove_dataset",
        bash_command=f"rm {path_to_local_home}/{dataset_file} {path_to_local_home}/cites_from_{COUNTRY}.json"
    )

    download_dataset_task >> dataframe_transformation >> upload_to_s3 >> remove_dataset_task   # pylint: disable=pointless-statement

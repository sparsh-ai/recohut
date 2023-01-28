import os
from datetime import datetime, timedelta
from time import strftime
import requests
import psycopg2
from sqlalchemy import create_engine
import pandas as pd

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType

from airflow import DAG
from airflow.hooks.base_hook import BaseHook
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.amazon.aws.operators.glue_crawler import GlueCrawlerOperator
from airflow.models import Variable

aws_conn = BaseHook.get_connection('aws_default')
aws_access_key = aws_conn.login
aws_secret_key = aws_conn.password
acled_bucket = Variable.get("acled_bucket")
acled_crawler_name = Variable.get("acled_crawler_name")
owner = "sparsh"

def ingest_data(date):
    """Ingest ACLED data for a given date"""

    conf = SparkConf()
    conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.4')
    conf.set('spark.hadoop.fs.s3a.aws.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
    conf.set('spark.hadoop.fs.s3a.access.key', aws_access_key)
    conf.set('spark.hadoop.fs.s3a.secret.key', aws_secret_key)
    spark = SparkSession.builder.config(conf=conf).getOrCreate()
    
    conn = BaseHook.get_connection('postgres')
    engine = create_engine(f'postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
    df = pd.read_sql_query(f"SELECT * FROM acled where event_date > '{date}'::date - '10 days'::interval and event_date <= '{date}'::date", engine)
    dataframe = spark.createDataFrame(df)
    
    if dataframe.count() == 0:
        return "No data"

    dataframe = dataframe.withColumn("event_date", F.to_date("event_date", "yyyy-MM-dd"))
    dataframe = dataframe.withColumn("fatalities", dataframe["fatalities"].cast("int"))
    dataframe = dataframe.withColumn("geo_precision", dataframe["geo_precision"].cast("int"))
    dataframe = dataframe.withColumn("inter1", dataframe["inter1"].cast("int"))
    dataframe = dataframe.withColumn("interaction", dataframe["interaction"].cast("int"))
    dataframe = dataframe.withColumn("latitude", dataframe["latitude"].cast("double"))
    dataframe = dataframe.withColumn("longitude", dataframe["longitude"].cast("double"))
    dataframe = dataframe.withColumn("time_precision", dataframe["time_precision"].cast("int"))
    dataframe = dataframe.withColumnRenamed("timestamp", "upload_date")
    dataframe = dataframe.withColumn("upload_date", F.from_unixtime("upload_date", "yyyy-MM-dd HH:mm:ss"))
    dataframe = dataframe.withColumn("upload_date", F.to_timestamp("upload_date", "yyyy-MM-dd HH:mm:ss"))

    for column in dataframe.columns:
        dataframe = dataframe.withColumn(column, F.when(F.col(column) == "", None).otherwise(F.col(column)))

    dataframe.coalesce(1).write.partitionBy('event_date').mode("append").option("mapreduce.fileoutputcommitter.marksuccessfuljobs", "false").parquet(f's3a://{acled_bucket}/acled_{owner}/')
    return "Success"

with DAG(
    dag_id="SPR_ACLED_ETL_GLUE",
    start_date=datetime(2022, 10, 22),
    schedule_interval="@weekly",
    catchup=False,
    default_args={
        "retries": 0,
        "email_on_failure": False,
        "email_on_retry": False,
        "owner": owner
    },
) as dag:

    start_task = EmptyOperator(task_id="acled_start_task", dag=dag)

    ingest_task = PythonOperator(
        task_id="acled_ingest_task",
        python_callable=ingest_data,
        op_args={"{{ds}}"},
        dag=dag,
    )
    
    glue_crawler_config = {
        'Name': f'{acled_crawler_name}_{owner}',
        'Role': 'arn:aws:iam::684199068947:role/service-role/AWSGlueServiceRole-FullS3Access',
        'DatabaseName': 'datalake',
        'Targets': {'S3Targets': [{'Path': f'{acled_bucket}/acled_{owner}'}]},
    }

    crawler_task = GlueCrawlerOperator(
        task_id = "acled_crawler_task",
        aws_conn_id='aws_default',
        config = glue_crawler_config,
        wait_for_completion=True,
        dag=dag,
    )

    end_task = EmptyOperator(task_id="acled_end_task", dag=dag)

    start_task >> ingest_task >> crawler_task >> end_task
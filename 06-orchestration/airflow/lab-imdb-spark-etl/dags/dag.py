import os
import sys
import logging
import ast 
from datetime import datetime, timedelta
import pandas as pd
import requests

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, regexp_replace, trim
from pyspark.sql.types import FloatType, IntegerType
from pyspark.sql import DataFrame
from pyspark.sql.functions import col, round

from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator


def make_dirs(path):
    """
    Create a directory in the specified path if not exist
    Args:
        path (str): full path of the directory to create
    """
    if not os.path.isdir(path):
        os.makedirs(path)


def donwload_movie_dataset(out_dir: str, urls_dict: dict, **context):
    """
    Downloads the data into p_path from the url list passed
    Args:
        out_dir (str): Download directory
        urls_dict (list): List of URL's to be downloaded
        context: Airflow context information
    """
    make_dirs(out_dir)
    for info_name, data_url in urls_dict.items():
        logging.info(f'Downloading file from {data_url}')
        if 'https:' in data_url:
            file_name = data_url.rsplit('/', 1)[1]
            download_file = os.path.join(out_dir, file_name)
            context['ti'].xcom_push(info_name, download_file)
            if os.path.isfile(download_file):
                logging.info(
                    f'File {file_name} has been already downloaded. Skipping it...')
                continue
            response = requests.get(data_url, allow_redirects=True)
            with open(download_file, 'wb') as f:
                f.write(response.content)
        else:
            context['ti'].xcom_push(info_name, data_url)

    else:
        logging.info('All files are downloaded succesfully')

@udf
def prod_companies_udf(prod_companies: str):
    """
    Extracts production company names and returns as ; delimited string
    Args:
        prod_companies (str): Production company info as list of dicts
    Returns:
        str: ; delimited string
    """
    prod_companies = ast.literal_eval(prod_companies)
    return [i['name'] for i in prod_companies] if isinstance(prod_companies, list) else []
    

def get_imdb_data(path_imdb_data: str):
    """
    Read and parse imdb data to make it more useable
    Args:
        path_imdb_data (str): imdb dataset file path
    """
    spark = SparkSession.getActiveSession()

    usecols = [
            'id',
            'title',
            'budget',
            'release_date',
            'revenue',
            'vote_average',
            'production_companies']
    
    logging.info('Reading imdb_data data')
    imdb_data = spark.read\
                        .option("header", True)\
                        .csv(path_imdb_data)\
                        .select(usecols)

    # cast budget and revenue to Int type
    imdb_data = imdb_data\
                    .withColumn('budget', col('budget').cast(IntegerType()))\
                    .withColumn('revenue', col('revenue').cast(IntegerType()))\
                    .withColumn('vote_average', col('vote_average').cast(FloatType()))


    # Filter movies with budget > 500 revenue > 0 & vote_average >= 0 in order to remove dirty data
    imdb_data = imdb_data.filter((imdb_data.budget > 500)\
                                & (imdb_data.revenue > 0)\
                                & (imdb_data.vote_average > 0))

    # Production companies is a list of dict, so converting it to a string delimited
    imdb_data = imdb_data.withColumn('production_companies', prod_companies_udf(col('production_companies')))
 
    return imdb_data

def get_high_profit_movies(df_imdb: DataFrame):
    """
    Get the first 1000 high profit movies calculating the colum ratio_rev_bud 
        as the ratio from revenue/budget and sorting in desc order
    Args:
        df_imdb (str): Imdb spark dataframe
    """
    logging.info(f'Calculating high profit movies...')
    return df_imdb.withColumn('ratio_rev_bud', round((col('revenue') / col('budget')), 2))\
                 .orderBy("ratio_rev_bud", ascending=False)\
                 .limit(1000)
                 
def parse_wiki_data(xml_wiki: str, rowTag: str):
    """
    Parses wiki xml dumps
    Args:
        xml_wiki (str): wiki dumps file
        rowTag (str): tag where start parsing docs
    """
    spark = SparkSession.getActiveSession()

    usecols = [
                'title',
                'abstract',
                'url']
        
    logging.info("Reading wiki data...")
    df_wiki = spark.read.format('xml')\
                        .option('rowTag', rowTag)\
                        .load(xml_wiki)\
                        .select(usecols)
    
    # clean title: remove Wikipedia: , genres and years into (1996) or (novel), trim and remove simbols 
    # clean abstract: remove simbols, start and end whitespace, keep only . and ,
    df_wiki = df_wiki.withColumn('title', trim(regexp_replace(col('title'), 'Wikipedia: ', '')))\
                    .withColumn('title', regexp_replace(col('title'), '\([^)]*\)', ''))\
                    .withColumn('title', regexp_replace(col('title'), '^\s0-9a-zA-Z.,$', ''))\
                    .withColumn('abstract', trim(regexp_replace(col('abstract'), '[^\s0-9a-zA-Z.,$]+', '')))   
    
    # drop title duplicates
    df_wiki = df_wiki.dropDuplicates(subset=['title'])
    
    return df_wiki

def get_wiki_data(path_wiki_data: str):
    """
    Parses and extracts required info from wiki xml dumps
        If parsed csv already exists it reads and sends back the dataframe
    Args:
        path_wiki_data (str): wiki dumps file
    """
    spark = SparkSession.getActiveSession()

    logging.info('Checking if parsed wiki dateset exists already...')
    csv_file = os.path.join(os.path.dirname(path_wiki_data),\
               os.path.basename(path_wiki_data).replace('.xml.gz', '.csv'))
    if os.path.isfile(csv_file):
        logging.info(f'Parsed file {csv_file} exists already... opening it without parse again')
        return spark.read.option("header", True).csv(csv_file)
    logging.info(f'Reading file: {path_wiki_data}')
    wiki_parsed = parse_wiki_data(path_wiki_data, 'doc', spark)
    wiki_parsed.toPandas().to_csv(csv_file, header=True, index=False)
    return wiki_parsed
    
def write_output(df, full_path_output:str, format='.csv'):
    """
    write file into a target directory in the specified format
    Args:
        df (DataFrame): dataframe to write
        format (str): output format, es. '.csv', '.xml', '.tsv'. Defualt is '.csv'
        orderColum (str): col name to sort values
    """
    logging.info(f'writing {full_path_output}')
    df.toPandas()\
        .to_csv(full_path_output , header=True, index=False)
    logging.info(f'writing of {full_path_output} completed')


def load_to_postgres(table_name: str, file_path: str):
    """
    Loads the specified file into Postgres.
    It creates the table if it doesnt exists and appends data if it exists
    Args:
        table_name (str): name of table
        file_path (str): Path to file to load
    """
    logging.info(f'Writing {file_path} into postgres {table_name} table ... ')
    pg_hook = PostgresHook(postgres_conn_id='conn_postgres')
    conn = pg_hook.get_sqlalchemy_engine()
    load_df = pd.read_csv(file_path)
    load_df.to_sql(table_name, conn, index=False, if_exists='append')
    logging.info(f'Write into {table_name} completed')
    
    
# spark = SparkSession \
#     .builder \
#     .appName("truefilm_pipe") \
#     .master("local[*]") \
#     .getOrCreate()

# spark.sparkContext.setLogLevel('WARN')

# # reading imdb_data data
# df_imdb = get_imdb_data(sys.argv[1])

# # get high profit movies calculating ration between revenue to budget
# df_imdb = get_high_profit_movies(df_imdb)
                 
# # read wiki data
# df_wiki = get_wiki_data(sys.argv[2])

# # left join df_imdb with df_wiki
# df_joined = df_imdb.join(df_wiki,  ['title'], "left")

# # write results to output location in alphabetic order
# write_output(df_joined, sys.argv[3])

# spark.stop()


DATA_DIR = 'data/'
OUTPUT_DIR = 'output/'
OUT_TABLE_NAME = 'tf_high_profit_movies'
OUTPUT_FULL_NAME = OUTPUT_DIR + 'high_profit_movies.csv' 
URL_INFO = {
    'imdb_info': 'data/movies_metadata.csv',
    'wiki_info': 'https://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml.gz'
}

default_args = {
    'owner': 'daniele_ciciani',
    'start_date': datetime(2020, 11, 18),
    'retries': 5,
	'retry_delay': timedelta(hours=1)
}

dag = DAG('truefile_pipeline_orchestrator', description='Dag truefilm pipeline',
    schedule_interval=None,
    default_args = default_args,
    start_date=datetime(2022, 1, 1), catchup=False)

# Airflow Tasks:
download_data = PythonOperator(
        task_id='1_download-data',
        dag=dag,
        python_callable=donwload_movie_dataset,
        op_kwargs={
            'out_dir': DATA_DIR,
            'urls_dict': URL_INFO
        }
    )

high_profit_movies = SparkSubmitOperator(
    dag=dag,
    task_id='2_spark_processing',
    application='/opt/airflow/dags/high_profit_movies_spark.py',
    conn_id='spark_local', 
    packages='com.databricks:spark-xml_2.12:0.15.0',
    driver_memory='12G',
    application_args=["{{ti.xcom_pull(key='imdb_info')}}",\
                     "{{ti.xcom_pull(key='wiki_info')}}",\
                      OUTPUT_FULL_NAME]
    )

load_to_postgres = PythonOperator(
        task_id='3_load_to_postgres',
        python_callable=load_to_postgres,
        op_kwargs = {
            'table_name': OUT_TABLE_NAME,
            'file_path' : OUTPUT_FULL_NAME
        }
    )

download_data >> high_profit_movies >> load_to_postgres
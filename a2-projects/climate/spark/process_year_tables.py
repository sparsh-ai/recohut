#!/usr/bin/env python
# coding: utf-8

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, IntegerType, DateType, StructField, StringType, TimestampType
import logging, traceback
import requests
import sys

start_year = int(sys.argv[1])
end_year = int(sys.argv[2])

# For ingestion to local (used when developing)
URL_PREFIX = 'https://noaa-ghcn-pds.s3.amazonaws.com'
TEMP_STORAGE_PATH = '/home/marcos/ghcn-d/spark/data'

"""
# For local spark master
spark = SparkSession.builder \
  .master("local[*]")
  .appName('test')
  .getOrCreate()
"""

# Dataproc yarn master
spark = SparkSession \
  .builder \
  .master('yarn') \
  .appName('ghcnd') \
  .getOrCreate()
#   .config("spark.executor.cores", "4") \

# Use the Cloud Storage bucket for temporary BigQuery export data used
# by the connector.
bucket = "ghcnd_raw"
spark.conf.set('temporaryGcsBucket', bucket)

# Used only when developing with local spark master
def download_file(url, local_file_path):
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_file_path

def process_year(year, mode, df_stations, df_countries):

  """
  # For developing process read directly from origin
  csv_file_name = f'/{year}.csv'
  dataset_url = URL_PREFIX + '/csv' + csv_file_name
  csv_file_path = TEMP_STORAGE_PATH + csv_file_name

  download_file(dataset_url, csv_file_path)    

  schema = StructType([
      StructField("id", StringType(), True),
      StructField("date", IntegerType(), True),
      StructField("element", StringType(), True),   
      StructField("value", IntegerType(), True),   
      StructField("m_flag", StringType(), True),   
      StructField("q_flag", StringType(), True),   
      StructField("s_flag", StringType(), True),
      StructField("obs_time",IntegerType(), True)
  ])

  df = spark.read \
    .options(header=False)
    .schema(schema)
    .csv(csv_file_path)
  """

  """
  # Option, read from BQ
  df = spark.read.format('bigquery') \
    .option('project','ghcn-d') \
    .option('dataset','ghcnd') \
    .option('table',f'{year}').load()
  """

  # Option, read from GCS
  df = spark.read.parquet(f'gs://ghcnd_raw/{year}.parquet')

  print(f'processing year {year}...')
  # Only used when reading from csv in order to convert to date. 
  # If reading from BQ, this is already done
  # df = df.withColumn("date", F.to_date(df.date.cast("string"), "yyyyMMdd"))

  df = df \
    .drop("q_flag") \
    .withColumn("tmax", 
          F.when(df.element == "TMAX", 
              F.when(df.value > 700, None).otherwise(
                  F.when(df.value < -700, None). otherwise(
                      df.value.cast("double")/10)
                  )
          ).otherwise("None")
      ) \
      .withColumn("tmin", 
          F.when(df.element == "TMIN", 
              F.when(df.value > 700, None).otherwise(
                  F.when(df.value < -700, None). otherwise(
                      df.value.cast("double")/10)
                  )
          ).otherwise("None")
      ) \
      .withColumn("prcp", F.when(df.element == "PRCP", df.value.cast("double")).otherwise(None)) \
      .withColumn("snow", F.when(df.element == "SNOW", df.value.cast("double")).otherwise(None)) \
      .withColumn("snwd", F.when(df.element == "SNWD", df.value.cast("double")).otherwise(None))

  df_daily = df \
      .groupBy("id", "date").agg( 
          F.avg("tmax"),
          F.avg("tmin"),
          F.avg("prcp"),
          F.avg("snow"),
          F.avg("snwd"),
          F.first("m_flag"),
          F.first("s_flag")
      ) \
      .join(df_stations, df.id == df_stations.station_id, "inner") \
      .join(df_countries, df_stations.country_code == df_countries.code, "inner") \
      .drop ('station_id', 'code') \
      .toDF('id','date','tmax','tmin','prcp','snow','snwd','m_flag','s_flag','latitude','longitude','elevation','station_name','country_code','country_name') 

  # Note: toDF after joins, otherwise join will raise error
  # Note: toDF since BQ does not allow field names with () and average generates these kind of names avg(tmax)

  df_yearly =  df \
    .withColumn("date", F.trunc("date", "year")) \
    .groupBy("id", "date").agg( 
      F.avg("tmax"),
      F.avg("tmin"),
      F.avg("prcp"),
      F.avg("snow"),
      F.avg("snwd"),
      F.first("m_flag"),
      F.first("s_flag")
    ) \
    .join(df_stations, df.id == df_stations.station_id, "inner") \
    .join(df_countries, df_stations.country_code == df_countries.code, "inner") \
    .drop ('station_id', 'code') \
    .toDF('id','date','tmax','tmin','prcp','snow','snwd','m_flag','s_flag','latitude','longitude','elevation','station_name','country_code','country_name') \

  # For some reason, partition by date does not work after F.year("date"). This has to be fixed
  # Also, partition is needed for clustering
  df_yearly.write \
    .format("bigquery") \
    .mode(mode) \
    .option("clusteredFields", "date, country_code") \
    .option('project','ghcn-d') \
    .option('dataset','production') \
    .option('table','fact_observations_spark_yearly') \
    .save()
    
  
  df_daily.write \
    .format("bigquery") \
    .mode(mode) \
    .option("partitionField", "date") \
    .option("partitionType", "YEAR") \
    .option("clusteredFields", "country_code") \
    .option('project','ghcn-d') \
    .option('dataset','production') \
    .option('table','fact_observations_spark') \
    .save()
  


  print(f'process {year} done')

"""
# USe if needed to read from BigQuery instead of GCS
df_stations = spark.read.format('bigquery') \
  .option('project','ghcn-d') \
  .option('dataset','ghcnd') \
  .option('table', 'stations').load() \
  .drop('state', 'gsn_flag', 'hcn_crn_flag', 'wmo_id') \
  .withColumnRenamed('name', 'station_name') \
  .withColumnRenamed('id', 'station_id') \
  .withColumn('country_code', F.substring('station_id', 0, 2))

df_countries = spark.read.format('bigquery') \
  .option('project','ghcn-d') \
  .option('dataset','ghcnd') \
  .option('table', 'countries').load() \
  .withColumnRenamed('name', 'country_name')
"""  

df_stations = spark.read.parquet('gs://ghcnd_raw/ghcnd-stations.parquet') \
  .drop('state', 'gsn_flag', 'hcn_crn_flag', 'wmo_id') \
  .withColumnRenamed('name', 'station_name') \
  .withColumnRenamed('id', 'station_id') \
  .withColumn('country_code', F.substring('station_id', 0, 2))

df_countries = spark.read.parquet('gs://ghcnd_raw/ghcnd-countries.parquet') \
  .withColumnRenamed('name', 'country_name')

for year in range(start_year, end_year+1):
  if year == start_year:
    process_year(year, 'overwrite', df_stations, df_countries)
  else:
    process_year(year, 'append', df_stations, df_countries)

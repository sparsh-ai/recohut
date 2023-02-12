# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC <img src="https://pages.databricks.com/rs/094-YMS-629/images/AWS - CDL KInesis to Delta- light BG.png" height="600" width="800"/>

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##Read Clicks Kinesis streams and produce the Bronze and Silver medallion tables

# COMMAND ----------

# DBTITLE 1,Clean up - in case I needed to rerun
dbutils.fs.rm("s3://aws-cdl-devdays/clicks-bronze", True)
dbutils.fs.rm("s3://aws-cdl-devdays/clicks-silver", True)
dbutils.fs.rm("s3://aws-cdl-devdays/checkpoint-clicks-bronze", True)
dbutils.fs.rm("s3://aws-cdl-devdays/checkpoint-clicks-silver", True)

# COMMAND ----------

# MAGIC %sql USE aws_cdl_devdays;

# COMMAND ----------

# DBTITLE 1,Read Kinesis Stream
from pyspark.sql.types import *
from pyspark.sql.functions import *

clicks_schema= StructType() \
          .add("uid", StringType()) \
          .add("clickTimestamp", TimestampType()) \
          .add("exchangeID", IntegerType()) \
          .add ("publisher", StringType()) \
          .add ("creativeID", IntegerType()) \
          .add("click", StringType()) \
          .add ("advertiserID", IntegerType()) \
          .add("browser", StringType()) \
          .add("geo", StringType()) \
          .add("bidAmount", DoubleType())

clicks = spark \
  .readStream \
  .format("kinesis") \
  .option("streamName", "aws-cdl-devdays-clicks") \
  .option("initialPosition", "latest") \
  .option("region", "us-west-2") \
  .load()

# COMMAND ----------

# DBTITLE 1,Convert JSON to String, and add Partitioning Columns
clicks_raw = clicks.selectExpr("cast (data as STRING) jsonData", "approximateArrivalTimestamp") \
                 .withColumn("approximateArrivalDate",to_date(col("approximateArrivalTimestamp")))
display(clicks_raw)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##Write Click data from Kinesis to Bronze delta table

# COMMAND ----------

# DBTITLE 1,Write to Bronze Table
clicks_raw.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation","s3://aws-cdl-devdays/checkpoint-clicks-bronze") \
    .partitionBy("approximateArrivalDate") \
    .trigger(processingTime='30 seconds') \
    .start("s3://aws-cdl-devdays/clicks-bronze")

# COMMAND ----------

# DBTITLE 1,Create Metastore Reference - Bronze Data
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS aws_cdl_devdays.clicks_bronze;
# MAGIC CREATE TABLE aws_cdl_devdays.clicks_bronze USING DELTA LOCATION "s3://aws-cdl-devdays/clicks-bronze"

# COMMAND ----------

# DBTITLE 1,Safely query the Clicks Bronze Data 
# MAGIC %sql
# MAGIC SELECT * FROM aws_cdl_devdays.clicks_bronze
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM aws_cdl_devdays.clicks_bronze

# COMMAND ----------

# MAGIC %md
# MAGIC ### Databricks Utilities - dbutils
# MAGIC * For in-notebook documentation on DBUtils you can execute the command `dbutils.help()`.
# MAGIC * See also Databricks Utilities for <a href="https://docs.databricks.com/notebooks/notebook-workflows.html" target="_blank">Notebooks</a>

# COMMAND ----------

dbutils.notebook.exit("stop") 

# COMMAND ----------

# DBTITLE 1,Read Bronze Delta table as a stream, and parse schema
bronze_data = spark \
  .readStream \
  .format("delta") \
  .load("s3://aws-cdl-devdays/clicks-bronze") \
  .select(from_json("jsonData", clicks_schema).alias("fields"), "approximateArrivalDate", "approximateArrivalTimestamp") \
  .select("fields.*","approximateArrivalDate","approximateArrivalTimestamp")

# COMMAND ----------

# DBTITLE 1,Perform some cleaning
#Example cleaning, lowercase browser and create date column
bronze_data_cleaned = bronze_data.withColumn("browserCleaned",lower(col("browser"))) \
                                 .withColumn("clickDate",to_date(col("clickTimestamp")))

# COMMAND ----------

display(bronze_data_cleaned)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ##Write Click data from Bronze to Silver delta table

# COMMAND ----------

# DBTITLE 1,Write parsed + cleaned Clicks data to silver
bronze_data_cleaned.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation","s3://aws-cdl-devdays/checkpoint-clicks-silver") \
    .partitionBy("clickDate") \
    .trigger(processingTime='30 seconds') \
    .start("s3://aws-cdl-devdays/clicks-silver")

# COMMAND ----------

# DBTITLE 1,Create metastore reference - Silver Data
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS aws_cdl_devdays.clicks_silver;
# MAGIC CREATE TABLE aws_cdl_devdays.clicks_silver USING DELTA LOCATION "s3://aws-cdl-devdays/clicks-silver"

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM aws_cdl_devdays.clicks_silver
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM aws_cdl_devdays.clicks_silver;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM aws_cdl_devdays.clicks_bronze;

# COMMAND ----------

# DBTITLE 1,Read the Profiles
people_profile = spark.read.format("delta").load("s3://aws-cdl-devdays/data/people-profile")

# COMMAND ----------

display(people_profile)

# COMMAND ----------

people_profile.count()

# COMMAND ----------

# DBTITLE 1,Read point-in-time Clicks_Silver into a DataFrame
clicks_silver = spark.read.format("delta").load("s3://aws-cdl-devdays/clicks-silver/")

# COMMAND ----------

clicks_silver.count()

# COMMAND ----------

# DBTITLE 1,Perform a Left Outer join between Clicks_Silver and the People_profile dataset
clicks_with_profile = clicks_silver.join(people_profile, on="uid", how="left")
clicks_with_profile.createOrReplaceTempView("clicks_view")

# COMMAND ----------

dbutils.fs.rm('s3://aws-cdl-devdays/clicks-with-profile', True)

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS clicks_with_profile;
# MAGIC 
# MAGIC CREATE TABLE clicks_with_profile 
# MAGIC USING delta 
# MAGIC LOCATION "s3://aws-cdl-devdays/clicks-with-profile" 
# MAGIC AS SELECT * FROM clicks_view;
# MAGIC 
# MAGIC -- View Delta Lake table
# MAGIC SELECT *
# MAGIC FROM clicks_with_profile
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM clicks_with_profile;

# COMMAND ----------

# MAGIC %sql
# MAGIC select geo, sum(bidAmount) as sum_bidAmount FROM clicks_with_profile group by geo order by sum_bidAmount desc

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE history clicks_with_profile

# COMMAND ----------

# MAGIC %md
# MAGIC ### [Back to the main demo - Step4](https://field-eng.cloud.databricks.com/#notebook/1566801/command/1566811)

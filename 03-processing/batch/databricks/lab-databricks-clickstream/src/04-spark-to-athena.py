# Databricks notebook source
# MAGIC %md
# MAGIC 
# MAGIC ##Implementing a Reliable Data Lake with Databricks Delta and the AWS Ecosystem

# COMMAND ----------

# MAGIC %sql
# MAGIC USE aws_cdl_devdays;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES;

# COMMAND ----------

# DBTITLE 1,Clean the Glue metastore - In case a rerun in place is needed
# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS clicks_with_profile_GOLD;
# MAGIC DROP TABLE IF EXISTS clicks_with_profile_GOLD_athena;

# COMMAND ----------

# DBTITLE 1,and clean up the corresponding S3 bucket working folders, if required
dbutils.fs.rm("s3://aws-cdl-devdays/clicks_with_profile_GOLD", True)

# COMMAND ----------

# MAGIC %md
# MAGIC ##Time to run an AWS Glue Crawler and populate the `uscitiesupdated_csv` table

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM aws_webinar_dt10014.uscitiesupdated_csv
# MAGIC ORDER BY city
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM clicks_with_profile
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS clicks_with_profile_GOLD
# MAGIC (uid STRING,
# MAGIC  clickTimestamp TIMESTAMP,
# MAGIC  exchangeID INT,
# MAGIC  publisher STRING,
# MAGIC  creativeID INT,
# MAGIC  click STRING,
# MAGIC  advertiserID INT,
# MAGIC  browser STRING,
# MAGIC  bidAmount DOUBLE,
# MAGIC  cdcTimestamp TIMESTAMP,
# MAGIC  city STRING,
# MAGIC  stateCode STRING,
# MAGIC  lat DOUBLE,
# MAGIC  long DOUBLE)
# MAGIC USING DELTA
# MAGIC LOCATION 's3://aws-cdl-devdays/clicks_with_profile_GOLD';

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO clicks_with_profile_GOLD
# MAGIC SELECT 
# MAGIC  uid,
# MAGIC  clickTimestamp,
# MAGIC  exchangeID,
# MAGIC  publisher,
# MAGIC  creativeID,
# MAGIC  click,
# MAGIC  advertiserID,
# MAGIC  browser,
# MAGIC  bidAmount,
# MAGIC  approximateArrivalTimestamp,
# MAGIC  geo,
# MAGIC  null,
# MAGIC  null,
# MAGIC  null
# MAGIC FROM clicks_with_profile;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT count(*) FROM clicks_with_profile;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT count(*) FROM clicks_with_profile_GOLD

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM clicks_with_profile_GOLD
# MAGIC WHERE city = 'Seattle'
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %md
# MAGIC ##![Delta Lake Logo Tiny](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Full DML Support
# MAGIC 
# MAGIC Delta Lake supports standard DML including UPDATE, DELETE and MERGE INTO providing developers more controls to manage their big datasets.

# COMMAND ----------

# MAGIC %md ###![Delta Lake Logo Tiny](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) MERGE INTO example
# MAGIC 
# MAGIC #### INSERT or UPDATE parquet: 7-step process
# MAGIC 
# MAGIC With a legacy data pipeline, to insert or update a table, you must:
# MAGIC 1. Identify the new rows to be inserted
# MAGIC 2. Identify the rows that will be replaced (i.e. updated)
# MAGIC 3. Identify all of the rows that are not impacted by the insert or update
# MAGIC 4. Create a new temp based on all three insert statements
# MAGIC 5. Delete the original table (and all of those associated files)
# MAGIC 6. "Rename" the temp table back to the original table name
# MAGIC 7. Drop the temp table
# MAGIC 
# MAGIC ![](https://pages.databricks.com/rs/094-YMS-629/images/merge-into-legacy.gif)

# COMMAND ----------

# MAGIC %sql
# MAGIC MERGE INTO clicks_with_profile_GOLD as t1
# MAGIC USING aws_webinar_dt10014.uscitiesupdated_csv as t2
# MAGIC ON t1.city = t2.city
# MAGIC WHEN MATCHED THEN
# MAGIC   UPDATE SET t1.stateCode = t2.state_id,
# MAGIC             t1.lat = t2.lat,
# MAGIC             t1.long = t2.lng

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM clicks_with_profile_GOLD
# MAGIC WHERE city = 'Seattle'
# MAGIC LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) 
# MAGIC FROM clicks_with_profile_GOLD
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) 
# MAGIC FROM clicks_with_profile_GOLD
# MAGIC WHERE stateCode is NULL
# MAGIC ;

# COMMAND ----------

# MAGIC %md ###![Delta Lake Logo Tiny](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Delete example

# COMMAND ----------

# MAGIC %sql
# MAGIC DELETE FROM clicks_with_profile_GOLD
# MAGIC WHERE stateCode is NULL
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) 
# MAGIC FROM clicks_with_profile_GOLD WHERE stateCode is NULL
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) 
# MAGIC FROM clicks_with_profile_GOLD
# MAGIC ;

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT publisher, COUNT(*)
# MAGIC FROM clicks_with_profile_GOLD
# MAGIC GROUP BY publisher
# MAGIC ORDER BY publisher

# COMMAND ----------

# MAGIC %md
# MAGIC ##Amazon Athena to Delta Lake integration 
# MAGIC 
# MAGIC Step 1: Generate manifests of a Delta table using Databricks Runtime

# COMMAND ----------

# DBTITLE 1,Step 1: Generate manifests of a Delta table using Databricks Runtime
# MAGIC %sql
# MAGIC GENERATE symlink_format_manifest FOR TABLE delta.`s3://aws-cdl-devdays/clicks_with_profile_GOLD`

# COMMAND ----------

# DBTITLE 1,Step 2: Configure Amazon Athena to read the generated manifests
# MAGIC %sql
# MAGIC CREATE EXTERNAL TABLE clicks_with_profile_GOLD_athena
# MAGIC (uid STRING,
# MAGIC  clickTimestamp TIMESTAMP,
# MAGIC  exchangeID INT,
# MAGIC  publisher STRING,
# MAGIC  creativeID INT,
# MAGIC  click STRING,
# MAGIC  advertiserID INT,
# MAGIC  browser STRING,
# MAGIC  bidAmount DOUBLE,
# MAGIC  cdcTimestamp TIMESTAMP,
# MAGIC  city STRING,
# MAGIC  stateCode STRING,
# MAGIC  lat DOUBLE,
# MAGIC  long DOUBLE)
# MAGIC ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
# MAGIC STORED AS INPUTFORMAT 'org.apache.hadoop.hive.ql.io.SymlinkTextInputFormat'
# MAGIC OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
# MAGIC LOCATION 's3://aws-cdl-devdays/clicks_with_profile_GOLD/_symlink_format_manifest/'

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT stateCode, browser, COUNT(*)
# MAGIC FROM clicks_with_profile_GOLD
# MAGIC GROUP BY stateCode, browser
# MAGIC ORDER BY stateCode

# COMMAND ----------

# MAGIC %md ## ![Delta Lake Tiny Logo](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Let's Travel back in Time!
# MAGIC Databricks Delta’s time travel capabilities simplify building data pipelines for the following use cases. 
# MAGIC 
# MAGIC * Audit Data Changes
# MAGIC * Reproduce experiments & reports
# MAGIC * Rollbacks
# MAGIC 
# MAGIC As you write into a Delta table or directory, every operation is automatically versioned.
# MAGIC 
# MAGIC You can query by:
# MAGIC 1. Using a timestamp
# MAGIC 1. Using a version number
# MAGIC 
# MAGIC using Python, Scala, and/or Scala syntax; for these examples we will use the SQL syntax.  
# MAGIC 
# MAGIC For more information, refer to [Introducing Delta Time Travel for Large Scale Data Lakes](https://databricks.com/blog/2019/02/04/introducing-delta-time-travel-for-large-scale-data-lakes.html)

# COMMAND ----------

# MAGIC %md ### ![Delta Lake Tiny Logo](https://pages.databricks.com/rs/094-YMS-629/images/delta-lake-tiny-logo.png) Review Delta Lake Table History
# MAGIC All the transactions for this table are stored within this table including the initial set of insertions, update, delete, merge, and inserts with schema modification

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE HISTORY clicks_with_profile_GOLD

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM clicks_with_profile_GOLD VERSION AS OF 1

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT COUNT(*) FROM clicks_with_profile_GOLD VERSION AS OF 3

# COMMAND ----------

# MAGIC %md
# MAGIC ### [Back to the main demo page - Step5](https://field-eng.cloud.databricks.com/#notebook/1566801/command/1572085)

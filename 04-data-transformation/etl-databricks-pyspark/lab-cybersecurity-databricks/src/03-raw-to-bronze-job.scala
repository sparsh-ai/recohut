// Databricks notebook source
// MAGIC %md 
// MAGIC ## Purpose 
// MAGIC -  This notebook helps to ingest crowdstrike data in a delta bronze table
// MAGIC ### How to use these demo notebooks 
// MAGIC  1. run fake_data_generator
// MAGIC  2. run raw_to_bronze_job
// MAGIC  3. run bronze_to_silver_job
// MAGIC   

// COMMAND ----------

import org.apache.spark.sql.functions._
import org.apache.spark.sql.streaming.Trigger

// COMMAND ----------

// MAGIC %sql 
// MAGIC -- creat database and table if not exist, on prod please do not use /tmp
// MAGIC CREATE SCHEMA IF NOT EXISTS demo_bronze LOCATION '/tmp/delta/demo/bronze';
// MAGIC CREATE TABLE IF NOT EXISTS demo_bronze.crowdstrike (event_simpleName STRING, load_date DATE , load_timestamp TIMESTAMP, value STRING ) USING DELTA PARTITIONED BY (load_date, event_simpleName) LOCATION '/tmp/delta/demo/bronze/crowdstrike/table' ;

// COMMAND ----------

// enable auto optimize and auto compact  
spark.conf.set("spark.databricks.delta.autoCompact.enabled", "true")
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled", "true")


// COMMAND ----------

// set table and checkpoint location 
val env = "demo"
val rawDataSource =  "dbfs:/tmp/raw/data"
val bronzeTableLocation = s"dbfs:/tmp/delta/$env/bronze/crowdstrike/table" 
val checkPointLocation = s"dbfs:/tmp/delta/$env/bronze/crowdstrike/_checkpoint"
val bronzeTable = "demo_bronze.crowdstrike"


// COMMAND ----------

val crowdstrikeStream = spark.readStream
  .format("cloudFiles")
  .option("cloudFiles.format", "text")    // text file doesn't need schema 
 // .option("cloudFiles.region", "us-west-1") // required when useNotifications is set to true
 // .option("cloudFiles.useNotifications", "true")  // recommended for larger number of files, This config needs extra permission please check : https://docs.databricks.com/spark/latest/structured-streaming/auto-loader.html
  .load(rawDataSource)
  .withColumn("load_timestamp", current_timestamp())
  .withColumn("load_date", to_date('load_timestamp))
  .withColumn("eventType", from_json('value, "struct<event_simpleName:string>", Map.empty[String, String]))   //extract event_simpleName only 
  .selectExpr("eventType.event_simpleName","load_date","load_timestamp", "value" )     
  

// COMMAND ----------

// MAGIC %md ## Display stream 
// MAGIC -  Here below we can display live stream data. You may remove the next cmd on production env

// COMMAND ----------

display(crowdstrikeStream)

// COMMAND ----------

// MAGIC %md ## Write to bronze table 

// COMMAND ----------

crowdstrikeStream.writeStream
  .format("delta")
  .option("checkpointLocation", checkPointLocation)
  .table("demo_bronze.crowdstrike")

// COMMAND ----------

// MAGIC %md #Query bronze table

// COMMAND ----------

// MAGIC %sql select count(*) from demo_bronze.crowdstrike

// COMMAND ----------

// MAGIC %sql select * from demo_bronze.crowdstrike

// COMMAND ----------

// MAGIC %md 
// MAGIC ## Demo is over! Now, Let us clean up
// MAGIC   - stop the stream on the previous command(cell)
// MAGIC   - remove checkpoints 
// MAGIC   - delete data in the table 
// MAGIC ### Note 
// MAGIC  - please don't delete checkpoints on production environments
// MAGIC   

// COMMAND ----------

//Uncomment the following lines to clean data 
//dbutils.fs.rm(checkPointLocation, true)


// COMMAND ----------

//Uncomment the following lines to clean data 
//%sql delete from demo_bronze.crowdstrike
   

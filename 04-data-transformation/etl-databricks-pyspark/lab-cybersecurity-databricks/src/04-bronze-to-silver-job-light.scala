// Databricks notebook source
// MAGIC %md 
// MAGIC ## Purpose 
// MAGIC -  This notebook reads semi-structured data from bronze table and writes to a structured silver table 
// MAGIC ### How to use these demo notebooks 
// MAGIC  1. run fake_data_generator
// MAGIC  2. run raw_to_bronze_job
// MAGIC  3. run bronze_to_silver_job
// MAGIC  4. run fake_data_generator if it is required to genarate more data  
// MAGIC  

// COMMAND ----------

import org.apache.spark.sql.functions.col
import org.apache.spark.sql.types._
import org.apache.spark.sql.Dataset
import org.apache.spark.sql.Row
import org.apache.spark.sql.streaming.Trigger
import java.time.LocalDateTime
import org.apache.spark.sql.functions._


// COMMAND ----------

// MAGIC %run ./lakehouse_pipeline_demo_0_sample_schema  

// COMMAND ----------

// MAGIC %sql -- creat database and table if not exist
// MAGIC CREATE SCHEMA IF NOT EXISTS demo_silver LOCATION 'dbfs:/tmp/demo/silver';
// MAGIC CREATE TABLE IF NOT EXISTS `demo_silver`.`hostInfo` (
// MAGIC   `BootArgs` STRING,
// MAGIC   `ConfigBuild` STRING,
// MAGIC   `ConfigStateHash` STRING,
// MAGIC   `DcName` STRING,
// MAGIC   `EffectiveTransmissionClass` STRING,
// MAGIC   `Entitlements` STRING,
// MAGIC   `MachineDn` STRING,
// MAGIC   `MachineDomain` STRING,
// MAGIC   `SIPIsEnabled` STRING,
// MAGIC   `SiteName` STRING,
// MAGIC   `aid` STRING,
// MAGIC   `aip` STRING,
// MAGIC   `cid` STRING,
// MAGIC   `event_platform` STRING,
// MAGIC   `event_simpleName` STRING,
// MAGIC   `id` STRING,
// MAGIC   `name` STRING,
// MAGIC   `timestamp` STRING,
// MAGIC   `silver_timestamp` TIMESTAMP,
// MAGIC   `load_timestamp` TIMESTAMP,
// MAGIC   `load_date` DATE
// MAGIC ) USING delta PARTITIONED BY (load_date) LOCATION 'dbfs:/tmp/demo/silver/crowdstrike/table/HostInfo'

// COMMAND ----------

spark.conf.set("spark.databricks.delta.autoCompact.enabled", "true")    // auto compact for the performace of delta 
spark.conf.set("spark.databricks.delta.optimizeWrite.enabled",  "true") // auto optimize for the performace of delta write
spark.conf.set("spark.sql.caseSensitive", "true") // enabled if some payloads have the same field name with different cases 

// COMMAND ----------

//set the evironement,  source and target tables 
val env = "demo"
val bronzeTable = env + "_bronze.crowdstrike"
val silverDb = env + "_silver"
val bronzeTableLocation = s"/tmp/$env/bronze/crowdstrike/table" 
val silverTablesLocation= s"/tmp/$env/silver/crowdstrike/table"
val checkPointLocation =  s"/tmp/$env/silver/crowdstrike/checkpoint"
val eventName = "HostInfo"
val checkPoint =  checkPointLocation + "/" + eventName
val tableLocation = silverTablesLocation + "/" + eventName   
val silverTable = silverDb + "." + eventName
val sampleJson = getHostInforSampleJson()  // get sample json file to create a schema 


// COMMAND ----------

 spark
  .readStream
  .option("maxBytesPerTrigger", "1g") //let us keep it slow for demo
  .option("maxFilesPerTrigger", "1") //let us keep it slow for demo, on prod we can increase this setting
  .format("delta")
  .table(bronzeTable)
  .filter('event_simpleName === eventName) // read only one partition 
  .withColumn("event", from_json('value, schema_of_json(sampleJson)) ) // json string to struct 
  .select($"event.*", $"load_timestamp", $"load_date")  // flatten an select important columns 
  .withColumn("silver_timestamp", current_timestamp()) // add current time 
  .writeStream
  .format("delta")
  .outputMode("append")         // event data is appended
  .option("mergeSchema", "true")    // schema can change with out affecting this job
  .option("checkpointLocation", checkPoint)
  .option("path", tableLocation) //  the location of the table where to write
  .table(silverTable)

// COMMAND ----------

display(spark.table(silverTable))

// COMMAND ----------

// MAGIC %md ## Demo is over. Let us clean up!
// MAGIC   - stop the stream on the previous command(cell)
// MAGIC   - remove checkpoints 
// MAGIC   - delete data in the table 

// COMMAND ----------

 //Uncomment the following line to clean data 
//dbutils.fs.rm(checkPoint, true)

// COMMAND ----------

//Uncomment the following lines to clean data 
// spark.conf.set("spark.databricks.delta.retentionDurationCheck.enabled", false)
// spark.sql(s"DELETE FROM $silverTable ")
// spark.sql(s"VACUUM $silverTable RETAIN 0 HOURS")


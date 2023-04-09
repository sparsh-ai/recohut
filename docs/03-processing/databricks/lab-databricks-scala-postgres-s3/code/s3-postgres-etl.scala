// Databricks notebook source
// MAGIC %python
// MAGIC import os

// COMMAND ----------

// MAGIC %python
// MAGIC !mkdir -p ~/.aws

// COMMAND ----------

// MAGIC %python
// MAGIC %%writefile ~/.aws/credentials
// MAGIC [default]
// MAGIC aws_access_key_id=
// MAGIC aws_secret_access_key=

// COMMAND ----------

// MAGIC %python
// MAGIC %%writefile ~/.aws/config
// MAGIC [default]
// MAGIC region=us-east-1
// MAGIC output=json

// COMMAND ----------

// MAGIC %python
// MAGIC import boto3
// MAGIC session = boto3.Session(profile_name='default')
// MAGIC credentials = session.get_credentials()
// MAGIC 
// MAGIC sc._jsc.hadoopConfiguration().set("fs.s3a.access.key", credentials.access_key)
// MAGIC sc._jsc.hadoopConfiguration().set("fs.s3a.secret.key", credentials.secret_key)
// MAGIC aws_region = "us-east-1"
// MAGIC sc._jsc.hadoopConfiguration().set("fs.s3a.endpoint", "s3." + aws_region + ".amazonaws.com")

// COMMAND ----------

import org.apache.spark.sql.SparkSession

// COMMAND ----------

val PG_HOSTNAME = ""
val PG_USERNAME = ""
val PG_PASSWORD = ""

// COMMAND ----------

object ETLApp {
    
  def main() {
        val spark = SparkSession.builder.appName("Scala Spark Data Frames").getOrCreate()
        val df = spark.read.format("jdbc").option("url", "jdbc:postgresql://"+PG_HOSTNAME+":5432/").option("dbtable", "orders").option("user", PG_USERNAME).option("password", PG_PASSWORD).load()
        df.show()
        
  }
}

// COMMAND ----------

ETLApp.main()

// COMMAND ----------

object ETLApp {
    
  def main() {
        val spark = SparkSession.builder.appName("Scala Spark Data Frames").getOrCreate()
        val df = spark.read.option("header",true).csv("s3a://wysde-assets/labs/lab-204-s3-postgres-scala/data.csv")
        df.write.format("jdbc").option("url", "jdbc:postgresql://"+PG_HOSTNAME+":5432/").option("dbtable", "etlDataLoad").option("user", PG_USERNAME).option("password", PG_PASSWORD).save()
        
  }
}

// COMMAND ----------

ETLApp.main()

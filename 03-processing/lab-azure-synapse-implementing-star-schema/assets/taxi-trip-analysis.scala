// Databricks notebook source
val storageAccountName = "databricks"
val fileSystemName = "sparshstorage1"
val commonPath = "abfss://" + fileSystemName  + "@" + storageAccountName + ".dfs.core.windows.net"
val appID = dbutils.secrets.get(scope="datalakekey",key="ApplicationID")
val secret = dbutils.secrets.get(scope="datalakekey",key="appsecret")
val tenantID = dbutils.secrets.get(scope="datalakekey",key="DirectoryID")
val endpoint = "https://login.microsoftonline.com/" + tenantID + "/oauth2/token"
val mountPoint = "/mnt/datalakestorage"

spark.conf.set("fs.azure.account.auth.type." + storageAccountName + ".dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type." + storageAccountName + ".dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id." + storageAccountName + ".dfs.core.windows.net", "" + appID + "")
spark.conf.set("fs.azure.account.oauth2.client.secret." + storageAccountName + ".dfs.core.windows.net", "" + secret + "")
spark.conf.set("fs.azure.account.oauth2.client.endpoint." + storageAccountName + ".dfs.core.windows.net", "https://login.microsoftonline.com/" + tenantID + "/oauth2/token")
spark.conf.set("fs.azure.createRemoteFileSystemDuringInitialization", "true")

val configs = Map(
  "fs.azure.account.auth.type" -> "OAuth",
  "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
  "fs.azure.account.oauth2.client.id" -> appID,
  "fs.azure.account.oauth2.client.secret" -> secret,
  "fs.azure.account.oauth2.client.endpoint" -> endpoint)

dbutils.fs.mount(
  source = "abfss://databricks@sparshstorage1.dfs.core.windows.net/",
  mountPoint = mountPoint,
  extraConfigs = configs)

dbutils.fs.ls(mountPoint)

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ## Let us generate some parquet data first

// COMMAND ----------

import org.apache.spark.sql.{DataFrame, Row, SaveMode}
import org.apache.spark.sql.types.{StringType, IntegerType, StructField, StructType}

// COMMAND ----------

val tripsParquetPath = mountPoint + "/parquet/trips"
val driverParquetPath = mountPoint + "/parquet/driver"

// Generate sample trips data
val tripSchema = new StructType().add("tripId", StringType).add("driverId", StringType).add("customerId", StringType).add("cabId", StringType).add("tripDate", StringType).add("startLocation", StringType).add("endLocation", StringType)

val tripData = Seq(
  Row("100", "200", "300", "400", "20220101", "New York", "New Jersey"),
  Row("101", "201", "301", "401", "20220102", "Tempe", "Phoenix"),
  Row("102", "202", "302", "402", "20220103", "San Jose", "San Franciso"),
  Row("103", "203", "303", "403", "20220102", "New York", "Boston"),
  Row("104", "204", "304", "404", "20220103", "New York", "Washington"),
  Row("105", "205", "305", "405", "20220201", "Miami", "Fort Lauderdale"),
  Row("106", "206", "306", "406", "20220202", "Seattle", "Redmond"),
  Row("107", "207", "307", "407", "20220203", "Los Angeles", "San Diego"),
  Row("108", "208", "308", "408", "20220301", "Phoenix", "Las Vegas"),
  Row("109", "209", "309", "409", "20220302", "Washington", "Baltimore"),
  Row("110", "210", "310", "410", "20220303", "Dallas", "Austin"),
  Row("111", "211", "311", "411", "20220303", "New York", "New Jersey"),
  Row("112", "212", "312", "412", "20220304", "New York", "Boston"),
  Row("113", "212", "312", "412", "20220401", "San Jose", "San Ramon"),
  Row("114", "212", "312", "412", "20220404", "San Jose", "Oakland"),
  Row("115", "212", "312", "412", "20220404", "Tempe", "Scottsdale"),
  Row("116", "212", "312", "412", "20220405", "Washington", "Atlanta"),
  Row("117", "212", "312", "412", "20220405", "Seattle", "Portland"),
  Row("118", "212", "312", "412", "20220405", "Miami", "Tampa")
)

// COMMAND ----------

// Write Trips to Parquet
val tripWriteDF = spark.createDataFrame(spark.sparkContext.parallelize(tripData),tripSchema)
tripWriteDF.write.mode("overwrite").parquet(tripsParquetPath)

val driverSchema = new StructType().add("driverId", StringType).add("name", StringType).add("license",StringType).add("gender",StringType).add("salary",IntegerType)

val driverData = Seq(
  Row("200", "Alice", "A224455", "Female", 3000),
  Row("202", "Bryan","B992244","Male",4000),
  Row("204", "Catherine","C887733","Female",4000),
  Row("208", "Daryl","D229988","Male",3000),
  Row("212", "Jenny","J663300","Female", 5000)
)
// Write Driver to Parquet
val driverWriteDF = spark.createDataFrame(spark.sparkContext.parallelize(driverData),driverSchema)
driverWriteDF.write.mode("overwrite").parquet(driverParquetPath)

// COMMAND ----------

display(dbutils.fs.ls(mountPoint + "/parquet/driver/"))

// COMMAND ----------

display(dbutils.fs.ls(mountPoint + "/parquet/trips/"))

// COMMAND ----------

// MAGIC %md
// MAGIC 
// MAGIC ## Let us read the data from Parquet files and view them as a Dataframe using Scala and SQL now

// COMMAND ----------

val spark = org.apache.spark.sql.SparkSession.builder.getOrCreate();

// COMMAND ----------

val df = spark.read
         .format("parquet")
         .load(mountPoint + "/parquet/trips/*.parquet")
df.printSchema()

// COMMAND ----------

spark.sql("CREATE DATABASE IF NOT EXISTS TripsDatabase")
df.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable("TripsTable")

val sqldf = spark.sql("SELECT * FROM TripsTable") 
display(sqldf)

// COMMAND ----------

val sqldf = spark.sql("""
   SELECT COUNT(*) AS Trips, 
   startLocation AS Location 
   FROM TripsTable 
   GROUP BY startLocation """) 
display(sqldf)

// COMMAND ----------



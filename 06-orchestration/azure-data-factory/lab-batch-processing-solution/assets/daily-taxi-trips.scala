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

import org.apache.spark.sql.{DataFrame, Row, SaveMode}
import org.apache.spark.sql.types.{StringType, IntegerType, StructField, StructType}

// COMMAND ----------

val tripsCSVPath = mountPoint + "/dailytrips/batch/csv/trips"
val faresParquetPath = mountPoint + "/dailytrips/batch/parquet/fares"
val outputParquetPath = mountPoint + "/dailytrips/batch/parquet/output"

// COMMAND ----------

// Generate sample data
val tripSchema = new StructType()
      .add("tripId",IntegerType)
      .add("driverId",IntegerType)
      .add("customerId",IntegerType)
      .add("cabId",IntegerType)
      .add("tripDate",StringType)
      .add("startLocation",StringType)
      .add("endLocation",StringType)
      
val tripData = Seq(
  Row(100, 200, 300, 400, "20220101", "New York", "New Jersey"),
  Row(101, 201, 301, 401, "20220102", "Tempe", "Phoenix"),
  Row(102, 202, 302, 402, "20220103", "San Jose", "San Franciso"),
  Row(103, 203, 303, 403, "20220102", "New York", "Boston"),
  Row(104, 204, 304, 404, "20220103", "New York", "Washington"),
  Row(105, 205, 305, 405, "20220201", "Miami", "Fort Lauderdale"),
  Row(106, 206, 306, 406, "20220202", "Seattle", "Redmond"),
  Row(107, 207, 307, 407, "20220203", "Los Angeles", "San Diego"),
  Row(108, 208, 308, 408, "20220301", "Phoenix", "Las Vegas"),
  Row(109, 209, 309, 409, "20220302", "Washington", "Baltimore"),
  Row(110, 210, 310, 410, "20220303", "Dallas", "Austin"),
)

// Write Trips to CSV file
val tripDF = spark.createDataFrame(spark.sparkContext.parallelize(tripData),tripSchema)
tripDF.printSchema()
tripDF.show(false)
tripDF.write.mode("overwrite").option("header", "true").csv(tripsCSVPath)

// COMMAND ----------

display(dbutils.fs.ls(tripsCSVPath))

// COMMAND ----------

// Generate sample fares data
val fareSchema = new StructType()
      .add("tripId",IntegerType)
      .add("fare",IntegerType)
      .add("currency",StringType)

val fareData = Seq(
  Row(100, 100, "USD"),
  Row(101, 20, "USD"),
  Row(102, 25, "USD"),
  Row(103, 140, "USD"),
  Row(104, 340, "USD"),
  Row(105, 75, "USD"),
  Row(106, 50, "USD"),
  Row(107, 125, "USD"),
  Row(108, 40, "USD"),
  Row(109, 80, "USD"),
  Row(110, 160, "USD")
)

// Write Trips to Parquet file
val faresDF = spark.createDataFrame(spark.sparkContext.parallelize(fareData),fareSchema)
faresDF.printSchema()
faresDF.show(false)
faresDF.write.mode("overwrite").option("header", "true").parquet(faresParquetPath)

// COMMAND ----------

display(dbutils.fs.ls(faresParquetPath))

// COMMAND ----------

// Read  the Trip data (stored as CSV file) and the Fares data (stored as Parquet files)
val tripsSchema = new StructType()
      .add("tripId",IntegerType)
      .add("driverId",IntegerType)
      .add("customerId",IntegerType)
      .add("cabId",IntegerType)
      .add("tripDate",IntegerType)
      .add("startLocation",StringType)
      .add("endLocation",StringType)

val tripsCSV = spark.read.format("csv")
      .option("header", "true")
      .schema(tripsSchema)
      .load(tripsCSVPath)

tripsCSV.printSchema()
tripsCSV.show(false)

// COMMAND ----------

val faresSchema = new StructType()
      .add("tripId",IntegerType)
      .add("fare",IntegerType)
      .add("currency",StringType)

val faresParquet = spark.read.format("parquet")
            .schema(faresSchema)
            .load(faresParquetPath)

faresParquet.printSchema()
faresParquet.show(false)

// COMMAND ----------

// Join them on the tripID and group by StartLocation.
val joinDF = tripsCSV.join(
faresParquet,tripsCSV("tripId") === 
      faresParquet("tripId"),"inner")
.groupBy("startLocation")
.sum("fare");

// Print the output table with columns: City and Fare
import org.apache.spark.sql.functions.col;
val outputDF = joinDF.select(col("startLocation").alias("City"),col("sum(fare)").alias("Fare"));
display(outputDF)
//	Finally, write the output back to ADLS Gen2 under the transform/fares/out folder.
outputDF.write.mode("overwrite").parquet(outputParquetPath)

// COMMAND ----------

display(dbutils.fs.ls(outputParquetPath))

// COMMAND ----------



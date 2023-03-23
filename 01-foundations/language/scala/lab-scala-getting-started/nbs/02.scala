// Databricks notebook source
import org.apache.spark.SparkContext
import org.apache.spark.SparkConf
import org.apache.spark.sql.SparkSession

// COMMAND ----------

val conf = new SparkConf().setAppName("Scala Spark")

// COMMAND ----------

val sc = SparkContext.getOrCreate(conf)

// COMMAND ----------

// MAGIC %python
// MAGIC %%writefile /sample_text_data.txt
// MAGIC sample line 1
// MAGIC sample line 2
// MAGIC sample line 3
// MAGIC sample line 4

// COMMAND ----------

// MAGIC %python
// MAGIC dbutils.fs.mv("file:/sample_text_data.txt", "/sample_text_data.txt")

// COMMAND ----------

val data = sc.textFile("/sample_text_data.txt")

// COMMAND ----------

data.collect()

// COMMAND ----------

val data2 = data.map(xyz => xyz + " Hello")

// COMMAND ----------

data2.collect()

// COMMAND ----------

val data2 = data.flatMap(xyz => xyz.split(" "))

// COMMAND ----------

data2.collect()

// COMMAND ----------

val mapdata = data2.map(word => (word,1))

// COMMAND ----------

mapdata.collect()

// COMMAND ----------

val reduceData = mapdata.reduceByKey(_+_)

// COMMAND ----------

reduceData.collect()

// COMMAND ----------

// MAGIC %python
// MAGIC %%writefile /df.csv
// MAGIC id,state,gender,phoneNumber,bill
// MAGIC 0,Alaska,Male,301183397011,97011
// MAGIC 1,Hawaii,Female,894727347347,47347
// MAGIC 2,Pennsylvania,Male,488271297683,97683
// MAGIC 3,North Carolina,Female,081815248019,48019
// MAGIC 4,Oklahoma,Male,675359198355,98355
// MAGIC 5,Hawaii,Female,268903148691,48691
// MAGIC 6,Colorado,Male,862447099027,99027
// MAGIC 7,Idaho,Male,455991049363,49363
// MAGIC 8,Illinois,Male,049534999699,99699
// MAGIC 9,North Dakota,Male,643078950035,50035
// MAGIC 10,Colorado,Male,236622900371,00371
// MAGIC 11,New Jersey,Male,830166850707,50707
// MAGIC 12,Idaho,Female,423710801043,01043
// MAGIC 13,Arkansas,Male,017254751379,51379
// MAGIC 14,New Jersey,Male,610798701715,01715
// MAGIC 15,Ohio,Male,204342652051,52051
// MAGIC 16,Delaware,Female,797886602387,02387
// MAGIC 17,Alaska,Female,391430552723,52723
// MAGIC 18,North Carolina,Male,984974503059,03059
// MAGIC 19,New Mexico,Male,578518453395,53395
// MAGIC 20,Florida,Female,172062403731,03731
// MAGIC 21,New Mexico,Male,765606354067,54067
// MAGIC 22,Arizona,Female,359150304403,04403
// MAGIC 23,Alaska,Female,952694254739,54739
// MAGIC 24,Arizona,Male,546238205075,05075
// MAGIC 25,North Dakota,Male,139782155411,55411
// MAGIC 26,Ohio,Male,733326105747,05747
// MAGIC 27,Colorado,Female,326870056083,56083
// MAGIC 28,Alabama,Female,920414006419,06419
// MAGIC 29,Oregon,Male,513957956755,56755
// MAGIC 30,Ohio,Male,107501907091,07091
// MAGIC 31,New York,Female,701045857427,57427
// MAGIC 32,Arkansas,Female,294589807763,07763
// MAGIC 33,New York,Female,888133758099,58099
// MAGIC 34,Connecticut,Male,481677708435,08435
// MAGIC 35,Delaware,Male,075221658771,58771
// MAGIC 36,Colorado,Female,668765609107,09107
// MAGIC 37,Arkansas,Male,262309559443,59443
// MAGIC 38,Rhode Island,Male,855853509779,09779
// MAGIC 39,Pennsylvania,Male,449397460115,60115
// MAGIC 40,North Carolina,Female,042941410451,10451
// MAGIC 41,Colorado,Female,636485360787,60787
// MAGIC 42,New York,Female,230029311123,11123
// MAGIC 43,Arkansas,Male,823573261459,61459
// MAGIC 44,New Jersey,Male,417117211795,11795
// MAGIC 45,Nevada,Male,010661162131,62131
// MAGIC 46,Idaho,Male,604205112467,12467
// MAGIC 47,California,Male,197749062803,62803
// MAGIC 48,Oklahoma,Female,791293013139,13139
// MAGIC 49,Rhode Island,Male,384836963475,63475
// MAGIC 50,Delaware,Male,978380913811,13811

// COMMAND ----------

// MAGIC %python
// MAGIC dbutils.fs.mv("file:/df.csv", "/df.csv")

// COMMAND ----------

val spark = SparkSession.builder.appName("Scala Spark Data Frames").getOrCreate()

// COMMAND ----------

val df = spark.read.option("header",true).csv("/df.csv")

// COMMAND ----------

df.show()

// COMMAND ----------

df.printSchema()

// COMMAND ----------

val df2 = df.select("state","id")

// COMMAND ----------

df2.show()

// COMMAND ----------

df.groupBy("gender").count().show()

// COMMAND ----------

val df3 = df.groupBy("state").count()

// COMMAND ----------

df3.write.option("header",true).csv("output")

// COMMAND ----------

df3.show()

// COMMAND ----------

val df_output_read = spark.read.option("header",true).csv("/output")

// COMMAND ----------

df_output_read.show()

// COMMAND ----------



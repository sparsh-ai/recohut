# Databricks notebook source
# MAGIC %md 
# MAGIC ### Restricting use of collect() method

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Spark's **collect()** function is an action, and it is used to retrieve all the elements of the **Resilient Distributed Dataset** (**RDD**) or DataFrame. We will first take a look at an example of using the function. Run the following code block:

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

# Read csv files to create Spark dataframe
airlines_1987_to_2008 = (
  spark
  .read
  .option("header",True)
  .option("delimiter",",")
  .option("inferSchema",True)
  .csv("dbfs:/databricks-datasets/asa/airlines/*")
)
# View the dataframe
display(airlines_1987_to_2008)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The preceding code block creates a Spark DataFrame and displays the first 1,000 records. Now, let's run some code with the **collect()** function:

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The preceding line of code returns a list of **row objects** for the **Year** column values. A *row object* is a collection of fields that can be iterated or accessed with an index. However, the major drawback with the function is that it brings all the data from the worker nodes to the driver. This could be very dangerous! This is because the driver can run out of memory and can potentially fail the cluster. This is why the **Out of Memory** (**OOM**) error is very common when using the **collect()** function.

# COMMAND ----------

# Using the collect function
airlines_1987_to_2008.select('Year').distinct().collect()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC In order to use the function, it is advisable to filter or aggregate the DataFrame first, before the **collect()** action. To demonstrate the limitations of using the function, we will run the following line of code. This simply brings the entire DataFrame onto the driver. But with the current cluster configuration, the Spark job is bound to fail:

# COMMAND ----------

# Run with caution
airlines_1987_to_2008.collect()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The error is basically trying to tell us that the job failed because the driver does not have enough memory. Therefore, it is best to restrict the use of this function. In cases where it is being used, we should ensure that we are filtering out the data before performing the action. To print the contents of the DataFrame, we can use the **display** function.

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Limiting use of inferSchema

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The **inferSchema** option is very often used to make Spark infer the data types automatically. While this approach works well for smaller datasets, performance bottlenecks can develop as the size of the data being scanned increases. In order to better understand the challenges that come with using this option for big data, we will perform a couple of experiments.

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC In this experiment, we will re-run the code block that we ran in the previous section:

# COMMAND ----------

# Read csv files to create Spark dataframe
airlines_1987_to_2008 = (
  spark
  .read
  .option("header",True)
  .option("delimiter",",")
  .option("inferSchema",True)
  .csv("dbfs:/databricks-datasets/asa/airlines/*")
)
# View the dataframe
display(airlines_1987_to_2008)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The code block simply reads CSV files and creates a Spark DataFrame by automatically inferring the schema. Note the time it takes for the job to run. For us, it took *13.14 minutes*. It can take a few minutes for the preceding code block to run.
# MAGIC 
# MAGIC Now, we will manually define the schema instead of making Spark infer it automatically. For that, we execute the following code block:

# COMMAND ----------

from pyspark.sql.types import *

manual_schema = StructType([
  StructField('Year',IntegerType(),True),
  StructField('Month',IntegerType(),True),
  StructField('DayofMonth',IntegerType(),True),
  StructField('DayOfWeek',IntegerType(),True),
  StructField('DepTime',StringType(),True),
  StructField('CRSDepTime',IntegerType(),True),
  StructField('ArrTime',StringType(),True),
  StructField('CRSArrTime',IntegerType(),True),
  StructField('UniqueCarrier',StringType(),True),
  StructField('FlightNum',IntegerType(),True),
  StructField('TailNum',StringType(),True),
  StructField('ActualElapsedTime',StringType(),True),
  StructField('CRSElapsedTime',StringType(),True),
  StructField('AirTime',StringType(),True),
  StructField('ArrDelay',StringType(),True),
  StructField('DepDelay',StringType(),True),
  StructField('Origin',StringType(),True),
  StructField('Dest',StringType(),True),
  StructField('Distance',StringType(),True),
  StructField('TaxiIn',StringType(),True),
  StructField('TaxiOut',StringType(),True),
  StructField('Cancelled',IntegerType(),True),
  StructField('CancellationCode',StringType(),True),
  StructField('Diverted',IntegerType(),True),
  StructField('CarrierDelay',StringType(),True),
  StructField('WeatherDelay',StringType(),True),
  StructField('NASDelay',StringType(),True),
  StructField('SecurityDelay',StringType(),True),
  StructField('LateAircraftDelay',StringType(),True)
])

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The preceding code block defines the schema of the DataFrame that we are trying to create.
# MAGIC 
# MAGIC Next, it's time to create the DataFrame, and display it by passing in the schema:

# COMMAND ----------

# Read csv files to create Spark dataframe
airlines_1987_to_2008 = (
  spark
  .read
  .option("header",True)
  .option("delimiter",",")
  .schema(manual_schema)
  .csv("dbfs:/databricks-datasets/asa/airlines/*")
)
# View the dataframe
display(airlines_1987_to_2008)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Much to our surprise, this code block returning the same DataFrame ran much faster! For us, it only took *1.73 seconds*. But how did this happen? Let's find out.
# MAGIC 
# MAGIC It all comes down to our use of **inferSchema**. When using this option, Spark scans the dataset to automatically determine the correct data types. But as the data size increases, so does the size of data that Spark needs to scan. For instance, just imagine working with terabytes of data! In that case, a huge amount of time would be spent scanning the data for inferring the correct data types. In order to avoid this, we tend to manually define the schema to save time and resources.

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Learning to differentiate CSV and Parquet

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Data scientists are more used to CSV files than Parquet files in the majority of the cases. When they are starting to use Databricks and Spark, it becomes quite obvious that they'll continue working with CSV files. Making that switch to Parquet might be daunting at first, but in the long run, it reaps huge returns!
# MAGIC 
# MAGIC Let's first discuss the advantages and disadvantages of CSV and Parquet files:
# MAGIC 
# MAGIC **Advantages of CSV files**:
# MAGIC 
# MAGIC -   CSV is the most common file type among data scientists and users.
# MAGIC -   They are human-readable, as data is not encoded before storing. They are also easy to edit.
# MAGIC -   Parsing CSV files is very easy, and they can be read by almost any text editor.
# MAGIC 
# MAGIC **Advantages of Parquet files**:
# MAGIC 
# MAGIC -   Parquet files are compressed using various compression algorithms, which is why they consume less space.
# MAGIC -   Being a columnar storage type, Parquet files are very efficient when reading and querying data.
# MAGIC -   The file carries the schema with itself and is partitioned in nature.
# MAGIC -   With Parquet files, Spark scans much less data than with CSV files. This leads to a reduction in costs.
# MAGIC 
# MAGIC **Disadvantages of CSV files**:
# MAGIC 
# MAGIC -   They cannot be partitioned, and being a row-based storage type, they are not very efficient for reading and querying data.
# MAGIC -   In the majority of use cases, when using CSV with Spark, the entire dataset needs to be scanned for working with the data.
# MAGIC 
# MAGIC **Disadvantages of Parquet files**:
# MAGIC 
# MAGIC -   Parquet files are not human-readable.
# MAGIC 
# MAGIC Parquet file formats have greatly reduced storage and data scanning requirements. Also, they work very well in partitions and help to leverage Spark's parallelism. A 1 TB CSV file, when converted to Parquet, can bring down the storage requirements to as low as 100 GB in cloud storage. This helps Spark to scan less data and speed up jobs in Databricks.

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Using built-in spark functions

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Spark gives us several built-in functions for working with DataFrames. These functions are built in such a way that they can be optimized by the catalyst optimizer. The *catalyst optimizer* is an essential component of the Spark program that helps to optimize our code using advanced programming constructs. It works very well with Spark DataFrames and built-in functions (higher-order functions). However, in the case of a UDF, the catalyst optimizer treats it as a black box. As a result, we see performance bottlenecks.
# MAGIC 
# MAGIC To learn about all the built-in functions in PySpark, check out the official documentation:
# MAGIC 
# MAGIC [https://spark.apache.org/docs/latest/api/python/_modules/pyspark/sql/functions.html](https://spark.apache.org/docs/latest/api/python/_modules/pyspark/sql/functions.html%0D)
# MAGIC 
# MAGIC In the following example, we are going to see performance differences between Spark higher-order functions and UDFs:
# MAGIC 
# MAGIC Let's begin by creating a Spark DataFrame in a new cell:

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

manual_schema = StructType([
  StructField('Year',IntegerType(),True),
  StructField('Month',IntegerType(),True),
  StructField('DayofMonth',IntegerType(),True),
  StructField('DayOfWeek',IntegerType(),True),
  StructField('DepTime',StringType(),True),
  StructField('CRSDepTime',IntegerType(),True),
  StructField('ArrTime',StringType(),True),
  StructField('CRSArrTime',IntegerType(),True),
  StructField('UniqueCarrier',StringType(),True),
  StructField('FlightNum',IntegerType(),True),
  StructField('TailNum',StringType(),True),
  StructField('ActualElapsedTime',StringType(),True),
  StructField('CRSElapsedTime',StringType(),True),
  StructField('AirTime',StringType(),True),
  StructField('ArrDelay',StringType(),True),
  StructField('DepDelay',StringType(),True),
  StructField('Origin',StringType(),True),
  StructField('Dest',StringType(),True),
  StructField('Distance',StringType(),True),
  StructField('TaxiIn',StringType(),True),
  StructField('TaxiOut',StringType(),True),
  StructField('Cancelled',IntegerType(),True),
  StructField('CancellationCode',StringType(),True),
  StructField('Diverted',IntegerType(),True),
  StructField('CarrierDelay',StringType(),True),
  StructField('WeatherDelay',StringType(),True),
  StructField('NASDelay',StringType(),True),
  StructField('SecurityDelay',StringType(),True),
  StructField('LateAircraftDelay',StringType(),True)
])

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The preceding code block defines the schema of the DataFrame that we are trying to create.
# MAGIC 
# MAGIC Next, it's time to create the DataFrame and display it by passing in the schema:

# COMMAND ----------

# Read csv files to create Spark dataframe
airlines_2007_to_2008 = (
  spark
  .read
  .option("header",True)
  .option("delimiter",",")
  .schema(manual_schema)
  .csv("dbfs:/databricks-datasets/asa/airlines/{2007,2008}.csv")
)
# View the dataframe
display(airlines_2007_to_2008)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC In order to capture the performance differences, we will first use the **regexp_replace** higher-order function to replace the airport codes in the **Origin** column with their full names. For example, the **ATL** airport code needs to be replaced with **Hartsfield-Jackson International Airport**. With this, we will create a Spark DataFrame and then write it to **DBFS** in **delta** format:

# COMMAND ----------

# Using higher order functions

built_in_df = (airlines_2007_to_2008
        .withColumn('Origin',
                    when(col('Origin') == 'ATL',regexp_replace(col('Origin'),'ATL','Hartsfield-Jackson International Airport'))
                    .when(col('Origin') == 'DFW',regexp_replace(col('Origin'),'DFW','Dallas/Fort Worth International Airport'))
                    .when(col('Origin') == 'DEN',regexp_replace(col('Origin'),'DEN','Denver International Airport'))
                    .when(col('Origin') == 'ORD',regexp_replace(col('Origin'),'ORD','O Hare International Airport'))
                    .when(col('Origin') == 'LAX',regexp_replace(col('Origin'),'LAX','Los Angeles International Airport'))
                    .when(col('Origin') == 'CLT',regexp_replace(col('Origin'),'CLT','Charlotte Douglas International Airport'))
                    .when(col('Origin') == 'LAS',regexp_replace(col('Origin'),'LAS','McCarran International Airport'))
                    .when(col('Origin') == 'PHX',regexp_replace(col('Origin'),'PHX','Phoenix Sky Harbor International Airport'))
                    .when(col('Origin') == 'MCO',regexp_replace(col('Origin'),'MCO','Orlando International Airport'))
                    .when(col('Origin') == 'SEA',regexp_replace(col('Origin'),'SEA','Seattle–Tacoma International Airport'))
                    .when(col('Origin') == 'MIA',regexp_replace(col('Origin'),'MIA','Miami International Airport'))
                    .when(col('Origin') == 'IAH',regexp_replace(col('Origin'),'IAH','George Bush Intercontinental Airport'))
                    .when(col('Origin') == 'JFK',regexp_replace(col('Origin'),'JFK','John F. Kennedy International Airport'))
                    .otherwise(None)
                   )
       )

# Write the dataframe to DBFS
built_in_df.write.format('delta').mode('overwrite').save('dbfs:/built_in_df')

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Let's note the time taken for the command to run. For us, it took 5.94 minutes. We will now perform the same operation, but this time with a UDF. To begin with, let's write the UDF:

# COMMAND ----------

import re

# Creating UDF
airports = {'ATL':'Hartsfield-Jackson International Airport','DFW':'Dallas/Fort Worth International Airport','DEN':'Denver International Airport','ORD':'O Hare International Airport','LAX':'Los Angeles International Airport','CLT':'Hartsfield-Jackson International Airport','LAS':'McCarran International Airport','PHX':'Phoenix Sky Harbor International Airport','MCO':'Orlando International Airport','SEA':'Seattle–Tacoma International Airport','MIA':'Miami International Airport','IAH':'George Bush Intercontinental Airport','JFK':'John F. Kennedy International Airport'}

def replace_origin(origin):
  
  for key in airports:
    
    if origin == key:
      replaced = re.sub(key,airports[key],origin)
      return replaced
  
  return None

replace_origin_udf = udf(replace_origin,StringType())

# Creating another dataframe and using UDF
udf_df = (airlines_2007_to_2008
        .withColumn('Origin',replace_origin_udf('Origin'))
       )

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The preceding code block defines a UDF, **replace_origin_udf**, which we will use with our DataFrame to replace the same airport IATA codes with their full names.
# MAGIC 
# MAGIC Next, we will create a Spark DataFrame and write it to DBFS in the delta format:

# COMMAND ----------

# Writing dataframe to 
udf_df.write.format('delta').mode('overwrite').save('dbfs:/udf_df')

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC This command took *6.32 minutes* for us, and it is always going to be higher than what we will get using Spark's built-in functions. The reason for this behavior is the serialization of code. When we write any Spark code, it has to be serialized, sent to the executors, and then deserialized before any output can be obtained.
# MAGIC 
# MAGIC In the case of Python, or more appropriately, PySpark, there is an even harder hit in performance because the code always needs to be pickled, and Spark must set up an instance of a Python interpreter on every executor. Besides the cost of serialization and deserialization, there is another issue -- the catalysts optimizer doesn't understand UDFs, and therefore cannot connect any code before or after it. This is why the cost of such operations is always higher. And as the data size increases, so will the code execution times, provided the cluster configurations remain consistent.
# MAGIC 
# MAGIC The best practice is to use Spark built-in functions as much as possible. In the case of scenarios where these functions are not fulfilling their purpose, UDFs may be employed. This usually happens when certain complex business logic needs to be implemented. In the next section, we will learn about column predicate pushdown.

# COMMAND ----------

# MAGIC %md 
# MAGIC ### Columns Predicate Pushdown

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC *Column predicate pushdown* is an optimization technique where we filter down to the level of the data source to reduce the amount of data getting scanned. This greatly enhances jobs, as Spark only reads the data that is needed for operations. For example, if we are reading from a **Postgres** database, we can push down a filter to the database to ensure that Spark only reads the required data. The same can be applied to Parquet and delta files as well. While writing Parquet and delta files to the storage account, we can partition them by one or more columns. And while reading, we can push down a filter to read only the required partitions.
# MAGIC 
# MAGIC In the following steps, we will look at an example of column predicate pushdown with Parquet files:
# MAGIC 
# MAGIC To get started, we will re-create our airlines DataFrame in a new cell:

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

manual_schema = StructType([
  StructField('Year',IntegerType(),True),
  StructField('Month',IntegerType(),True),
  StructField('DayofMonth',IntegerType(),True),
  StructField('DayOfWeek',IntegerType(),True),
  StructField('DepTime',StringType(),True),
  StructField('CRSDepTime',IntegerType(),True),
  StructField('ArrTime',StringType(),True),
  StructField('CRSArrTime',IntegerType(),True),
  StructField('UniqueCarrier',StringType(),True),
  StructField('FlightNum',IntegerType(),True),
  StructField('TailNum',StringType(),True),
  StructField('ActualElapsedTime',StringType(),True),
  StructField('CRSElapsedTime',StringType(),True),
  StructField('AirTime',StringType(),True),
  StructField('ArrDelay',StringType(),True),
  StructField('DepDelay',StringType(),True),
  StructField('Origin',StringType(),True),
  StructField('Dest',StringType(),True),
  StructField('Distance',StringType(),True),
  StructField('TaxiIn',StringType(),True),
  StructField('TaxiOut',StringType(),True),
  StructField('Cancelled',IntegerType(),True),
  StructField('CancellationCode',StringType(),True),
  StructField('Diverted',IntegerType(),True),
  StructField('CarrierDelay',StringType(),True),
  StructField('WeatherDelay',StringType(),True),
  StructField('NASDelay',StringType(),True),
  StructField('SecurityDelay',StringType(),True),
  StructField('LateAircraftDelay',StringType(),True)
])

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The preceding code block defines the schema of the DataFrame that we are trying to create.
# MAGIC 
# MAGIC Next, it's time to create the DataFrame and display it by passing in the schema:

# COMMAND ----------

# Read csv files to create Spark dataframe
airlines_2007_to_2008 = (
  spark
  .read
  .option("header",True)
  .option("delimiter",",")
  .schema(manual_schema)
  .csv("dbfs:/databricks-datasets/asa/airlines/{2007,2008}.csv")
)
# View the dataframe
display(airlines_2007_to_2008)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Next, we will write the DataFrame to Parquet in two ways:
# MAGIC 
# MAGIC 1.  **Without partitioning**: Here, we will simply write the DataFrame to DBFS in the Parquet format without creating any partitions. Run the following code:

# COMMAND ----------

# Write the dataframe to DBFS
airlines_2007_to_2008.write.format('parquet').mode('overwrite').save('dbfs:/columns_predicate_pushdown')

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC 2. **With partitioning**: Here, we will write the DataFrame to DBFS in Parquet by partitioning by the **DayOfWeek** column. Later, we will be filtering our query on this column. Run the following code:

# COMMAND ----------

# Write the dataframe to DBFS
airlines_2007_to_2008.write.format('parquet').mode('overwrite').partitionBy('DayOfWeek').save('dbfs:/columns_predicate_pushdown_partitioned')

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Now, we will run queries on the two Parquet files that we have created.
# MAGIC 
# MAGIC First, we will be filtering the Parquet file with no partitions to return the count of rows that meet the condition where **DayOfWeek** equals **7**. Run the following code block:

# COMMAND ----------

without_cpp_df = (spark
               .read
               .format('parquet')
               .load('dbfs:/columns_predicate_pushdown')
               .filter(col('DayOfWeek') == 7)
)
without_cpp_df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Note the time taken for the code to run. For us, it took *11.78 seconds*. Let's take a look at the Spark UI to better understand what is happening under the hood. Click on **Spark Jobs** under this command and select **View** next to the second job. This opens up the job page in Spark UI.
# MAGIC 
# MAGIC Click on **Associated SQL Query** to open up the query plan. Here, we can find the Parquet scan details, which tell us the amount of data scanned by Spark. The **number of files read** field indicates the total number of Parquet partition files read. The **rows output** field tells us the number of rows returned by Spark. Here, the number of rows returned equals the total number of rows in the Parquet file. If we scroll down, we can find the **Filter** box. On expanding this box, it tells us that out of 14.46 million records in the Parquet file, only 2.07 million are returned after the filtering process.
# MAGIC 
# MAGIC Similarly, we will now run our code to filter on the Parquet file with partitions:

# COMMAND ----------

with_cpp_df = (spark
               .read
               .format('parquet')
               .load('dbfs:/columns_predicate_pushdown_partitioned')
               .filter(col('DayOfWeek') == 7)
)
with_cpp_df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC This command took only *3.85 seconds*! And it is not hard to guess why we observed this behavior. Let's take a look at the SQL query plan in the Spark UI. 
# MAGIC 
# MAGIC The query plan clearly tells us that Spark only read 2.07 million records. This happened because we partitioned our data by the **DayOfWeek** column. So, Spark had to read the partition where the filter condition met successfully. We can also verify this by taking a look at the contents inside the Parquet file directory:

# COMMAND ----------

# MAGIC %fs ls dbfs:/columns_predicate_pushdown_partitioned

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Even if we are using predicate pushdown with delta, the semantics remain the same, and we get similar performance gains. Similar to this concept, there is another optimization technique called *column pruning*. This simply means reading a subset of columns from a data store or DataFrame. For instance, say for every row we have 1,000 columns, but we only require five columns for our current purpose. In this case, we will only read five columns.
# MAGIC 
# MAGIC We have started learning about partitioning, and we will learn about some more partitioning strategies in the next section.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Partitioning strategies

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC In this section, we will discuss some of the useful strategies for Spark partitions and **Apache** **Hive** partitions. Whenever Spark processes data in memory, it breaks that data down into partitions, and these partitions are processed in the cores of the executors. These are the Spark partitions. On the other hand, Hive partitions help to organize persisted tables into parts based on columns.

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC #### Understanding Spark partitions

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Before we learn about the strategies to manage Spark partitions, we need to know the number of partitions for any given DataFrame:
# MAGIC 
# MAGIC To check the Spark partitions of a given DataFrame, we use the following syntax: **dataframe.rdd.getNumPartitions()**. Also, remember that the total number of tasks doing work on a Spark DataFrame is equal to the total number of partitions of that DataFrame.
# MAGIC 
# MAGIC Next, we will learn how to check the number of records in each Spark partition. We will begin with re-creating the airlines DataFrame, but this time with **Scala**. We are shifting to Scala so that we can use the **mapPartitionsWithIndex** function. Run the following code block to create the DataFrame and display it:

# COMMAND ----------

# MAGIC %scala
# MAGIC // Read csv files to create Spark dataframe
# MAGIC val airlines_2007_to_2008 = (
# MAGIC   spark
# MAGIC   .read
# MAGIC   .option("header",true)
# MAGIC   .option("delimiter",",")
# MAGIC   .option("inferSchema",true)
# MAGIC   .csv("dbfs:/databricks-datasets/asa/airlines/{2007,2008}.csv")
# MAGIC )
# MAGIC // View the dataframe
# MAGIC display(airlines_2007_to_2008)

# COMMAND ----------

# MAGIC %scala
# MAGIC // Check number of partitions in spark dataframe
# MAGIC airlines_2007_to_2008.rdd.getNumPartitions

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Our DataFrame has 11 partitions! Now we will execute Scala code that displays the number of records in each partition:

# COMMAND ----------

# MAGIC %scala
# MAGIC display(airlines_2007_to_2008
# MAGIC   .rdd
# MAGIC   .mapPartitionsWithIndex{case (i,rows) => Iterator((i,rows.size))}
# MAGIC   .toDF("partition_number","number_of_records")
# MAGIC   )

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Here, we get a DataFrame consisting of two columns:
# MAGIC 
# MAGIC 1.  **partition_number**: This gives a unique ID to every partition of the DataFrame, starting from **0**.
# MAGIC 2.  **number_of_records**: This indicates the number of records in a particular partition.
# MAGIC 
# MAGIC We can even create a histogram from this DataFrame to understand data skew in the DataFrame. *Data skewing* simply refers to the phenomenon where some partitions of the DataFrame are heavily loaded with records while others are not. In other words, DataFrames that have data evenly spread across partitions are not skewed in nature.
# MAGIC 
# MAGIC We can also use a Spark configuration, **spark.sql.files.maxPartitionBytes**, to limit the maximum size of a Spark partition when reading from Parquet, **JSON**, or **ORC** files. By default, the limit is set to 128 MB. The syntax is as follows, where **N** equals the maximum size in bytes:
# MAGIC 
# MAGIC ```
# MAGIC spark.conf.set("spark.sql.files.maxPartitionBytes",N)
# MAGIC ```
# MAGIC 
# MAGIC Apart from this, there are also two very useful functions to manage Spark partitions. These functions are used to change the number of Spark partitions of a DataFrame:
# MAGIC 
# MAGIC -   **repartition()**: This function is used to increase or decrease the number of Spark partitions for a DataFrame. It induces a shuffle when called and is often very helpful to remove skew from a DataFrame. The syntax is **dataframe.repartition(number)**. Here, **number** designates the new partition count of the DataFrame. The **repartition** function leads to roughly equally sized partitions.
# MAGIC -   **coalesce()**: This function is used to decrease the number of partitions and is extremely helpful when the partition count needs to be drastically reduced. Also, note that it does not lead to shuffling. The syntax is **dataframe.coalesce(number)**. Here, **number** designates the new partition count of the DataFrame. The **coalesce** function can often lead to skew in partitions.
# MAGIC 
# MAGIC To check the number of cores in a cluster programmatically, we can use:

# COMMAND ----------

spark.sparkContext.defaultParallelism

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC If we have more cores and fewer partitions and fewer tasks being performed, then it is better to increase the partitions of the DataFrame so that all the cores get engaged. This can be very useful with the delta file format, as even though the result of such a job might spit out small files, these could be later compacted using various techniques. Next, we will learn about how to effectively manage Hive partitions.

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC #### Understanding Hive partitions

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Apache Hive is a data warehouse project that provides an SQL-like interface to query data stored in databases and file systems. We have already seen an example of partitioning with parquet in an earlier section. In this section, we will look at an example of partitioning with delta. We will first create a delta file partitioned by the year and month in a nested fashion. Then, using that file, we will create an external Hive table (delta table) in Databricks.
# MAGIC 
# MAGIC To get started, we will re-create our airlines DataFrame in a new cell:

# COMMAND ----------

from pyspark.sql.types import *
from pyspark.sql.functions import *

manual_schema = StructType([
  StructField('Year',IntegerType(),True),
  StructField('Month',IntegerType(),True),
  StructField('DayofMonth',IntegerType(),True),
  StructField('DayOfWeek',IntegerType(),True),
  StructField('DepTime',StringType(),True),
  StructField('CRSDepTime',IntegerType(),True),
  StructField('ArrTime',StringType(),True),
  StructField('CRSArrTime',IntegerType(),True),
  StructField('UniqueCarrier',StringType(),True),
  StructField('FlightNum',IntegerType(),True),
  StructField('TailNum',StringType(),True),
  StructField('ActualElapsedTime',StringType(),True),
  StructField('CRSElapsedTime',StringType(),True),
  StructField('AirTime',StringType(),True),
  StructField('ArrDelay',StringType(),True),
  StructField('DepDelay',StringType(),True),
  StructField('Origin',StringType(),True),
  StructField('Dest',StringType(),True),
  StructField('Distance',StringType(),True),
  StructField('TaxiIn',StringType(),True),
  StructField('TaxiOut',StringType(),True),
  StructField('Cancelled',IntegerType(),True),
  StructField('CancellationCode',StringType(),True),
  StructField('Diverted',IntegerType(),True),
  StructField('CarrierDelay',StringType(),True),
  StructField('WeatherDelay',StringType(),True),
  StructField('NASDelay',StringType(),True),
  StructField('SecurityDelay',StringType(),True),
  StructField('LateAircraftDelay',StringType(),True)
])

# Read csv files to create Spark dataframe
airlines_2007_to_2008 = (
  spark
  .read
  .option("header",True)
  .option("delimiter",",")
  .schema(manual_schema)
  .csv("dbfs:/databricks-datasets/asa/airlines/{2007,2008}.csv")
)

# Partition and write the dataframe
(airlines_2007_to_2008.write
 .format('delta')
 .mode('overwrite')
 .partitionBy('Year','Month')
 .save('dbfs:/airlines_2007_to_2008_partitioned')
)

# COMMAND ----------

# MAGIC %fs ls dbfs:/airlines_2007_to_2008_partitioned

# COMMAND ----------

# MAGIC %fs ls dbfs:/airlines_2007_to_2008_partitioned/Year=2007/

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Now, we will create a delta table that will be registered in the **Hive** **Metastore**. Run the following code to create the delta table:

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE airlines
# MAGIC USING DELTA
# MAGIC LOCATION 'dbfs:/airlines_2007_to_2008_partitioned'

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC We can further validate if the delta table is partitioned as expected or not. Run the **%sql DESCRIBE DETAIL airlines** command, and this returns a table containing a lot of useful metadata about the delta table (Hive table). Here, the **partitionColumns** field confirms that our table has been partitioned by **Year** and **Month**.

# COMMAND ----------

# MAGIC %sql DESCRIBE DETAIL airlines

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC This concludes our discussion on partitioning strategies. Next, we will learn about some helpful Spark SQL optimizations.

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ### Understanding Spark SQL optimizations
# MAGIC 
# MAGIC In this section, we will learn about how to write efficient Spark SQL queries, along with tips to help optimize the existing SQL queries:
# MAGIC 
# MAGIC -   Avoid using **NOT IN** in the SQL queries, as it is a very expensive operation.
# MAGIC -   Filter the data before performing join operations by using the **WHERE** clause before joining the tables.
# MAGIC -   Mention the column name when using the **SELECT** clause instead of giving a ***** to select all of them. Try to use the columns required for operations instead of selecting all of them unnecessarily.
# MAGIC -   Avoid using **LIKE** in the **WHERE** clause, as it is another expensive operation.
# MAGIC -   Try not to join the same set of tables multiple times. Instead, write a **common table expression** (**CTE**) using the **WITH** clause to create a subquery, and use it to join the tables wherever necessary.
# MAGIC -   When joining the same table for different conditions, use the **CASE** statements.
# MAGIC 
# MAGIC In the next and final section of this lab, we will learn about bucketing in Spark.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Bucketing

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC *Bucketing* is an optimization technique that helps to prevent shuffling and sorting of data during compute-heavy operations such as joins. Based on the bucketing columns we specify, data is collected in a number of *bins*. Bucketing is similar to partitioning, but in the case of partitioning, we create directories for each partition. In bucketing, we create equal-sized buckets, and data is distributed across these buckets by a hash on the value of the bucket. Partitioning is helpful when filtering data, whereas bucketing is more helpful during joins.
# MAGIC 
# MAGIC It is often helpful to perform bucketing on dimension tables that contain primary keys for joining. Bucketing is also helpful when join operations are being performed between small and large tables. In this section, we will go through a quick example to understand how to implement bucketing on a Hive table.
# MAGIC 
# MAGIC We will begin by creating a Spark DataFrame in a new cell. Run the following code block:

# COMMAND ----------

from pyspark.sql.functions import *
# Create a sample dataframe
sample_df = spark.range(start = 1, end = 100000001, step = 1, numPartitions = 100).select(col("id").alias("key"),rand(seed = 12).alias("value"))
display(sample_df)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Here, we create a Spark DataFrame, **sample_df**, with 100 million rows and 100 Spark partitions. It has two columns: **id** and **value**. Let's validate the number of Spark partitions using **sample_df.rdd.getNumPartitions()**. Now, we will validate the count of the DataFrame. Run **sample_df.count()** to confirm the count of the DataFrame.

# COMMAND ----------

# Check number of spark partitions
sample_df.rdd.getNumPartitions()

# COMMAND ----------

# Check count of dataframe
sample_df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Next, we will write the DataFrame as a bucket Hive table in a Parquet format. We will create 100 buckets in the table. Run the following code block to write the DataFrame as a bucketed table:

# COMMAND ----------

# Write as bucketed table
(sample_df
 .write
 .format('parquet')
 .mode('overwrite')
 .bucketBy(100, "key")
 .sortBy("value")
 .saveAsTable('bucketed_table')
)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC Once the code block has finished executing, we can confirm if the table has been bucketed as per the configurations we have provided. To confirm this, let's run the following code:

# COMMAND ----------

# MAGIC %sql DESCRIBE TABLE EXTENDED bucketed_table

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC The output confirms that our table has been *bucketed* into 100 bins, using the **key** column.

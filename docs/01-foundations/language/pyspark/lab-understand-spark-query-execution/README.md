# Lab: Understanding Spark Query Execution

To write efficient Spark applications, we need to have some understanding of how Spark executes queries. Having a good understanding of how Spark executes a given query helps big data developers/engineers work efficiently with large volumes of data.

Query execution is a very broad subject, and, in this lab, we will understand jobs, stages, and tasks. We will also learn how Spark lazy evaluation works, how to check and understand the execution plan when working with DataFrames or SparkSQL, how joins work in Spark and the different types of join algorithms Spark uses while joining two tables. We will also learn about the input, output, and shuffle partitions and the storage benefits of using different file formats.

Knowing about the internals will help you troubleshoot and debug your Spark applications more efficiently. By the end of this lab, you will know how to execute Spark queries, as well as how to write and debug your Spark applications more efficiently.

We're going to cover the following recipes:

- Introduction to jobs, stages, and tasks
- Checking the execution details of all the executed Spark queries via the Spark UI
- Deep diving into schema inference
- Looking into the query execution plan
- How joins work in Spark
- Learning about input partitions
- Learning about output partitions
- Learning about shuffle partitions
- The storage benefits of different file types

## Setup

You will find a dbc file in assets folder. Import that file in databricks. It will create a folder named `job-process`. Inside this folder, you will find the notebooks we are using in this lab.

![Screen Shot 2023-02-13 at 6 48 31 PM](https://user-images.githubusercontent.com/62965911/218468595-84f79396-c6a4-487c-a60f-2b80caa9bcb2.png)

## Introduction to jobs, stages, and tasks

In this recipe, you will learn how Spark breaks down an application into job, stages, and tasks. You will also learn how to create **directed acyclic graphs** (**DAGs**) and how pipelining works in Spark query execution.

By the end of this recipe, you will have learned how to check the DAG you've created for the query you have executed and look at the jobs, stages, and tasks associated with a specific query.

We are using `01-introduction-to-jobs-stages-and-tasks` notebook.

Follow these steps to check the jobs, number of stages, and tasks Spark created while executing the query via the Spark UI:

Step 1 - Run the notebook cells upto first aggregate display and open the `SQL / DataFrame` DAG:

![Databricks Shell - Details for Query 14](https://user-images.githubusercontent.com/62965911/218369607-e6659ec1-1a79-4bf1-9e64-43103e5f8f1e.png)

Under Spark Jobs, we can see that two stages have been created. Multiple stages are created when there is a shuffle involved. A shuffle operation is involved when the data is moved across the nodes, and this happens when we are using transformations such as average and sum. The sum transformation needs to collect data from various executors and send it to the driver node when actions such as Show display or Limit are called. As you can see, there is an exchange operator involved as we are performing aggregations on the data that we read from the CSV file.

Here, you can also see that there are multiple sortAggregates in the DAG. One was created by the mapper, while another was created after the exchange operator. This happens before the results are given to the driver.

Step 2 - Now run the next aggregate and display. Go to the DAG:

![Databricks Shell - Details for Query 15](https://user-images.githubusercontent.com/62965911/218370127-9962eaed-c152-4b1e-bb07-fdd5b6307831.png)

Your task is to compare these 2 dags and analyze the differences. For your help, I am putting the 2 queries here:

```python
#Query 1 - Group By on C_MKTSEGMENT.
df_cust_agg = df_cust.groupBy("C_MKTSEGMENT")\
   .agg(sum("C_ACCTBAL").cast('decimal(20,3)').alias("sum_acctbal"), \
     avg("C_ACCTBAL").alias("avg_acctbal"), \
     max("C_ACCTBAL").alias("max_bonus")).orderBy("avg_acctbal",ascending=False)
```

```python
#Query 2 - Without groupBy and check the DAG for this query execution by executing the display command in the next cell
df_cust_agg = df_cust.\
agg(sum("C_ACCTBAL").cast('decimal(20,3)').alias("sum_acctbal"), \
     avg("C_ACCTBAL").alias("avg_acctbal"), \
     max("C_ACCTBAL").alias("max_bonus"))#.orderBy("avg_acctbal",ascending=False)
```

## Deep diving into schema inference

In this recipe, you will learn about the benefits of explicitly specifying a schema while reading any file format data from an **ADLS Gen-2,** **Azure Blob storage** or **S3** storage account.

By the end of this recipe, you will have learned how Spark executes a query when a schema is inferred versus explicitly specified.

We are using `02-schema-inference` notebook.

You can learn about the benefits of specifying a schema while reading the files from your storage account. First, we will read the set of files by inferring the schema from the file and explicitly specify the schema. Then, we will look at how Spark's execution differs in both scenarios:

We will read the CSV files directly from the mount point without specifying any schema options.

Spark uses the concept of lazy evaluation, which means until an action is called, Spark will not execute the query. In the preceding query, we haven't invoked an action, and all transformation are lazy in nature. This means that you should not see a DAG when there are no actions in the query. However, after executing the preceding query, you will see that the Spark optimizer has created a DAG:

```python
# Reading customer csv files in a dataframe with specifying the schema explicitly
df_cust = spark.read.format("csv").option("header", True).option(
    "inferSchema", True).load("s3a://wysde-datasets/spark/Customer/csvFiles")
```

Now, we will create a schema and explicitly provide it while reading the **.csv** files in a DataFrame.

```python
df_cust_sch = spark.read.format("csv").option("header", True).schema(
    cust_schema).load("s3a://wysde-datasets/spark/Customer/csvFiles")
```

After running the preceding query, you will see that Spark hasn't generated a DAG for the query and that the execution time has reduced from 16.9 seconds to 1.83 seconds.

Thus, it is always recommended to specify the schema wherever possible, as this will improve the performance of your queries. This is because you're not creating the DAG when no action is being triggered. But in scenarios where we don't have a schema at hand and we want to create one, we can read one file from the entire folder and get the schema for the underlying dataset:

```python
# Using first file
df_cust_sch = spark.read.format("csv").option("header", True).load(
    "s3a://wysde-datasets/spark/Customer/csvFiles/part-00000-tid-3200334632332214470-9b4dec79-7e2e-495d-8657-3b5457ed3753-108-1-c000.csv")
```

When the preceding query is executed, you will see that a DAG has been created but not multiple stages and that fewer tasks have been completed. You will also see that the execution duration is only 2.34 seconds. After executing the preceding query, you can get the schema by running the **df_cust_sch.printSchema()** command, which you can use to define a schema and use it while reading the **.csv** files.

By inferring the schema, you are asking Spark to identify all the columns and the data types of the column(s). Providing the schema while creating a DataFrame removes the overhead of reading the data types and columns we expect from the **.csv** files. Only at runtime does it validate whether the schema is matching the columns in the files. If the column(s) that are mentioned in the schema can't be found in the **.csv** files, then you will see **NULL** as the value in those columns. Ensure the column's name maps to the columns you have in the underlying **.csv** files.

As we mentioned in the preceding section, if you are not sure what the schema of the dataset it, you can get the schema by creating the DataFrame. Do this by reading only one file and printing the schema that Spark has inferred. You can use the schema that was identified by Spark, and then define the required schema that will be used to read all the **.csv** files and improve the performance of your query.

**There's more...**

To identify why it takes more time to read the **.csv** files when an action isn't performed, check the number of partitions that Spark created while reading the **.csv** files to infer the schema. Based on the number of cores in your cluster, you will see a significantly high number. If you specify just one file to infer the schema, you will see a different number for the partition count.

In case of only one csv file, only one partition was created and that the time it takes to read one file is much faster than reading all the files in the folder. We will discuss the different types of partitions later in this lab.

## Looking into the query execution plan

It's important to understand the execution plan and how to view its different stages when the Spark optimizer executes a query using a dataframe or the SparkSQL API.

In this recipe, we will learn how to create a logical and physical plan and the different stages involved. By the end of this recipe, you will have generated an execution plan using the dataframe API or the SparkSQL API and have a fair understanding of the different stages involved.

We are using `03-query-execution-plan` notebook.

Let's learn how to generate an execution plan using the dataframe API or SparkSQL API, understand the various stages involved, and identify how the execution plan can be viewed from the Spark UI.

First read the csv files into dataframe and then create an aggregate query using market segment by running the following code. We will filter the DataFrame on the machinery market segment and get all the records where **AvgAcctBal>4500**. We can also check the execution plan.

```python
df_agg = df_cust_sch.groupBy("C_MKTSEGMENT").agg(
    avg("C_ACCTBAL").alias("AvgAcctBal"))
df_agg.where(df_agg.C_MKTSEGMENT == "MACHINERY").where(
    df_agg.AvgAcctBal > 4500).show()
```

After running the preceding query, we must get the DAG for the query we executed. Click on **ID for your query**. When you scroll to the end, you will find details of the execution plan for the dataframe or SparkSQL API. It will contain the **Parsed Logical Plan**, **Analyzed Logical Plan**, **Optimized Logical Plan**, and **Physical Plan stages**:

![B12761_03_19](https://user-images.githubusercontent.com/62965911/218402422-2d93a404-64c3-49fa-b324-7e7ff9b840aa.jpg)

Now, let's learn how to get the plan using the **Explain()** function. The plans that are generated using the dataframe API and SparkSQL API is the same. Create a **tempview**, and execute the following command to generate an execution plan using both APIs:

```python
df_cust_sch.createOrReplaceTempView("df_Customer")
sql = spark.sql("SELECT C_MKTSEGMENT, count(1) FROM df_Customer GROUP BY C_MKTSEGMENT ")

dataframe = df_cust_sch\
  .groupBy("C_MKTSEGMENT")\
  .count()

sql.explain()
dataframe.explain()
```

The following is the output of executing the preceding code:

![Screen Shot 2023-02-13 at 1 40 52 PM](https://user-images.githubusercontent.com/62965911/218404255-1a52e385-2eb3-4639-ae32-b07b4bcfc7c2.png)

Here, you can see that the plan is similar to the query's, which was executed using two different APIs.

**How it works...**

You can use either the Spark UI or the **Explain()** command to get the execution plan for the query. Whether you use the dataframe API or the SparkSQL API, the execution plan that's generated by Spark is similar. This gives the developer the flexibility to use their API of choice.

If the data has been partitioned, you can also view the partition filters by using the appropriate partitions. This will help you avoid reading all the data. If there is a **where** clause, you can find the **PushedFilters** value that was populated for the predicate clause you are using in your query. The following example shows the where clause in the query. Here, you will find **PushedFilters**, which helps in restricting the data that is fetched while reading the data:

![Screen Shot 2023-02-13 at 1 36 28 PM](https://user-images.githubusercontent.com/62965911/218403897-aeee8a19-6b8f-4748-951a-4d4986763961.png)

At the core of SparkSQL is the Catalyst optimizer, which breaks down a query that's been submitted by the user into multiple phases. It does this by using optimization techniques, which efficiently execute the query:

![B12761_03_22](https://user-images.githubusercontent.com/62965911/218404405-5daaa820-409e-4b98-b209-805fc37a1d85.jpeg)

Here, we can see that there are multiple phases that the Spark Catalyst optimizer goes through. It shows how a query that's been submitted for execution is parsed into multiple logical and physical plans and then converted into Define acronym, which then gets executed.

## How joins work in Spark 

In this recipe, you will learn how query joins are executed by the Spark optimizer using different types of sorting algorithms such as **SortMerge** and **BroadcastHash** joins. You will learn how to identify which algorithm has been used by looking at the DAG that Spark generates. You will also learn how to use the hints that are provided in the queries to influence the optimizer to use a specific join algorithm.

We are using `04-joins` notebook.

Let's learn how to identify the **join** algorithm the optimizer uses to join two DataFrames.

First, run initial cells of the notebook to load the orders and customer dataframes with the given schema and data paths.

Now, get the default value for **autoBroadcastJoinThreshold**. The output of the preceding query should be **10485760**, which is 10 MB. We will change the default value for **autoBroadcastJoinThreshold** to 2 MB from 10 MB to simulate that we are joining two large tables. The size of the customer DataFrame is around 5 MB.

We will execute a query that will perform an equijoin between the two DataFrames. Then, we will look at the DAG that Spark creates:

![Databricks Shell - Details for Query 38](https://user-images.githubusercontent.com/62965911/218411843-39181aff-f888-493d-8776-fe7bdd692f2a.png)

Here, we can see that the **BroadcastHash** join algorithm is being used.

**How it works...**

The Spark query optimizer identifies which join algorithm should be used based on the size of the data in both tables/DataFrames that were used in the query. The **SortMerge** join is used when the size of both tables/DataFrames is large. If the table/DataFrame that's used in the join size is less than 10 MB, then the **BroadcastHash** join algorithm will be used. So, when we are joining a big table to another big table, the **SortMerge** join will be used, while if we are joining a big table to a small table, then the **BroadcastHash** join will be used.

In the **BroadcastHash** join, there is **BroadcastExchange**. Here, a smaller dataset is transferred to every executor on the worker nodes, and it avoids data shuffle between the nodes. This approach improves the query's performance as no shuffle operation happens. This is because all the executors have the smaller table cached locally, in memory. The optimizer checks if the size of the smaller table is less than 10 MB and then broadcasts the smaller table to all the executors. If the size of the table(s) is greater than 10 MB, then the **SortMerge** algorithm will be used to join the two DataFrames/tables in a Spark 2.4.5 cluster.

Spark 3.0.x or later, the behavior is a little different, as they auto-optimize it further and selects **BroadcastHash** strategy even though you set the parameter to 2 MB. When we use a Spark 3.0.x cluster, the optimizer generates a different DAG when we set the value for **autoBroadcastJoinThreshold** to less than 10 MB. When we change the **autoBroadcastJoinThreshold** value to 2 MB by attaching the notebook to a Spark 3.x cluster, the Spark engine will use a **BroadcastHash** join algorithm to execute the query.

To force a **sortmerge** join, Spark 3.0.x and later has introduced a new hint called **merge**. We can use this to force the optimizer to use a **SortMerge** join. Execute the query having a merge hint and check the DAG for **SortMerge**:

![Databricks Shell - Details for Query 40](https://user-images.githubusercontent.com/62965911/218415065-47c215c7-45ec-413b-8727-51764c13ab1f.png)

By using the DAG, you will see that the Spark query optimizer is using a **SortMerge** join to join the two dataframes.

## Learning about partitions 

Partitions are subsets of files in memory or storage. In Spark, partitions are more utilized compared to the Hive system or SQL databases. Spark uses partitions for parallel processing and to gain maximum performance.

Spark and Hive partitions are different; Spark processes data in memory, whereas Hive partitions are in storage. In this recipe, we will cover three different partitions; that is, the input, shuffle, and output partitions.

We are using `05-partitions` notebook.

Let's start by looking at input partitions.

### Input partitions

Apache Spark has a layered architecture, and the driver nodes communicate with the worker nodes to get the job done. All the data processing happens in the worker nodes. When the job is submitted for processing, each data partition is sent to the specific executors. Each executor processes one partition at a time. Hence, the time it takes each executor to process data is directly proportional to the size and number of partitions. The more partitions there are, the more work will be distributed across the executors. There will also be fewer partitions. This means that processing will be done faster and in larger chunks.

You can manipulate partitions to speed up data processing.

While sending the partition to each executor, you can control the size of the partitions to get optimized performance.

By specifying the **spark.sql.files.maxPartitionBytes** parameter, you can control the number of bytes that can be packed into single partition. You can do this while reading data from JSON, ORC, and Parquet files.

First, load the dataframe and see the number of partitions that were created for the dataframe. Considering the default block size, 10 partitions will be created.

Now, you can change the default partition size to 1 MB. When you load the dataframe and check the number of partitions, you will see that 30 partitions have been created.

You can tweak the partitions of the files to achieve better parallelism.You can test this by creating partitions based on the number of cores in your cluster.

**How it works...**

Spark reads a HDFS file as a single partition for each file split. Spark's default block size is 128 MB.

Let's understand this by taking an example of 60 GB uncompressed text data files that have been stored in a HDFS filesystem. As you already know, the default block size is 128 MB, so 480 blocks will be created. There will also be 480 partitions. If the data can't be divided, then Spark will use the default number of partitions.

### Output partitions 

Saving partitioned data using the proper condition can significantly boost performance while you're reading and retrieving data for further processing.

Reading the required partition limits the number of files and partitions that Spark reads while querying data. It also helps with dynamic partition pruning.

But sometimes, too many optimizations can make things worse. For example, if you have several partitions, data is scattered within multiple files, so searching the data for particular conditions in the initial query can take time. Also, memory utilization will be more while processing the metadata table as it contains several partitions.

While saving the in-memory data to disk, you must consider the partition sizes as Spark produces files for each task. Let's consider a scenario: if the cluster configuration has more memory for processing the dataframe and saving it as larger partition sizes, then processing the same data even further with a smaller cluster configuration may cause issues while you're reading the saved data.

There are two ways to manage partitions: by using the **repartitioning** and **coalesce** operations.

First, load the necessary data into the dataframe and check the partitions created. you will see that 10 tasks have been created for 10 partitions. Spark created 10 tasks to achieve parallelism.

If you have a very large file, you can increase the number of output partitions that Spark will write the output to using many cores.

You can repartition the existing dataframe using the **repartition** function. You can also pass the name of the column where you want the data to be partitioned.

The **coalesce** method is used to reduce parallelism while processing data. It avoids fully shuffling data by reducing the number of partitions. You should be careful when applying **coalesce** as it may also reduce the number of partitions you are expecting, which will impact parallel processing and performance.

You can remediate the problem we mentioned in the preceding step by passing **shuffle = true**. This adds a shuffle step, but reshuffled partitions will use full cluster resources wherever they're required.

You can use the **maxRecordsPerFile** parameter to control the size of the files. With this parameter we are asking Spark to create files with certain number of records.

**How it works...**

The **repartitioning** operation reduces or increases the number of partitions that the data in the cluster will be split by. This is an expensive operation and involves fully shuffling the data over the network and redistributing the data evenly. When this operation is performed, data is serialized, moved, and then deserialized.

You should only use repartitioning when you understand when it can speed up data processing by Spark jobs. The **coalesce** operation uses existing partitions and reduces the number of partitions to minimize the amount of data that's shuffled. Coalesce results in partitions that contain different amounts of data. In this case, the coalesce operation executor leaves data in a minimum number of partitions and only moves data from redundant nodes. Therefore, the coalesce operation usually runs faster than the repartition operation. But sometimes, when there is a significant difference in the partition sizes, it is slower.

### Shuffle partitions

In this recipe part, you will learn how to set the **spark.sql.shuffle.partitions** parameter and see the impact it has on performance when there are fewer partitions.

Most of the time, in the case of wide transformations, where data is required from other partitions, Spark performs a data shuffle. Unfortunately, you can't avoid such transformations, but we can configure parameters to reduce the impact this has on performance.

Wide transformations uses shuffle partitions to shuffle data. However, irrespective of the data's size or the number of executors, the number of partitions is set to **200**.

The data shuffle procedure is triggered by data transformations such as **join()**, **union()**, **groupByKey(**), **reduceBykey()**, and so on. The **spark.sql.shuffle.partitions** configuration sets the number of partitions to use during data shuffling. The partition numbers are set to 200 by default when Spark performs data shuffling.

Let's learn how the execution time gets reduced when the number of shuffle partitions are reduced for small datasets:

First, load your dataframe from the csv files. Then execute the following code snippet and see how long it takes to execute. Note that the time varies according to the volume of data in the dataframe:

```python
spark.conf.set("spark.sql.shuffle.partitions", 200)
mktSegmentDF = df.groupBy("C_MKTSEGMENT").count().collect()
```

The preceding code took 2.96 seconds to execute on the cluster we used with **spark.sql.shuffle.partitions** set to **200** (default value).

Now, change the value of the **spark.sql.shuffle.partitions** parameter to **30** and look at the execution time for the same query. Note that the execution time when **spark.sql.shuffle.partitions** is set to **30** is 1.57 seconds.

You will see that the time taken after changing the number of partitions to **30** is comparatively less than when the **spark.sql.shuffle.partitions** parameter value was **200**.

**How it works...**

Spark shuffling can increase or decrease the performance of your job, so based on your memory, data size, and processor, the **spark.sql.shuffle.partitions** configuration value must be set. When the data is small, then the number of partitions should be reduced; otherwise, too many partitions containing less data will be created, resulting in too many tasks with less data to process. However, when the data size is huge, having a higher number for the shuffle partition from default 200 might improve the query execution time. There is no direct formula to get the right number for shuffle partitions. It depends on the cluster size and the size of data you are processing.

## Storage benefits of different file types

Storage formats are a way to define how data is stored in a file. Hadoop doesn't have a default file format, but it supports multiple file formats for storing data. Some of the common storage formats for Hadoop are as follows:

- Text files
- Sequence files
- Parquet files
- **Record-columnar (RC)** files
- **Optimized row columnar (ORC)** files
- Avro files

Choosing a write file format will provide significant advantages, such as the following:

- Optimized performance while reading and writing data
- Schema evolution support (allows us to change the attributes in a dataset)
- Higher compression, resulting in less storage space being required
- Splittable files (files can be read in parts)

Let's focus on columnar storage formats as they are widely used in big data applications because of how they store data and can be queried by the SQL engine. The columnar format is very useful when a subset of data needs to be referred to. However, when most of the columns in a dataset need to be fetched, then row-oriented storage formats are beneficial.

The following are some columnar file formats:

- **RC files**: This stands for **record columnar files**. They provide many advantages over non-columnar files, such as fast data loading, quick query processing, and highly efficient storage space utilization. RC files are a good option for querying data, but writing them requires more memory and computation. Also, they don't support schema evolution.
- **ORC files**: This stands for **optimized row columnar files**. They have almost the same advantages and disadvantages as RC files. However, ORC files have better compression. They were designed for Hive and cannot be used with non-Hive MapReduce interfaces such as Pig, Java, or Impala.
- **Parquet files**: Parquet is a columnar data format that is suitable for large-scale queries. Parquet is just as good as RC and ORC in terms of performance while reading data, but it is slower when writing compared to other columnar file formats. Parquet supports schema evolution, which is not supported in RC and ORC file formats. Parquet also supports column pruning and predicate pushdown, which are not supported in CSV or JSON.

Now, let's look at partition pruning and predicate pushdown:

- **Partition pruning**: When you are dealing with terabytes of data, it is very difficult to retrieve the required data in a performant way. In this case, if files support partition pruning, then data can be retrieved faster. Partition pruning is a performance optimization technique that restricts the number of files and partitions that Spark can read while querying data. When partitioning is done, data is stored according to the partitioning scheme that's been segregated in the hierarchical folder structure and when data is queried, only a particular partition where data is available will be searched.
- **Predicate pushdown**: This is a condition in Spark queries that's used to filter the data that's restricting the number of records being returned from databases, thus improving the query's performance. While writing Spark queries, you need to ensure that the partition key columns are included in the filter condition of the query. Using predicate pushdown lets you skip over huge portions of the data while you're scanning and processing.

In this recipe, you will learn about and compare the different storage spaces that are required while saving the data in different file formats.

We are using `06-file-formats` notebook.

Let's learn how to load data from a data file into a dataframe and then write that dataframe in different file formats:

- Load the customer data into your dataframe and sort the customer data on the **C_CUSTKEY** column.

- Write the sorted and unsorted dataframes in different file formats, such as Parquet and JSON.

- Compare the storage space that was taken up by each file. You will observe that the sorted data is the smallest, followed by unsorted and then JSON.

**How it works...**

Parquet supports all the features that are provided by the RC and ORC file formats. It stores data in binary files with metadata. Using this metadata information, Spark can easily determine data types, column names, and compression by parsing the data files. Because of these features, it is widely used in big data applications.

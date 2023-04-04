# PySpark

## Install

To get started with PySpark, you will need to have the Spark software installed on your machine. You can download the latest version of Spark from the Apache Spark website. Once you have Spark installed, you can start using it to process data.

One of the most common ways to use Spark is through the PySpark library, which allows you to use Python to interact with Spark. The following code snippet shows how to create a SparkSession and read it in a CSV file:

```py
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()

# Read in a CSV file
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)# Create a SparkSession
spark = SparkSession.builder.appName("MyApp").getOrCreate()
```

In this example, we are creating a SparkSession and setting the appName to “MyApp”. We then use the read.csv() function to read in a CSV file and store it in a DataFrame. The header and inferSchema options are set to True, which tells Spark to use the first row of the CSV file as the header and to infer the schema of the data.

## Creating a DataFrame in PySpark

The DataFrames are a fundamental data structure in PySpark, and they provide a powerful and flexible way to work with structured and semi-structured data. A DataFrame is a distributed collection of data organized into named columns. It is similar to a table in a relational database or a data frame in R/Python. DataFrames are built on top of RDDs and provide a higher-level abstraction for data processing. They also support a more powerful query optimizer, known as the Catalyst Optimizer, which can greatly improve the performance of Spark queries.

DataFrames can be created from a variety of data sources, including structured data files, Hive tables, external databases, and streaming data sources. The following code snippet shows how to create a DataFrame from a CSV file:

```py
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
```

Once a DataFrame has been created, it can be transformed and processed using the same functions as an RDD, as well as additional functions specific to DataFrames.

## Methods, Operations and Functions

PySpark provides a variety of methods to work with data, some of the most commonly used are:

- `.show()`: Displays the first 20 rows of a DataFrame
- `.count()`: Counts the number of rows in a DataFrame
- `.describe()`: Computes basic statistics of a DataFrame
- `.head()`: Returns the first n rows of a DataFrame
- `.select()`: Selects specific columns from a DataFrame
- `.filter()`: Filters the rows of a DataFrame based on a condition
- `.groupBy()`: Groups the rows of a DataFrame by a specific column
- `.orderBy()`: Sorts the rows of a DataFrame by one or more columns

PySpark also provides a variety of operations for transforming and processing data, such as:

- `.map()`: Applies a function to each element of an RDD or DataFrame
- `.reduce()`: Combines the elements of an RDD or DataFrame using a specified function
- `.flatMap()`: Applies a function to each element of an RDD or DataFrame, and flattens the results
- `.filter()`: Filters the elements of an RDD or DataFrame based on a condition
- `.distinct()`: Returns a new RDD or DataFrame with distinct elements
- `.union()`: Returns a new RDD or DataFrame with elements from both the source RDD or DataFrame and another RDD or DataFrame

PySpark provides a variety of built-in functions for data manipulation, such as:

- `count()`: Counts the number of rows in a DataFrame
- `sum()`: Sums the values of a specific column
- `avg()`: Computes the average of the values of a specific column
- `min()`: Returns the minimum value of a specific column
- `max()`: Returns the maximum value of a specific column
- `concat()`: Concatenates two or more columns into a single column
- `split()`: Splits a string column into multiple columns
- `substring()`: Returns a substring of a string column

These functions can be used in combination with the PySpark SQL module to perform a variety of data manipulation tasks.

Here is an example of how to use the sum() function to compute the sum of a specific column in a DataFrame:

```py
from pyspark.sql.functions import sum

# Compute the sum of the "value" column
df.select(sum("value")).show()
```

Once you have read your data, you can use Spark to perform various data processing tasks. The following code snippet shows how to perform a simple groupby operation on the data:

```py
from pyspark.sql.functions import count

# Group the data by the "category" column and count the number of occurrences
grouped_data = df.groupBy("category").agg(count("*").alias("count"))
```

In this example, we are using the groupBy() function to group the data by the “category” column and the agg() function to count the number of occurrences in each group. We then store the result in a new DataFrame called grouped_data.

## Partitioning

A partition in spark is a logical chunk of data mapped to a single node in a cluster. Partitions are basic units of parallelism. Each partition is processed by a single task slot. In a multicore system, total slots for tasks will be `num of executors x number of cores`. Hence the number of partitions decides the task parallelism.

Problem due to inadequate/misconfigured partitions:

- **Too many partitions —** slower data reads
- **Too many small partitions —** waste of resource
- **Overly large partitions** can even cause executor “out of memory” errors.
- **A small number of large partitions** may leave some worker cores idle.
- **Few partitions:** long computation and write times. Also, it can cause skewed data and inefficient resource use. Skewed partition may lead to slow stage/tasks, data spilling to disk, and OOM errors.

In Spark, the number of partitions comes into the picture at three stages of the pipeline:

![partitioning](https://user-images.githubusercontent.com/62965911/223931567-7bc4652d-09a3-430a-9677-e96ec541c069.png)

### Input

The first place where we can decide the number of partitions that get created while we read data from files, DBs, or any other source. We can mention the size of each partition and based on the amount of data that is being read spark will create as many partitions.

For reading files from Parquet, JSON, and ORC we can set the bytes for each partition.

* spark.default.parallelism — how many partitions are read in when doing `spark.read`
* spark.sql.files.maxPartitionBytes — The maximum number of bytes to put into a single partition when reading files
* spark.sql.files.minPartitionNum — minimum number of split file partition
* spark.files.openCostInBytes — estimated cost to open a file

While reading from databases we can ser (`partitionColumn`, `lowerBound`, `upperBound`, `numPartitions` ). These values will divide the data (between lower & upper bound) into partitions (a number equal to numPartitions). So let us say we have an Id column and we set `lowerBound` to 1 and `upperBound` to 40000 with `numPartitions` to 4. Then in the case of equal distribution spark will have 4 partitions with 10000 records each.

NOTE

> While reading from folders containing large number of files, enumeration of datasets is a challenge as it happens on driver. This processing of file listing follows a serial code path and can be slow. There are third party solutions, like RapidFile, to speed up file listing.

### Shuffle

When we perform a wide transformation (group by, join, window function) there is a shuffle of data. During this shuffle, new partitions get created or removed.

The smaller size of partitions (more partitions) will increase the parallel running jobs, which can improve performance, but too small of a partition will cause overhead and increase the GC time. Larger partitions (fewer number of partitions) will decrease the number of jobs running in parallel.

* **spark.sql.shuffle.partitions** — Default number of partitions returned by transformations like `join`, `reduceByKey`, and `parallelize` when not set by user. Default is **200**.

We can manually tweak the number of partitions by coalescing or repartitioning.

* repartition(numPartitions) — Uses RoundRobinPartitioning
* repartition(partitionExprs) — Uses HashPartitioner
* repartitionByRange(partitionExprs) — Uses range partitioning
* coalesce(numPartitions) — Use only to reduce the number of partitions

NOTE

> In most cases, Coalesce should be preferred over repartition while reducing the number of partitions. But Repartition guarantees that the data distribution in the partition is roughly the same size. So in some cases, it may be preferred.

In case where are performing aggregate on unique columns we should control the shuffle by using repartition. Good partitioning of data leads to better speed and fewer OOMs errors. The _repartition_ leads to a full shuffle of data between the executors making the job slower. The _coalesce_ operation doesn’t trigger a full shuffle when it reduces the number of partitions. It only transfers the data from partitions being removed to existing partitions.

We can get partitions and there record count for each one using the following code:

```python
from pyspark.sql.functions import spark\_partition\_id, asc, desc

df.withColumn("partitionId", spark\_partition\_id())\\
    .groupBy("partitionId")\\
    .count()\\
    .orderBy(asc("count"))\\
    .show()
```

With AQE we can dynamically split & coalesce the partitions to have equal-sized partitions.

- spark.sql.adaptive.skewJoin.skewedPartitionFactor
- spark.sql.adaptive.skewJoin.skewedPartitionThresholdInByte
- spark.sql.adaptive.coalescePartitions.enabled
- spark.sql.adaptive.coalescePartitions.minPartitionSize
- spark.sql.adaptive.advisoryPartitionSizeInBytes
- spark.sql.adaptive.coalescePartitions.initialPartitionNum
- spark.sql.shuffle.partitions

### Output

The number of files that get written out is controlled by the parallelization of your DataFrame or RDD. So if your data is split across 10 Spark partitions you cannot write fewer than 10 files without reducing partitioning (e.g. `coalesce` or `repartition`).

* **partitionBy()** — Partitions the output by the given columns on the file system
* **maxRecordsPerFile** — number of records in a single file in each partition. This helps in fixing large file problem

When we write data, using the `maxRecordsPerFile` option, we can limit the number of records that get written per file in each partition.

To get one file per partition, use `repartition()` with the same columns you want the output to be partitioned by. The `partitionBy` method does not trigger any shuffle but it may generate a two many files. Imagine we have 200 partitions, and we want to partition data by date. Each spark task will produce 365 files in which leads to 365×200=73k files.

```python
partition_cols = []
df.repartition(*partition_cols)\
  .write.partitionBy(*partition_cols)\
  .mode(SaveMode.Append).parquet(path)
```

Spark also gives us the option of bucketing while writing data to tables. In bucketing data is divided into smaller portions called “buckets”.

```python
df.write.bucketBy(12, "key").saveAsTable("table\_name")
```

*No of files in bucketing = df.partition * number of bucket*

Also, To use bucket join for tables having buckets multiple of each other we need to set the following:

* _spark.sql.bucketing.coalesceBucketsInJoin.enabled_

> 🔬 Lab: [Calculating Spark Partitions](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/01-foundations/language/spark/lab-calculating-partitions.ipynb)

## Lazy Processing

PySpark uses a concept called lazy processing, which means that operations on DataFrames and RDDs are not executed immediately, but rather are recorded in a lineage. The actual execution of the operations is delayed until an action is called. This allows Spark to optimize the execution plan by analyzing the entire lineage of operations, rather than executing each operation individually.

This can significantly improve the performance of Spark jobs by reducing the amount of data that needs to be read and processed.

Here is an example of how lazy processing works in PySpark:

```py
# Define a DataFrame
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Define a transformation on the DataFrame
df = df.filter(df["age"] > 30)

# The transformation is not executed yet

# Perform an action on the DataFrame
df.count()

# The transformation is executed and the DataFrame is filtered
```

In this example, the filter operation on the DataFrame is not executed until the count() action is called. This allows Spark to optimize the execution plan by analyzing the entire lineage of operations before executing them.

## Using Filter and Where on DataFrame

The `where()` and `filter()` methods are used to select rows from a DataFrame based on one or more conditions. Both methods are used to filter data based on a specified condition, and they are often used interchangeably.

The `where()` method is a synonym for the `filter()` method, and they have the same syntax.

## Different Types of Joins in PySpark

There are several types of joins in PySpark, including inner join, outer join, left join, right join, and cross join.

The most commonly used join in PySpark is the inner join, which returns only the rows that have matching keys in both DataFrames.

## Using Union and Union All on DataFrames

In PySpark, `union()` and `unionAll()` are methods used to combine two or more DataFrames vertically, i.e., they stack rows from one DataFrame on top of another.

The main difference between the two methods is that `union()` removes duplicate rows, while `unionAll()` retains all rows.

## Working with Columns Using withColumn

In PySpark, `withColumn()` is a method used to add a new column to a DataFrame or replace an existing column with a modified version.

The method takes two parameters: the name of the new column, and an expression that defines the values for the new column.

## Where to Use withColumnRenamed

In PySpark, `withColumnRenamed()` is a method used to rename a column in a DataFrame.

The method takes two parameters: the current name of the column, and the new name of the column.

## Aggregation and Filtering Using groupBy

In PySpark, `groupBy()` is a method used to group rows of a DataFrame based on one or more columns, and apply aggregation functions on each group.

This method is useful for summarizing and analyzing data based on certain criteria.

## How to Clean your Data Using drop

In PySpark, `drop()` is a method used to remove one or more columns from a DataFrame.

The method takes one or more column names as parameters and returns a new DataFrame with the specified columns removed.

## How to Pivot in PySpark

In PySpark, `pivot()` is a method used to transform a DataFrame from a long format to a wide format, by rotating values from a column into separate columns.

This method is useful for summarizing and analyzing data in a different format.

## Eliminate Duplicate Data with distinct

In PySpark, `distinct()` is a method used to return a DataFrame with distinct rows based on all columns or a subset of columns.

## How to Use map and mapPartitions

In PySpark, `map()` and `mapPartitions()` are methods used to transform the data in an RDD (Resilient Distributed Dataset).

The `map()` method applies a function to each element of an RDD and returns a new RDD with the transformed elements.

The `mapPartitions()` method applies a function to each partition of an RDD and returns a new RDD with the transformed partitions. This method is more efficient than `map()` when the function you're applying to each element of the RDD requires some setup or teardown work.

## What are foreach and foreachPartition

In PySpark, `foreach()` and `foreachPartition()` are methods used to perform actions on each element of an RDD.

The `foreach()` method applies a function to each element of an RDD, without returning any result. It is typically used for side effects, such as writing the elements to a file or a database.

The `foreachPartition()` method applies a function to each partition of an RDD, instead of each element. This method is useful when you need to perform some expensive initialization or teardown work for each partition, such as establishing a database connection or opening a file.

## Understanding Data Structures Using StructType and StructField

In PySpark, `StructType` and `StructField` are classes used to define the schema of a DataFrame.

`StructType` is a class that represents a schema, which is a collection of `StructField` objects. A schema defines the structure of a DataFrame, including the names, data types, and nullable flags of its columns.

## What are UDFs in PySpark

In PySpark, `UDF` stands for User-Defined Function, which is a feature that allows users to define their own functions and apply them to Spark data frames or RDDs.

UDFs are useful when you need to apply a custom transformation to your data that is not available in Spark’s built-in functions. For example, you might want to apply a complex calculation or perform a text processing task that is not covered by Spark’s standard library.

## Collect vs Select in PySpark Best Practices

In PySpark, `collect()` and `select()` are methods used to extract data from a DataFrame or RDD.

`collect()` is a method that returns all the data from a DataFrame or RDD as a list in the driver program. This method should be used with caution because it can potentially cause the driver program to run out of memory if the data is too large.

`select()` is a method that returns a new DataFrame with only the specified columns. This method is used to filter the data and reduce the amount of data that needs to be processed.

## Caching

Caching is the process of storing the results of an operation in memory so that they can be reused later. This can significantly improve the performance of Spark jobs by reducing the amount of data that needs to be read and processed.

PySpark provides the `.persist()` and `.cache()` methods to cache DataFrames and RDDs in memory. The difference between the two methods is that `.persist()` allows for specifying the storage level, such as MEMORY_ONLY, MEMORY_AND_DISK, etc.

Here is an example of how to cache a DataFrame in memory:

```py
# Cache a DataFrame in memory
df.persist(StorageLevel.MEMORY_ONLY)
```

It is important to note that caching can consume a large amount of memory and should be used with care. It’s also important to check the storage level Spark is using and remove the cache if you run out of memory.

## Broadcasting

Broadcasting is the process of sending a read-only variable to the worker nodes, rather than sending a copy of the variable to each worker node. This can greatly improve the performance of Spark jobs by reducing the amount of data that needs to be sent over the network.

Spark provides the `broadcast()` method to broadcast a variable to the worker nodes. The broadcast variable can then be used in operations such as `join()` and `map()`.

Here is an example of how to use broadcasting in Spark:

```py
# Create a broadcast variable
broadcast_var = spark.sparkContext.broadcast([1, 2, 3])

# Use the broadcast variable in a map operation
rdd.map(lambda x: x + broadcast_var.value)
```

In this example, the broadcast variable is created using the spark.sparkContext.broadcast() method and passed as a second argument in the join operation. Spark will use this broadcast variable to join the two DataFrames on the "id" column, which can be more efficient than sending a copy of the second DataFrame to each worker node.

## Execution Planning

Spark uses a query optimizer known as Catalyst to optimize the execution plan of Spark jobs. The execution plan is a representation of the physical execution of a query and it can be used to understand how Spark is processing data.

The `explain()` the method can be used to view the execution plan of a query. The `explain()` method can be used on DataFrames and RDDs to view the physical execution plan of a query.

Here is an example of how to view the execution plan of a query:

```py
# View the execution plan of a query
df.filter(df["age"] > 30).explain()
```

In this example, the `explain()` the method is used to view the physical execution plan of a query that filters the DataFrame to include only rows where the "age" column is greater than 30. The output of the `explain()` the method will show the physical execution plan of the query, which can be used to understand how Spark is processing data.

We can express the same query using any interface. The Spark SQL engine generates the same query plan used to optimize and execute on our Spark cluster.

![query execution engine](https://user-images.githubusercontent.com/62965911/214256593-38afbb18-1bc3-405d-916f-9981edb57522.png)

Broadcasting in Spark can greatly improve the performance of Spark jobs by reducing the amount of data that needs to be sent over the network. Understanding the execution plan in Spark can also be helpful to understand how Spark is processing data and to optimize the performance of Spark jobs.

Whenever we execute transformations, Spark prepares a plan, and as soon as an action is called, it performs those transformations. Now, it's time to expand that knowledge. Let's dive deeper into Spark's query execution mechanism.

Every time a query is executed by Spark, it is done with the help of the following four plans:

- **Parsed Logical Plan**: Spark prepares a *Parsed Logical Plan*, where it checks the metadata (table name, column names, and more) to confirm whether the respective entities exist or not.
- **Analyzed Logical Plan**: Spark accepts the Parsed Logical Plan and converts it into what is called the *Analyzed Logical Plan*. This is then sent to Spark's catalyst optimizer, which is an advanced query optimizer for Spark.
- **Optimized Logical Plan**: The catalyst optimizer applies further optimizations and comes up with the final logical plan, called the *Optimized Logical Plan*.
- **Physical Plan**: The *Physical Plan* specifies how the Optimized Logical Plan is going to be executed on the cluster.

Apart from the catalyst optimizer, there is another framework in Spark called the **cost-based optimizer** (**CBO**). The CBO collects statistics on data, such as the number of distinct values, row counts, null values, and more, to help Spark come up with a better Physical Plan. AQE is another optimization technique that speeds up query execution based on runtime statistics. It does this with the help of the following three features:

- **Dynamically coalescing shuffle partitions**
- **Dynamically switching join strategies**
- **Dynamically optimizing skew joins**

To write efficient Spark applications, we need to have some understanding of how Spark executes queries. Having a good understanding of how Spark executes a given query helps big data developers/engineers work efficiently with large volumes of data.

Query execution is a very broad subject, and, in this section, we will understand jobs, stages, and tasks. We will also learn how Spark lazy evaluation works, how to check and understand the execution plan when working with DataFrames or SparkSQL, how joins work in Spark and the different types of join algorithms Spark uses while joining two tables. We will also learn about the input, output, and shuffle partitions and the storage benefits of using different file formats.

Knowing about the internals will help you troubleshoot and debug your Spark applications more efficiently. By the end of this section, you will know how to execute Spark queries, as well as how to write and debug your Spark applications more efficiently.

### Tuning shuffle partitions

Spark uses a technique called **shuffle** to move data between its executors or nodes while performing operations such as **join**, **union**, **groupby**, and **reduceby**. The shuffle operation is very expensive as it involves the movement of data between nodes. Hence, it is usually preferable to reduce the amount of shuffle involved in a Spark query. The number of partition splits that Spark performs while shuffling data is determined by the following configuration:

```python
spark.conf.set("spark.sql.shuffle.partitions",200)
```

**200** is the default value and you can tune it to a number that suits your query the best. If you have too much data and too few partitions, this might result in longer tasks. But, on the other hand, if you have too little data and too many shuffle partitions, the overhead of shuffle tasks will degrade performance. So, you will have to run your query multiple times with different shuffle partition numbers to arrive at an optimum number.

You can learn more about Spark performance tuning and shuffle partitions here: [https://spark.apache.org/docs/latest/sql-performance-tuning.html](https://spark.apache.org/docs/latest/sql-performance-tuning.html).

### Identifying shuffles in a Spark query plan

Similar to SQL, we can use the **EXPLAIN** command to print the plans in Spark. Here is a simple example to generate two sets of numbers, partition them, and then join them. This will cause lot of data movement:

```python
val jump2Numbers = spark.range(0, 100000,2)
val jump5Numbers = spark.range(0, 200000, 5)
val ds1 = jump2Numbers.repartition(3)
val ds2 = jump5Numbers.repartition(5)
val joined = ds1.join(ds2)
joined.explain
```

The **joined.explain** request will print a plan similar to the sample shown as follows:

```
== Physical Plan ==
BroadcastNestedLoopJoin BuildRight, Inner
:- **Exchange** RoundRobinPartitioning(3), [id=#216]
:  +- *(1) Range (0, 100000, step=2, splits=4)
+- BroadcastExchange IdentityBroadcastMode, [id=#219]
   +- **Exchange** RoundRobinPartitioning(5), [id=#218]
      +- *(2) Range (0, 200000, step=5, splits=4)
```

Just search for the **Exchange** keyword to identify the shuffle stages.

Alternatively, you can identify the shuffle stage from the Spark DAG. In the DAG, look for sections named **Exchange**. These are the shuffle sections. Here is an example Spark DAG containing two **Exchange** stages:

![B17525_14_013](https://user-images.githubusercontent.com/62965911/218312617-1624668d-96d7-449d-87ea-60edf79edf2d.jpeg)

If there are very expensive shuffle sections, consider enabling the statistics and checking whether the engine generates a better plan. If not, you will have to rewrite the query to reduce the shuffles as much as possible.

## Partition pruning and Predicate pushdown

- **Partition pruning**: When you are dealing with terabytes of data, it is very difficult to retrieve the required data in a performant way. In this case, if files support partition pruning, then data can be retrieved faster. Partition pruning is a performance optimization technique that restricts the number of files and partitions that Spark can read while querying data. When partitioning is done, data is stored according to the partitioning scheme that's been segregated in the hierarchical folder structure and when data is queried, only a particular partition where data is available will be searched.
- **Predicate pushdown**: This is a condition in Spark queries that's used to filter the data that's restricting the number of records being returned from databases, thus improving the query's performance. While writing Spark queries, you need to ensure that the partition key columns are included in the filter condition of the query. Using predicate pushdown lets you skip over huge portions of the data while you're scanning and processing.

## Managing Memory and Disk Resources in PySpark with Cache and Persist

> An overview of PySpark's cache and persist methods and how to optimize performance and scalability in PySpark applications

In PySpark, `cache()` and `persist()` are methods used to improve the performance of Spark jobs by storing intermediate results in memory or on disk. Here's a brief description of each:

1. `cache()`: This method is used to cache the RDD (Resilient Distributed Dataset) in memory. When an RDD is cached, the data is stored in memory so that it can be quickly accessed the next time it is needed. This can greatly improve the performance of Spark jobs by reducing the amount of time spent reading data from disk.

For example, consider the following code:

```python
rdd = sc.parallelize(range(1000000))
rdd.cache()
result = rdd.reduce(lambda x, y: x + y)
```

(OR)

```python
df = spark.range(1000000)
df.cache()
df_filtered = df.filter("id % 2 == 0")
df_sum = df_filtered.selectExpr("sum(id)").collect()
```

In this code, the RDD is cached before the reduce operation. This means that the data will be stored in memory and can be quickly accessed during the reduce operation, which should improve performance.

> Note that caching a DataFrame can be especially useful if you plan to reuse it multiple times in your PySpark application. However, it's important to use caching judiciously, as it can consume a lot of memory if not used correctly. In some cases, persisting a DataFrame with a more suitable storage level (e.g. disk storage) may be a better option.

2\. `persist()`: This method is similar to `cache()`, but it allows you to specify where the RDD should be stored (in memory, on disk, or both). By default, `persist()` caches the RDD in memory, but you can use the `StorageLevel` parameter to specify a different storage level.

For example, consider the following code:

```python
rdd = sc.parallelize(range(1000000))
rdd.persist(storageLevel=StorageLevel.DISK_ONLY)
result = rdd.reduce(lambda x, y: x + y)
```

(OR)

```python
df = spark.range(1000000)
df.persist(storageLevel="DISK_ONLY")
df_filtered = df.filter("id % 2 == 0")
df_sum = df_filtered.selectExpr("sum(id)").collect()
```

In this code, the RDD is persisted on disk instead of being cached in memory. This means that the data will be stored on disk and can be accessed from there during the reduce operation, which should improve performance compared to reading the data from disk.

> Also note that, like caching, persisting a DataFrame can be useful if you plan to reuse it multiple times in your PySpark application. However, it's important to use persistence judiciously, as it can consume a lot of disk space if not used correctly.

> Note that Dataset `cache()` is an alias for `persist(StorageLevel.MEMORY_AND_DISK)`

### Advantages of using Cache and Persist in PySpark

There are several advantages to using `cache()` and `persist()` in PySpark:

1. Faster Execution: By caching or persisting an RDD or DataFrame, subsequent computations that use the same RDD or DataFrame can avoid the overhead of reading the data from a disk. This can result in much faster execution times, especially for iterative or interactive workloads.
2. Reduced Data Movement: When an RDD or DataFrame is cached or persisted, it stays on the nodes where it was computed, which can reduce data movement across the network. This can be particularly beneficial in distributed environments where network bandwidth is limited.
3. Improved Resource Utilization: Caching or persisting an RDD or DataFrame can reduce the need for recomputing the same data multiple times, which can improve the utilization of compute resources. This can be particularly useful when working with large datasets or complex computations.
4. Improved Debugging: Caching or persisting an RDD or DataFrame can help with debugging by allowing you to examine the data that is stored in memory or on a disk. This can be particularly useful when working with complex or iterative algorithms.
5. Custom Storage Levels: `persist()` allows you to specify custom storage levels for an RDD or DataFrame, which can be useful when working with different types of data or hardware configurations. For example, you might want to store some data in memory but persist other data on disk.

Overall, using `cache()` and `persist()` can help improve the performance, scalability, and usability of Spark applications. However, it's important to use these methods judiciously, as caching or persisting too much data can lead to memory issues or inefficient use of resources.

### Different Levels of Caching and Persistence in PySpark

PySpark provides different levels of caching and persistence for RDDs, which determines where the data is stored and how it is partitioned across the cluster. Here are the different storage levels that can be used with `cache()` and `persist()` methods:

1. MEMORY_ONLY: This level stores the RDD in memory as deserialized Java objects. This is the default level used by `cache()` and `persist()`. It provides fast access to the data, but if the RDD does not fit entirely in memory, it may need to be recomputed from the original data source.
2. MEMORY_ONLY_SER: This level stores the RDD or DataFrame in memory as serialized Java objects. This can reduce memory usage compared to MEMORY_ONLY, but accessing the data requires deserialization, which can be slower than using deserialized objects.
3. MEMORY_AND_DISK: This level stores the RDD or DataFrame in memory as deserialized Java objects, but if the RDD or DataFrame does not fit entirely in memory, it spills the excess data to disk. This provides better performance than recomputing the data, but accessing data from disk can be slower than accessing it from memory.
4. MEMORY_AND_DISK_SER: This level stores the RDD or DataFrame in memory as serialized Java objects, and spills excess data to disk if needed. This can be useful when memory usage is a concern, but accessing the data requires deserialization, which can be slower than using deserialized objects.
5. DISK_ONLY: This level stores the RDD or DataFrame on disk only, and not in memory. This can be useful when memory usage is a concern and the data does not fit entirely in memory, but accessing the data from disk can be slower than accessing it from memory.

In addition to these basic storage levels, PySpark also provides options for controlling how the data is partitioned and cached, such as `MEMORY_ONLY_2`, which replicates the data on two nodes for fault tolerance, or `MEMORY_ONLY_SER_10`, which serializes the data and splits it into ten partitions.

### What is uncache() and unpersist() in PySpark

In PySpark, `uncache()` and `unpersist()` are methods used to remove RDDs from memory or disk, respectively, after they have been cached or persisted using `cache()` or `persist()` methods. Here's a brief description of each:

1. `uncache()`: This method is used to remove an RDD from memory that was previously cached using the `cache()` method. Once an RDD has been uncached, its data is no longer stored in memory, and it must be recomputed from its original source if it is needed again.

For example, consider the following code:

```python
rdd = sc.parallelize(range(1000000))
rdd.cache()
result = rdd.reduce(lambda x, y: x + y)
rdd.unpersist()
```

(OR)

```python
df = spark.range(1000000)
df.cache()
df_filtered = df.filter("id % 2 == 0")
df_sum = df_filtered.selectExpr("sum(id)").collect()
df.unpersist()
```

In this code, the RDD is uncached after the reduce operation has been completed. This frees up the memory used by the RDD, which can be beneficial in cases where memory usage is a concern.

2. `unpersist()`: This method is used to remove an RDD from the disk that was previously persisted using the `persist()` method. Once an RDD has been unpersisted, its data is no longer stored on disk, and it must be recomputed from its original source if it is needed again.

For example, consider the following code:

```python
rdd = sc.parallelize(range(1000000))
rdd.persist(storageLevel=StorageLevel.DISK_ONLY)
result = rdd.reduce(lambda x, y: x + y)
rdd.unpersist()
```

(OR)

```python
df = spark.range(1000000)
df.persist(storageLevel="DISK_ONLY")
df_filtered = df.filter("id % 2 == 0")
df_sum = df_filtered.selectExpr("sum(id)").collect()
df.unpersist()
```

In this code, the RDD is unpersisted after the reduce operation has been completed. This frees up the disk space used by the RDD, which can be beneficial in cases where disk usage is a concern.

> Note that it's important to use `uncache()` and `unpersist()` methods carefully to avoid unnecessary recomputations or data movements. It's generally a good practice to remove RDDs from memory or disk when they are no longer needed, especially if the RDDs are large or memory or disk resources are limited.

In conclusion, `uncache()` and `unpersist()` methods in PySpark are used to remove RDDs from memory or disk, respectively after they have been cached or persisted using `cache()` or `persist()` methods. These methods are important to manage memory and disk resources efficiently and avoid unnecessary recomputations or data movements. When using these methods, it's important to carefully consider when an RDD is no longer needed and remove it from memory or disk accordingly. By doing so, we can optimize performance and scalability in PySpark applications.

## PySpark vs Pandas

Spark DataFrames were inspired by pandas, which also provides an abstraction on top of the data called a DataFrame. pandas is a widely adopted library for data manipulation and analytics. Many developers use it to extrapolate data using Python.

It may seem easy to confuse the two at the beginning, but there are many key differences between pandas and Spark. Most importantly, pandas was not built for scale; it was built to operate on data that fits into one machine’s memory. Consequently, it does not have the distributed Spark architecture. It also does not adhere to functional programming principles: pandas DataFrames are mutable.

|                           | Spark DataFrame | pandas DataFrame   |
|---------------------------|-----------------|--------------------|
| **Operation in parallel** | Yes             | Not out of the box |
| **Lazy evaluation**       | Yes             | No                 |
| **Immutable**             | Yes             | No                 |

Although, as you can see, there is no out-of-the-box way to operate in parallel over a pandas DataFrame, that does not mean it is entirely impossible. It simply means that you have to create a solution and consider the possible problems you might encounter (thread locks, race conditions, etc.) and their impact on the end result. Other differences are that Spark supports lazy evaluation, while in pandas, operations take place immediately as soon as the Python code line is executed, and DataFrames in pandas are not immutable. This makes it easy to operate on pandas DataFrames, as you don’t need to remember or be aware of the lazy execution approach—when you call a function, it is executed immediately and you can interact with the results right away. However, it also makes it challenging to scale using parallel or distributed computing.

## PySpark Cheat Sheet

![](https://user-images.githubusercontent.com/62965911/214256713-2433ba5e-3050-47a2-9a5c-27e5e923f034.jpg)

## Labs

1. Create databricks account
2. Create your first databricks cluster
3. Create your first databricks notebook
4. [PySpark Basics](01-foundations/language/pyspark/lab-pyspark-basics/)
5. M&M color balls analysis with PySpark
6. Movielens and Song analysis with PySpark
7. San Francisco Fire Department call analysis with PySpark
8. [Connect AWS to PySpark and build an ETL pipeline](03-processing/databricks/lab-databricks-pyspark-s3/)
9. [Spark Optimizations](01-foundations/language/pyspark/lab-spark-optimizations/)
10. [Spark Optimization II](01-foundations/language/pyspark/lab-spark-optimizations-2/)
11. [Uber Analysis](01-foundations/language/pyspark/lab-uber-analysis/)
12. [Understand Spark Query Execution](01-foundations/language/pyspark/lab-understand-spark-query-execution/)
13. [Window Functions](01-foundations/language/pyspark/lab-window-functions/)
14. [BCG Case Study](01-foundations/language/pyspark/lab-bcg/)
15. [Building extract and load pipeline with Scala, S3 and Postgres](03-processing/databricks/lab-databricks-scala-postgres-s3/)

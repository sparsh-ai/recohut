# Spark

> A unified engine for large-scale data analytics

Apache Spark is an Open source analytical processing engine for large scale powerful distributed data processing and machine learning applications. Spark is Originally developed at the University of California, Berkeley’s, and later donated to Apache Software Foundation. In February 2014, Spark became a Top-Level Apache Project and has been contributed by thousands of engineers and made Spark one of the most active open-source projects in Apache.

Spark is a distributed data processing engine meaning its components work collaboratively on a cluster of machines to run your tasks. It can be run on a single machine (standalone mode) as well for testing purposes. Spark is an open-source project that was originally developed in 2009 by Matei Zaharia as a replacement/alternative to MapReduce.

Apache Spark is a framework that is supported in Scala, Python, R Programming, and Java. Below are different implementations of Spark.

- Spark – Default interface for Scala and Java
- PySpark – Python interface for Spark
- SparklyR – R interface for Spark.

**Features:**

- In-memory computation
- Distributed processing using parallelize
- Can be used with many cluster managers (Spark, Yarn, Mesos e.t.c)
- Fault-tolerant
- Immutable
- Lazy evaluation
- Cache & persistence
- Inbuild-optimization when using DataFrames
- Supports ANSI SQL

**Advantages:**

- Spark is a general-purpose, in-memory, fault-tolerant, distributed processing engine that allows you to process data efficiently in a distributed fashion.
- Applications running on Spark are 100x faster than traditional systems.
- You will get great benefits using Spark for data ingestion pipelines.
- Using Spark we can process data from Hadoop HDFS, AWS S3, Databricks DBFS, Azure Blob Storage, and many file systems.
- Spark also is used to process real-time data using Streaming and Kafka.
- Using Spark Streaming you can also stream files from the file system and also stream from the socket.
- Spark natively has machine learning and graph libraries.

Watch this video:

Watch this video: https://www.youtube.com/watch?v=Hciruu3Gb3E

Watch this video: https://www.youtube.com/watch?v=QaoJNXW6SQo

![](https://user-images.githubusercontent.com/62965911/214256759-3ebd302e-8d9f-4f29-98ae-1841dacf9cd3.jpeg)

## When would you need Apache Spark?

It was designed for large-scale data processing ETLs, streaming pipelines, and complex data exploration activities. It can be integrated with a wide range of databases and technologies such as HDFS, JDBC, MongoDB, Kafka, and more! It supports different data formats such as Parquet (recommended), ORC, CSV.

It was designed to be developer-friendly. You can use your favorite programming language: Python, Scala, R, and you can even run SQL-like queries!

It is a unified stack that offers Speed, Ease of Use, Modularity, and Extensibility.

:::note
Data engineers use Spark because it provides a simple way to parallelize computations and hides all the complexity of distribution and fault tolerance. This leaves them free to focus on using high-level DataFrame-based APIs and domain-specific language (DSL) queries to do ETL, reading and combining data from multiple sources.

The performance improvements in Spark 2.x and Spark 3.0, due to the Catalyst optimizer for SQL and Tungsten for compact code generation, have made life for data engineers much easier. They can choose to use any of the three Spark APIs—RDDs, DataFrames, or Datasets—that suit the task at hand, and reap the benefits of Spark.
:::

## Hadoop vs Spark

Watch this video: https://www.youtube.com/watch?v=xDpvyu0w0C8

## PySpark Cheat Sheet

![](https://user-images.githubusercontent.com/62965911/214256713-2433ba5e-3050-47a2-9a5c-27e5e923f034.jpg)

## Cloud Storage instead of HDFS

Watch this video: https://www.youtube.com/watch?v=cfXJFrSJkeI

## Spark DataFrames

A DataFrame is a distributed collection of data organized into named columns. It is similar to a table in a relational database or a data frame in R/Python. DataFrames are built on top of RDDs and provide a higher-level abstraction for data processing. They also support a more powerful query optimizer, known as the Catalyst Optimizer, which can greatly improve the performance of Spark queries.

The following code snippet shows how to create a DataFrame from a CSV file:

```py
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
```

Once a DataFrame has been created, it can be transformed and processed using the same functions as an RDD, as well as additional functions specific to DataFrames.

## Getting Started with Spark

To get started with Spark, you will need to have the Spark software installed on your machine. You can download the latest version of Spark from the Apache Spark website. Once you have Spark installed, you can start using it to process data.

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

## PySpark Methods

PySpark provides a variety of methods to work with data, some of the most commonly used are:

-   `.show()`: Displays the first 20 rows of a DataFrame
-   `.count()`: Counts the number of rows in a DataFrame
-   `.describe()`: Computes basic statistics of a DataFrame
-   `.head()`: Returns the first n rows of a DataFrame
-   `.select()`: Selects specific columns from a DataFrame
-   `.filter()`: Filters the rows of a DataFrame based on a condition
-   `.groupBy()`: Groups the rows of a DataFrame by a specific column
-   `.orderBy()`: Sorts the rows of a DataFrame by one or more columns

## PySpark Operations

PySpark also provides a variety of operations for transforming and processing data, such as:

-   `.map()`: Applies a function to each element of an RDD or DataFrame
-   `.reduce()`: Combines the elements of an RDD or DataFrame using a specified function
-   `.flatMap()`: Applies a function to each element of an RDD or DataFrame, and flattens the results
-   `.filter()`: Filters the elements of an RDD or DataFrame based on a condition
-   `.distinct()`: Returns a new RDD or DataFrame with distinct elements
-   `.union()`: Returns a new RDD or DataFrame with elements from both the source RDD or DataFrame and another RDD or DataFrame

## PySpark Functions

PySpark provides a variety of built-in functions for data manipulation, such as:

-   `count()`: Counts the number of rows in a DataFrame
-   `sum()`: Sums the values of a specific column
-   `avg()`: Computes the average of the values of a specific column
-   `min()`: Returns the minimum value of a specific column
-   `max()`: Returns the maximum value of a specific column
-   `concat()`: Concatenates two or more columns into a single column
-   `split()`: Splits a string column into multiple columns
-   `substring()`: Returns a substring of a string column

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

## Partitioning in PySpark

Partitioning is the process of dividing a large dataset into smaller, more manageable chunks. In PySpark, partitioning can be performed on RDDs and DataFrames to improve the performance of certain operations.

Partitioning is performed using the `repartition()` method, which can be used to increase or decrease the number of partitions in a DataFrame or RDD.

Here is an example of how to use the `repartition()` method to increase the number of partitions in a DataFrame:

```py
# Increase the number of partitions to 100
df = df.repartition(100)
```

It’s important to note that repartitioning is a costly operation and should be used with care. It is also recommended to use the coalesce() method to decrease the number of partitions rather than the repartition() method.

In conclusion, PySpark provides a variety of functions, methods, and operations for data manipulation. Partitioning is an important aspect to consider when working with large datasets in PySpark, as it can greatly improve the performance of certain operations.

## Lazy Processing in PySpark

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

## Caching in PySpark

Caching is the process of storing the results of an operation in memory so that they can be reused later. This can significantly improve the performance of Spark jobs by reducing the amount of data that needs to be read and processed.

PySpark provides the `.persist()` and `.cache()` methods to cache DataFrames and RDDs in memory. The difference between the two methods is that `.persist()` allows for specifying the storage level, such as MEMORY_ONLY, MEMORY_AND_DISK, etc.

Here is an example of how to cache a DataFrame in memory:

```py
# Cache a DataFrame in memory
df.persist(StorageLevel.MEMORY_ONLY)
```

It is important to note that caching can consume a large amount of memory and should be used with care. It’s also important to check the storage level Spark is using and remove the cache if you run out of memory.

## Broadcasting in Spark

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

## Spark Execution Plan

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

In conclusion, Broadcasting in Spark can greatly improve the performance of Spark jobs by reducing the amount of data that needs to be sent over the network. Understanding the execution plan in Spark can also be helpful to understand how Spark is processing data and to optimize the performance of Spark jobs.

## Real-life Applications of Pyspark

1.  Data Processing and ETL: PySpark is widely used for processing and transforming large datasets, making it a popular choice for ETL (Extract, Transform, Load) operations. PySpark's ability to handle semi-structured and structured data, along with its support for a wide range of file formats, makes it a powerful tool for pre-processing.
2.  Machine Learning: PySpark's MLlib library provides a wide range of machine learning algorithms, making it a popular choice for building large-scale machine learning models. It allows for distributed processing of large datasets, which can speed up the training process for machine learning models.
3.  Streaming: PySpark's Streaming API provides a way to process data in real time, making it a popular choice for building real-time data processing pipelines. It can handle data streams from various sources such as Kafka, Flume, and Kinesis.
4.  Graph Processing: PySpark's GraphX library provides a way to process graph data, making it a popular choice for building graph-based applications such as social network analysis, recommendation systems, and fraud detection.
5.  Natural Language Processing: PySpark's MLlib library provides a way to process text data, making it a popular choice for building NLP (Natural Language Processing) applications such as text classification, sentiment analysis, and language translation.

# References

1. [Getting Started with Apache Spark](https://knowledgetree.notion.site/Getting-Started-with-Apache-Spark-2c51e0d721eb4b4ca04e309c7fb296e7)
2. [Spark Interview Questions](https://knowledgetree.notion.site/Spark-Interview-Questions-94ff173de85d4df6849b289665e8fff3)
4. [Spark Quiz & Solution [Videos]](https://knowledgetree.notion.site/Spark-Quiz-Solution-Videos-0ad90ea3035541e2af22eeaf18b738aa)
6. [Distributed Computing and the difference between Hadoop and Spark](https://knowledgetree.notion.site/Distributed-Computing-and-the-difference-between-Hadoop-and-Spark-1b741e18ddf5474da3a2b941f48dcea3)
7. [igfasouza.com/blog/what-is-apache-spark](http://www.igfasouza.com/blog/what-is-apache-spark/)
8. [2003–2023: A Brief History of Big Data](https://towardsdatascience.com/2003-2023-a-brief-history-of-big-data-25712351a6bc)
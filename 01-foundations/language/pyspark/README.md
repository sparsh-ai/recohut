# Apache Spark

Apache Spark is an open-source, multi-language, in-memory, large-scale data processing engine. It provides high-level APIs in Java, Scala, Python & R programming languages. It works on the concept of in-memory computation, making it around 100x faster than Hadoop MapReduce. It also provides tools & libraries like Spark SQL(for structured data processing), MLlib (Machine Learning), Streaming (Stream processing) & GraphX (Graph processing).

Apache Spark is an analytical processing engine for large scale powerful distributed data processing and machine learning applications. Spark is Originally developed at the University of California, Berkeley’s, and later donated to Apache Software Foundation. In February 2014, Spark became a Top-Level Apache Project and has been contributed by thousands of engineers and made Spark one of the most active open-source projects in Apache.

Spark is a distributed data processing engine meaning its components work collaboratively on a cluster of machines to run your tasks. It can be run on a single machine (standalone mode) as well for testing purposes. Spark is an open-source project that was originally developed in 2009 by Matei Zaharia as a replacement/alternative to MapReduce.

Spark is a distributed computing framework that is designed to work with large datasets. It is built on top of the Hadoop Distributed File System (HDFS) and allows for in-memory data processing, which can greatly speed up data processing tasks. Spark can be used to process data in a variety of formats, including structured data (such as CSV and Parquet) and unstructured data (such as JSON and XML).

One of the key features of Spark is its ability to perform distributed data processing. This means that Spark can split up a large dataset and process it in parallel across multiple machines. This can greatly speed up data processing tasks and allows for the processing of much larger datasets than would be possible with a single machine.

Apache Spark is a framework that is supported in Scala, Python, R Programming, and Java. Below are different implementations of Spark.

- Spark – Default interface for Scala and Java
- PySpark – Python interface for Spark
- SparklyR – R interface for Spark.

**Components of Apache Spark**

Spark consists of several components that work together to provide a comprehensive data processing ecosystem. The main components of Spark are:

- Spark Core: The foundation of Spark, provides the basic functionality for scheduling tasks and managing the execution of tasks in a cluster.
- Spark SQL: Allows for the processing of structured data using SQL-like commands.
- Spark Streaming: Allows for the processing of streaming data.
- Spark MLlib: A library for machine learning tasks.
- Spark GraphX: A library for graph processing.

**Features**

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

Watch these videos

- https://www.youtube.com/watch?v=Hciruu3Gb3E
- https://www.youtube.com/watch?v=QaoJNXW6SQo

Apache Spark supports transformations with three different **Application Programming Interfaces** (**APIs**): **Resilient Distributed Datasets** (**RDDs**), **DataFrames**, and **Datasets**. We will learn about RDDs and DataFrame transformations in this chapter. Datasets are just extensions of DataFrames, with additional features like being type-safe (where the compiler will strictly check for data types) and providing an **object-oriented** (**OO**) interface.

## Spark Architecture

Apache Spark works in a master-slave architecture where the master is called “Driver” and slaves are called “Workers”. When you run a Spark application, Spark Driver creates a context that is an entry point to your application, and all operations (transformations and actions) are executed on worker nodes, and the resources are managed by Cluster Manager.

![img](https://user-images.githubusercontent.com/62965911/214256759-3ebd302e-8d9f-4f29-98ae-1841dacf9cd3.jpeg)

## Spark Ecosystem

![1_TK3eaVzHplkaHS6rLIciTA](https://user-images.githubusercontent.com/62965911/223375021-2db8e20b-4b2c-4ea2-bfb9-744620d186e3.png)

## The Genesis of Spark

Watch this video: https://www.youtube.com/watch?v=1BGFzDj60SY

### Big Data and Distributed Computing at Google

When we think of scale, we can’t help but think of the ability of Google’s search engine to index and search the world’s data on the internet at lightning speed. The name Google is synonymous with scale. In fact, Google is a deliberate misspelling of the mathematical term googol: that’s 1 plus 100 zeros!

Neither traditional storage systems such as relational database management systems (RDBMSs) nor imperative ways of programming were able to handle the scale at which Google wanted to build and search the internet’s indexed documents. The resulting need for new approaches led to the creation of the Google File System (GFS), MapReduce (MR), and Bigtable.

While GFS provided a fault-tolerant and distributed filesystem across many commodity hardware servers in a cluster farm, Bigtable offered scalable storage of structured data across GFS. MR introduced a new parallel programming paradigm, based on functional programming, for large-scale processing of data distributed over GFS and Bigtable.

In essence, your MR applications interact with the MapReduce system that sends computation code (map and reduce functions) to where the data resides, favoring data locality and cluster rack affinity rather than bringing data to your application.

The workers in the cluster aggregate and reduce the intermediate computations and produce a final appended output from the reduce function, which is then written to a distributed storage where it is accessible to your application. This approach significantly reduces network traffic and keeps most of the input/output (I/O) local to disk rather than distributing it over the network.

Most of the work Google did was proprietary, but the ideas expressed in the aforementioned three papers spurred innovative ideas elsewhere in the open source community—especially at Yahoo!, which was dealing with similar big data challenges of scale for its search engine.

### Hadoop at Yahoo!

The computational challenges and solutions expressed in Google’s GFS paper provided a blueprint for the Hadoop File System (HDFS), including the MapReduce implementation as a framework for distributed computing. Donated to the Apache Software Foundation (ASF), a vendor-neutral non-profit organization, in April 2006, it became part of the Apache Hadoop framework of related modules: Hadoop Common, MapReduce, HDFS, and Apache Hadoop YARN.

Although Apache Hadoop had garnered widespread adoption outside Yahoo!, inspiring a large open source community of contributors and two open source–based commercial companies (Cloudera and Hortonworks, now merged), the MapReduce framework on HDFS had a few shortcomings.

First, it was hard to manage and administer, with cumbersome operational complexity. Second, its general batch-processing MapReduce API was verbose and required a lot of boilerplate setup code, with brittle fault tolerance. Third, with large batches of data jobs with many pairs of MR tasks, each pair’s intermediate computed result is written to the local disk for the subsequent stage of its operation. This repeated performance of disk I/O took its toll: large MR jobs could run for hours on end, or even days.

And finally, even though Hadoop MR was conducive to large-scale jobs for general batch processing, it fell short for combining other workloads such as machine learning, streaming, or interactive SQL-like queries.

To handle these new workloads, engineers developed bespoke systems (Apache Hive, Apache Storm, Apache Impala, Apache Giraph, Apache Drill, Apache Mahout, etc.), each with their own APIs and cluster configurations, further adding to the operational complexity of Hadoop and the steep learning curve for developers.

The question then became (bearing in mind Alan Kay’s adage, “Simple things should be simple, complex things should be possible”), was there a way to make Hadoop and MR simpler and faster?

### Spark’s Early Years at AMPLab

Researchers at UC Berkeley who had previously worked on Hadoop MapReduce took on this challenge with a project they called Spark. They acknowledged that MR was inefficient (or intractable) for interactive or iterative computing jobs and a complex framework to learn, so from the onset they embraced the idea of making Spark simpler, faster, and easier. This endeavor started in 2009 at the RAD Lab, which later became the AMPLab (and now is known as the RISELab).

Early papers published on Spark demonstrated that it was 10 to 20 times faster than Hadoop MapReduce for certain jobs. Today, it’s many orders of magnitude faster. The central thrust of the Spark project was to bring in ideas borrowed from Hadoop MapReduce, but to enhance the system: make it highly fault tolerant and embarrassingly parallel, support in-memory storage for intermediate results between iterative and interactive map and reduce computations, offer easy and composable APIs in multiple languages as a programming model, and support other workloads in a unified manner. We’ll come back to this idea of unification shortly, as it’s an important theme in Spark.

By 2013 Spark had gained widespread use, and some of its original creators and researchers—Matei Zaharia, Ali Ghodsi, Reynold Xin, Patrick Wendell, Ion Stoica, and Andy Konwinski—donated the Spark project to the ASF and formed a company called Databricks.

Databricks and the community of open source developers worked to release Apache Spark 1.0 in May 2014, under the governance of the ASF. This first major release established the momentum for frequent future releases and contributions of notable features to Apache Spark from Databricks and over 100 commercial vendors.

## When would you need Apache Spark?

It was designed for large-scale data processing ETLs, streaming pipelines, and complex data exploration activities. It can be integrated with a wide range of databases and technologies such as HDFS, JDBC, MongoDB, Kafka, and more! It supports different data formats such as Parquet (recommended), ORC, CSV.

It was designed to be developer-friendly. You can use your favorite programming language: Python, Scala, R, and you can even run SQL-like queries!

It is a unified stack that offers Speed, Ease of Use, Modularity, and Extensibility.

NOTE

> Data engineers use Spark because it provides a simple way to parallelize computations and hides all the complexity of distribution and fault tolerance. This leaves them free to focus on using high-level DataFrame-based APIs and domain-specific language (DSL) queries to do ETL, reading and combining data from multiple sources.
>
> The performance improvements in Spark 2.x and Spark 3.0, due to the Catalyst optimizer for SQL and Tungsten for compact code generation, have made life for data engineers much easier. They can choose to use any of the three Spark APIs—RDDs, DataFrames, or Datasets—that suit the task at hand, and reap the benefits of Spark.

## Hadoop

Apache Hadoop is an open source framework that is used to efficiently store and process large datasets ranging in size from gigabytes to petabytes of data. Instead of using one large computer to store and process the data, Hadoop allows clustering multiple computers to analyze massive datasets in parallel more quickly.

Hadoop consists of four main modules:

1. Hadoop Distributed File System (HDFS) – A distributed file system that runs on standard or low-end hardware. HDFS provides better data throughput than traditional file systems, in addition to high fault tolerance and native support of large datasets.
2. Yet Another Resource Negotiator (YARN) – Manages and monitors cluster nodes and resource usage. It schedules jobs and tasks.
3. MapReduce – A framework that helps programs do the parallel computation on data. The map task takes input data and converts it into a dataset that can be computed in key value pairs. The output of the map task is consumed by reduce tasks to aggregate output and provide the desired result.
4. Hadoop Common – Provides common Java libraries that can be used across all modules.

Watch this video: https://www.youtube.com/watch?v=aReuLtY0YMI

Hadoop makes it easier to use all the storage and processing capacity in cluster servers, and to execute distributed processes against huge amounts of data. Hadoop provides the building blocks on which other services and applications can be built.

Applications that collect data in various formats can place data into the Hadoop cluster by using an API operation to connect to the NameNode. The NameNode tracks the file directory structure and placement of “chunks” for each file, replicated across DataNodes. To run a job to query the data, provide a MapReduce job made up of many map and reduce tasks that run against the data in HDFS spread across the DataNodes. Map tasks run on each node against the input files supplied, and reducers run to aggregate and organize the final output.

The Hadoop ecosystem has grown significantly over the years due to its extensibility. Today, the Hadoop ecosystem includes many tools and applications to help collect, store, process, analyze, and manage big data. Some of the most popular applications are:

- Spark – An open source, distributed processing system commonly used for big data workloads. Apache Spark uses in-memory caching and optimized execution for fast performance, and it supports general batch processing, streaming analytics, machine learning, graph databases, and ad hoc queries.
- Presto – An open source, distributed SQL query engine optimized for low-latency, ad-hoc analysis of data. It supports the ANSI SQL standard, including complex queries, aggregations, joins, and window functions. Presto can process data from multiple data sources including the Hadoop Distributed File System (HDFS) and Amazon S3.
- Hive – Allows users to leverage Hadoop MapReduce using a SQL interface, enabling analytics at a massive scale, in addition to distributed and fault-tolerant data warehousing.
- HBase – An open source, non-relational, versioned database that runs on top of Amazon S3 (using EMRFS) or the Hadoop Distributed File System (HDFS). HBase is a massively scalable, distributed big data store built for random, strictly consistent, real-time access for tables with billions of rows and millions of columns.
- Zeppelin – An interactive notebook that enables interactive data exploration.

### The Hadoop ecosystem

Watch this video: https://www.youtube.com/watch?v=ohroxsisQ0w

Let's take a quick look at the simplified Hadoop components in this figure, where the starting point is the servers:

![Figure_5 1](https://user-images.githubusercontent.com/62965911/219852824-20a08079-101c-4e86-bd49-1a5a0fbade42.jpg)

Hadoop has one too many working servers or, in Hadoop terms, **worker nodes**. The worker nodes are simply computers with a filesystem where you can store files. HDFS sits on top of these multiple filesystems; when you store data in HDFS, Hadoop seamlessly distributes the files to these filesystems. You can create a table structure on top of the files using Hive, so SQL users can access the data using the SQL language. The other option is to process it using distributed processing frameworks such as Spark or MapReduce. These frameworks can read and write directly to HDFS.  

There are tools that are usually used to ingest data to HDFS, for example, Flume, Kafka, and Sqoop. The above figure is just a very simplified summary of the Hadoop ecosystem; in the marketplace, there are a lot of other alternatives for each component. If this is the first time you have learned about Hadoop, don't fall into a trap where you think you need to understand all of the products and their alternatives. Instead, focus on understanding how HDFS works and how Spark or MapReduce can process data in HDFS. The other components will come naturally with time when you understand HDFS and the processing framework.

### Map Reduce

***A quick look at how big data technologies store data***

Knowing that answering the *how* question is what is important to understanding big data, the first question we need to answer is how does it actually store the data? What makes it different from non-big data storage?

The word *big* in big data is relative. For example, say you analyze Twitter data and then download the data as JSON files with a size of 5 GB, and your laptop storage is 1 TB with 16 GB memory.

I don't think that's big data. But if the Twitter data is 5 PB, then it becomes big data because you need a special way to store it and a special way to process it. So, the key is not about whether it is social media data or not, or unstructured or not, which sometimes many people still get confused by. It's more about the size of the data relative to your system.

Big data technology needs to be able to distribute the data in multiple servers. The common terminology for multiple servers working together is a cluster. I'll give an illustration to show you how a very large file can be distributed into multiple chunks of file parts on multiple machines:

![B16851_01_10](https://user-images.githubusercontent.com/62965911/219039802-98a7e299-d0cc-49d0-bd49-878490df57cc.jpeg)

*Figure - Distributed filesystem*

In a distributed filesystem, a large file will be split into multiple small parts. In the preceding example, it is split into nine parts, and each file is a small 128 MB file. Then, the multiple file parts are distributed into three machines randomly. On top of the file parts, there will be metadata to store information about how the file parts formed the original file, for example, a large file is a combination of file part 1 located in machine 1, file part 2 located in machine 2, and more.

The distributed parts can be stored in any format that isn't necessarily a file format; for example, it can be in the form of data blocks, byte arrays in memory, or some other data format. But for simplicity, what you need to be aware of is that in a big data system, data can be stored in multiple machines and in order to optimize performance, sometimes you need to think about how you want to distribute the parts. 

After we know data can be split into small parts on different machines, it leads to further questions:

- How do I process the files?
- What if I want to aggregate some numbers from the files?
- How does each part know the records value from other parts while it is stored in different machines?

There are many approaches to answer these three questions. But one of the most famous concepts is MapReduce. 

***A quick look at how to process multiple files using MapReduce***

Historically speaking, **MapReduce** is a framework that was published as a white paper by Google and is widely used in the Hadoop ecosystem. There is an actual open source project called MapReduce mainly written in Java that still has a large user base, but slowly people have started to change to other distributed processing engine alternatives, such as **Spark**, **Tez**, and **Dataflow**. But MapReduce as a concept itself is still relevant regardless of the technology. 

In a short summary, the word MapReduce can refer to two definitions: 

- MapReduce as a technology
- MapReduce as a concept

What is important for us to understand is MapReduce as a concept. MapReduce is a combination of two words: map and reduce. 

Let's take a look at an example, if you have a file that's divided into two file parts:

![B16851_01_11](https://user-images.githubusercontent.com/62965911/219039818-28f03250-b0e9-410d-ba13-f7786f45fc23.jpeg)

*Figure - File parts*

Each of the parts contains one or more words, which in this example are fruit. The file parts are stored on different machines. So, each machine will have these three file parts:

- File **Part 1** contains two words: **Banana** and **Apple**.
- File **Part 2** contains three words: **Melon**, **Apple**, and **Banana**.
- File **Part 3** contains one word: **Apple**.

How can you write a program to calculate a word count that produces these results?

- **Apple** = 3 
- **Banana** = 2
- **Melon** = 1

Since the file parts are separated in different machines, we cannot just count the words directly. We need MapReduce. Let's take a look at the following diagram, where file parts are *mapped*, *shuffled*, and lastly *reduced* to get the final result:

![B16851_01_12](https://user-images.githubusercontent.com/62965911/219039824-8c15e566-84a1-4c88-98dd-3607a5c07f46.jpeg)

*Figure - MapReduce step diagram*

There are four main steps in the diagram:

1. **Map**: Add to each individual record a static value of 1. This will transform the word into a key-value pair when the value is always 1.
2. **Shuffle**: At this point, we need to move the fruit words between machines. We want to group each word and store it in the same machine for each group.
3. **Reduce**: Because each fruit group is already in the same machine, we can count them together. The **Reduce** step will sum up the static value 1 to produce the count results.
4. **Result**: Store the final results back in the single machine. 

The key idea here is to process any possible process in a distributed manner. Looking back at the diagram, you can imagine each box on each step is a different machine. 

Each step, **Map**, **Shuffle**, and **Reduce**, always maintains three parallel boxes. What does this mean? It means that the processes happened in parallel on three machines. This paradigm is different from calculating all processes in a single machine. For example, we can simply download all the file parts into a pandas DataFrame in Python and do a count using the pandas DataFrame. In this case, the process will happen in one machine.

MapReduce is a complex concept. The concept is explained in a 13-page-long document by Google. You can find the document easily on the public internet. In this book, I haven't added much deeper explanation about MapReduce. In most cases, you don't need to really think about it; for example, if you use BigQuery to process 1 PB of data, you will only need to run a SQL query and BigQuery will process it in a distributed manner in the background.

As a matter of fact, all technologies in cloud that we generally use are highly scalable and without question able to handle big data out of the box. But understanding the underlying concepts helps you as a data engineer in many ways, for example, choosing the right technologies, designing data pipeline architecture, troubleshooting, and improving performance.

### Apache Hadoop on Amazon EMR

> Amazon EMR is a managed service that lets you process and analyze large datasets using the latest versions of big data processing frameworks such as Apache Hadoop, Spark, HBase, and Presto on fully customizable clusters.

Elastic MapReduce, or EMR, is Amazon Web Services’ solution for managing prepackaged Hadoop clusters and running jobs on them. You can work with regular MapReduce jobs or Apache Spark jobs, and can use Apache Hive, Apache Pig, Apache HBase, and some third-party applications. Scripting hooks enable the installation of additional services. Data is typically stored in Amazon S3 or Amazon DynamoDB.

The normal mode of operation for EMR is to define the parameters for a cluster, such as its size, location, Hadoop version, and variety of services, point to where data should be read from and written to, and define steps to execute such as MapReduce or Spark jobs. EMR launches a cluster, performs the steps to generate the output data, and then tears the cluster down. However, you can leave clusters running for further use, and even resize them for greater capacity or a smaller footprint.

EMR provides an API so that you can automate the launching and management of Hadoop clusters.

Follow [this](https://aws.amazon.com/emr/features/hadoop/) blog for more information.

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

## Spark Methods

PySpark provides a variety of methods to work with data, some of the most commonly used are:

- `.show()`: Displays the first 20 rows of a DataFrame
- `.count()`: Counts the number of rows in a DataFrame
- `.describe()`: Computes basic statistics of a DataFrame
- `.head()`: Returns the first n rows of a DataFrame
- `.select()`: Selects specific columns from a DataFrame
- `.filter()`: Filters the rows of a DataFrame based on a condition
- `.groupBy()`: Groups the rows of a DataFrame by a specific column
- `.orderBy()`: Sorts the rows of a DataFrame by one or more columns

## Spark Operations

PySpark also provides a variety of operations for transforming and processing data, such as:

- `.map()`: Applies a function to each element of an RDD or DataFrame
- `.reduce()`: Combines the elements of an RDD or DataFrame using a specified function
- `.flatMap()`: Applies a function to each element of an RDD or DataFrame, and flattens the results
- `.filter()`: Filters the elements of an RDD or DataFrame based on a condition
- `.distinct()`: Returns a new RDD or DataFrame with distinct elements
- `.union()`: Returns a new RDD or DataFrame with elements from both the source RDD or DataFrame and another RDD or DataFrame

## Spark Functions

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

Partitioning is the process of dividing a large dataset into smaller, more manageable chunks. In PySpark, partitioning can be performed on RDDs and DataFrames to improve the performance of certain operations.

Partitioning is performed using the `repartition()` method, which can be used to increase or decrease the number of partitions in a DataFrame or RDD.

Here is an example of how to use the `repartition()` method to increase the number of partitions in a DataFrame:

```py
# Increase the number of partitions to 100
df = df.repartition(100)
```

It’s important to note that repartitioning is a costly operation and should be used with care. It is also recommended to use the coalesce() method to decrease the number of partitions rather than the repartition() method.

In conclusion, PySpark provides a variety of functions, methods, and operations for data manipulation. Partitioning is an important aspect to consider when working with large datasets in PySpark, as it can greatly improve the performance of certain operations.

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

### Interpreting a Spark DAG

A DAG is just a regular graph with nodes and edges but with no cycles or loops. In order to understand a Spark DAG, we first have to understand where a DAG comes into the picture during the execution of a Spark job.

When a user submits a Spark job, the Spark driver first identifies all the tasks involved in accomplishing the job. It then figures out which of these tasks can be run in parallel and which tasks depend on other tasks. Based on this information, it converts the Spark job into a graph of tasks. The nodes at the same level indicate jobs that can be run in parallel, and the nodes at different levels indicate tasks that need to be run after the previous nodes. This graph is acyclic, as denoted by *A* in DAG. This DAG is then converted into a physical execution plan. In the physical execution plan, nodes that are at the same level are segregated into stages. Once all the tasks and stages are complete, the Spark job is termed as completed.

Let's look at what a DAG looks like. You can access a Spark DAG from the Spark UI. Just click on any of the job links and then click on the **DAG Visualization** link.

Here is a DAG for a simple word count problem:

![B17525_13_024](https://user-images.githubusercontent.com/62965911/218313245-4835191c-3363-48ec-a246-97b85b434a52.jpg)

In the first stage, we see that the word count has three steps and a reduce step in the next stage. Ignore the stage numbers, as Spark assigns consecutive numbers for all jobs that are run in that Spark session. So, if you have run any other job before this job, the number gets sequentially incremented. Here is some further information about each task:

- The **textFile** task corresponds to the reading of the file from the storage.
- The **flatMap** task corresponds to the splitting of the words.
- The **map** task corresponds to the formation of (**word**, **1**) pairs.
- The **reduceByKey** task corresponds to the aggregation of all the (word, 1) pairs together to get the sum of each distinct word.

You can get more details about each step by clicking on the **Stage** boxes. Here is an example of a detailed view of **Stage 12** from the previous screenshot:

![B17525_13_025](https://user-images.githubusercontent.com/62965911/218313250-cb765fa4-f16f-4cbe-aaf1-16233287c00c.jpg)

The main advantage of learning to read Spark DAGs is that they help you identify bottlenecks in your Spark queries. You can identify how much data movement is happening between stages (also known as **data shuffle**), if there are too many sequential stages, if there are slow stages in the critical path, and so on.

You can learn more about Spark DAGs here: [https://spark.apache.org/docs/3.0.0/web-ui.html](https://spark.apache.org/docs/3.0.0/web-ui.html).

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

## Real-life Applications of Pyspark

1. Data Processing and ETL: PySpark is widely used for processing and transforming large datasets, making it a popular choice for ETL (Extract, Transform, Load) operations. PySpark's ability to handle semi-structured and structured data, along with its support for a wide range of file formats, makes it a powerful tool for pre-processing.
2. Machine Learning: PySpark's MLlib library provides a wide range of machine learning algorithms, making it a popular choice for building large-scale machine learning models. It allows for distributed processing of large datasets, which can speed up the training process for machine learning models.
3. Streaming: PySpark's Streaming API provides a way to process data in real time, making it a popular choice for building real-time data processing pipelines. It can handle data streams from various sources such as Kafka, Flume, and Kinesis.
4. Graph Processing: PySpark's GraphX library provides a way to process graph data, making it a popular choice for building graph-based applications such as social network analysis, recommendation systems, and fraud detection.
5. Natural Language Processing: PySpark's MLlib library provides a way to process text data, making it a popular choice for building NLP (Natural Language Processing) applications such as text classification, sentiment analysis, and language translation.

## RDD

An RDD (Resilient Distributed Dataset) is the primary data structure in Spark. It is a distributed collection of data that can be processed in parallel. RDDs are immutable, meaning that once an RDD is created, it cannot be modified. Instead, any transformations applied to an RDD will return a new RDD.

RDDs are the low-level representation of datasets processed by a Spark cluster. In early versions of Spark, you had to write code manipulating RDDs directly. In modern versions of Spark you should instead use the higher-level DataFrame APIs, which Spark automatically compiles into low-level RDD operations.

Once an RDD has been created, it can be transformed and processed using a variety of functions, such as map, filter, and reduce.

![rdd-process](https://user-images.githubusercontent.com/62965911/215011129-929b3b1e-ca32-4669-a4de-d40e96b8c272.png)

These are the most fundamental data structures that Spark operates on. RDDs support a wide variety of data formats such as JSON, **comma-separated values** (**CSV**), Parquet, and so on.

### Creating RDDs

An RDD can be created from a variety of data sources, including text files, sequences, and external data sources such as HBase and Cassandra.

The following code snippet shows how to create an RDD from a text file:

```py
rdd = sc.textFile("path/to/file.txt")
```

Here is an easy way using the parallelize() function:

```python
val cities = Seq("New York", "Austin")

val rdd=spark.sparkContext.parallelize(cities)
```

## Test your knowledge

Below are a few questions that should come handy in the first go :

- Spark Architecture ? Cluster types, modes and spot instances ? Mounting storage ? Job vs Stage vs Task ?
- Actions vs Transformations ? Directed Acyclic Graphs? Lazy Evaluation ?
- RDD vs Dataframe vs Dataset ? Parquet file vs Avro file ?
- StructType vs StructField? Delta lake ? Time travel ?
- Syntax errors vs Exceptions ?
- startsWith() vs endsWith() ? withColumn vs select vs withColumnRenamed ? Map vs FlatMap ? Why to use ‘literals’ ?
- .collect() ? show vs display ? How to display full values of a column ?
- Create RDD from a list ? Create RDD from a textfile ? Current_date vs current_timestamp ?
- Reading and writing a file ? Create empty dataframe ?
- Convert dataframe to rdd and rdd to dataframe ?
- Broadcast variable, explode, coalesce and repartition ?
- Merge or union two dataframes with different number of columns ?
- Iterate through eachrow of dataframe in pyspark ?
- How to handle NULL values ?

## References

1. [Getting Started with Apache Spark](https://knowledgetree.notion.site/Getting-Started-with-Apache-Spark-2c51e0d721eb4b4ca04e309c7fb296e7)
2. [Spark Interview Questions](https://knowledgetree.notion.site/Spark-Interview-Questions-94ff173de85d4df6849b289665e8fff3)
3. [Spark Quiz &amp; Solution [Videos]](https://knowledgetree.notion.site/Spark-Quiz-Solution-Videos-0ad90ea3035541e2af22eeaf18b738aa)
4. [Distributed Computing and the difference between Hadoop and Spark](https://knowledgetree.notion.site/Distributed-Computing-and-the-difference-between-Hadoop-and-Spark-1b741e18ddf5474da3a2b941f48dcea3)
5. [igfasouza.com/blog/what-is-apache-spark](http://www.igfasouza.com/blog/what-is-apache-spark/)
6. [2003–2023: A Brief History of Big Data](https://towardsdatascience.com/2003-2023-a-brief-history-of-big-data-25712351a6bc)

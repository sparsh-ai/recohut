# Apache Spark Basics

## What is Apache Spark?

Apache Spark is an open-source, multi-language, in-memory, large-scale data processing engine. It provides high-level APIs in Java, Scala, Python & R programming languages. It works on the concept of in-memory computation, making it around 100x faster than Hadoop MapReduce. It also provides tools & libraries like Spark SQL(for structured data processing), MLlib (Machine Learning), Streaming (Stream processing) & GraphX (Graph processing). Spark can be used to process data in a variety of formats, including structured data (such as CSV and Parquet) and unstructured data (such as JSON and XML).

![1_TK3eaVzHplkaHS6rLIciTA](https://user-images.githubusercontent.com/62965911/223375021-2db8e20b-4b2c-4ea2-bfb9-744620d186e3.png)

Spark was originally developed at the University of California, Berkeley’s, and later donated to Apache Software Foundation. In February 2014, Spark became a Top-Level Apache Project and has been contributed by thousands of engineers and made Spark one of the most active open-source projects in Apache.

One of the key features of Spark is its ability to perform distributed data processing. This means that Spark can split up a large dataset and process it in parallel across multiple machines. This can greatly speed up data processing tasks and allows for the processing of much larger datasets than would be possible with a single machine.

<iframe width="1440" height="595" src="https://www.youtube.com/embed/Hciruu3Gb3E" title="Apache Spark in 10 Minutes | What is Apache Spark? | Learn Apache Spark" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Advantages

- Spark is a general-purpose, in-memory, fault-tolerant, distributed processing engine that allows you to process data efficiently in a distributed fashion.
- Applications running on Spark are 100x faster than traditional systems.
- You will get great benefits using Spark for data ingestion pipelines.
- Using Spark we can process data from Hadoop HDFS, AWS S3, Databricks DBFS, Azure Blob Storage, and many file systems.
- Spark also is used to process real-time data using Streaming and Kafka.
- Using Spark Streaming you can also stream files from the file system and also stream from the socket.
- Spark natively has machine learning and graph libraries.

<iframe width="1440" height="595" src="https://www.youtube.com/embed/QaoJNXW6SQo" title="Spark Tutorial For Beginners | Big Data Spark Tutorial | Apache Spark Tutorial | Simplilearn" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Apache Spark was designed for large-scale data processing ETLs, streaming pipelines, and complex data exploration activities. It can be integrated with a wide range of databases and technologies such as HDFS, JDBC, MongoDB, Kafka, and more! It supports different data formats such as Parquet (recommended), ORC, CSV.

It was designed to be developer-friendly. You can use your favorite programming language: Python, Scala, R, and you can even run SQL-like queries!

It is a unified stack that offers Speed, Ease of Use, Modularity, and Extensibility.

NOTE

> Data engineers use Spark because it provides a simple way to parallelize computations and hides all the complexity of distribution and fault tolerance. This leaves them free to focus on using high-level DataFrame-based APIs and domain-specific language (DSL) queries to do ETL, reading and combining data from multiple sources.
>
> The performance improvements in Spark 2.x and Spark 3.0, due to the Catalyst optimizer for SQL and Tungsten for compact code generation, have made life for data engineers much easier. They can choose to use any of the three Spark APIs—RDDs, DataFrames, or Datasets—that suit the task at hand, and reap the benefits of Spark.

### Key Features

- In-memory computation
- Distributed processing using parallelize
- Can be used with many cluster managers (Spark, Yarn, Mesos etc.)
- Fault-tolerant
- Immutable
- Lazy evaluation
- Cache & persistence
- Inbuild-optimization when using DataFrames
- Supports ANSI SQL

### Components of Apache Spark

Spark consists of several components that work together to provide a comprehensive data processing ecosystem. The main components of Spark are:

- Spark Core: The foundation of Spark, provides the basic functionality for scheduling tasks and managing the execution of tasks in a cluster.
- Spark SQL: Allows for the processing of structured data using SQL-like commands.
- Spark Streaming: Allows for the processing of streaming data.
- Spark MLlib: A library for machine learning tasks.
- Spark GraphX: A library for graph processing.

Apache Spark supports transformations with three different **Application Programming Interfaces** (**APIs**): **Resilient Distributed Datasets** (**RDDs**), **DataFrames**, and **Datasets**. Datasets are just extensions of DataFrames, with additional features like being type-safe (where the compiler will strictly check for data types) and providing an **object-oriented** (**OO**) interface.

## Spark Architecture

Apache Spark works in a master-slave architecture where the master is called “Driver” and slaves are called “Workers”. When you run a Spark application, Spark Driver creates a context that is an entry point to your application, and all operations (transformations and actions) are executed on worker nodes, and the resources are managed by Cluster Manager.

![img](https://user-images.githubusercontent.com/62965911/214256759-3ebd302e-8d9f-4f29-98ae-1841dacf9cd3.jpeg)

### Driver program

The driver program (aka Spark driver) is a dedicated process that runs on the driver machine. It is responsible for executing and holding the `SparkSession`, which encapsulates the `SparkContext`—this is considered the application’s entry point, or the “real program.” The `SparkContext` contains all the basic functions, context delivered at start time, and information about the cluster. The driver also holds the DAG scheduler, task scheduler, block manager, and everything that is needed to turn the code into jobs that the worker and executors can execute on the cluster. The driver program works in synergy with the cluster manager to find the existing machines and allocated resources.

### Executor

An executor is a process launched for a particular Spark application on a worker node. Multiple tasks can be assigned to each executor. A JVM process communicates with the cluster manager and receives tasks to execute. Tasks on the same executor can benefit from shared memory, such as the cache, and global parameters, which make the tasks run fast.

NOTE

> A task is the smallest unit of schedulable work in Spark. It runs the code assigned to it, with the data pieces assigned to it.

### Worker node

A worker node, as its name indicates, is responsible for executing the work. Multiple executors can run on a single worker node and serve multiple Spark applications.

### Cluster manager

Together with the driver program, the cluster manager is responsible for orchestrating the distributed system. It assigns executors to worker nodes, assigns resources, and communicates information about resource availability to the driver program. In addition to Spark’s standalone cluster manager, this can be any other cluster manager that can manage machines and network capacity, such as Kubernetes, Apache Mesos, or Hadoop YARN.

## Cloud Storage instead of HDFS

<iframe width="1440" height="595" src="https://www.youtube.com/embed/cfXJFrSJkeI" title="Cloud Storage instead of HDFS" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Real-life Applications of Spark

1. Data Processing and ETL: Spark is widely used for processing and transforming large datasets, making it a popular choice for ETL (Extract, Transform, Load) operations. Spark's ability to handle semi-structured and structured data, along with its support for a wide range of file formats, makes it a powerful tool for pre-processing.
2. Machine Learning: Spark's MLlib library provides a wide range of machine learning algorithms, making it a popular choice for building large-scale machine learning models. It allows for distributed processing of large datasets, which can speed up the training process for machine learning models.
3. Streaming: Spark's Streaming API provides a way to process data in real time, making it a popular choice for building real-time data processing pipelines. It can handle data streams from various sources such as Kafka, Flume, and Kinesis.
4. Graph Processing: Spark's GraphX library provides a way to process graph data, making it a popular choice for building graph-based applications such as social network analysis, recommendation systems, and fraud detection.
5. Natural Language Processing: Spark's MLlib library provides a way to process text data, making it a popular choice for building NLP (Natural Language Processing) applications such as text classification, sentiment analysis, and language translation.
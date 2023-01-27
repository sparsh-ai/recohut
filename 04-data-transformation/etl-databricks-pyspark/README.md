# Databricks and PySpark

## Concepts

1. [Hadoop](./hadoop.md)
1. [The Genesis of Spark](./spark-origin.md)
1. [Spark](./spark.md)
1. [RDD](./rdd.md)
1. [Spark Questions](./spark-questions.md)

## Steps

1. [Setup Databricks Account](./setup.md)
1. [Project: Data Engineering with Databricks](./project-databricks-de/)
1. [Project: Apache Spark Programming with Databricks](./project-bedbricks/)
1. [Project: Data Engineer Learner Path with Databricks](./project-learnerbricks/)
1. [Project: Advanced Data Engineering with Databricks](./project-advancedbricks/)
1. [Lab: PySpark Basics](./lab-pyspark-basics/)
1. [Lab: Simplifying Data Engineering and Analytics with Delta](./lab-loan-application/)
1. [Project: Data Pipeline with Databricks PySpark and Superset](./project-databricks-superset/)
1. [Lab: PySpark Basics with ITversity](./lab-pyspark-itversity/)
1. [Lab: Building a Cybersecurity Lakehouse for CrowdStrike Falcon Events](./lab-cybersecurity-databricks/)
1. [Lab: Databricks AWS Integration and Clickstream Analysis](./lab-databricks-clickstream/)
1. [Lab: Databricks Deltalake](./lab-databricks-deltalake/)
1. [Lab: Unlocking the Power of Health Data With a Modern Data Lakehouse](./lab-healthcare-databricks/)
1. [Lab: Real-time Health Tracking and Monitoring System](./lab-iot-health-tracker/)
1. [Lab: Real-Time Point-of-Sale Analytics With the Data Lakehouse](./lab-retail-pos-databricks/)
1. [Lab: Delta Live Tables vs dbt](./lab-dlt-dbt/)
1. [Lab: NYC Taxi Data Analysis with PySpark](./lab-pyspark-nyctaxi/)
1. [Lab: Getting Started with Scala](./lab-scala-getting-started/)
1. [Additional: SQL to PySpark Code Conversion](./lab-sql-to-pyspark/)

## Databricks

> Databricks is a platform that enables enterprises to quickly build their Data Lakehouse infrastructure and enable all data personas – data engineers, data scientists, and business intelligence personnel – in their organization to extract and deliver insights from the data. The platform provides a curated experience for each data persona, enabling them to execute their daily workflows. The foundational technologies that enable these experiences are open source – Apache Spark, Delta lake, MLflow, and more.
> 

Databricks was founded in 2013 by seven researchers at the University of California, Berkeley.

This was the time when the world was learning how the **Meta, Amazon, Netflix, Google, and Apple** (**MANGA**) companies had built their success by scaling up their use of AI techniques in all aspects of their operations. Of course, they could do this because they invested heavily in talent and infrastructure to build their data and AI systems. Databricks was founded with the mission to enable everyone else to do the same – use data and AI in service of their business, irrespective of their size, scale, or technological prowess.

The mission was to democratize AI. What started as a simple platform, leveraging the open source technologies that the co-founders of Databricks had created, has now evolved into the lakehouse platform, which unifies data, analytics, and AI in one place.

Databricks was born out of the frustration of the Hadoop vendors and two Apache projects: Hadoop and Spark. Databricks is the commercial entity of Apache Spark. Apache Spark was born out of frustration with Apache Hadoop and the commercial vendors where only one is left: Cloudera. Hadoop does not do well with concurrency and it has huge latency issues. Apache MapReduce is dead and was replaced with Apache Spark to remedy these limitations. Apache Spark has problems of its own and thus Databricks was born to take Spark to Enterprise.

![](https://user-images.githubusercontent.com/62965911/214503488-88a696f6-8e78-495f-813f-4a95ef7cfe7e.png)

## Apache Spark

Apache Spark is a powerful open-source data processing engine that allows for large-scale data processing and analysis. It is built on top of the Hadoop ecosystem and is designed to be fast, flexible, and easy to use. In this lab, we will provide an introduction to Spark and its various components, functions, methods, and operations as well as a detailed explanation of the two primary data structures used in Spark: Resilient Distributed Datasets (RDDs) and Spark DataFrames.

### Why Apache Spark?

Spark is a distributed computing framework that is designed to work with large datasets. It is built on top of the Hadoop Distributed File System (HDFS) and allows for in-memory data processing, which can greatly speed up data processing tasks. Spark can be used to process data in a variety of formats, including structured data (such as CSV and Parquet) and unstructured data (such as JSON and XML).

One of the key features of Spark is its ability to perform distributed data processing. This means that Spark can split up a large dataset and process it in parallel across multiple machines. This can greatly speed up data processing tasks and allows for the processing of much larger datasets than would be possible with a single machine.

### Components of Apache Spark

Spark consists of several components that work together to provide a comprehensive data processing ecosystem. The main components of Spark are:

-   Spark Core: The foundation of Spark, provides the basic functionality for scheduling tasks and managing the execution of tasks in a cluster.
-   Spark SQL: Allows for the processing of structured data using SQL-like commands.
-   Spark Streaming: Allows for the processing of streaming data.
-   Spark MLlib: A library for machine learning tasks.
-   Spark GraphX: A library for graph processing.

## Resources

1. [Data Lakehouse Explained](https://youtu.be/yumysN3XwbQ)
1. [What is Delta Lake](https://youtu.be/PftRBoqjhZM)
1. [Delta Lake Deep Dive](https://youtu.be/BMO90DI82Dc)
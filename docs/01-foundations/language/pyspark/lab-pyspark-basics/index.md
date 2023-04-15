# Lab: Pyspark Basics

In this lab, we will use the power of PySpark to perform various activities in databricks environment.

1. [M&M Counts](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/3716027562706644/4695044765152887/latest.html)
2. [San Francisco Fire Calls](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1448249936481974/4695044765152887/latest.html)
3. [SQL on US Flights Dataset](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1448249936482029/4695044765152887/latest.html)
4. [Spark Data Sources](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1448249936482069/4695044765152887/latest.html)
5. [Spark SQL & UDFs](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1448249936482145/4695044765152887/latest.html)
6. [File Formats](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1579681995515196/4695044765152887/latest.html)
7. [Delta Lake](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1579681995515243/4695044765152887/latest.html)
8. [Taxi Trip Analysis](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1579681995515304/4695044765152887/latest.html)
9. [Movielens Data Analysis](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/3114720643048633/4695044765152887/latest.html)
10. [MapReduce Practice](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/3114720643048660/4695044765152887/latest.html)
11. [Data Wrangling with Spark](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/3114720643048669/4695044765152887/latest.html)
12. [Data Lake Schema on Read](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1729220346146661/4695044765152887/latest.html)
13. [Python vs PySpark](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/310144235288371/4695044765152887/latest.html)
14. [Weather Forecast Analysis](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1473168627488941/4695044765152887/latest.html)
15. [Candy Sales analysis with PySpark](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/3961935502928289/4695044765152887/latest.html)

## Electricity Data processing with PySpark

### Read and follow these articles

1. https://ownyourdata.ai/wp/data-processing-with-spark-intro/
2. https://ownyourdata.ai/wp/data-processing-with-spark-data-catalog/
3. https://ownyourdata.ai/wp/data-processing-with-spark-schema-evolution/
4. https://ownyourdata.ai/wp/data-analysis-electricity-consumption-data/

### Code

https://github.com/acirtep/ginlong-data-processing-spark#ginlong-data-processing-spark

## Pyspark Databricks ETL

Objective: Building an ETL Pipeline with databricks Pyspark and AWS S3

![arch drawio](https://user-images.githubusercontent.com/62965911/214513989-fca32e57-e8a7-40c2-a871-a9498b5e4745.svg)

[Notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1729220346146695/4695044765152887/latest.html)

## Sales Orders PySpark

In this notebook, you'll use Spark in Databricks to explore data in files. One of the core ways in which you work with data in Spark is to load data into a **Dataframe** object, and then query, filter, and manipulate the dataframe to explore the data it contains.

We first download the sales order data and then move it to dbfs file system. Then we load the data into Pyspark dataframe and then apply schema. And then we apply pyspark functions like filter and groupby. 

After this, we explore Spark SQL and then plot the charts using matplotlib and seaborn libraries.

[Notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/3208697936837428/1828594820839020/4695044765152887/latest.html)

## Databricks Deltalake

Objective: Explore how to use Delta Lake in a Databricks Spark cluster

Delta Lake is an open source project to build a transactional data storage layer for Spark on top of a data lake. Delta Lake adds support for relational semantics for both batch and streaming data operations, and enables the creation of a Lakehouse architecture in which Apache Spark can be used to process and query data in tables that are based on underlying files in the data lake.

This lab will take approximately 40 minutes to complete.

In this lab, we are exploring various features of deltalake (a lakehouse) that we generally do not get in datalake.

[Notebook](./assets/databricks-deltalake.dbc)
# Data Transformation

## Concepts

1. [Hadoop](./concepts/hadoop.md)
1. [The Genesis of Spark](./concepts/spark-origin.md)
1. [Spark](./concepts/spark.md)
1. [RDD](./concepts/rdd.md)
1. [Spark Questions](./concepts/spark-questions.md)

## Steps

## Data Preparation

1. [Cloud Dataprep](./cloud-dataprep/)

## ELT

1. [DBT](./elt-dbt/)
1. [Snowpark](./elt-snowpark/)

## ETL

1. [Databricks & PySpark](./etl-databricks-pyspark/)
1. [Cloud Dataproc](./etl-dataproc/)
1. [EMR](./etl-emr/)
1. [Glue Studio](./etl-glue-studio/)
1. [Lambda Function](./etl-lambda-function/)

## Note

Data transformation involves taking source data which has been ingested into your data platform and cleansing it, combining it, and modeling it for downstream use. Historically the most popular way to transform data has been with the SQL language and data engineers have built data transformation pipelines using SQL often with the help of ETL/ELT tools. But recently many folks have also begun adopting the DataFrame API in languages like Python/Spark for this task. For the most part a data engineer can accomplish the same data transformations with either approach, and deciding between the two is mostly a matter of preference and particular use cases. That being said, there are use cases where a particular data transform can't be expressed in SQL and a different approach is needed. The most popular approach for these use cases is Python/Spark along with a DataFrame API.

![](https://user-images.githubusercontent.com/62965911/214255202-0563b49c-1708-4dbb-ac2f-cca3843055d6.gif)

### Transformation in the Warehouse using SQL

It’s time to transform the raw data into the end-user data model. Transformations can affect

- Data processing time.
- Data warehouse cost. Modern data warehouses usually charge based on the amount of data scanned.
- Data pipeline development speed and issues.

#### Transformation types

The ultimate goal for optimizing transformations is to reduce the movement of data within your data warehouse. Data warehouses are distributed systems with the data stored as chunks across the cluster. Reducing the movement of data across the machines within the distributed system significantly speeds up the processing of data.

There are two major types of transformations as explained below.

1. Narrow transformations: These are transformations that do not involve the movement of data across machines within the warehouse. The transformations are applied to the rows without having to move these rows to other machines within the warehouse.

E.g. Lower(), Concat(), etc are functions that are applied directly to the data in memory

2. Wide transformations: These are transformations that involve the movement of data across machines within the warehouse.

E.g. When you join 2 tables, the warehouse engine will move the smaller table’s data to the same machine(s) as the larger table’s data. This is so that these 2 tables can be joined. Moving data around is a high-cost operation in a distributed system, and as such, the warehouse engine will optimize to keep the data movement to a minimum.

When self-joining, it’s beneficial to join on the partitioned column(s) as this will keep data movement within the system to a minimum.

Some common transformations to know are

- Joins, anti joins
- String, numeric, and date functions
- Group by, aggregates, order by, union, having
- CTEs
- Window functions
- Parsing JSON
- Stored procedures, sub queries and functions

Some points you need answered/explored are

1. How does transformation time increase with an increase in the data size? Is it linear or worse? Hint: A cross join will not scale linearly
1. Read the data warehouse documentation to know what features exist. This allows you to go back to the docs in case you need to use a feature. Most transformations can be done within your data warehouse.
1. When evaluating performance be aware of cached reads on subsequent queries.
1. When possible, filter the data before or during the transformation query.
1. Most SQL queries are a mix of wide and narrow transformations.

#### Query planner

The query planner lets you see what steps the warehouse engine will take to run your query. You can use the EXPLAIN command to see the query plan.

Most data warehouse documentation has steps you can take to optimize your queries. E.G. Snowflake’s common query issues, Redshift’s query plan and execution

In short

1. Use explain to see the query plan.
2. Optimize the steps that have the highest costs. Use available warehouse documentation for optimization help.

### Most Common Data Transformations

#### File format optimizations

CSV, XML, JSON, and other types of plaintext files are commonly used to store structured and semi-structured data. These file formats are useful when manually exploring data, but there are much better, binary-based file formats to use for computer-based analytics. A common binary format that is optimized for read-heavy analytics is the Apache Parquet format. A common transformation is to convert plaintext files into an optimized format, such as Apache Parquet.
    
Within modern data lake environments, there are a number of file formats that can be used that are optimized for data analytics. From an analytics perspective, the most popular file format currently is **Apache Parquet**.

**Parquet** files are columnar-based, meaning that the contents of the file are physically stored to have data grouped by columns, rather than grouped by rows as with most file formats. (CSV files, for example, are physically stored to be grouped by rows.) As a result, queries that select a set of specific columns (rather than the entire row) do not need to read through all the data in the Parquet file to return a result, leading to performance improvements.

Parquet files also contain metadata about the data they store. This includes schema information (the data type for each column), as well as statistics such as the minimum and maximum value for a column contained in the file, the number of rows in the file, and so on.

A further benefit of Parquet files is that they are optimized for compression. A 1 TB dataset in CSV format could potentially be stored as 130 GB in Parquet format once compressed. Parquet supports multiple compression algorithms, although Snappy is the most widely used compression algorithm.

These optimizations result in significant savings, both in terms of storage space used and for running queries.

For example, the cost of an Amazon Athena query is based on the amount of compressed data scanned (at the time of writing, this cost was $5 per TB of scanned data). If only certain columns are queried of a Parquet file, then between the compression and only needing to read the data chunks for the specific columns, significantly less data needs to be scanned to resolve the query.

In a scenario where your data table is stored across perhaps hundreds of Parquet files in a data lake, the analytics engine is able to get further performance advantages by reading the metadata of the files. For example, if your query is just to count all the rows in a table, this information is stored in the Parquet file metadata, so the query doesn't need to actually scan any of the data. For this type of query, you will see that Athena indicates that 0 KB of data was scanned, therefore there is no cost for the query.

Or, if your query is for where the sales amount is above a specific value, the analytics engine can read the metadata for a column to determine the minimum and maximum values stored in the specific data chunk. If the value you are searching for is higher than the maximum value recorded in the metadata, then the analytics engine knows that it does not need to scan that specific column data chunk. This results in both cost savings and increased performance for queries.

Because of these performance improvements and cost savings, a very common transformation is to convert incoming files from their original format (such as CSV, JSON, XML, and so on) into the analytics-optimized Parquet format.

#### Data standardization

When building out a pipeline, we often load data from multiple different data sources, and each of those data sources may have different naming conventions for referring to the same item. For example, a field containing someone's birth date may be called *DOB*, *dateOfBirth*, *birth_date*, and so on. The format of the birth date may also be stored as *mm/dd/yy*, *dd/mm/yyyy*, or in a multitude of other formats.

One of the tasks we may want to do when optimizing data for analytics is to standardize column names, types, and formats. By having a corporate-wide analytic program, standard definitions can be created and adopted across all analytic projects in the organization.

#### Data quality checks

Another aspect of data transformation may be the process of verifying data quality and highlighting any ingested data that does not meet the expected quality standards.

#### Data partitioning

A common optimization strategy for analytics is to partition the data, grouping the data at the physical storage layer by a field that is often used in queries. For example, if data is often queried by a date range, then data can be partitioned by a date field. If storing sales data, for example, all the sales transactions for a specific month would be stored in the same Amazon S3 prefix (which is much like a directory). When a query is run that selects all the data for a specific day, the analytic engine only needs to read the data in the directory that's storing data for the relevant month.

Another common approach for optimizing datasets for analytics is to **partition** the data, which relates to how the data files are organized in the storage system for a data lake.

**Hive partitioning** splits the data from a table to be grouped together in different folders, based on one or more of the columns in the dataset. While you can partition the data in any column, a common partitioning strategy that works for many datasets is to partition based on date.

For example, suppose you had sales data for the past four years from around the country, and you had columns in the dataset for **Day**, **Month** and **Year**. In this scenario, you could select to partition the data based on the **Year** column. When the data was written to storage, all the data for each of the past few years would be grouped together with the following structure:

datalake_bucket/year=2021/file1.parquet

datalake_bucket/year=2020/file1.parquet

datalake_bucket/year=2019/file1.parquet

datalake_bucket/year=2018/file1.parquet

If you then run a SQL query and include a **WHERE Year = 2018** clause, for example, the analytics engine only needs to open up the single file in the **datalake_bucket/year=2018** folder. Because less data needs to be scanned by the query, it costs less and completes quicker.

Deciding on which column to partition by requires that you have a good understanding of how the dataset will be used. If you partition your dataset by year but a majority of your queries are by the **business unit** (**BU**) column across all years, then the partitioning strategy would not be effective.

Queries you run that do not use the partitioned columns may also end up causing those queries to run slower if you have a large number of partitions. The reason for this is that the analytics engine needs to read data in all partitions, and there is some overhead in working between all the different folders. If there is no clear common query pattern, it may be better to not even partition your data. But if a majority of your queries use a common pattern, then partitioning can provide significant performance and cost benefits.

You can also partition across multiple columns. For example, if you regularly process data at the day level, then you could implement the following partition strategy:

datalake_bucket/year=2021/month=6/day=1/file1.parquet

This significantly reduces the amount of data to be scanned when queries are run at the daily level and also works for queries at the month or year level. However, another warning regarding partitioning is that you want to ensure that you don't end up with a large number of small files. The optimal size of Parquet files in a data lake is 128 MB–1 GB. The Parquet file format can be split, which means that multiple nodes in a cluster can process data from a file in parallel. However, having lots of small files requires a lot of overhead for opening, reading metadata, scanning data, and closing each file, and can significantly impact performance.

Partitioning is an important data optimization strategy and is based on how the data is expected to be used, either for the next transformation stage or for the final analytics stage. Determining the best partitioning strategy requires that you understand how the data will be used next.

#### Data denormalization

In traditional relational database systems, the data is normalized, meaning that each table contains information on a specific focused topic, and associated, or related, information is contained in a separate table. The tables can then be linked through the use of foreign keys.

For data lakes, combining the data from multiple tables into a single table can often improve query performance. Data denormalization takes two (or more) tables and creates a new table with data from both tables.

#### Data cataloging

Another important component that we should include in the transformation section of our pipeline architecture is the process of cataloging the dataset. During this process, we ensure all the datasets in the data lake are referenced in the data catalog and can add additional business metadata.

## More Resources

1. https://www.fivetran.com/blog/what-is-data-transformation
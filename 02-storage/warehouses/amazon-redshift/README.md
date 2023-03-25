# Amazon Redshift

Amazon Redshift is a data warehousing service optimized for **online analytical processing** (**OLAP**) applications. You can start with just a few hundred **gigabytes** (**GB**) of data and scale to a **petabyte** (**PB**) or more. Designing your database for analytical processing lets you take full advantage of Amazon Redshift's columnar architecture.

An analytical schema forms the foundation of your data model. You can choose a star or snowflake schema by using Normalized, Denormalized, or Data Vault data modeling techniques. Redshift is a relational database management system (RDBMS) that supports a number of data model structures, including dimensional, denormalized, and aggregate (rollup) structures. This makes it optimal for analytics.

Watch this video: https://www.youtube.com/watch?v=lWwFJV_9PoE

## Amazon Redshift Serverless

Amazon Redshift Serverless makes it simple to run and scale analytics without having to manage the instance type, instance size, lifecycle management, pausing, resuming, and so on. It automatically provisions and intelligently scales data warehouse compute capacity to deliver fast performance for even the most demanding and unpredictable workloads, and you pay only for what you use. Just load your data and start querying right away in the Amazon Redshift Query Editor or in your favorite business intelligence (BI) tool and continue to enjoy the best price performance and familiar SQL features in an easy-to-use, zero administration environment.

## Data Ingestion in Amazon Redshift

Data ingestion is the process of getting data from the source system to Amazon Redshift. This can be done by using one of many AWS cloud-based ETL tools like AWS Glue, Amazon EMR, or AWS Step Functions, or you can simply load data from Amazon Simple Storage Service (Amazon S3) to Amazon Redshift using the COPY command. A COPY command is the most efficient way to load a table because it uses the Amazon Redshift massively parallel processing (MPP) architecture to read and load data in parallel from a file or multiple files in an S3 bucket.

Now SQL users can easily automate data ingestion from Amazon S3 to Amazon Redshift with a simple SQL command using the Amazon Redshift auto-copy feature. COPY statements are triggered and start loading data when Amazon Redshift auto-copy detects new files in the specified Amazon S3 paths. This also ensures end-users have the latest data available in Amazon Redshift shortly after the source data is available.

Copy jobs have the following benefits:

- SQL users such as data analysts can now load data from Amazon S3 automatically without having to build a pipeline or using an external framework
- Copy jobs offer continuous and incremental data ingestion from an Amazon S3 location without the need to implement a custom solution
- This functionality comes at no additional cost
- Existing COPY statements can be converted into copy jobs by appending the JOB CREATE <job_name> parameter
- It keeps track of all loaded files and prevents data duplication
- It can be easily set up using a simple SQL statement and any JDBC or ODBC client

> [Code snippets](./code-snippets.md)

## Vacuum

**Vacuum Delete:**

When you perform delete on a table, the rows are marked for deletion(soft deletion), but are not removed. When you perform an update, the existing rows are marked for deletion(soft deletion) and updated rows are inserted as new rows. Amazon Redshift automatically runs a VACUUM DELETE operation in the background to reclaim disk space occupied by rows that were marked for deletion by UPDATE and DELETE operations, and compacts the table to free up the consumed space. To minimize impact to your system performance, automatic VACUUM DELETE runs during periods when workloads are light.

If you need to reclaim diskspace immediately after a large delete operation, for example after a large data load, then you can still manually run the VACUUM DELETE command.

**Vacuum Sort:**

When you define [SORT KEYS ](https://docs.aws.amazon.com/redshift/latest/dg/t_Sorting_data.html) on your tables, Amazon Redshift automatically sorts data in the background to maintain table data in the order of its sort key. Having sort keys on frequently filtered columns makes block level pruning, which is already efficient in Amazon Redshift, more efficient.

Amazon Redshift keeps track of your scan queries to determine which sections of the table will benefit from sorting and it automatically runs VACUUM SORT to maintain sort key order. To minimize impact to your system performance, automatic VACUUM SORT runs during periods when workloads are light.

COPY command automatically sorts and loads the data in sort key order. As a result, if you are loading an empty table using COPY command, the data is already in sort key order. If you are loading a non-empty table using COPY command, you can optimize the loads by loading data in incremental sort key order because VACUUM SORT will not be needed when your load is already in sort key order.

**Vacuum recluster:**

Use VACUUM recluster whenever possible for manual VACUUM operations. This is especially important for large objects with frequent ingestion and queries that access only the most recent data. Vacuum recluster only sorts the portions of the table that are unsorted and hence runs faster. Portions of the table that are already sorted are left intact. This command doesn't merge the newly sorted data with the sorted region. It also doesn't reclaim all space that is marked for deletion.

**Vacuum boost:**

Boost runs the VACUUM command with additional compute resources, as they're available. With the BOOST option, VACUUM operates in one window and blocks concurrent deletes and updates for the duration of the VACUUM operation. Note that running vacuum with the BOOST option contends for system resources, which might affect performance of other queries. As a result, it is recommended to run the VACUUM BOOST when the load on the system is light, such as during maintenance operations.

## Labs

### Data Loading

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/02-storage/warehouses/amazon-redshift/lab-redshift-immersion/01-data-loading.ipynb)

1. Create 8 Tables based on TPCH data model in Redshift (DDL)
2. Load data into these tables from S3 bucket using COPY command (DML)
3. See the effect of different VACUUM commands

### Data Loading using Python

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/02-storage/warehouses/amazon-redshift/lab-redshift-taxi.ipynb)

1. Connect to Redshift and Read data using Psycopg2 library
2. Taxi Data Process and Save to Redshift using AWS Wrangler library

### Data Loading and Analysis

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/02-storage/warehouses/amazon-redshift/lab-redshift-retail.ipynb)

1. Load csv and json data from S3 into Redshift using COPY command
2. Running Joins and aggregation queries in Redshift

### Table Design and Query Tuning

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/02-storage/warehouses/amazon-redshift/lab-redshift-immersion/02-query-tuning.ipynb)

1. Setting distribution and sort keys
2. Deep copy
3. Explain plans
4. System table queries

### Implement a slowly changing dimension

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/02-storage/warehouses/amazon-redshift/lab-redshift-scd.ipynb)

1. Learn how to create a type 2 dimension table by adding slowly changing tracking columns
2. Dataset: customer table from the TPC-DS benchmark dataset
3. Uses the best practices and anti-patterns
4. Go over the extract, transform, and load (ETL) merge technique, demonstrating the SCD process

### Ongoing Load - ELT

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/02-storage/warehouses/amazon-redshift/lab-redshift-immersion/03-ongoing-load-elt.ipynb)

This lab demonstrates how you can modernize your ongoing data loads using `Stored Procedures`, `Materialized Views` and `Pre-defined Functions` to transform data within Redshift.

### Query Data Lake - Redshift Spectrum

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/02-storage/warehouses/amazon-redshift/lab-redshift-immersion/04-query-data-lake-spectrum.ipynb)

In this lab, we show you how to query data in your Amazon S3 data lake with Amazon Redshift without loading or moving data. We will also demonstrate how you can leverage views which union data in Redshift Managed storage with data in S3. You can query structured and semi-structured data from files in Amazon S3 without having to copy or move data into Amazon Redshift tables.

### Spectrum Query Tuning

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/02-storage/warehouses/amazon-redshift/lab-redshift-immersion/05-spectrum-query-tuning.ipynb)

In this lab, we show you how to diagnose your Redshift Spectrum query performance and optimize performance by leveraging partitions, optimizing storage, and predicate pushdown.

### Slowly Changing Dimension

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/data-science-engineering-bootcamp/blob/main/02-storage/warehouses/amazon-redshift/lab-redshift-scd-2/main.ipynb)

Data loading into a SCD table involves a first-time bulk data loading, referred to as the _initial data load_. This is followed by continuous or regular data loading, referred to as an _incremental data load_, to keep the records up to date with changes in the source tables.

To demonstrate the solution, we walk through the following steps for initial data load (1–7) and incremental data load (8–12):

1. Land the source data files in an Amazon S3 location, using one subfolder per source table.
2. Use an [AWS Glue](https://aws.amazon.com/glue) crawler to parse the data files and register tables in the AWS Glue Data Catalog.
3. Create an external schema in Amazon Redshift to point to the AWS Glue database containing these tables.
4. In Amazon Redshift, create one view per source table to fetch the latest version of the record for each primary key (`customer_id`) value.
5. Create the `dim_customer` table in Amazon Redshift, which contains attributes from all relevant source tables.
6. Create a view in Amazon Redshift joining the source table views from Step 4 to project the attributes modeled in the dimension table.
7. Populate the initial data from the view created in Step 6 into the `dim_customer` table, generating `customer_sk`.
8. Land the incremental data files for each source table in their respective Amazon S3 location.
9. In Amazon Redshift, create a temporary table to accommodate the change-only records.
10. Join the view from Step 6 and `dim_customer` and identify change records comparing the combined hash value of attributes. Populate the change records into the temporary table with an `I`, `U`, or `D` indicator.
11. Update `rec_exp_dt` in `dim_customer` for all `U` and `D` records from the temporary table.
12. Insert records into `dim_customer`, querying all `I` and `U` records from the temporary table.

## Explore further

1. [Accelerate Application Development with Real Time Streams in Amazon Redshift](https://bit.ly/3Se99Ur)
2. [Data Engineering at Udem](https://www.slideshare.net/ankarabigdata/data-engineering-at-udemy?qid=d835f0e3-f290-4445-bd19-d6ac6824e24c&v=&b=&from_search=5)
3. [Implement a slowly changing dimension in Amazon Redshift](https://aws.amazon.com/blogs/big-data/implement-a-slowly-changing-dimension-in-amazon-redshift/)

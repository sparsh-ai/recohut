# Curriculum - Data Engineering Training

## Level 100

**Estimated Time:** 55 hours

### Modules

* [ ] Developer Foundations
* [ ] Data Engineering Foundations
* [ ] AWS Cloud Essentials
* [ ] Programming - SQL
* [ ] Programming - Python
* [ ] Programming - PySpark
* [ ] Programming - Scala
* [ ] Data Modeling and Warehousing
* [ ] Data Lakes and Lakehouses
* [ ] Big Data Processing
* [ ] Orchestration and Data Pipelines
* [ ] Capstone Projects

### Developer Foundations

* [ ] Download and Install vscode
* [ ] Understand vscode features
* [ ] Install extensions in vscode
* [ ] Download and Install Anaconda
* [ ] Create virtual environment in anaconda
* [ ] Create jupyter notebook in vscode and connect to venv
* [ ] Create github account
* [ ] Install git cli
* [ ] Create git repo and add students as collaborator
* [ ] Connect local workspace to git repo
* [ ] Learn git commands
* [ ] Learn bash commands
* [ ] Download and Install DBeaver

### Data Engineering Foundations

* [ ] What is Data Engineering?
* [ ] Role of Data Engineering in Organizations
* [ ] Skills required to become a Data Engineer
* [ ] Data engineer versus data scientist
* [ ] What is data lake and data warehouse?
* [ ] What is medallion architecture?
* [ ] What is EL, ETL and ELT?
* [ ] H/w - Most common questions

### AWS Cloud Essentials

* [ ] (Optional) Create AWS Account
* [ ] Create IAM user and generate credentials
* [ ] Install AWS CLI
* [ ] Setup AWS credentials
* [ ] Walkthrough of various AWS Services (S3, RDS, Redshift, Glue, Athena, Lambda, EMR, Keyspace, Cloudformation, IAM, Secrets Manager)
* [ ] Comparison of AWS services with GCP Services (GCS Bucket, Dataproc, IAM, Cloud Functions, BigQuery, CloudSQL, BigTable)
* [ ] Comparison of AWS services with Azure Services (Blob Storge, DataLake Gen2 buckets, Databricks/Synapse Analytics, Azure Data Factory, Azure SQL Databases)
* [ ] Learn AWS CLI S3 essential commands
* [ ] Copy and Sync data to/from S3 with AWS CLI
* [ ] Create database in RDS DBMS and generate credentials
* [ ] Connect to RDS DBMS in DBeaver
* [ ] Create a Secret in Secrets Manager Vault
* [ ] Get the credential using AWS CLI

### Programming - SQL

* [ ] Ingest data from CSV file into MySQL database table [[source code](../02-storage/databases/mysql/lab-data-ingestion-to-mysql)]
* [ ] SQL Basics - Select, Limit, Where, Comparison and Logical operators, Order by
* [ ] SQL Intermediate - Aggregations, Group by, Case statements, Joins
* [ ] SQL Advanced - Dates, Text, Subqueries, Window functions, Optimizations

### Programming - Python

* [ ] Lists and dictionaries
* [ ] For loops and while loops
* [ ] Functions and Inline functions
* [ ] Read/Write and Manipulate Data using Pandas
* [ ] Pulling data from APIs using requests library
* [ ] Reading and writing data to databases using psycopg2 and sqlalchemy library
* [ ] Reading data from S3 and athena using aws data wrangler library
* [ ] Pull credentials from Secrets Manager using boto3 library
* [ ] Lab - Exchange Rate ETL process [[source code](../01-foundations/language/python/lab-exchange-rate-etl)]

### Programming - PySpark

* [ ] Create databricks account
* [ ] Create your first databricks cluster
* [ ] Create your first databricks notebook
* [ ] M&M color balls analysis with PySpark
* [ ] Movielens and Song analysis with PySpark
* [ ] San Francisco Fire Department call analysis with PySpark
* [ ] Connect AWS to PySpark and build an ETL pipeline [[source code](../03-processing/databricks/lab-databricks-pyspark-s3)]

### Programming - Scala

* [ ] Introduction to Scala programming
* [ ] Getting started with Spark Scala
* [ ] Building extract and load pipeline with Scala, S3 and Postgres [[source code](../03-processing/databricks/lab-databricks-scala-postgres-s3)]

### Data Modeling and Warehousing

* [ ] Building a sql data model for a music company in Postgres
* [ ] Building a nosql data model for a music company in Cassandra
* [ ] Difference between databases, warehouses, lakes and lakehouses
* [ ] OLTP vs OLAP technologies
* [ ] Loading data into Redshift warehouse with S3 staging and COPY command

### Data Lakes and Lakehouses

* [ ] Building a data lake for a healthcare company with AWS, S3 and Athena
* [ ] Working with AWS S3 and Delta lake in Databricks

### Big Data Processing

* [ ] Creating and Monitoring Production Data Processing Jobs in Databricks
* [ ] Creating and submitting Word count Spark Job in EMR Serverless
* [ ] Building a near real-time serverless data pipeline with AWS lambda function [[source code](../03-processing/aws-lambda-function/lab-lambda-csv-parquet)]
* [ ] Building an ELT pipeline for a cab service company using dbt and Postgres

### Orchestration and Data Pipelines

* [ ] Install Airflow in your PC
* [ ] Starting Airflow scheduler and web server
* [ ] Building a BASH commands execution pipeline in Airflow
* [ ] Building a CSV to JSON pipeline in Airflow
* [ ] Integrate email notifications in Airflow with AWS SNS/SES service

### Capstone Projects

* [ ] ACLED ETL Data Pipeline for war and conflict analysis (Airflow, Postgres, Glue, Spark)
* [ ] Sales & Orders ELT Data Pipeline (dbt, Redshift, SQL, Jinja)

## Level 200

**Estimated Time:** 75 hours

### Language - SQL

* [ ] Postgres SQL basics to advanced [[source code](../01-foundations/language/sql/lab-postgres-queries)]
* [ ] Running Dates, String and Advanced queries in Postgres on Sales data [[source code](../02-storage/databases/postgres/lab-postgres-sales)]
* [ ] Working with Book dataset on SQLite database [[source code](../02-storage/databases/sqlite/lab-sqlite-basics)]

### Storage Layer - Flat Files

* [ ] Introduction to various file formats - CSV, Parquet, JSON, Avro, and ORC [[link to note](../02-storage/flat-files/README.md)]
* [ ] Processing JSON data in Python [[source code](../02-storage/flat-files/lab-processing-json-data)]

### Storage Layer - Databases

* [ ] Configuring and Securing Azure SQL Database [[source code](../02-storage/databases/azure-sql/lab-securing-azure-sql-databases)]
* [ ] Load CSV data from on-premise to GCP CloudSQL [[source code](../02-storage/databases/cloudsql/lab-gcp-cloudsql-nyctaxi)]
* [ ] db2 BookShop and PetSale Data Ingestion and Stored Procedure [[source code](../02-storage/databases/db2/lab-dbt-bookshop-petsale-data-ingestion)]
* [ ] OLAP Analytics on bank, TPCH and NYC Taxi datasets using DuckDB [[source code](../02-storage/databases/duckdb/lab-analytics-bank-tpch-nyctaxi)]
* [ ] Getting started with Postgres and Python [[source code](../02-storage/databases/postgres/lab-postgres-getting-started)]
* [ ] Use bash shell commands to extract, transform and load data into Postgres [[source code](../02-storage/databases/postgres/lab-bash-etl)]
* [ ] Extract and load food data into Postgres using Python [[source code](../02-storage/databases/postgres/lab-extract-and-load-food-data)]
* [ ] Build a database for crime reports in Postgres [[source code](../02-storage/databases/postgres/lab-postgres-crime-reports)]

### Storage Layer - NoSQL Databases

* [ ] Streaming Data Processing - Streaming Data Pipelines into GCP Bigtable [[source code](../02-storage/nosql-databases/bigtable/lab-gcp-streaming-bigtable)]
* [ ] Fundamentals of Apache Cassandra  [[link to note](../02-storage/nosql-databases/cassandra/README.md)]
* [ ] Setup Cassandra in local system [[source code](../02-storage/nosql-databases/cassandra/lab-getting-started-with-cassandra)]
* [ ] Getting started with Cassandra [[source code](../02-storage/nosql-databases/cassandra/lab-getting-started-with-cassandra)]
* [ ] Cassandra on Cloud with Amazon Keyspaces [[source code](../02-storage/nosql-databases/cassandra/lab-amazon-keyspaces)]
* [ ] Fundamentals of DynamoDB [[link to note](../02-storage/nosql-databases/dynamodb/README.md)]
* [ ] Getting started with MongoDB [[source code](../02-storage/nosql-databases/mongodb/lab-mongodb-basics)]

### Storage Layer - Data Warehouses

* [ ] Amazon Athena Basics [[link to note](../02-storage/warehouses/athena/README.md)]
* [ ] Building Federated Query System using Amazon Athena [[source code](../02-storage/warehouses/athena/project-athena-federated)]
* [ ] GCP BigQuery Basics [[link to note](../02-storage/warehouses/bigquery/README.md)]
* [ ] Using BigQuery to do analysis [[source code](../02-storage/warehouses/bigquery/lab-bigquery-analysis)]
* [ ] Bigquery basics command line operations [[source code](../02-storage/warehouses/bigquery/lab-bigquery-commandline)]
* [ ] Creating a Data Warehouse Through Joins and Unions [[source code](../02-storage/warehouses/bigquery/lab-bigquery-data-warehousing)]
* [ ] Build and Optimize Data Warehouses with BigQuery [[source code](../02-storage/warehouses/bigquery/lab-bigquery-optimization)]
* [ ] Optimizing your BigQuery Queries for Performance [[source code](../02-storage/warehouses/bigquery/lab-bigquery-query-optimization)]
* [ ] Building a BigQuery Data Warehouse [[source code](../02-storage/warehouses/bigquery/lab-biqeury-building-warehouse)]
* [ ] Predict Visitor Purchases with a Classification Model in BigQuery ML [[source code](../02-storage/warehouses/bigquery/lab-gcp-bigquery-ml)]
* [ ] NYC Cab Prediction Model in BigQuery ML [[source code](../02-storage/warehouses/bigquery/lab-gcp-bigquery-nyctaxi)]
* [ ] Copy data from S3 into Amazon Redshift [[source code](../02-storage/warehouses/redshift/lab-copy-from-s3)]
* [ ] Create, Train and Deploy Multi Layer Perceptron (MLP) models using Amazon Redshift ML [[source code](../02-storage/warehouses/redshift/lab-redshift-ml)]
* [ ] Connect and Query Redshift with Python [[source code](../02-storage/warehouses/redshift/lab-redshift-python)]
* [ ] Implement a slowly changing dimension in Amazon Redshift [[source code](../02-storage/warehouses/redshift/lab-redshift-scd)]
* [ ] Load NYC Taxi csv data into Redshift using Python AWS Data Wrangler [[source code](../02-storage/warehouses/redshift/lab-redshift-taxi)]
* [ ] Advanced Data Analytics on TPCH Sales data in Redshift [[source code](../02-storage/warehouses/redshift/project-redshift-sales)]

### Storage Layer - Data Lakes

* [ ] Working with S3 using Boto3 in Python [[source code](../02-storage/datalakes/lab-s3-boto3)]
* [ ] Creating and Managing Data in Azure Data Lake [[source code](../02-storage/datalakes/lab-adl-create-manage-data)]
* [ ] Securing and Monitoring Data in Azure Data Lake [[source code](../02-storage/datalakes/lab-adl-securing-monitoring-lakes)]

### Storage Layer - Data Lakehouses

* [ ] Introduction to Data Lakehouses - Delta, Iceberg and Hudi [[link to note](../02-storage/lakehouses/README.md)]

### Serving Layer - SQL Data Modeling

### Serving Layer - NoSQL Data Modeling

### Processing Layer - Batch Data Processing

* [ ] Data Transformation with PySpark using Amazon EMR Serverless Application [[source code](../03-processing/aws-emr/lab-emr-serverless)]
* [ ] Advanced Data Engineering and Data Processing with AWS Glue Jobs [[source code](../03-processing/aws-glue/lab-glue-advanced)]
* [ ] Handle UPSERT data operations using open-source Delta Lake and AWS Glue [[source code](../03-processing/aws-glue/lab-glue-deltalake-cdc-upsert)]
* [ ] Create your own reusable visual transforms for AWS Glue Studio [[source code](../03-processing/aws-glue/lab-glue-studio-custom-transforms)]
* [ ] Tickets ETL with Glue Studio [[source code](../03-processing/aws-glue/lab-glue-studio-tickets)]
* [ ] CSV to Parquet Transformation with Glue Studio [[source code](../03-processing/aws-glue/lab-csv-to-parquet-conversion)]
* [ ] Processing Data Using Azure Databricks - Configuring the Azure Databricks environment, Integrate Databricks with Azure Key Vault, Mounting an Azure Data Lake container in Databricks, Processing data using notebooks, Scheduling notebooks using job clusters, Working with Delta Lake tables [[source code](../03-processing/azure-databricks/lab-data-processing-azure-dbr)]
* [ ] Build Data Pipeline with HDInsight [[source code](../03-processing/azure-hdinsight/lab-simple-data-processing)]
* [ ] Processing Data Using Azure Synapse Analytics - This lab covers exploring data using Synapse Serverless SQL pool, processing data using Synapse Spark Pools, Working with Synapse Lake database, and integrating Synapse Analytics with Power BI. Recipe 1 - Provisioning an Azure Synapse Analytics workspace. Recipe 2 - Analyzing data using serverless SQL pool. Recipe 3 - Provisioning and configuring Spark pools. Recipe 4 - Processing data using Spark pools and a lake database. Recipe 5 - Querying the data in a lake database from serverless SQL pool. Recipe 6 - Scheduling notebooks to process data incrementally [[Source code](../03-procesing/azure-synapse-analytics/lab-data-processing-synapse-analytics)]
* [ ] Transforming Data Using Azure Synapse Dataflows - This lab focuses on performing transformations using Synapse Dataflows, optimizing data flows using partitioning, and managing dynamic source schema changes using schema drifting. Recipe 1 - Copying data using a Synapse data flow. Recipe 2 - Performing data transformation using activities such as join, sort, and filter. Recipe 3 - Monitoring data flows and pipelines. Recipe 4 - Configuring partitions to optimize data flows. Recipe 5 - Parameterizing mapping data flows. Recipe 6 - Handling schema changes dynamically in data flows using schema drift [[Source code](../03-procesing/azure-synapse-analytics/lab-azure-synapse-dataflows)]
* [ ] Implementing the Serving Layer Star Schema - In this lab, we will learn about implementing the serving layer, which involves implementing star schemas, techniques to read and write different data formats, sharing data between services such as SQL and Spark, and more. Once you complete this lab, you should be able to understand the differences between a Synapse dedicated SQL pool versus traditional SQL systems for implementing the Star schema, the various ways of accessing Parquet data using technologies such as Spark and SQL, and the details involved in storing metadata across services. All this knowledge should help you build a practical and maintainable serving layer in a data lake. Recipe 1 - Delivering data in a relational star schema. Recipe 2 - Implementing a dimensional hierarchy. Recipe 3 - Delivering data in Parquet files. Recipe 4 - Maintaining metadata [[Source code](../03-procesing/azure-synapse-analytics/lab-implementing-star-schema)]
* [ ] Getting started with Apache Beam [[source code](../03-processing/beam/lab-getting-started-with-beam)]
* [ ] MapReduce in Beam using Python [[source code](../03-processing/beam/lab-gcp-beam-mapreduce)]
* [ ] Building a Cybersecurity Lakehouse for CrowdStrike Falcon Events in Databricks [[source code](../03-processing/databricks/lab-cybersecurity-databricks)]
* [ ] Databricks AWS Integration and Clickstream Analysis [[source code](../03-processing/databricks/lab-databricks-clickstream)]
* [ ] Create an elementary Data Lakehouse using Databricks and the Delta lake technology [[source code](../03-processing/databricks/lab-databricks-deltalake)]
* [ ] Delta Lake Optimizations [[source code](../03-processing/databricks/lab-deltalake-optimizations)]
* [ ] Compare dbt and Delta Live Tables (dlt) for data transformation [[source code](../03-processing/databricks/lab-dlt-dbt)]
* [ ] Unlocking the Power of Health Data With a Modern Data Lakehouse [[source code](../03-processing/databricks/lab-healthcare-databricks)]
* [ ] Real-time Health Tracking and Monitoring System [[source code](../03-processing/databricks/lab-iot-health-tracker)]
* [ ] Simplifying Data Engineering and Analytics with Delta [[source code](../03-processing/databricks/lab-loan-application)]
* [ ] Real-Time Point-of-Sale Analytics With the Data Lakehouse [[source code](../03-processing/databricks/lab-retail-pos-databricks)]
* [ ] Data Engineering with Databricks [[source code](../03-processing/databricks/project-databricks-de)]
* [ ] Data Engineer Learner Path with Databricks [[source code](../03-processing/databricks/project-learnerbricks)]
* [ ] Advanced Data Engineering with Databricks [[source code](../03-processing/databricks/project-advancedbricks)]
* [ ] Databricks PySpark Ecommerce Data Processing Case Study [[source code](../03-processing/databricks/project-bedbricks)]
* [ ] Data Pipeline with Databricks PySpark and Superset [[source code](../03-processing/databricks/project-databricks-superset)]
* [ ] dbt Postgres on Jaffle Shop data [[source code](../03-processing/dbt/lab-jaffle-shop)]
* [ ] dbt Snowflake on Knoema data [[source code](../03-processing/dbt/lab-knoema)]
* [ ] dbt Postgres on NYC Taxi data [[source code](../03-processing/dbt/lab-nyctaxi)]
* [ ] dbt Postgres on Olist Retail data [[source code](../03-processing/dbt/lab-olist)]
* [ ] dbt BigQuery on Stack Exchange data [[source code](../03-processing/dbt/lab-stackexchnge)]
* [ ] Building an ELT Pipeline with dbt and Amazon Redshift on TICKIT data [[source code](../03-processing/dbt/lab-tickit)]
* [ ] dbt Snowflake on TPCH data [[source code](../03-processing/dbt/lab-tpch)]

### Processing Layer - Stream Data Processing

* [ ] Apache Druid Fundamentals [[link to note](../03-processing/druid/README.md)]
* [ ] Real-time Taxi Price Model based Prediction using Flink [[source code](../03-processing/flink/lab-taxi-pricing)]
* [ ] Real-time Twitter Stream Wordcount using Flink [[source code](../03-processing/flink/lab-twitter-stream-processing)]
* [ ] Build a simple Dataflow Pipeline (Python) [[source code](../03-processing/dataflow/lab-gcp-dataflow-pipeline.md)]
* [ ] Batch Analytics Pipelines with Cloud Dataflow (Python) [[source code](../03-processing/dataflow/lab-gcp-dataflow-batch-pipeline.md)]
* [ ] Providing Side Inputs in Dataflow (Python) [[source code](../03-processing/dataflow/lab-gcp-dataflow-side-inputs.md)]
* [ ] Using Dataflow for Streaming Analytics (Python) [[source code](../03-processing/dataflow/lab-gcp-dataflow-stream-pipeline.md)]
* [ ] Writing an ETL Pipeline using Apache Beam and Cloud Dataflow (Python) [[source code](../03-processing/dataflow/lab-gcp-serverless-dataflow.md)]
* [ ] ETL Processing on Google Cloud Using Dataflow and BigQuery [[source code](../03-processing/dataflow/lab-dataflow-bigquery-etl.md)]

### Processing Layer - Unified Data Processing

### Workflow Orchestration

* [ ] Copying BigQuery Tables Across Different Locations using Cloud Composer [[source code](../02-storage/warehouses/bigquery/lab-gcp-bigquery-composer)]

### Visualization

### DevOps

### Data Science & Machine Learning

### Capstone Projects

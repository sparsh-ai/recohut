# Data Engineering Bootcamp

**Hit the ⭐️ button if you like the repo.**

## Level 100

**Estimated Time:** 55 hours

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

* [ ] Ingest data from CSV file into MySQL database table [[source code](02-storage/databases/mysql/lab-data-ingestion-to-mysql)]
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
* [ ] Lab - Exchange Rate ETL process [[source code](01-foundations/language/python/lab-exchange-rate-etl)]

### Programming - PySpark

* [ ] Create databricks account
* [ ] Create your first databricks cluster
* [ ] Create your first databricks notebook
* [ ] M&M color balls analysis with PySpark
* [ ] Movielens and Song analysis with PySpark
* [ ] San Francisco Fire Department call analysis with PySpark
* [ ] Connect AWS to PySpark and build an ETL pipeline [[source code](03-processing/databricks/lab-databricks-pyspark-s3)]

### Programming - Scala

* [ ] Introduction to Scala programming
* [ ] Getting started with Spark Scala
* [ ] Building extract and load pipeline with Scala, S3 and Postgres [[source code](03-processing/databricks/lab-databricks-scala-postgres-s3)]

### Data Modeling and Warehousing

* [ ] Building a sql data model for a music company in Postgres
* [ ] Building a nosql data model for a music company in Cassandra
* [ ] Difference between databases, warehouses, lakes and lakehouses
* [ ] OLTP vs OLAP technologies
* [ ] Loading data into Redshift warehouse with S3 staging and COPY command

### Data Lakes and Lakehouses

* [ ] Building a data lake for a healthcare company with AWS, S3 and Athena [[source code](02-storage/datalakes/lab-datalake-healthcare-s3-glue-athena)]
* [ ] Working with AWS S3 and Delta lake in Databricks

### Big Data Processing

* [ ] Creating and Monitoring Production Data Processing Jobs in Databricks
* [ ] Creating and submitting Word count Spark Job in EMR Serverless
* [ ] Building a near real-time serverless data pipeline with AWS lambda function [[source code](03-processing/aws-lambda-function/lab-lambda-csv-parquet)]
* [ ] Building an ELT pipeline for a cab service company using dbt and Postgres

### Orchestration and Data Pipelines

* [ ] Getting started with Airflow - Install Airflow in local system, Starting Airflow Web server and Scheduler, Building a BASH commands execution pipeline in Airflow, Building a CSV to JSON pipeline in Airflow [[source code](06-orchestration/airflow/lab-airflow-getting-started)]
* [ ] Integrate email notifications in Airflow with AWS SNS/SES service [[source code](06-orchestration/airflow/lab-airflow-email-notifications)]

### Capstone Projects

* [ ] ACLED ETL Data Pipeline for war and conflict analysis (Airflow, Postgres, Glue, Spark) [[source code](12-capstones/acled)]
* [ ] Sales & Orders ELT Data Pipeline (dbt, Redshift, SQL, Jinja) [[source code](12-capstones/dbt-redshift)]

## Level 200

**Estimated Time:** 75 hours

### Language - SQL

* [ ] Postgres SQL basics to advanced [[source code](01-foundations/language/sql/lab-postgres-queries)]
* [ ] Running Dates, String and Advanced queries in Postgres on Sales data [[source code](02-storage/databases/postgres/lab-postgres-sales)]
* [ ] Working with Book dataset on SQLite database [[source code](02-storage/databases/sqlite/lab-sqlite-basics)]

### Language - Python

* [ ] ETL process and reading/writing CSV, JSON and XML files in pandas [[source code](01-foundations/language/python/lab-etl-csv-json-xml)]

### Storage Layer - Flat Files

* [ ] Introduction to various file formats - CSV, Parquet, JSON, Avro, and ORC [[link to note](02-storage/flat-files/README.md)]
* [ ] Processing JSON data in Python [[source code](02-storage/flat-files/lab-processing-json-data)]

### Storage Layer - Databases

* [ ] Configuring and Securing Azure SQL Database - This lab covers configuring a Serverless SQL database, Hyperscale SQL database, and securing Azure SQL Database using virtual networks and private links. Recipe 1 - Provisioning and connecting to an Azure SQL database using PowerShell. Recipe 2 - Implementing an Azure SQL Database elastic pool using PowerShell [[source code](02-storage/databases/azure-sql/lab-securing-azure-sql-databases)]
* [ ] Load CSV data from on-premise to GCP CloudSQL [[source code](02-storage/databases/cloudsql/lab-gcp-cloudsql-nyctaxi)]
* [ ] db2 BookShop and PetSale Data Ingestion and Stored Procedure [[source code](02-storage/databases/db2/lab-dbt-bookshop-petsale-data-ingestion)]
* [ ] OLAP Analytics on bank, TPCH and NYC Taxi datasets using DuckDB [[source code](02-storage/databases/duckdb/lab-analytics-bank-tpch-nyctaxi)]
* [ ] Getting started with Postgres and Python [[source code](02-storage/databases/postgres/lab-postgres-getting-started)]
* [ ] Use bash shell commands to extract, transform and load data into Postgres [[source code](02-storage/databases/postgres/lab-bash-etl)]
* [ ] Extract and load food data into Postgres using Python [[source code](02-storage/databases/postgres/lab-extract-and-load-food-data)]
* [ ] Build a database for crime reports in Postgres [[source code](02-storage/databases/postgres/lab-postgres-crime-reports)]

### Storage Layer - NoSQL Databases

* [ ] Streaming Data Processing - Streaming Data Pipelines into GCP Bigtable [[source code](02-storage/nosql-databases/bigtable/lab-gcp-streaming-bigtable)]
* [ ] Fundamentals of Apache Cassandra  [[link to note](02-storage/nosql-databases/cassandra/README.md)]
* [ ] Setup Cassandra in local system [[source code](02-storage/nosql-databases/cassandra/lab-getting-started-with-cassandra)]
* [ ] Getting started with Cassandra [[source code](02-storage/nosql-databases/cassandra/lab-getting-started-with-cassandra)]
* [ ] Cassandra on Cloud with Amazon Keyspaces [[source code](02-storage/nosql-databases/cassandra/lab-amazon-keyspaces)]
* [ ] Fundamentals of DynamoDB [[link to note](02-storage/nosql-databases/dynamodb/README.md)]
* [ ] Getting started with MongoDB [[source code](02-storage/nosql-databases/mongodb/lab-mongodb-basics)]

### Storage Layer - Data Warehouses

* [ ] Amazon Athena Basics [[link to note](02-storage/warehouses/athena/README.md)]
* [ ] Building Federated Query System using Amazon Athena [[source code](02-storage/warehouses/athena/project-athena-federated)]
* [ ] GCP BigQuery Basics [[link to note](02-storage/warehouses/bigquery/README.md)]
* [ ] Using BigQuery to do analysis [[source code](02-storage/warehouses/bigquery/lab-bigquery-analysis)]
* [ ] Bigquery basics command line operations [[source code](02-storage/warehouses/bigquery/lab-bigquery-commandline)]
* [ ] Creating a Data Warehouse Through Joins and Unions [[source code](02-storage/warehouses/bigquery/lab-bigquery-data-warehousing)]
* [ ] Build and Optimize Data Warehouses with BigQuery [[source code](02-storage/warehouses/bigquery/lab-bigquery-optimization)]
* [ ] Optimizing your BigQuery Queries for Performance [[source code](02-storage/warehouses/bigquery/lab-bigquery-query-optimization)]
* [ ] Building a BigQuery Data Warehouse [[source code](02-storage/warehouses/bigquery/lab-biqeury-building-warehouse)]
* [ ] Predict Visitor Purchases with a Classification Model in BigQuery ML [[source code](02-storage/warehouses/bigquery/lab-gcp-bigquery-ml)]
* [ ] NYC Cab Prediction Model in BigQuery ML [[source code](02-storage/warehouses/bigquery/lab-gcp-bigquery-nyctaxi)]
* [ ] Copy data from S3 into Amazon Redshift [[source code](02-storage/warehouses/redshift/lab-copy-from-s3)]
* [ ] Create, Train and Deploy Multi Layer Perceptron (MLP) models using Amazon Redshift ML [[source code](02-storage/warehouses/redshift/lab-redshift-ml)]
* [ ] Connect and Query Redshift with Python [[source code](02-storage/warehouses/redshift/lab-redshift-python)]
* [ ] Implement a slowly changing dimension in Amazon Redshift [[source code](02-storage/warehouses/redshift/lab-redshift-scd)]
* [ ] Load NYC Taxi csv data into Redshift using Python AWS Data Wrangler [[source code](02-storage/warehouses/redshift/lab-redshift-taxi)]
* [ ] Advanced Data Analytics on TPCH Sales data in Redshift [[source code](02-storage/warehouses/redshift/project-redshift-sales)]

### Storage Layer - Data Lakes and Lakehouses

* [ ] Working with S3 using Boto3 in Python [[source code](02-storage/datalakes/lab-s3-boto3)]
* [ ] Creating and Managing Data in Azure Data Lake [[source code](02-storage/datalakes/lab-adl-create-manage-data)]
* [ ] Securing and Monitoring Data in Azure Data Lake [[source code](02-storage/datalakes/lab-adl-securing-monitoring-lakes)]
* [ ] Introduction to Data Lakehouses - Delta, Iceberg and Hudi [[link to note](02-storage/lakehouses/README.md)]

### Serving Layer - SQL Data Modeling

* [ ] Build a Star Schema based Data Model in Postgres on the AirBnB dataset [[source code](04-serving/lab-airbnb-postgres-datamodel)]
* [ ] Car company Data Model in MySQL [[source code](04-serving/lab-cars-mysql-datamodel)]
* [ ] Create a star schema from 3NF schema on DVD rental Pagila dataset [[source code](04-serving/lab-dvd-rental-datamodel)]
* [ ] Create a Postgres data model of Google Playstore dataset [[source code](04-serving/lab-google-playstore-datamodel)]
* [ ] Inegi Snowflake Data Model [[source code](04-serving/lab-inegi-snowflake-datamodel)]
* [ ] Northwind Data Model in MySQL [[source code](04-serving/lab-mysql-northwind-datamodel)]
* [ ] Retail Store Data Model in MySQL [[source code](04-serving/lab-mysql-retail-store-datamodel)]
* [ ] Creating a Bus Rapid Transit (BRT) Database in Postgres [[source code](04-serving/lab-postgres-busrapid-transit)]
* [ ] Create Fact and Dimension Tables from Denormalized Raw Data [[source code](04-serving/lab-postgres-elt-datamodel)]
* [ ] Postgres e-Wallet Data Model [[source code](04-serving/lab-postgres-ewallet-datamodel)]
* [ ] Housing Data Model with CDC and SCD Type 2 [[source code](04-serving/lab-postgres-housing-cdc-scd)]
* [ ] Credit Debit Finance Data Model in Snowflake [[source code](04-serving/lab-snowflake-creditdebit-datamodel)]
* [ ] Sparkify Music Company Data Model in Postgres [[source code](04-serving/lab-sparkify-data-model-postgres)]

### Serving Layer - NoSQL Data Modeling

* [ ] Create a NoSQL Data Model for a Digital Music Library using Cassandra [[source code](02-storage/datalakes/lab-adl-securing-monitoring-lakes)]
* [ ] Create a NoSQL Data Model for an Email System using Cassandra [[source code](04-serving/cassandra-email-data-model)]
* [ ] Create a NoSQL Data Model for Hotel Reservations using Cassandra [[source code](04-serving/cassandra-hotel-reservations)]
* [ ] Create a NoSQL Data Model for Investment Accounts or Portfolios using Cassandra [[source code](04-serving/cassandra-investment-data-model)]
* [ ] Create a NoSQL Data Model for Temperature Monitoring Sensor Networks using Cassandra [[source code](04-serving/cassandra-sensor-data-model)]
* [ ] Create a NoSQL Data Model for Online Shopping Carts using Cassandra [[source code](04-serving/cassandra-shopping-cart-data-model)]
* [ ] Ingest Movies data into CouchDB database [[source code](02-storage/nosql-databases/couchdb/lab-couchdb-movies-data-migration)]

### Processing Layer - Batch Data Processing

* [ ] Data Transformation with PySpark using Amazon EMR Serverless Application [[source code](03-processing/aws-emr/lab-emr-serverless)]
* [ ] Advanced Data Engineering and Data Processing with AWS Glue Jobs [[source code](03-processing/aws-glue/lab-glue-advanced)]
* [ ] Handle UPSERT data operations using open-source Delta Lake and AWS Glue [[source code](03-processing/aws-glue/lab-glue-deltalake-cdc-upsert)]
* [ ] Create your own reusable visual transforms for AWS Glue Studio [[source code](03-processing/aws-glue/lab-glue-studio-custom-transforms)]
* [ ] Tickets ETL with Glue Studio [[source code](03-processing/aws-glue/lab-glue-studio-tickets)]
* [ ] CSV to Parquet Transformation with Glue Studio [[source code](03-processing/aws-glue/lab-csv-to-parquet-conversion)]
* [ ] Processing Data Using Azure Databricks - Configuring the Azure Databricks environment, Integrate Databricks with Azure Key Vault, Mounting an Azure Data Lake container in Databricks, Processing data using notebooks, Scheduling notebooks using job clusters, Working with Delta Lake tables [[source code](03-processing/azure-databricks/lab-data-processing-azure-dbr)]
* [ ] Build Data Pipeline with HDInsight [[source code](03-processing/azure-hdinsight/lab-simple-data-processing)]
* [ ] Processing Data Using Azure Synapse Analytics - This lab covers exploring data using Synapse Serverless SQL pool, processing data using Synapse Spark Pools, Working with Synapse Lake database, and integrating Synapse Analytics with Power BI. Recipe 1 - Provisioning an Azure Synapse Analytics workspace. Recipe 2 - Analyzing data using serverless SQL pool. Recipe 3 - Provisioning and configuring Spark pools. Recipe 4 - Processing data using Spark pools and a lake database. Recipe 5 - Querying the data in a lake database from serverless SQL pool. Recipe 6 - Scheduling notebooks to process data incrementally [[Source code](03-procesing/azure-synapse-analytics/lab-data-processing-synapse-analytics)]
* [ ] Transforming Data Using Azure Synapse Dataflows - This lab focuses on performing transformations using Synapse Dataflows, optimizing data flows using partitioning, and managing dynamic source schema changes using schema drifting. Recipe 1 - Copying data using a Synapse data flow. Recipe 2 - Performing data transformation using activities such as join, sort, and filter. Recipe 3 - Monitoring data flows and pipelines. Recipe 4 - Configuring partitions to optimize data flows. Recipe 5 - Parameterizing mapping data flows. Recipe 6 - Handling schema changes dynamically in data flows using schema drift [[Source code](03-procesing/azure-synapse-analytics/lab-azure-synapse-dataflows)]
* [ ] Implementing the Serving Layer Star Schema - In this lab, we will learn about implementing the serving layer, which involves implementing star schemas, techniques to read and write different data formats, sharing data between services such as SQL and Spark, and more. Once you complete this lab, you should be able to understand the differences between a Synapse dedicated SQL pool versus traditional SQL systems for implementing the Star schema, the various ways of accessing Parquet data using technologies such as Spark and SQL, and the details involved in storing metadata across services. All this knowledge should help you build a practical and maintainable serving layer in a data lake. Recipe 1 - Delivering data in a relational star schema. Recipe 2 - Implementing a dimensional hierarchy. Recipe 3 - Delivering data in Parquet files. Recipe 4 - Maintaining metadata [[Source code](03-procesing/azure-synapse-analytics/lab-implementing-star-schema)]
* [ ] Getting started with Apache Beam [[source code](03-processing/beam/lab-getting-started-with-beam)]
* [ ] MapReduce in Beam using Python [[source code](03-processing/beam/lab-gcp-beam-mapreduce)]
* [ ] Building a Cybersecurity Lakehouse for CrowdStrike Falcon Events in Databricks [[source code](03-processing/databricks/lab-cybersecurity-databricks)]
* [ ] Databricks AWS Integration and Clickstream Analysis [[source code](03-processing/databricks/lab-databricks-clickstream)]
* [ ] Create an elementary Data Lakehouse using Databricks and the Delta lake technology [[source code](03-processing/databricks/lab-databricks-deltalake)]
* [ ] Delta Lake Optimizations [[source code](03-processing/databricks/lab-deltalake-optimizations)]
* [ ] Compare dbt and Delta Live Tables (dlt) for data transformation [[source code](03-processing/databricks/lab-dlt-dbt)]
* [ ] Unlocking the Power of Health Data With a Modern Data Lakehouse [[source code](03-processing/databricks/lab-healthcare-databricks)]
* [ ] Real-time Health Tracking and Monitoring System [[source code](03-processing/databricks/lab-iot-health-tracker)]
* [ ] Simplifying Data Engineering and Analytics with Delta [[source code](03-processing/databricks/lab-loan-application)]
* [ ] Real-Time Point-of-Sale Analytics With the Data Lakehouse [[source code](03-processing/databricks/lab-retail-pos-databricks)]
* [ ] Data Engineering with Databricks [[source code](03-processing/databricks/project-databricks-de)]
* [ ] Data Engineer Learner Path with Databricks [[source code](03-processing/databricks/project-learnerbricks)]
* [ ] Advanced Data Engineering with Databricks [[source code](03-processing/databricks/project-advancedbricks)]
* [ ] Databricks PySpark Ecommerce Data Processing Case Study [[source code](03-processing/databricks/project-bedbricks)]
* [ ] Data Pipeline with Databricks PySpark and Superset - You’ll build a modern, cloud-based, three-layer data Lakehouse - First, you’ll set up your workspace on the Databricks platform, leveraging important Databricks features, before pushing the data into the first two layers of the data lake - Next, using Apache Spark, you’ll build the third layer, used to serve insights to different end-users - Then, you’ll use Delta Lake to turn your existing data lake into a Lakehouse - Finally, you’ll deliver an infrastructure that allows your end-users to perform specific queries, using Apache Superset, and build dashboards on top of the existing data [[source code](03-processing/databricks/project-databricks-superset)]
* [ ] dbt Postgres on Jaffle Shop data [[source code](03-processing/dbt/lab-jaffle-shop)]
* [ ] dbt Snowflake on Knoema data [[source code](03-processing/dbt/lab-knoema)]
* [ ] dbt Postgres on NYC Taxi data [[source code](03-processing/dbt/lab-nyctaxi)]
* [ ] dbt Postgres on Olist Retail data [[source code](03-processing/dbt/lab-olist)]
* [ ] dbt BigQuery on Stack Exchange data [[source code](03-processing/dbt/lab-stackexchnge)]
* [ ] Building an ELT Pipeline with dbt and Amazon Redshift on TICKIT data [[source code](03-processing/dbt/lab-tickit)]
* [ ] dbt Snowflake on TPCH data [[source code](03-processing/dbt/lab-tpch)]
* [ ] Creating a Data Transformation Pipeline with Cloud Dataprep [[source code](03-processing/gcp-dataprep/lab-gcp-dataprep)]
* [ ] Running Apache Spark jobs on Cloud Dataproc [[source code](03-processing/gcp-dataproc/lab-gcp-dataproc)]
* [ ] Churn Analytics Demo with dbt Snowpark Python models [[source code](03-processing/snowpark/churnpark)]
* [ ] Getting started with dbt and Snowpark [[source code](03-processing/snowpark/dbtsnowpy)]
* [ ] FIFA prediction model with dbt and Snowpark [[source code](03-processing/snowpark/fifapark)]
* [ ] Jaffle shop analytics modeling with dbt and Snowpark [[source code](03-processing/snowpark/jafflepark)]
* [ ] Knoema Regression with dbt Snowpark and Streamlit [[source code](03-processing/snowpark/knoema-regression)]

### Processing Layer - Stream and Unified Data Processing

* [ ] Apache Druid Fundamentals [[link to note](03-processing/druid/README.md)]
* [ ] Real-time Taxi Price Model based Prediction using Flink [[source code](03-processing/flink/lab-taxi-pricing)]
* [ ] Real-time Twitter Stream Wordcount using Flink [[source code](03-processing/flink/lab-twitter-stream-processing)]
* [ ] Build a simple Dataflow Pipeline (Python) [[source code](03-processing/dataflow/lab-gcp-dataflow-pipeline.md)]
* [ ] Batch Analytics Pipelines with Cloud Dataflow (Python) [[source code](03-processing/dataflow/lab-gcp-dataflow-batch-pipeline.md)]
* [ ] Providing Side Inputs in Dataflow (Python) [[source code](03-processing/dataflow/lab-gcp-dataflow-side-inputs.md)]
* [ ] Using Dataflow for Streaming Analytics (Python) [[source code](03-processing/dataflow/lab-gcp-dataflow-stream-pipeline.md)]
* [ ] Writing an ETL Pipeline using Apache Beam and Cloud Dataflow (Python) [[source code](03-processing/dataflow/lab-gcp-serverless-dataflow.md)]
* [ ] ETL Processing on Google Cloud Using Dataflow and BigQuery [[source code](03-processing/dataflow/lab-dataflow-bigquery-etl.md)]
* [ ] Getting started with Kafka and CLI [[source code](03-processing/kafka/lab-kafka-cli)]
* [ ] Getting started with Kafka and Python [[source code](03-processing/kafka/lab-kafka-python)]
* [ ] Getting started with Confluent Kafka and Python [[source code](03-processing/kafka/lab-confluent-python)]
* [ ] Real-time CDC-enabled Extract and Load Pipeline with Kafka on Cloud [[source code](03-processing/kafka/lab-confluent-kafka-faker)]
* [ ] Real-time fraud detection by applying filter in Kafka topic [[source code](03-processing/kafka/lab-kafka-fraud-detection)]
* [ ] Kafka Streams for NYC Taxi data [[source code](03-processing/kafka/lab-kafka-nyctaxi)]
* [ ] Kafka on Cloud with Amazon ECS and Container Orchestration [[source code](03-processing/kafka/lab-kafka-python-ecs)]
* [ ] Realtime Streaming analytics with Apache Kafka and Spark Streaming [[source code](03-processing/kafka/lab-kafka-spark-streaming)]
* [ ] Stock Market Kafka Real Time [[source code](03-processing/kafka/lab-kafka-stock-market)]
* [ ] Data Streaming Pipeline with Kafka for livetolldata [[source code](03-processing/kafka/lab-kafka-toll-analysis)]
* [ ] Building an event-driven IKEA app with Kafka [[source code](03-processing/kafka/project-ikea)]
* [ ] Real Time Apache Log Analytics with Kinesis [[source code](03-processing/kinesis/lab-kinesis-apache-logs)]
* [ ] Real-Time Clickstream Anomaly Detection with Kinesis [[source code](03-processing/kinesis/lab-kinesis-clickstream-anomaly)]
* [ ] Streaming Data Pipelines with GCP PubSub [[source code](03-processing/pubsub/lab-gcp-pubsub-processing.md)]
* [ ] Publish Streaming Data into PubSub [[source code](03-processing/pubsub/lab-gcp-pubsub.md)]
* [ ] Log Analytics and Processing in Real-Time (Apache Flink, Beam, Amazon Kinesis Data Analytics) [[source code](12-capstones/kinesis-flink-beam)]
* [ ] Streaming ETL pipeline with Apache Flink and Amazon Kinesis Data Analytics [[source code](12-capstones/kinesis-flink-etl)]

### Data Extraction

* [ ] Extract data using API from archive.org [[source code](03-processing/pubsub/lab-gcp-pubsub.md)]
* [ ] Extract data using API from dummyjson [[source code](05-extraction/api/lab-dummyjson)]
* [ ] Extract data using API from exchangerates [[source code](05-extraction/api/lab-exchangerates)]
* [ ] Extract data using API from coinmarketcap [[source code](05-extraction/api/lab-extract-coinmarketcap)]
* [ ] Extract data using API from opennotify [[source code](05-extraction/api/lab-extract-opennotify)]
* [ ] Extract data using API from git [[source code](05-extraction/api/lab-processing-rest-payloads-git)]
* [ ] Extract data using API from saveonfoods [[source code](05-extraction/api/lab-saveonfoods)]
* [ ] Extract data using API from twitter [[source code](05-extraction/api/lab-twitter)]
* [ ] Extract data using API from datausa [[source code](05-extraction/api/lab-uspopulation)]
* [ ] Extract data using API from git and Hacker News [[source code](05-extraction/api/lab-hackernews-git-api)]
* [ ] Extract synthetic data using Faker library in python [[source code](05-extraction/faker/lab-generate-data-with-faker)]
* [ ] Extract data using Web Scraping from Finance websites [[source code](05-extraction/webscraping/lab-finance-extract-load)]

### Workflow Orchestration

* [ ] Copying BigQuery Tables Across Different Locations using Cloud Composer [[source code](02-storage/warehouses/bigquery/lab-gcp-bigquery-composer)]
* [ ] Bike Sharing Service Data Pipeline using Cloud Composer [[source code](06-orchestration/airflow/lab-bike-sharing-service-pipeline)]
* [ ] Forex ETL with Airflow [[source code](06-orchestration/airflow/lab-forex-etl)]
* [ ] Building an Airflow ETL pipeline to pull NFT data from Github and store in SQLite database [[source code](06-orchestration/airflow/github-nft)]
* [ ] IMDB Spark ETL - Build a data pipeline that download data, process it, calculate the hight profit movies and save the processed data into Postgres database [[source code](06-orchestration/airflow/lab-imdb-spark-etl)]
* [ ] Building Data Ingestion Pipelines using Azure Data Factory - This lab covers ingesting data using Azure Data Factory and copying data between Azure SQL Database and Azure Data Lake. Recipe 1 - Provisioning Azure Data Factory. Recipe 2 - Copying files to a database from a data lake using a control flow and copy activity. Recipe 3 - Triggering a pipeline in Azure Data Factory. Recipe 4 - Copying data from a SQL Server virtual machine to a data lake using the Copy data wizard [[Source code](06-orchestration/azure-data-factory/lab-data-ingestion-pipeline)]
* [ ] Incremental Data Loading using Azure Data Factory - This lab covers various methods to perform data loading in incremental fashion. Recipe 1 - Using Watermarking. Recipe 2 - Using File Timestamps. Recipe 3 - Using File partitions and folder structures [[Source code](06-orchestration/azure-data-factory/lab-adf-incremental-loading)]
* [ ] Assignment - Build ETL Pipeline in Airflow using Toll data [[source code](06-orchestration/airflow/lab-tolldata)]
* [ ] Develop Batch Processing Solution using Azure Data Factory - In this lab, we design an end-to-end batch processing solution by using Data Factory, Data Lake, Spark, Azure Synapse Pipelines, PolyBase, and Azure Databricks. Recipe 1 - Data Ingestion using Data Flow. Recipe 2 - Data Transformation using Azure Databricks. Recipe 3 - Data Serving using PolyBase. Recipe 4 - Data Pipeline using Azure Data Factory Pipeline. Recipe 5 - End to end data processing with Azure Batch [[Source code](06-orchestration/azure-data-factory/lab-batch-processing-solution)]
* [ ] Building and Executing a Pipeline Graph with Data Fusion [[source code](06-orchestration/datafusion/lab-datafusion-pipeline)]
* [ ] Prefect Getting Started [[source code](06-orchestration/prefect/lab-prefect-getting-started)]
* [ ] Athena Query Orchestration with AWS Step Functions with SNS notifications [[source code](06-orchestration/stepfunctions/lab-stepfunction-athena-sns)]
* [ ] AWS Step Functions and Amazon SQS to design and run a serverless workflow that orchestrates a message queue-based microservice [[source code](06-orchestration/stepfunctions/lab-stepfunction-ecomm-sqs)]

### Visualization

* [ ] Streaming Analytics and Dashboards - Connect to a BigQuery data source, Create reports and charts to visualize BigQuery data [[source code](08-visualization/looker-studio/lab-gcp-streaming-analytics.md)]

### DevOps

* [ ] Introduction to Infra-as-code [[link to note](07-devops/infra-as-code.md)]
* [ ] Introduction to Dockers [[link to note](07-devops/docker/README.md)]
* [ ] Deploy docker in Amazon ECS [[source code](07-devops/ecs/lab-deploy-simple-docker-ecs)]
* [ ] Create and managing Cloudformation stacks with AWS CLI [[source code](07-devops/cloudformation)]
* [ ] Building your first FastAPI application [[source code](07-devops/fastapi/lab-simple-api)]
* [ ] Building FastAPI application and Dockerize it [[source code](07-devops/fastapi/lab-simple-api-docker)]
* [ ] FastAPI applications - Online Academic Discussion Forum API, Online Book Reselling System API, Auction System, ERP System, Todo App, Task Planner System, Fitness Club Management System API, NewsStand Manegement System API, Poverty Analysis System API, Online Recipe System API, Online Restaurant Review System API, Intelligent Tourist System API [[source code](07-devops/fastapi/README.md)]
* [ ] FastAPI DevOps - In this lab, we will build and deploy a FastAPI. We will deploy it in a serverless manner using AWS's SAM (Serverless Application Model) framework. We will also use Cloudformation stack to automate the pipeline CICD [[source code](07-devops/fastapi/lab-fastapi-devops)]
* [ ] Build and deploy NodeJS Kubia app in Kubernetes [[source code](07-devops/kubernetes/lab-kubernetes-kubia-app)]
* [ ] Build Address parsing system in python and dockerize it [[source code](07-devops/docker/lab-assignment-etl-docker)]

### Data Science & Machine Learning

* [ ] Basics of Regression and Classification models on Tabular data
* [ ] Getting started with NLP Deep Learning - Text Classification, Topic Modeling, Chatbots, Language Modeling, Named Entity Recognition, Text Clearning, Text Embedding, Text Generation, Text Similarity, Text Summarization, Transformers, Word2vec
* [ ] Getting started with Computer Vision Deep Learning - Face Detection and Recognition, Image Classification, Image Similairty, Image Segmentation, Object Detection, Pose Estimation, Object Tracking, Scene Text Recognition, Video Classification, Video Action Recognition
* [ ] Getting started with Recommender Systems - Content-based Recommender Systems, Collaborative  Recommender Systems, Hybrid Recommender Systems, Session-based Recommender Systems, Candidate Retrieval Model, Scoring and Ranking Model

### Capstone Projects

* [ ] Building End to end data pipeline in AWS - Activity 1: Ingestion with DMS, Activity 2: Data Lake Hydration, Activity 3: DMS Migration, Activity 4: Transforming data with Glue - Data Validation and ETL, Activity 5: Query and Visualize [[source code](12-capstones/cloudmaze)]
* [ ] Funflix - You are working as a data engineer in an Australian media company Funflix. You got the following requirements and tasks to solve. 1 - Design the data warehouse for Funflix. 2 - Build and deploy the data pipeline for Funflix's multi-region business. 3 - Build a data lake [[source code](12-capstones/funflix)]
* [ ] Datalake Schema Correction (AWS S3, Glue, Athena) [[source code](12-capstones/hmc)]
* [ ] Kortex - In this Capstone project, you will: 1. Design a data platform that uses MySQL as an OLTP database and MongoDB as a NoSQL database. 2. Design and implement a data warehouse and generate reports from the data. 3. Design a reporting dashboard that reflects the key metrics of the business. 4. Extract data from OLTP, and NoSQL databases, transform it and load it into the data warehouse, and then create an ETL pipeline. 5. And finally, create a Spark connection to the data warehouse, and then deploy a machine learning model [[source code](12-capstones/kortex)]
* [ ] Movie Review Sentiment Analysis Pipeline - Build a pipeline that expresses the fact artist review sentiment and film review sentiment, based on the data provided by IMDb and TMDb [[source code](12-capstones/movie-sentiment)]
* [ ] Building Recommender System from Scratch - In this capstone, you will build 1. Front-end website built with Plotly Dash. 2. Clickstream data collection using Divolte pipeline. 3. Model building in python. 4. Recommendation Serving [[source code](12-capstones/recofront)]
* [ ] Reddit Submissions, Authors and Subreddits analysis - This project will use a sample of publicly available dump of Reddit and load it into a AWS Redshift warehouse so that Data Scientists can make use of the content and for example develop a recommender system that finds the most suitable subreddit for your purposes. The goal of this project is to create a Data Warehouse to analyze trending and new subreddits using Airflow. The project uses the Reddit API to get subreddits and stores them on AWS S3 in JSON format. Data processing happens on an EMR cluster on AWS using PySpark and processed data gets stored on AWS S3 in parquet format. Finally, the data gets inserted into AWS Redshift, gets denormalized to create fact and dimension tables [[source code](12-capstones/reddit)]
* [ ] Data Pipeline with dbt, Airflow and Great Expectations - In this project, we will learn how to combine the functions of three open source tools - Airflow, dbt and Great expectations - to build, test, validate, document, and orchestrate an entire pipeline, end to end, from scratch. We are going to load the NYC Taxi data into Redshift warehouse and then transform and validate the data using dbt and great expectations. By the end of this project, you’ll understand- The basics of dbt, Airflow, and Great Expectations - How to effectively combine these components to build a robust data pipeline - When and how to implement data validation using these tools - How to start developing a data quality strategy for your organization that goes beyond implementing data validation. And you’ll be able to - Write and run Airflow, dbt, and Great Expectations code - Design and implement a robust data pipeline - Implement data validation and alerting across a data pipeline [[source code](12-capstones/robust-data-pipeline)]
* [ ] Sparkify - In this capstone, you will build 1. SQL Data Modeling with Postgres, 2. NoSQL Data Modeling with Cassandra, 3. Data Lake with AWS and PySpark, 4. Data Warehouse with Redshift, 5. Data Pipeline with Airflow [[source code](12-capstones/spectrum)]
* [ ] US Immigration analysis and data pipeline - In this capstone, you will build - 1. Data Load into S3, 2. Data Preprocessing with PySpark, 3. Data Modeling and Warehousing with Amazon Redshift, 4. Advanced analytics using Python and Matplotlib and 5. Convert the whole process into an airflow pipeline [[source code](12-capstones/us-immigration)]
* [ ] CitiBike Trip Histories Data Pipeline - In this capstone, you will build an end-to-end data pipeline. Cloud: GCP, Data Lake (DL): GCS, Data Warehouse (DWH): BigQuery, Infrastructure as code (IaC): Terraform, Workflow orchestration: Airflow, Transforming data: DBT, and Data Visualization: Google Data Studio [[source code](12-capstones/citibike-trip-histories)]
* [ ] Global Historical Climatology Network Daily Data Pipeline - In this capstone, your goal is to build a global historical climatology network data pipeline that runs daily. Cloud: GCP, Infrastructure as code (IaC): Terraform, Workflow orchestration: Airflow (ingestion pipeline and transformation pipeline), Data Warehouse: BigQuery, Data Lake: GCS, Batch processing/Transformations: dbt cloud or DataProc/Spark (transformation pipeline), and Dashboard: Google Data Studio [[source code](12-capstones/climate)]

## Level 300


## How to Join

1. [Agency Partner 1](https://api.whatsapp.com/send?phone=919517720888&text=Hi%20Sowmya%20(WeHire)%0AI%20am%20interested%20in%20the%20data%20engineering%20training%20from%20Sparsh) (US & India only) - Pay for the training to the agency partner directly, vendor association required
2. [Agency Partner 2](https://api.whatsapp.com/send?phone=918484005449&text=Hi%20Vishwas%20(Wynisco)%0AI%20am%20interested%20in%20the%20data%20engineering%20training%20from%20Sparsh) (US & Canada only) - Pay after getting hired - 15% of your income for 1 year, directly to agency partner
3. [Direct](https://api.whatsapp.com/send?phone=918384805365&text=Hi%20Sparsh%0AI%20am%20interested%20in%20the%20data%20engineering%20training) - Directly hire me for 1:1 or 1:many training `@$25/hr`. E.g. 35-hr basic training in a batch of 15 would cost you `$58/-` (=25*35/15)

---

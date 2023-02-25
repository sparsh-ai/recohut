# Curriculum - Data Engineering Training (AWS)

## Foundations

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

### Data Engineering - Must Know Concepts

We will learn the basic concepts we should know as a data engineer. We will focus primarily on the following set of questions:

1. What is Data Engineering?
2. Role of Data Engineering in Organizations
3. Skills required to become a Data Engineer
4. What is data lake and data warehouse?
5. What is medallion architecture?
6. What is EL, ETL and ELT?
7. What are the benefits of cloud computing?
8. OLTP vs OLAP technologies

### AWS Cloud Essentials

**Tools**: AWS S3, RDS, Redshift, AWS Glue, Athena, AWS Lambda, EMR and EMR Serverless, Keyspace, Cloudformation, AWS IAM, Secrets Manager

**Concepts:** Cloud Computing and Data Engineering tools in Cloud

**Labs**

* [ ] (Optional) Create AWS Account
* [ ] Create IAM user and generate credentials
* [ ] Install AWS CLI
* [ ] Setup AWS credentials
* [ ] Walkthrough of various AWS Services
* [ ] Copy and Sync data to/from S3
* [ ] Create database in RDS DBMS and generate credentials
* [ ] Connect to RDS DBMS in DBeaver
* [ ] Pull credentials from Secrets Manager in Python using Boto3

### Programming

#### SQL

**Labs**

* [ ] SQL Basic - SELECT, LIMIT, WHERE, Comparison and Logical Operators, ORDER BY
* [ ] SQL Intermediate - Aggregation Functions, GROUP BY, CASE, JOINS
* [ ] SQL Advanced - Dates, Texts, Subqueries, Window Functions, EXPLAIN

#### Python

In this module, we will learn the essential python concepts we use in data engineering. We will primarily focus on the following topics:

1. Lists and dictionaries
2. For loops and while loops
3. Functions and Inline functions
4. Pandas Dataframes
5. `requests` library
6. `psycopg2` and `sqlalchemy` library

**Labs**

* [ ] Building Functions in Python
* [ ] Read/Write and Manipulate Data using Pandas
* [ ] Data Format Conversion - CSV to Parquet, JSON to CSV/Parquet
* [ ] Pulling Data from APIs using requests library
* [ ] Connect to Postgres and Redshift from Python
* [ ] Load and Read the data from Postgres using Python

#### PySpark

**Tools and Concepts**

1. Spark and Hadoop Fundamentals
2. Databricks
3. Spark UDFs
4. Spark Dataframe API

**Labs**

1. [ ] Create Databricks Account
2. [ ] Create Spark Cluster in Databricks
3. [ ] M&M Analysis
4. [ ] Movielens and Song Analysis
5. [ ] San Francisco Fire Department Analysis
6. [ ] Data Transformation with PySpark
7. [ ] Connect AWS to PySpark
8. [ ] ETL Pipeline with AWS S3 and PySpark

#### Scala

**Labs**

1. [ ] Introduction to Scala Programming
2. [ ] Transform complex data types
3. [ ] Extract and Load Process with Spark Scala, S3 and Postgres

## Storage Layer

### Flat Files

CSV, Parquet, TSV, Excel

### Databases

SQLite, MySQL, Postgres, RDS, DuckDB

### Data Warehouses

**Tools:** Redshift, Snowflake, Athena

**Labs**

* [ ] Loading Data into Redshift
* [ ] Queries in Redshift
* [ ] Loading Data into Snowflake
* [ ] Queries in Snowflake

### Data Lakes and Lakehouses

**Tools:** S3, Delta, Iceberg, Hudi

**Labs**

5. [ ] Data lake with AWS, S3 and Athena
6. [ ] Working with Delta lake in Databricks

### NoSQL Databases

**Tools:** Cassandra, MongoDB, DynamoDB, HBase, CouchDB, Keyspaces

### Data Catalogs

**Tools:** AWS Glue

## Serving Layer

### Data Modeling

#### SQL Data Modeling

**Tools and Concepts**

1. Data Modeling
2. SQL vs NoSQL
3. Star and Snowflake Schema
4. dbdiagram.io

**Labs**

1. [ ] Music Data Modeling with Postgres
2. [ ] Healthcare Data Modeling with Postgres
3. [ ] Building Data Model in Snowflake

#### NoSQL Data Modeling

* [ ] Music Data Modeling with Cassandra

## Processing Layer

### Batch Data Processing

**Tools**: EMR (Serverless), Databricks, Glue Studio, dbt, Lambda, Snowpark

**Concepts**: Spark and Hadoop, Spark Jobs, Big Data Processing, Clusters, Horizontal and Vertical Scaling

**Labs**

1. [ ] Processing data with EMR Serverless
2. [ ] Processing data using dbt in Snowflake
3. [ ] Processing data with Databricks
4. [ ] Building Serverless Pipeline in Lambda

#### Understanding Spark Query Execution

[Source code](../03-processing/01-batch/spark/lab-understand-spark-query-execution)

- Recipe 1 - Introduction to jobs, stages, and tasks
- Recipe 2 - Deep diving into schema inference
- Recipe 3 - Looking into the query execution plan
- Recipe 4 - How joins work in Spark
- Recipe 5 - Learning about input, output and shuffle partitions
- Recipe 6 - The storage benefits of different file types

### Streaming & Unified Data Processing

**Tools:** Kafka, Kinesis, Spark Streaming, Faust, Beam, Flink, Delta Live Tables, Debezium (CDC)

## Orchestration Layer

**Tools and Concepts**

1. Data Pipelines (ETL/ELT)
2. Apache Airflow
   1. UI
   2. Operators
   3. Variables
   4. Plugins
   5. Schedules
   6. etc.
3. Prefect
4. Step Functions
5. Modern Data Stack
6. AWS SNS and SES for Notifications

**Labs**

1. [ ] Install Airflow in your PC
2. [ ] First DAG/Pipeline - executing Bash commands
3. [ ] CSV to JSON ETL Pipeline
4. [ ] ACLED Data Pipeline
5. [ ] Sending Email notifications using SNS and SES

## Extraction Layer

### API Data Extraction

### Webscraping

### Synthetic Data Generation

## Governance

### Data Quality

**Tools:** Great Expectations

### Data Access Control

**Tools:** AWS IAM Roles and Policy Management, AWS Secrets Manager

## Visualization

* Superset/Preset
* Redash
* Streamlit
* Plotly Dash
* Looker Studio
* Quicksight

## DevOps

* Containerizarion with Docker
* Container Orchestration - Kubernetes, Docker Compose, ECS
* Build APIs with FastAPI
* CI/CD Pipelines with GitHub Actions, CodePipelines
* Infra-as-code (IaC) with AWS CloudFormation, Terraform, Ansible

## Data Science & Machine Learning

1. Regression and Classification
2. NLP and Computer Vision
3. Recommendation Systems - Personalize
4. MLOps - Sagemaker
5. PyTorch/Lightning, Tensorflow/Lite

## Capstone Projects

### Features

- We will build end-to-end projects with tools and concepts we learned and adopted in the training sessions.
- The project will be added in your resume.
- We will also release the project in your github. (Recruiters are interested in seeing your projects in git

### Basic

1. Forex
2. Git-NFT
3. Hipolabs Education API
4. Spotify Extract & Load Pipeline
5. Hackernews Git API Data Extraction
6. Bash ETL
7. ETL Docker
8. S3 Postgres Scala
9. Sakila
10. MySQL to S3 Incremental
11. ETL Assignment

### Intermediate

1. Lufthansa
2. ACLED
3. Robust Data Pipeline
4. IMDB Spark ETL
5. Toll Data Pipeline
6. Scoota ETL Pipeline
7. Dataflow BigQuery ETL
8. Railway API
9. Kinesis Flink ETL
10. Kinesis Flink Beam
11. SQS Postgres ETL
12. Disaster Response
13. Fireflow
14. Movies Data Migration
15. Star Jeans ETL
16. YouTube Insights
17. Mistplay Takehome

### Advanced

1. Movie Review Sentiment Analysis
2. Taxi Fare Prediction
3. Athena Federated
4. Funflix
5. Kortex
6. Cloudmaze
7. CityBike
8. Climate
9. Covid-19 Datalake
10. DigitalSkola
11. US Immigration
12. Datalake Schema Correction
13. Twitter Sentiment Realtime
14. Realtime Fraud Detection
15. Recofront
16. Reddit
17. Text-to-speech Data Pipeline
18. US Job Vacancies
19. Twitter Sentiment Glue
20. Klodars Datalake Design
21. Yammer
22. Patent Analytics
23. Spectrum
24. Sakila

## Interview Prep

* Mock Telephonic Rounds
* Assignments
* Mock Onsite Resume Discussion Round
* Mock Onsite System Design Round
* Mock Onsite Development Round

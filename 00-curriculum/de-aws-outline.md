# Curriculum - Data Engineering Training (AWS)

**Estimated Time:** 55 hours

- Getting Started

  - Create AWS Account
  - Install AWS CLI
  - Create IAM user and generate credentials
  - Setup AWS credentials
  - A quick overview of AWS services for data engineering
- Developer Foundations

  - VS Code
    - Download and Install vscode
    - Understand vscode features
    - Install extensions in vscode
  - Anaconda (Python)
    - Download and Install Anaconda
    - Create virtual environment in anaconda
    - Create jupyter notebook in vscode and connect to venv
  - Github
    - Create github account
    - Install git cli
    - Create git repo and add students as collaborator
    - Connect local workspace to git repo
    - Learn git commands
  - Bash
    - Learn bash commands
- Data Engineering Basics

  - What is Data Engineering?
  - Role of Data Engineering in Organizations
  - Skills required to become a Data Engineer
  - Data engineer versus data scientist
  - What is data lake and data warehouse?
  - What is medallion architecture?
  - What is EL, ETL and ELT?
  - What are the benefits of cloud computing?
  - Understanding what the cloud is
  - The difference between the cloud and non-cloud era
  - The on-demand nature of the cloud
  - OLTP vs OLAP technologies
- Programming

  - SQL
    - Query Types
    - Query Engines
    - SQL Basic
      - SELECT, LIMIT, WHERE
      - Comparison and Logical Operators
      - ORDER BY
    - SQL Intermediate
      - Aggregation Functions and GROUP BY
      - CASE
      - JOINS
    - SQL Advanced
      - Dates
      - Texts
      - Subqueries
      - Window Functions
    - Query Optimizations
  - Python
    - Lists and dictionaries
    - For loops and while loops
    - Functions and Inline functions
    - Pandas Dataframes
    - `requests` library
    - `psycopg2` and `sqlalchemy` library
    - Building Functions in Python
    - Read/Write and Manipulate Data using Pandas
    - Data Format Conversion - CSV to Parquet, JSON to CSV/Parquet
    - Pulling Data from APIs using requests library
    - Connect to Postgres and Redshift from Python
    - Load and Read the data from Postgres using Python
  - PySpark
    - Spark and Hadoop Fundamentals
    - Databricks
    - Spark UDFs
    - Spark Dataframe API
    - Create Databricks Account
    - Create Spark Cluster in Databricks
    - M&M Analysis
    - Movielens and Song Analysis
    - San Francisco Fire Department Analysis
    - Data Transformation with PySpark
    - Connect AWS to PySpark
    - ETL Pipeline with AWS S3 and PySpark
  - Scala
    - Introduction to Scala Programming
    - Transform complex data types
    - Extract and Load Process with Spark Scala, S3 and Postgres
- Data Modeling

  - SQL Data Modeling
    - Music Data Modeling with Postgres
    - Healthcare Data Modeling with Postgres
    - Building Data Model in Snowflake
  - NoSQL Data Modeling
    - Music Data Modeling with Cassandra
- AWS S3

  - Create S3 Bucket
  - List S3 Bucket
  - Copy and Sync data to/from S3
- AWS RDS

  - RDS Postgres
  - RDS MySQL
  - Create database in RDS DBMS and generate credentials
  - Connect to RDS DBMS in DBeaver
- AWS Secrets Manager

  - Create a Secret in Secrets Manager Vault
  - Pull credentials from Secrets Manager in Python using Boto3
  - Get the credential using AWS CLI
- Data Warehouse and Data Lakes

  - Data Warehouses vs Data Lakes
  - Data Lakes and Lakehouses
  - Loading Data into Redshift
  - Queries in Redshift
  - Data lake with AWS, S3 and Athena
  - Snowflake Data Warehousing
    - Loading Data into Snowflake
    - Queries in Snowflake
- Data Lakes and Lakehouses

  - Delta, Iceberg and Hudi
  - Working with Delta lake in Databricks
- Big Data Processing

  - Spark and Hadoop
  - Spark Jobs
  - Big Data Processing
  - Clusters
  - Horizontal and Vertical Scaling
  - Processing data using dbt in Snowflake
  - Processing data with Databricks
  - Processing data with EMR Serverless
  - Serverless Pipeline with AWS Lambda Function
- Orchestration Layer

  - Data Pipelines (ETL/ELT)
  - Apache Airflow
    - Common features
      - UI
      - Operators
      - Variables
      - Plugins
      - Schedules
    - Install Airflow in your PC
    - First DAG/Pipeline - executing Bash commands
    - CSV to JSON ETL Pipeline
  - AWS SNS and SES for Notifications
- Capstone Project - ACLED Data Pipeline

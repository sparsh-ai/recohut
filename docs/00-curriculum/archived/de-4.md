# Data Engineering Training

**Estimated Time:** 55 hours

### Developer Foundations

* [ ] Visual Studio Code (vscode) [[link to note](01-foundations/developer/vscode)]
  * [ ] Download and Install vscode
  * [ ] Understand vscode features
  * [ ] Install extensions in vscode
* [ ] Anaconda [[link to note](01-foundations/developer/anaconda)]
  * [ ] Download and Install Anaconda
  * [ ] Create virtual environment in anaconda
  * [ ] Create jupyter notebook in vscode and connect to venv
* [ ] Github [[link to note](01-foundations/developer/github)]
  * [ ] Create github account
  * [ ] Install git cli
  * [ ] Create git repo and add students as collaborator
  * [ ] Connect local workspace to git repo
  * [ ] Learn git commands
* [ ] Bash [[link to note](01-foundations/developer/bash)]
  * [ ] Starting bash terminal in vscode
  * [ ] Learn bash commands
* [ ] DBeaver [[link to note](01-foundations/developer/dbeaver)]
  * [ ] Download and Install DBeaver

### Data Engineering Foundations

* [ ] Data Engineering Must-to-know concepts [[link to note](01-foundations/basics/README.md)]
  * [ ] What is Data Engineering?
  * [ ] Role of Data Engineering in Organizations
  * [ ] Skills required to become a Data Engineer
  * [ ] Data engineer versus data scientist
  * [ ] What is data lake and data warehouse?
  * [ ] What is medallion architecture?
  * [ ] What is EL, ETL and ELT?
* [ ] Data Engineering most common interview questions [[link to note](01-foundations/basics/README.md)]

### AWS Cloud Essentials

* [ ] (Optional) Create AWS Account
* [ ] AWS Services Walkthrough

  * [ ] Storage Services - [S3](01-foundations/cloud/aws/s3.md), [RDS](01-foundations/cloud/aws/rds.md), Redshift, Keyspace
  * [ ] ETL Services - [Glue](01-foundations/cloud/aws/glue.md)
  * [ ] Compute Services - Lambda, EMR, [EC2](01-foundations/cloud/aws/ec2/README.md), Athena
  * [ ] DevOps Services - Cloudformation, [IAM](01-foundations/cloud/aws/iam/README.md), Secrets Manager
* [ ] GCP Services Walkthrough

  * [ ] Storage Services - GCS, Cloud SQL, BigQuery, BigTable
  * [ ] Compute Services - Cloud Functions, Dataproc, Cloud Compute, Dataflow
  * [ ] DevOps Services - IAM
* [ ] Azure Services Walkthrough

  * [ ] Storage Services - Blob Storge, DataLake Gen2 buckets, Azure SQL Databases
  * [ ] Compute Services - Databricks/Synapse Analytics, Azure Data Factory
  * [ ] DevOps Services - IAM
* [ ] AWS Account Setup [[source code](01-foundations/cloud/aws/lab-aws-setup)]

  * [ ] Install AWS CLI
  * [ ] Create IAM user and generate credentials
  * [ ] Setup AWS credentials
* [ ] AWS IAM Service [[source code](01-foundations/cloud/aws/iam/README.md)]

  * [ ] Create policies and roles
  * [ ] Attach policies to the roles
* [ ] AWS S3 Service

  * [ ] Learn AWS CLI S3 essential commands
  * [ ] Copy and Sync data to/from S3 with AWS CLI
* [ ] AWS RDS Service

  * [ ] Create database in RDS DBMS and generate credentials
  * [ ] Connect to RDS DBMS in DBeaver
* [ ] AWS Secrets Manager Service [[source code](01-foundations/cloud/aws/secrets-manager)]

  * [ ] Create a Secret in Secrets Manager Vault
  * [ ] Get the credential using AWS CLI

### Programming - SQL

* [ ] Ingest data from CSV file into MySQL database table [[source code](02-storage/mysql/lab-data-ingestion-to-mysql)]
* [ ] SQL Basics to Advanced Primer [[source code](01-foundations/language/sql/mode)]
  * [ ] SQL Basics - Select, Limit, Where, Comparison and Logical operators, Order by
  * [ ] SQL Intermediate - Aggregations, Group by, Case statements, Joins
  * [ ] SQL Advanced - Dates, Text, Subqueries, Window functions, Optimizations

### Programming - Python

* [ ] Lists and dictionaries
* [ ] For loops and while loops
* [ ] Functions and Inline functions
* [ ] Read/Write and Manipulate Data using Pandas
* [ ] Pulling data from APIs using requests library
* [ ] Reading data from flat files - csv, json, parquet, avro, excel, txt [[source code](02-storage/flat-files/lab-data-loading-python)]
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

* [ ] Building a data lake for a healthcare company with AWS, S3 and Athena [[source code](02-storage/lab-datalake-healthcare-s3-glue-athena)]
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

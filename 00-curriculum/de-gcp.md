# Curriculum - Data Engineering Training (GCP)

**Estimated Time:** 45 hours

- Getting Started
  - Creating an account
  - Creating your first GCP project
  - Using GCP Cloud Shell
  - A quick overview of GCP services for data engineering
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
- Selecting Appropriate Storage Technologies
  - From Business Requirements to Storage Systems
  - Technical Aspects of Data: Volume, Velocity, Variation, Access, and Security
  - Types of Structure: Structured, Semi-Structured, and Unstructured
  - Schema Design Considerations
- Building and Operationalizing Storage Systems
  - Cloud SQL
  - Cloud Spanner
  - Cloud Bigtable
  - Cloud Firestore
  - BigQuery
  - Cloud Memorystore
  - Cloud Storage
  - Unmanaged Databases
- Designing a Data Processing Solution
  - Designing Infrastructure
  - Designing for Distributed Processing
  - Migrating a Data Warehouse
- BigQuery Data Warehouse
  - Introduction to BigQuery
    - Introduction to Google Cloud Storage and BigQuery
    - BigQuery data location
    - Introduction to the BigQuery console
    - Creating a dataset in BigQuery using the console
    - Loading a local CSV file into the BigQuery table
    - Using public data in BigQuery
    - Data types in BigQuery compared to other databases
    - Timestamp data in BigQuery compared to other databases
  - Lab - Building a Data Warehouse in BigQuery
    - Preparing the prerequisites before developing our data warehouse
    - Step 1: Access your Cloud shell
    - Step 2: Check the current setup using the command line
    - Step 3: The gcloud init command
    - Step 4: Download example data from Git
    - Step 5: Upload data to GCS from Git
    - Practicing developing a data warehouse
    - Data warehouse in BigQuery – Requirements for scenario 1
    - Steps and planning for handling scenario 1
    - Data warehouse in BigQuery – Requirements for scenario 2
    - Steps and planning for handling scenario 2
    - Exercise – Scenario 3
- Snowflake Data Warehousing
  - Loading Data into Snowflake
  - Queries in Snowflake
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
- Lab - ACLED Data Pipeline
- Batch Data Processing
  - Spark and Hadoop
  - Spark Jobs
  - Big Data Processing
  - Clusters
  - Horizontal and Vertical Scaling
  - Processing data using dbt in Snowflake
  - Processing data with Databricks
- Data Lakes and Lakehouses
  - Delta, Iceberg and Hudi
  - Working with Delta lake in Databricks
- Designing Databases for Reliability, Scalability, and Availability
  - Designing Cloud Bigtable Databases for Scalability and Reliability
  - Designing Cloud Spanner Databases for Scalability and Reliability
  - Designing BigQuery Databases for Data Warehousing
- Designing Data Pipelines
  - Overview of Data Pipelines
  - GCP Pipeline Components
  - Migrating Hadoop and Spark to GCP
- Cloud Composer
  - Introduction to Cloud Composer
  - Understanding the working of Airflow
  - Provisioning Cloud Composer in a GCP project
  - Lab - Building Orchestration for Batch Data Loading Using Cloud Composer
    - Level 1 DAG – Creating dummy workflows
    - Level 2 DAG – Scheduling a pipeline from Cloud SQL to GCS and BigQuery datasets
    - Level 3 DAG – Parameterized variables
    - Level 4 DAG – Guaranteeing task idempotency in Cloud Composer
    - Level 5 DAG – Handling late data using a sensor
- Dataproc
  - Introduction to Dataproc
    - A brief history of the data lake and Hadoop ecosystem
    - A deeper look into Hadoop components
    - How much Hadoop-related knowledge do you need on GCP?
    - Introducing the Spark RDD and the DataFrame concept
    - Introducing the data lake concept
    - Hadoop and Dataproc positioning on GCP
  - Lab - Building a Data Lake Using Dataproc
    - Creating a Dataproc cluster on GCP
    - Using Cloud Storage as an underlying Dataproc file system
    - Exercise: Creating and running jobs on a Dataproc cluster
    - Preparing log data in GCS and HDFS
    - Developing Spark ETL from HDFS to HDFS
    - Developing Spark ETL from GCS to GCS
    - Developing Spark ETL from GCS to BigQuery
    - Understanding the concept of the ephemeral cluster
    - Practicing using a workflow template on Dataproc
    - Building an ephemeral cluster using Dataproc and Cloud Composer
- Understanding Data Operations for Flexibility and Portability
  - Cataloging and Discovery with Data Catalog
  - Data Preprocessing with Dataprep
  - Visualizing with Data Studio
  - Exploring Data with Cloud Datalab
  - Orchestrating Workflows with Cloud Composer
- Pub/Sub and Dataflow
  - Processing streaming data
  - Streaming data for data engineers
  - Introduction to Pub/Sub
  - Introduction to Dataflow
  - Lab – Publishing event streams to cloud Pub/Sub
    - Creating a Pub/Sub topic
    - Creating and running a Pub/Sub publisher using Python
    - Creating a Pub/Sub subscription
    - Lab – Using Cloud Dataflow to stream data from Pub/Sub to GCS
    - Creating a HelloWorld application using Apache Beam
    - Creating a Dataflow streaming job without aggregation
    - Creating a streaming job with aggregation
- Key Strategies for Architecting Top-Notch Data Pipelines
  - User and Project Management in GCP
    - Understanding IAM in GCP
    - Planning a GCP project structure
    - Understanding the GCP organization, folder, and project hierarchy
    - Deciding how many projects we should have in a GCP organization
    - Controlling user access to our data warehouse
  - Use-case scenario – planninga BigQuery ACL on an e-commerce organization
  - Column-level security in BigQuery
  - Practicing the concept of IaC using Terraform
    - Lab – creating and running basic Terraform scripts
    - Self-exercise – managing a GCP project and resources using Terraform
- Designing for Security and Compliance
  - Identity and Access Management with Cloud IAM
  - Using IAM with Storage and Processing Services
  - Data Security
  - Ensuring Privacy with the Data Loss Prevention API
  - Legal Compliance
- CI/CD on Google Cloud Platform for Data Engineers
  - Introduction to CI/CD
  - Understanding the data engineer's relationship with CI/CD practices
  - Understanding CI/CD components with GCP services
  - Lab – implementing continuous integration using Cloud Build
    - Creating a GitHub repository using Cloud Source Repository
    - Developing the code and Cloud Build scripts
    - Creating the Cloud Build Trigger
    - Pushing the code to the GitHub repository
  - Lab – deploying Cloud Composer jobs using Cloud Build
    - Preparing the CI/CD environment
    - Preparing the cloudbuild.yaml configuration file
    - Pushing the DAG to our GitHub repository
    - Checking the CI/CD result in the GCS bucket and Cloud Composer

## Getting Started

### Creating an account

To use the GCP console, we need to register using a Google account (Gmail). This requires a payment method. Please check the available payment method to make sure you are successfully registered.

These steps are mandatory to follow:

1. Access the GCP console from this link from any browser: [http://console.cloud.google.com/](http://console.cloud.google.com/)
2. Log in with your Google account (for example, Gmail).
3. With the Google account, register for GCP.

At this point, I won't write many step-by-step instructions, since it's a straightforward registration process. You can check on the internet if you have doubts about any step, at this link: [https://cloud.google.com/free](https://cloud.google.com/free).

A common question at this point is, *am I going to pay for this?*

When you initially register for GCP, you will be asked for a payment method, but you won't be charged for anything at that point. So, when will you get charged?

You will be charged after the following: 

- Using any services
- Using the service more than the free tier allows
- Using GCP for longer than the free trial

I'll explain. You will get charged after you use a service, but not until you pass the free tier limits. Some products have free tiers, some do not.

For example, if you use BigQuery, you won't be charged until you store more than 10 GB a month or query tables more than 1 TB per month. If your usage in BigQuery is less than that, your bill will be zero. But it is different when you use Cloud Composer -- you will be charged when you start Cloud Composer instances.

Check the GCP pricing calculator if you are interested in simulating costs: [https://cloud.google.com/products/calculator](https://cloud.google.com/products/calculator).

It must be confusing at this point about the cost aspect because every single service in GCP has its own pricing mechanism. But on the cloud, the cost is one of the major factors to be considered and needs to be strategized.

### GCP Cloud Essentials

[Source code](../01-foundations/cloud/gcp/README.md)

In this sub-module, we will cover the following topics:

- A quick overview of GCP services for data engineering

## Developer Foundations

### VS Code

- Download and Install vscode
- Understand vscode features
- Install extensions in vscode

### Anaconda (Python)

- Download and Install Anaconda
- Create virtual environment in anaconda
- Create jupyter notebook in vscode and connect to venv

### Github

- Create github account
- Install git cli
- Create git repo and add students as collaborator
- Connect local workspace to git repo
- Learn git commands

### Bash

- Learn bash commands

## Data Engineering Basics

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

## Programming

### SQL

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

### Python

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

### PySpark

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

### Scala

- Introduction to Scala Programming
- Transform complex data types
- Extract and Load Process with Spark Scala, S3 and Postgres

## Databases

## Data Warehouses

## Data Lakes

## Data Modeling

### SQL Data Modeling

- Music Data Modeling with Postgres
- Healthcare Data Modeling with Postgres
- Building Data Model in Snowflake

### NoSQL Data Modeling

- Music Data Modeling with Cassandra

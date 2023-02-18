# Curriculum - Data Engineering Training (GCP)

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

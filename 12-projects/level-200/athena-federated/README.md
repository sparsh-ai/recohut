# Building Federated Query System using Amazon Athena

## Activity 1: Athena Lab Environment Setup

In this activity, we will run a cloudformation stack to create the lab environment. The stack will create a sample TPC database running on Amazon RDS, Amazon EMR Cluster with HBase, Amazon Elasticache Redis, Amazon DynamoDB, Glue Database and tables, S3 Bucket, S3 VPC Endpoint, Glue VPC Endpoint, Athena Named Queries, Cloud9 IDE, SageMaker Notebook instance and other IAM resources.

## Activity 2: Athena Basics

In this activity, we will do the following items:

1. Enable Cloudwatch metrics for Athena
2. Athena Interface - Create tables and run queries
3. Create tables with Glue
4. Create Views
5. Query results and history
6. ETL with Athena CTAS
7. Athena Workgroups
8. Visualize with Quicksight using Athena

## Activity 3: Athena Federation

To demonstrate Athena federation capabilities, a sample data set is being used in this activity along with sample tables and sample data sources.

TPCH data, which is public, is a decision support benchmark. It consists of a suite of business-oriented ad hoc queries and concurrent data modifications. The queries and the data populating the database have been chosen to have broad industry-wide relevance. This benchmark illustrates decision support systems that examine large volumes of data, execute queries with a high degree of complexity, and give answers to critical business questions. The components of TPC-H consist of eight separate and individual tables (the Base Tables).

Imagine a hypothetical e-commerce company who's architecture uses:

- Lineitems processing records stored in HBase on EMR
- Redis is used to store nations and active orders so that the processing engine can get fast access to them
- Aurora with MySQL engine for Orders, Customer and Suppliers accounts data like email address, shipping addresses, etc.
- DynamoDB to host part and partsupp data for high performance

![tpch_athena_federated](https://user-images.githubusercontent.com/62965911/215285196-8a09470f-981c-4d7f-9ade-65ea754ae6b5.png)

In this activity, we will learn:

1. Install db connectors - MySQL, HBase, DynamoDB, and Redis
2. Run Federated queries
3. Visualize with Quicksight
4. Running queries with Quicksight

## Activity 4: ACID transactions with Iceberg

1. Create Iceberg table and insert data into iceberg table
2. Updating datalake using Athena and Iceberg tables
3. Deleting data from datalake using Athena and Iceberg table
4. Time Travel and Version Travel Queries
5. Schema Evolution
6. Optimizing Iceberg Tables

## Project Structure

```
├── [ 60K]  01-sa-main.ipynb
├── [2.8K]  README.md
└── [ 47K]  cfn
    ├── [ 33K]  athena_federated_stack.yml
    └── [ 14K]  athena_stack.yml

 110K used in 1 directory, 4 files
```
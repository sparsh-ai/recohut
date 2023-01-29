# Building End to end data pipeline in AWS

## Architecture Diagram

![](https://user-images.githubusercontent.com/62965911/211014268-7050505c-bafc-431d-b95a-a2d05081e528.png)

## Activity 1: Ingestion with DMS

In this activity, you will complete the following tasks using AWS CloudFormation template:

1. Create the source database environment.
1. Hydrate the source database environment.
1. Update the source database environment to demonstrate Change Data Capture (CDC) replication within DMS.
1. Create a Lambda function to trigger the CDC data to be replicated to Amazon S3 from the DMS CDC endpoint.

Relevant information about this activity:

- Expected setup time | 15 minutes
- Source database name | sportstickets
- Source schema name | dms_sample
- Database credentials: adminuser/admin123

## Activity 2: Data Lake Hydration

In this activity, you will complete the following prerequisites using an AWS CloudFormation template:

1. Create required VPC for AWS DMS instance.
1. Create Amazon S3 bucket for destination endpoint configuration.
1. Create Amazon S3 buckets for Amazon Athena query result storage.
1. Create required Amazon S3 bucket policy to put data from the AWS DMS service.
1. Create AWS Glue Service Role to use in later section of project.
1. Create Amazon Athena workgroup users to use in the Athena project.
1. Create Amazon Lake formation users to use in the Lake Formation project.

## Activity 3: DMS Migration

You will migrate data from an existing Amazon Relational Database Service (Amazon RDS) Postgres database to an Amazon Simple Storage Service (Amazon S3) bucket that you create.

In this activity you will complete the following tasks:

1. Create a subnet group within the DMS activity VPC
1. Create a DMS replication instance
1. Create a source endpoint
1. Create a target endpoint
1. Create a task to perform the initial migration of the data.
1. Create target endpoint for CDC files to place these files in a separate location than the initial load files
1. Create a task to perform the ongoing replication of data changes

## Activity 4: Transforming data with Glue - Data Validation and ETL

In this activity, you will:

1. Create Glue Crawler for initial full load data
1. Create Glue Crawler for Parquet Files
1. Transforming data with Glue - Incremental Data Processing with Hudi
1. Create glue job and create HUDI table
1. Query the HUDI table in Athena
1. Upsert Incremental Changes
1. Run Incremental Queries using Spark SQL

## Activity 5: Query and Visualize

In this activity, you will:

1. Query the data with Amazon Athena
1. Connect Athena to Quicksight
1. Build Dashboard in Amazon Quicksight

## Project Structure

```
.
├── [ 61K]  01-sa.ipynb
├── [ 32K]  cfn
│   ├── [ 14K]  dms.yml
│   └── [ 18K]  hydration.yml
├── [708K]  img
│   ├── [297K]  arch-diagram.png
│   ├── [ 84K]  athena-federated.png
│   └── [327K]  dashboard.png
├── [3.1K]  README.md
└── [ 14K]  src
    ├── [ 11K]  glu_hdi_ticket_purchase_hist.py
    └── [3.2K]  glu_hdi_ticket_purchase_hist_incremental.py

 818K used in 3 directories, 9 files
```
# Lab: Databricks Clickstream Analysis

## Objective

Databricks AWS Integration and Clickstream Analysis

## Introduction

Components and steps we will follow in this lab:

1. AWS Glue as our Central Metastore
2. We will launch 1 Kinesis Stream ie. **User click stream**
3. Join an already existing user Profile Delta table registered in our Glue metastore 
4. We will execute a crawler job to pull in an S3 datasets into our AWS Glue metastore
5. The pipeline consists of a Data Lake medallion appproach
6. We will demonstrate the Full DML support of Delta Lake while curating the Data Lake
6. The curated GOLD dataset will be available to Athena and pushed to Redshift for later consumption
7. Finally, a QuickSight dashboard

## Architecture

![](https://user-images.githubusercontent.com/62965911/214504502-a2cdf9ca-6c87-4fbf-a049-f60aa58e7c6d.png)
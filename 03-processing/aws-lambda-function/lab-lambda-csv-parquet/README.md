# Lambda CSV to Parquet

*Create an S3 bucket and IAM user with user-defined policy. Create Lambda layer and lambda function and add the layer to the function. Add S3 trigger for auto-transformation from csv to parquet and query with Glue.*

## Objective

Serverless Data Conversion and Loading into Data Lake

## Problem Statement

Prolambda sources its data from Salesforce and the source extraction process stores the raw data into Prolambda's data lake.

Currently Prolambda's data engineering team uses a Spark cluster to load that csv by scanning the S3 every few minutes and then converts it into Parquet format using PySpark functions and then saves it back into the data lake's refined layer. Then they run Glue crawler is scheduled to run every 5 mins that picks the latest changes in the source data and update the Glue database.

The process is going well but it is costing the company a lot of money because a Spark cluster needs to be active all the time and the glue crawler's DPU units is through the roof which again costs a huge bill.

Your goal is to design and develop a data pipeline which solves the same purpose but at a reduced cost.

## Use Cases

1. Design and develop a data pipeline for 1) CSV to Parquet conversion, 2) Glue registry and database update

## Architecture Diagram

![arch drawio](https://user-images.githubusercontent.com/62965911/214528163-d8ad4bd2-b1b1-4cf4-a530-bc47df2b0710.svg)

## What you'll build

- Create an S3 bucket
- IAM user with user-defined policy
- Create and Upload `AWS Wrangler` Lambda layer
- Develop the python function for csv to parquet conversion
- Python code to update Glue database
- Add the layer to the function
- Add trigger in Lambda for automation
- Query with Athena

## Code

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut-bootcamps/blob/main/03-processing/aws-lambda-function/lab-lambda-csv-parquet/01-sa-etl-lambda.ipynb)

# ACLED

## Objective

Building data pipeline using Armed Conflict Location & Event Data Project (ACLED) API

## Problem Statement

The Armed Conflict Location & Event Data Project (ACLED) collects real-time data on the locations, dates, actors, fatalities, and types of all reported political violence and protest events around the world. Let's imagine that you are working for a media organization and you want to bring processed version of the ACLED data to your analysts so that they can generate war and conflict related insights for their stories.

Your goal is to design and develop a data pipeline for it.

## Architecture Diagram

![ACLED process_flow drawio](https://user-images.githubusercontent.com/62965911/215261267-f02269fe-103c-410f-a5ad-7eba42eed136.svg)

## What you'll build

1. Data pull from ACLED api
2. CSV data ingestion into Postgres database
3. Use PySpark for data transformation
4. Store the intermediary and final data into S3
5. Develop Data pipeline with Airflow
6. Create and Trigger the Glue crawler using Airflow operator
7. Run the analysis in Athena
8. Setting up and using connections and variables in Airflow
9. Send an Email to stakeholders about pipeline execution status

## DAG Run instructions

1. Create a free account on ACLED
2. Get the API key and add in the DAG
3. Install the python libraries mentioned in the DAG
4. Set the environment variables - ACLED key and user, S3 bucket and AWS credentials
5. Create a Glue crawler named `acled`
6. Modify the DAG - update name, owner and change catchup, scheduling and other info as required
7. Run the DAG

NOTE

> We first tried pipeline 1 but due to limitation in API requests, we decided to go with pipeline 2.

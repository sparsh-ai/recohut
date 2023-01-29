# Datalake Schema Correction

## Objective

AWS Datalake Schema Correction

## Problem Statement

HMC Analytics is a UK-based startup building a marketing product. They are pulling data from their online platform into S3 datalake. Their analyst team generates daily insights report by executing queries (using AWS Athena).

Yesterday, their Analyst team reported that they are facing some problem while running the queries. They need your help in resolving this problem on an urgent basis because the executive team is waiting for those daily reports and key strategic decisions are dependent on these reports.

Your first goal is to replicate this situation by generating the error in Athena and then successfully resolve it by running queries in Athena.

Follow these steps:

1. The data table is `other_events`. This data is already loaded for you in `s3://<bucket>/hmc`. Explore the data.
2. Create a Glue crawler to add this data into the glue catalog.
3. Once crawler adds the table in catalog, try to get the first few records and record counts in Athena. Note: At this point, you are supposed to replicate the error. Athena will tell you what the error is.
4. Understand the problem and find the root cause.
5. Resolve the issue. Hint1: Research online about the possible solutions and try them out. Do not spend a lot of time but try 1-2 solutions max.
6. Create a brief report of 50-200 words.

## Use Cases

1. Error replication
2. Problem identification
3. Root cause analysis
4. Research & development
5. Solution development

## Project Structure

```
├── [ 25K]  01-sa.ipynb
├── [1.5K]  README.md
├── [ 12K]  data
│   └── [ 12K]  raw
│       └── [ 12K]  other_events
│           └── [ 12K]  event=journey_closed
│               └── [ 12K]  brand=paw-and-glory
│                   ├── [5.5K]  part-00000-4a7006e4-1695-44eb-ae29-b8f438652eed-c000.snappy.parquet
│                   └── [6.2K]  part-00008-1f817ad7-0889-4df0-a1f0-f714b8163389.c000.snappy.parquet
├── [  44]  download.sh
└── [708K]  files
    ├── [3.2K]  athena_queries.sql
    ├── [ 17K]  change.drawio.svg
    ├── [4.3K]  glue_etl_original.py
    ├── [1.3K]  glue_etl_v0.py
    ├── [3.3K]  glue_etl_v1.py
    ├── [5.2K]  glue_etl_v2.py
    ├── [218K]  nbs.zip
    ├── [8.8K]  src
    │   ├── [4.4K]  glue_new.py
    │   └── [4.2K]  glue_old.py
    ├── [1.8K]  temp.py
    ├── [240K]  tiger
    │   ├── [217K]  Resolving\ the\ parquet\ schema\ error\ 8c9b3aa4157c4ce2b5ead115512b39f2
    │   │   ├── [ 58K]  Screenshot_2022-08-31_at_11.11.50_PM.png
    │   │   ├── [ 56K]  Untitled\ 1.png
    │   │   └── [103K]  Untitled.png
    │   └── [ 23K]  Resolving\ the\ parquet\ schema\ error\ 8c9b3aa4157c4ce2b5ead115512b39f2.html
    └── [205K]  tiger.zip

 747K used in 9 directories, 20 files
```
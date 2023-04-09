# Equitize Data Migration

> Financial Data Extraction and Storage

Suppose you are ingesting large amounts of data into SQL and NoSQL. You got big data! For Data Engineering, there are the 3 Vs: volume, velocity, variety. Both SQL and NoSQL can take care of volume and velocity if they are transactional databases. However NoSQL can take care of variety with semi-structured and unstrucuted data. However you also want OLAP data warehouse for easy querying for business analytics. To replicate the source databases to the target data warehouse is a process called Change Discovery Capture (CDC).

In this lab, you will develop a pipeline that will migrate the data from SQL and NoSQL databases to Redshift Warehouse.

- Every 5 minutes, Eventbridge triggers a Lambda to load txns.csv to RDS. Since I defined the table with no primary key/uniqueness restriction, the table gets appended. AWS DMS (data migration service) task is synchronize the data from RDS to Redshift via CDC.
- Every 5 minutes, Eventbridge triggers a Lambda to load trades.json to DynamoDB. Any INSERTS or UPDATES triggers DynamoDB stream to trigger another separate Lambda that will write those new records into a file stored in an S3 bucket. Every 5 minutes, another Lambda will load files from the S3 bucket to the Redshift cluster, then delete the files.

We will use Cloud Development Kit tool for deploying the pipeline.

![aws-resources](https://user-images.githubusercontent.com/62965911/224529736-64e57849-fad2-4721-b46b-fb14e5240b29.jpg)

### Python for Data Engineering - Building an ETL Pipeline

For this project, you will assume the role of data engineer working for an international financial analysis company. Your company tracks stock prices, commodities, forex rates, inflation rates.  Your job is to extract financial data from various sources like websites, APIs and files provided by various financial analysis firms. After you collect the data, you extract the data of interest to your company and transform it based on the requirements given to you. Once the transformation is complete you load that data into a database.

In this project, you will:

- Collect data using APIs
- Collect data using webscraping.
- Download files to process.
- Read csv, xml and json file types.
- Extract data from the above file types.
- Transform data.
- Use the built-in logging module.
- Save the transformed data in a ready-to-load format which data engineers can use to load the data.

## Solution

```
.
├── [ 27K]  CDK.ipynb
├── [2.6K]  equitize.mdx
├── [1.0K]  readme.md
├── [  53]  requirements.txt
└── [ 34K]  source
    ├── [9.9K]  load_data_to_dynamodb_lambda
    │   ├── [ 429]  handler.py
    │   ├── [4.0K]  poetry.lock
    │   ├── [ 295]  pyproject.toml
    │   └── [5.0K]  trades.json
    ├── [5.3K]  load_data_to_rds_lambda
    │   ├── [1.6K]  handler.py
    │   ├── [ 641]  poetry.lock
    │   ├── [ 290]  pyproject.toml
    │   ├── [  40]  requirements.txt
    │   └── [2.5K]  txns.csv
    ├── [7.5K]  load_s3_files_from_dynamodb_stream_to_redshift_lambda
    │   ├── [3.1K]  handler.py
    │   ├── [4.0K]  poetry.lock
    │   └── [ 320]  pyproject.toml
    ├── [5.4K]  start_dms_replication_task_lambda
    │   ├── [1023]  handler.py
    │   ├── [4.0K]  poetry.lock
    │   └── [ 300]  pyproject.toml
    └── [6.1K]  write_dynamodb_stream_to_s3_lambda
        ├── [1.7K]  handler.py
        ├── [4.0K]  poetry.lock
        └── [ 301]  pyproject.toml

 553K used in 7 directories, 28 files
```

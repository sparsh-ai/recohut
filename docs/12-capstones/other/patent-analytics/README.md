# Patent Analytics Data Pipeline

![front](https://user-images.githubusercontent.com/62965911/215308154-ff084580-94de-4cd6-883a-69086fd8d462.png)

## Problem Statement

According to the WIPO definition, a patent is an exclusive right granted for an invention, which is a product or a process that provides, in general, a new way of doing something, or offers a new technical solution to a problem. To get a patent, technical information about the invention must be disclosed to the public in a patent application. By acquiring a patent, the patent owner has the exclusive right to prevent or stop others from commercially exploiting the patent invention.

Although not all inventions may be patented, it is still worth using patents to indicate the extent of the technological advancement happening in academic and industry settings.

At the macro level, by analyzing patent data, we could see the technology trends in different decades. We can see which technology is growing and which technology is getting dimmer. We can understand different industry focus in different countries. For example, Taiwan has more patents in semiconductors, US and China have more patents in ICT sectors.

At the company level, patent analytics play a part in guiding their understanding of their industries. Companies may be interested in who are the key players in their industry, understanding the key development in their industry, understanding what technologies their competitors are patenting, is there any part of their product infringes the patent of other companies, is there any patent they are interested in buying, in which direction should they take for their research, etc.

In this project, we are building a data pipeline to process the US patent data from the year 2000 until 2021, totaling slightly more than 5 million records into an analytical database. The analytical database will be used for an interactive dashboard to explore patent data.

Some analysis that could be done via the dashboard are:

**Global analysis of patent**:

- Number of patents by classification by year
- Top 20 companies with the highest number of patent
- Top 5 companies with the highest number of patents for each classification
- Top 10 keywords for each classification

**Company analysis of patent**:

- Number of patents per year
- Top keywords from their patents over the year

## What you'll build

1. We use Spark as compute engine for the data cleaning, keyword extraction, and ETL due to the size of our data. Spark allows us to process a large amount of data in parallel. In this project, we are using AWS EMR to run the spark job. EMR cluster can be brought up and down as required hence is more cost-effective.
2. We use Airflow as our orchestration engine to manage the dependencies between one task and the other. For example, run a data quality check after the ETL job is completed. Airflow is run using docker for simplicity.
3. We use Redshift as the analytical database. Redshift is built for data warehouse and supports efficient analytical queries because of its columnar table design and ability to do massively parallel processing with data distributed across various nodes. In addition to that, we choose Redshift because our raw data and EMR cluster reside in AWS. Since they are located in the same infrastructure, the data transfer would be faster.
4. We placed our raw data and cleaned data in AWS S3 for easy and fast processing
5. We use Spark NLP Yake Keyword Extraction for extracting the keyword from the patent title and abstract. Yake Keyword Extraction is independent of language and corpus, and it is efficient and fast. Spark NLP libraries are open source NLP libraries for spark application provided by John Snow LABS

This is the dashboard we built using AWS QuickSight:

![quicksight_dashboard](https://user-images.githubusercontent.com/62965911/215308150-92144f41-71d5-440a-8030-079b4b919fdf.gif)

## Project Architecture

![architecture](https://user-images.githubusercontent.com/62965911/215308145-ebb20354-6e4b-4097-9425-0bbe19665bc9.png)

These are the overview of the steps involved in the data pipeline:

1. Copy the data sources from various source systems to S3
2. Trigger a spark job at an EMR cluster to clean the raw data and place the cleaned data into partitioned parquet files in S3
3. Trigger a spark job at an EMR cluster to extract keywords from cleaned data and put the result in S3
4. Trigger a spark job at the EMR cluster to perform ETL from the cleaned data and dump the result in a Redshift table

## ETL

After the data is cleaned, we perform the ETL of the data from S3 to the Redshift table.

This is the data model of the analytics tables in Redshift:

![data_model](https://user-images.githubusercontent.com/62965911/215308147-a59490cd-6f9b-4cdd-b54c-e935f587bb53.png)

There are two facts tables:

- Patents
- PatentKeywords

There are five dimension tables:

- Dates
- Details
- WipoClassifications
- Owners
- Locations

## Orchestration - Airflow

![airflow_dag](https://user-images.githubusercontent.com/62965911/215308143-5e2ded78-4f44-41e8-b371-e4ae294b9030.png)

- `Begin_execution`: Start of the dag
- `download_raw_patent_data_to_s3`: Download the patents' data from USPTO website to AWS S3
- `upload_local_raw_data_to_S3`: Upload the country shapes and country info from the local folder to AWS S3
- `check_raw_exists`: Check that all the raw data have been successfully uploaded to the AWS S3 bucket
- `cleaning_emr_task`: Trigger an EMR job to clean the data and write the result back to the AWS S3 bucket
- `check_cleaned_data_exists`: Check whether all the cleaned data exists in the AWS S3 bucket
- `keyword_extraction_erm_task`: Trigger an EMR job to extract keywords from patents' title and abstract and write the result to the AWS S3 bucket
- `check_keyword_data_exists`: Check whether all the keyword extraction data exists in the AWS S3 bucket
- `etl_emr_task`: Trigger an EMR job to run ETL on the cleaned data and write the result to Redshift
- `check_table_count`: Check that each table has at least 10 rows of data to ensure that the write operation was successful.
- `check_table_data_quality`: Check the quality of the data in each table
- `End_execution`: End of the dag

## Solution

```
├── [ 24K]  README.md
├── [4.2M]  airflow
│   ├── [4.1K]  README.md
│   ├── [4.2M]  dags
│   │   ├── [1.1M]  data
│   │   │   ├── [ 28K]  countryInfo.txt
│   │   │   └── [1.1M]  shapes_simplified_low.json.zip
│   │   ├── [ 14K]  patent_analytics_dag.py
│   │   ├── [ 426]  patent_analytics_drop_create_table_dag.py
│   │   ├── [3.1M]  scripts
│   │   │   └── [3.1M]  dependencies
│   │   │       └── [3.1M]  packages.zip
│   │   └── [2.0K]  sql
│   │       └── [1.9K]  drop_create_tables.sql
│   ├── [ 10K]  docker-compose.yaml
│   └── [ 11K]  plugins
│       ├── [2.2K]  operators
│       │   ├── [   0]  __init__.py
│       │   ├── [1.0K]  check_s3_key_exist_operator.py
│       │   └── [1.0K]  download_data_and_put_in_s3_operator.py
│       └── [9.0K]  task_builder
│           ├── [   0]  __init__.py
│           ├── [5.1K]  build_emr_task.py
│           └── [3.7K]  job_flow_overrides.py
├── [ 22K]  airflow_dag.png
├── [ 85K]  architecture.png
├── [ 81K]  data_model.png
├── [697K]  notebooks
│   ├── [2.6K]  1_ingest_raw_data.ipynb
│   ├── [158K]  2_exploratory_data_analysis.ipynb
│   ├── [ 52K]  3_b_keyword_extraction_yake.ipynb
│   ├── [319K]  3_data_cleaning.ipynb
│   └── [164K]  4_etl_to_redshift.ipynb
├── [1.8M]  quicksight_dashboard.gif
└── [153K]  spark
    ├── [ 235]  Pipfile
    ├── [8.4K]  Pipfile.lock
    ├── [3.7K]  README.md
    ├── [1.4K]  build_dependencies.sh
    ├── [ 170]  copy_jobs_to_airflow.sh
    ├── [9.2K]  dependencies
    │   ├── [   0]  __init__.py
    │   ├── [1.2K]  logging.py
    │   ├── [4.2K]  spark.py
    │   └── [3.6K]  utils.py
    ├── [ 42K]  jobs
    │   ├── [ 24K]  Data_Cleaning
    │   │   ├── [4.0K]  cleaning_assignee_job.py
    │   │   ├── [3.8K]  cleaning_country_shapes_job.py
    │   │   ├── [1.8K]  cleaning_inventor_job.py
    │   │   ├── [9.6K]  cleaning_location_job.py
    │   │   ├── [ 920]  cleaning_patent_assignee_job.py
    │   │   ├── [ 921]  cleaning_patent_inventor_job.py
    │   │   ├── [1.3K]  cleaning_patent_job.py
    │   │   ├── [ 917]  cleaning_wipo_field_job.py
    │   │   └── [ 954]  cleaning_wipo_job.py
    │   ├── [ 14K]  ETL
    │   │   ├── [1.1K]  dates_etl_job.py
    │   │   ├── [1.3K]  details_etl_job.py
    │   │   ├── [4.3K]  intermediary_patent_etl_job.py
    │   │   ├── [1.2K]  locations_etl_job.py
    │   │   ├── [1.2K]  owners_etl_job.py
    │   │   ├── [1.3K]  patent_keywords_etl_job.py
    │   │   ├── [1.8K]  patents_etl_job.py
    │   │   └── [1.6K]  wipo_classifications_etl_job.py
    │   └── [3.7K]  Keyword_Extraction
    │       ├── [1.3K]  rank_keyword_job.py
    │       └── [2.3K]  yake_keyword_extraction_job.py
    └── [ 87K]  tests
        ├── [ 37K]  Data_Cleaning
        │   ├── [   0]  __init__.py
        │   ├── [1.3K]  test_cleaning_assignee_job.py
        │   ├── [1.7K]  test_cleaning_country_shapes_job.py
        │   ├── [1.3K]  test_cleaning_inventor_job.py
        │   ├── [1.8K]  test_cleaning_location_job.py
        │   ├── [1.3K]  test_cleaning_patent_assignee_job.py
        │   ├── [1.3K]  test_cleaning_patent_inventor_job.py
        │   ├── [1.2K]  test_cleaning_patent_job.py
        │   ├── [1.3K]  test_cleaning_wipo_field_job.py
        │   ├── [1.2K]  test_cleaning_wipo_job.py
        │   └── [ 24K]  test_data
        │       ├── [ 549]  country_info.txt
        │       └── [ 24K]  country_shapes_cleaned.csv
        ├── [ 17K]  ETL
        │   ├── [   0]  __init__.py
        │   ├── [1.5K]  test_dates_etl_job.py
        │   ├── [2.0K]  test_details_etl_job.py
        │   ├── [2.2K]  test_intermediary_patent_etl_job.py
        │   ├── [1.8K]  test_locations_etl_job.py
        │   ├── [1.9K]  test_owners_etl_job.py
        │   ├── [2.6K]  test_patent_keywords_etl_job.py
        │   ├── [2.7K]  test_patents_etl_job.py
        │   └── [2.0K]  test_wipo_classifications_etl_job.py
        ├── [2.9K]  Keyword_Extraction
        │   ├── [   0]  __init__.py
        │   ├── [1.3K]  test_rank_keyword_job.py
        │   └── [1.4K]  test_yake_keyword_extraction_job.py
        ├── [   0]  __init__.py
        ├── [1.4K]  common.py
        └── [ 29K]  data.py

 7.1M used in 21 directories, 79 files
```
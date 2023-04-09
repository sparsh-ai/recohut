# Patent Analytics Data Pipeline

## Introduction

### Background

According to the WIPO definition, a patent is an exclusive right granted for an invention, which is a product or a process that provides, in general, a new way of doing something, or offers a new technical solution to a problem. To get a patent, technical information about the invention must be disclosed to the public in a patent application. By acquiring a patent, the patent owner has the exclusive right to prevent or stop others from commercially exploiting the patent invention.

Although not all inventions may be patented, it is still worth using patents to indicate the extent of the technological advancement happening in academic and industry settings.

At the macro level, by analyzing patent data, we could see the technology trends in different decades. We can see which technology is growing and which technology is getting dimmer. We can understand different industry focus in different countries. For example, Taiwan has more patents in semiconductors, US and China have more patents in ICT sectors.

At the company level, patent analytics play a part in guiding their understanding of their industries. Companies may be interested in who are the key players in their industry, understanding the key development in their industry, understanding what technologies their competitors are patenting, is there any part of their product infringes the patent of other companies, is there any patent they are interested in buying, in which direction should they take for their research, etc

### Objective

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

This is the dashboard we built using AWS QuickSight:

![dashboard_demo2](https://user-images.githubusercontent.com/33612460/190854889-15b905cd-e409-457d-9de5-9e42b6f1b8aa.gif)

## Table of Contents

- [Introduction](#introduction)
- [Technologies](#technologies)
- [Project Architecture](#project-architecture)
- [Project Structure](#project-structure)
- [Data Source](#data-source)
- [Data Exploratory](#data-exploratory)
- [Data Pipeline - Spark](#data-pipeline---spark)
- [Orchestration - Airflow](#orchestration---airflow)
- [Getting Started](#getting-started)
- [Future Works](#future-works)
- [References](#references)

## Technologies

### Apache Spark

We use Spark as compute engine for the data cleaning, keyword extraction, and ETL due to the size of our data. Spark allows us to process a large amount of data in parallel. In this project, we are using AWS EMR to run the spark job. EMR cluster can be brought up and down as required hence is more cost-effective.

### Apache Airflow 2.3.3

We use Airflow as our orchestration engine to manage the dependencies between one task and the other. For example, run a data quality check after the ETL job is completed. Airflow is run using docker for simplicity.

### AWS Redshift

We use Redshift as the analytical database. Redshift is built for data warehouse and supports efficient analytical queries because of its columnar table design and ability to do massively parallel processing with data distributed across various nodes. In addition to that, we choose Redshift because our raw data and EMR cluster reside in AWS. Since they are located in the same infrastructure, the data transfer would be faster.

### AWS S3

We placed our raw data and cleaned data in AWS S3 for easy and fast processing

### Spark NLP

We use Spark NLP Yake Keyword Extraction for extracting the keyword from the patent title and abstract. Yake Keyword Extraction is independent of language and corpus, and it is efficient and fast. Spark NLP libraries are open source NLP libraries for spark application provided by John Snow LABS

## Project Architecture

![architecture.png](https://user-images.githubusercontent.com/62965911/215308145-ebb20354-6e4b-4097-9425-0bbe19665bc9.png)

These are the overview of the steps involved in the data pipeline:

1. Copy the data sources from various source systems to S3
2. Trigger a spark job at an EMR cluster to clean the raw data and place the cleaned data into partitioned parquet files in S3
3. Trigger a spark job at an EMR cluster to extract keywords from cleaned data and put the result in S3
4. Trigger a spark job at the EMR cluster to perform ETL from the cleaned data and dump the result in a Redshift table

## Project Structure

The project is structured into 3 main folders:

- `airflow` folder contains all the dags implementation. The folder scripts under `dags` folder are the pyspark scripts to be submitted to EMR, it is generated from the `spark` folder.
- `notebooks` folder contains the jupyter notebooks file used for exploration before developing pyspark scripts. All the notebooks except the `1_ingest_raw_data.ipynb` are pyspark notebooks and are supposed to be run on the Spark cluster.
- `spark` folder contains the pyspark scripts for cleaning data, extracting keywords, and doing ETL jobs and their respective unit tests.

```bash
root/

|   .gitignore
|   img.png
|   README.md
|
|---airflow # ---- Airflow DAG ----
|   |   .env
|   |   docker-compose.yaml
|   |
|   |---dags
|   |   |   patent_analytics_dag.py
|   |   |   patent_analytics_drop_create_table_dag.py
|   |   |
|   |   |---data
|   |   |       countryInfo.txt
|   |   |       shapes_simplified_low.json
|   |   |
|   |   |---scripts # Pyspark scripts to be submitted to EMR. These are to be copied from the spark  folder
|   |   |---sql
|   |   |       drop_create_tables.sql
|   |   |
|   |
|   |---plugins
|       |---operators
|       |   |   check_s3_key_exist_operator.py
|       |   |   download_data_and_put_in_s3_operator.py
|       |   |   __init__.py
|       |
|       |---task_builder
|       |   |   build_emr_task.py
|       |   |   job_flow_overrides.py
|       |   |   __init__.py
|       |   |
|---notebooks # ---- Notebook file for exploration ----
|   |   1_ingest_raw_data.ipynb
|   |   2_exploratory_data_analysis.ipynb
|   |   3_b_keyword_extraction_yake.ipynb
|   |   3_data_cleaning.ipynb
|   |   4_etl_to_redshift.ipynb
|   |
|---spark # ---- Spark Scripts ----
    |   build_dependencies.sh
    |   copy_jobs_to_airflow.sh
    |   packages.zip
    |   Pipfile
    |   Pipfile.lock
    |   README.md
    |
    |---configs
    |       etl_config.json
    |
    |---dependencies
    |   |   logging.py
    |   |   spark.py
    |   |   utils.py
    |   |   __init__.py
    |   |
    |
    |---jobs
    |   |---Data_Cleaning
    |   |       cleaning_assignee_job.py
    |   |       cleaning_country_shapes_job.py
    |   |       cleaning_inventor_job.py
    |   |       cleaning_location_job.py
    |   |       cleaning_patent_assignee_job.py
    |   |       cleaning_patent_inventor_job.py
    |   |       cleaning_patent_job.py
    |   |       cleaning_wipo_field_job.py
    |   |       cleaning_wipo_job.py
    |   |
    |   |---ETL
    |   |       dates_etl_job.py
    |   |       details_etl_job.py
    |   |       intermediary_patent_etl_job.py
    |   |       locations_etl_job.py
    |   |       owners_etl_job.py
    |   |       patents_etl_job.py
    |   |       patent_keywords_etl_job.py
    |   |       wipo_classifications_etl_job.py
    |   |
    |   |---Keyword_Extraction
    |   |       rank_keyword_job.py
    |   |       yake_keyword_extraction_job.py
    |   |
    |---tests # ---- Spark Scripts Unit Test ----
        |   common.py
        |   data.py
        |   __init__.py
        |
        |---Data_Cleaning
        |   |   test_cleaning_assignee_job.py
        |   |   test_cleaning_country_shapes_job.py
        |   |   test_cleaning_inventor_job.py
        |   |   test_cleaning_location_job.py
        |   |   test_cleaning_patent_assignee_job.py
        |   |   test_cleaning_patent_inventor_job.py
        |   |   test_cleaning_patent_job.py
        |   |   test_cleaning_wipo_field_job.py
        |   |   test_cleaning_wipo_job.py
        |   |
        |   |---test_data
        |           country_info.txt
        |           country_shapes_cleaned.csv
        |
        |---ETL
        |       test_dates_etl_job.py
        |       test_details_etl_job.py
        |       test_intermediary_patent_etl_job.py
        |       test_locations_etl_job.py
        |       test_owners_etl_job.py
        |       test_patents_etl_job.py
        |       test_patent_keywords_etl_job.py
        |       test_wipo_classifications_etl_job.py
        |       __init__.py
        |
        |---Keyword_Extraction
        |       test_rank_keyword_job.py
        |       test_yake_keyword_extraction_job.py



```

## Data Source

### Patent data from USPTO PatentsView

- patent: [https://s3.amazonaws.com/data.patentsview.org/download/patent.tsv.zip](https://s3.amazonaws.com/data.patentsview.org/download/patent.tsv.zip)
- patent_asignee: [https://s3.amazonaws.com/data.patentsview.org/download/patent_assignee.tsv.zip](https://s3.amazonaws.com/data.patentsview.org/download/patent_assignee.tsv.zip)
- asignee: [https://s3.amazonaws.com/data.patentsview.org/download/assignee.tsv.zip](https://s3.amazonaws.com/data.patentsview.org/download/assignee.tsv.zip)
- location: [https://s3.amazonaws.com/data.patentsview.org/download/location.tsv.zip](https://s3.amazonaws.com/data.patentsview.org/download/location.tsv.zip)
- wipo: [https://s3.amazonaws.com/data.patentsview.org/download/wipo.tsv.zip](https://s3.amazonaws.com/data.patentsview.org/download/wipo.tsv.zip)
- wipo_field: [https://s3.amazonaws.com/data.patentsview.org/download/wipo_field.tsv.zip](https://s3.amazonaws.com/data.patentsview.org/download/wipo_field.tsv.zip)
- inventor: [https://s3.amazonaws.com/data.patentsview.org/download/inventor.tsv.zip](https://s3.amazonaws.com/data.patentsview.org/download/inventor.tsv.zip)
- patent_inventor: [https://s3.amazonaws.com/data.patentsview.org/download/patent_inventor.tsv.zip](https://s3.amazonaws.com/data.patentsview.org/download/patent_inventor.tsv.zip)

The data dictionary can be found at https://patentsview.org/download/data-download-dictionary

### Country Shapes and Country Info from Geonames.org

- country latitude and longitude polygon: http://download.geonames.org/export/dump/shapes_simplified_low.json.zip
- country info: http://download.geonames.org/export/dump/countryInfo.txt

## Data Exploratory

The data exploratory is performed using pyspark notebook `notebooks/2_exploratory_data_analysis.ipynb`

### Patent data

- There are 7,991,058 patents in the data
- The patents were issued from 1976 to 2021
- All the patents were issued in the US

### Patent assignee data

- There are some patents without an assignee
- There are some patents with multiple assignees

### Assignee data

- Some assignees have missing type
- Based on the data dictionary, assignee types range from 1 to 9. If there is 1 appears in front, it signifies part interest
- Some assignees have both organization and individual name

### Location data

- Location data have city, state, country, latitude, longitude, county, state_fips, and county_fips, however any of these columns may be null

### wipo data

- The data contains the WIPO classification for the patent
- There are some patents with no WIPO classification
- There are some patents with multiple WIPO classifications and the sequence to tell the priority

### WIPO field data

- The data contains the sector and the field of WIPO classification

### patent inventor data

- There are some patents with no inventor data
- There are some patents with multiple inventors

### inventor data

- There are some inventors with no first name

## Data Pipeline - Spark

The spark project is structured as recommended by https://github.com/AlexIoannides/pyspark-example-project

The spark scripts consist of data cleaning, keyword extraction, and ETL

### Data cleaning steps

#### Patent data

- Remove the withdrawn patents
- Remove the patents granted before the year of 2000
- Remove columns `number`, `filename`, and `withdrawn`

#### Patent assignee data

- Take only one patent assignee for each patent

#### Assignee data

- Remove the unassigned assignee
- Replace the type from number to string
- Combine the column `name_first`, `name_last` and `organisation` into one column called `name`
- Create a new unique ID based on name and type

#### Location data

We will aggregate the data at the country level, so for the data without a country, we will derive it based on the available data:

- if the state belongs to the US, map the country to the US
- if there is latitude and longitude, infer the country from the latitude and longitude
- Create a new unique ID based on country

#### wipo data

- Only take the WIPO sequence 0 for each patent, meaning take the first classification only
- Only select field `patent_id` and `field_id`

#### wipo field data

- Remove the data whose `id` starts with "D"

#### patent inventor data

- Take only one patent inventor for each patent

#### inventor data

- Combine the column `name_first` and `name_last` into `name` column
- Assign the `type` as "individual"
- Create a new unique ID based on the `name` and `type`

### Keyword extraction

#### Extract keywords using Yake Keyword Extraction

In these steps, we process each patent's title and abstract through a keyword extraction pipeline which consists of:

- assembling the document
- detecting the sentence
- tokenizing the sentence
- extracting the keyword

#### Rank and Take the top 10 keywords

- Extract the keyword and the score
- Rank the score and take the top 10 keywords with the least score.

### ETL

After the data is cleaned, we perform the ETL of the data from S3 to the Redshift table.

This is the data model of the analytics tables in Redshift:
![data_model.png](https://user-images.githubusercontent.com/62965911/215308147-a59490cd-6f9b-4cdd-b54c-e935f587bb53.png)

There are two facts tables:

- Patents
- PatentKeywords

There are five dimension tables:

- Dates
- Details
- WipoClassifications
- Owners
- Locations

#### Patents Table

The `Patent` table is distributed with a key distribution style using the `id` as the distribution key. The reason we choose this distribution style are:

- In the user query, we will join the table with `PatentKeywords` using the `id`, so using `id` as the distribution key will reduce the need to shuffle the data.
- The patent table size is big, so it's not efficient if we distribute it to all the nodes.

#### Patent Keywords Table

The `PatentKeywords` table is also distributed with a key distribution style using the `patent_id` column as the distribution key. This allows us to perform an efficient join with the `patents` table.

#### Dates Table

The `Dates` table is distributed with the style `ALL`. The table size is not big, hence it's fine to have some duplicates for the sake of performance.

#### Owners Table

The `Owners` table is also distributed with the style `ALL` for the same reason as the `dates` table

#### Locations Table

The `Locations` table is also distributed with the style `ALL` for the same reason as the `dates` and `owners` table.

#### WipoClassifications Table

`WipoClassifications` table is distributed with style `KEY` using the `wipo_classification_id`. In most cases, `wipo_classifications_id` have the same value as `Patents` table `id` field. Hence, it allows us to perform an efficient join between the `Patents` table and the `WipoClassifications` table.

#### Details Table

The `Details` table is distributed with the style `KEY` using the `detail_id`. In most cases, `detail_id` have the same value as the `Patents` table `id` field. Hence, it allows us to perform an efficient join between the `Patents` table and the `Details` table.

### Data Dictionary of the Analytics Table

#### Patent Table

| Field                  | Definition                                                           | Type   | Example |
| ---------------------- | -------------------------------------------------------------------- | ------ | ------- |
| id                     | patent number                                                        | string | 9683848 |
| granted_date           | date when the patent was granted                                         | date   | 10/1/07 |
| detail_id              | refer to field `detail_id` in details table                          | string | 9683848 |
| owner_id               | refer to field `owner_id` in owners table                            | string |         |
| location_id            | refer to field `location_id` in locations table                      | string |         |
| wipo_classification_id | refer to field `wipo_classification_id` in WipoClassifications table | string | 9683848 |
| num_claims             | number of claims                                                     | int    | 2       |

#### PatentKeywords Table

| Field             | Definition                                | Type   | Example                |
| ----------------- | ----------------------------------------- | ------ | ---------------------- |
| patent_keyword_id | unique id for this table                  | string |                        |
| patent_id         | patent number                             | string | 9683848                |
| keyword           | keyword extracted from the title and abstract | string | semiconductor material |

#### Dates Table

| Field | Definition                   | Type | Example |
| ----- | ---------------------------- | ---- | ------- |
| date  | date                         | date | 10/1/07 |
| year  | year extracted from the date | int  | 2007    |

#### Details Table

| Field     | Definition               | Type   | Example                      |
| --------- | ------------------------ | ------ | ---------------------------- |
| detail_id | unique id for this table | string | 3930271                      |
| title     | title of patent          | string | Golf glove                   |
| abstract  | abstract text of patent  | string | A golf glove is disclosed... |

#### WipoClassifications Table

| Field                  | Definition                   | Type   | Example                                 |
| ---------------------- | ---------------------------- | ------ | --------------------------------------- |
| wipo_classification_id | unique id for this table     | string | 3930271                                 |
| sector                 | WIPO technology sector title | string | Electrical engineering                  |
| field                  | WIPO technology field title  | string | Electrical machinery, apparatus, energy |

#### Owners Table

| Field    | Definition                                                 | Type   | Example                        |
| -------- | ---------------------------------------------------------- | ------ | ------------------------------ |
| owner_id | unique id for this table                                   | string |                                |
| type     | classification of owner: company, individual, or government | string | company                        |
| name     | name of individual or organization                         | string | E-Z Anchor Bolt Template, Inc. |

#### Locations Table

| Field       | Definition                                | Type   | Example |
| ----------- | ----------------------------------------- | ------ | ------- |
| location_id | unique id for this table                  | string |         |
| country     | country associated with the `location_id` | string | Germany |
| continent   | continent of the country                  | string | EU      |

## Orchestration - Airflow

### Drop and Create Table

`patent_analytics_drop_create_table_dag` is used to drop and recreate Redshift table. It is only supposed to be run once.

### Patent Analytics Data Pipeline End to End

`patent_analytics_dag` runs the end-to-end data pipeline to prepare the data. This is the design of the DAG:

![airflow_dag.png](https://user-images.githubusercontent.com/62965911/215308143-5e2ded78-4f44-41e8-b371-e4ae294b9030.png)

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

## Getting Started

Please check respective folders `spark` and `airflow` on how to start the project.

## Future Works

### Data Updates

In the current design, the data pipeline is triggered manually. In the future, we can schedule the data pipeline to run at regular intervals.
Looking at their release notes, it seems that USPTO patents data was updated every March and September yearly, with the data lag of 3 months behind, but there is no clear indicator on the release date. To be safe, we can schedule the pipeline to run in April and October.
In addition to that, since the raw data is in the form of bulk data (not incremental), we may need to parameterize our pipeline to only process the additional data.

### What if the data were increased by 100x?

Running the current data pipeline, end-to-end took about 4 hours using Spark Cluster with 1 master node and 2 worker nodes with instance types of `m4.xlarge`.
If the data size were increased by 100x, we need to:

- Increase the number of worker nodes to speed up the processing
- Increase the driver memory to ensure it can accommodate the data size
- Increase the data partitioning to reduce the data chunk size and improve the parallel processing

### What if the data were run on a daily basis by 7 am?

If the data need to be refreshed daily for user consumption and the time is sensitive, we need to set up automatic retries if the dag failed and configure airflow to send an alert if the dag fails x number of times. This ensures that we can address the issue promptly.

### What If the database needed to be accessed by 100+ people?

We can scale our database either horizontally or vertically:

- Horizontal scaling means adding more nodes to our database cluster; by doing so, we increase the amount of computing power available to handle user queries
- Vertical scaling means using higher specification nodes in our cluster; by doing so, we increase the resources in each node.

## References

### Author

- https://blog.devgenius.io/analyzing-patent-data-using-spark-and-airflow-74a6860b03ac
- https://github.com/tjoakarlina/Udacity-Patents-Analytics-Data-Pipeline

### About Patent

- [What is a patent?](https://www.wipo.int/patents/en/)
- [WIPO Report](https://www.wipo.int/edocs/pubdocs/en/wipo-pub-944-2022-en-world-intellectual-property-report-2022.pdf)

### USPTO PatentsView

- [PatentsView](https://patentsview.org/)

### Geonames (Data on country latitude and longitude and country information)

- [Geonames](https://www.geonames.org/)

### Spark Resources

- [How to structure pyspark project](https://github.com/AlexIoannides/pyspark-example-project)
- [Spark NLP](https://nlp.johnsnowlabs.com/)
- [Use Spark on Amazon Redshift with connector](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-redshift.html)

### Airflow Resources

- [Running airflow using docker](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html)
- [How to submit EMR job from airflow](https://www.startdataengineering.com/post/how-to-submit-spark-jobs-to-emr-cluster-from-airflow/)

### Redshift Resources

- [Redshift Engineering's Advanced Table Design](https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-distribution-styles-and-distribution-keys/)
- [Scaling Amazon Redshift](https://aws.amazon.com/blogs/big-data/scale-amazon-redshift-to-meet-high-throughput-query-requirements/)

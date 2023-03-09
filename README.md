# Data Engineering Intensive Training Program

**Hit the ⭐️ button if you like the repo.**

## Join the Program

Join the 55-hour intensive training program now. Price is $175 /-

[Book your seat today!](https://sparshcloud.typeform.com/to/fX9s14Ir)

For more information, read the [faqs](b3-misc/faq.md).

## Curriculum

### Data Serving

#### SQL Data Modeling

* [ ] Building a sql data model for a music company in Postgres
* [ ] Build a Star Schema based Data Model in Postgres on the AirBnB dataset [[source code](04-serving/lab-airbnb-postgres-datamodel/)]
* [ ] Car company Data Model in MySQL [[source code](04-serving/lab-cars-mysql-datamodel/)]
* [ ] Create a star schema from 3NF schema on DVD rental Pagila dataset [[source code](04-serving/lab-dvd-rental-datamodel/)]
* [ ] Create a Postgres data model of Google Playstore dataset [[source code](04-serving/lab-google-playstore-datamodel/)]
* [ ] Inegi Snowflake Data Model [[source code](04-serving/lab-inegi-snowflake-datamodel/)]
* [ ] Northwind Data Model in MySQL [[source code](04-serving/lab-mysql-northwind-datamodel/)]
* [ ] Retail Store Data Model in MySQL [[source code](04-serving/lab-mysql-retail-store-datamodel/)]
* [ ] Creating a Bus Rapid Transit (BRT) Database in Postgres [[source code](04-serving/lab-postgres-busrapid-transit/)]
* [ ] Create Fact and Dimension Tables from Denormalized Raw Data [[source code](04-serving/lab-postgres-elt-datamodel/)]
* [ ] Postgres e-Wallet Data Model [[source code](04-serving/lab-postgres-ewallet-datamodel/)]
* [ ] Housing Data Model with CDC and SCD Type 2 [[source code](04-serving/lab-postgres-housing-cdc-scd/)]
* [ ] Credit Debit Finance Data Model in Snowflake [[source code](04-serving/lab-snowflake-creditdebit-datamodel/)]
* [ ] Sparkify Music Company Data Model in Postgres [[source code](04-serving/lab-sparkify-data-model-postgres/)]

#### NoSQL Data Modeling

* [ ] Building a nosql data model for a music company in Cassandra
* [ ] Create a NoSQL Data Model for a Digital Music Library using Cassandra [[source code](02-storage/datalakes/lab-adl-securing-monitoring-lakes/)]
* [ ] Create a NoSQL Data Model for an Email System using Cassandra [[source code](04-serving/cassandra-email-data-model/)]
* [ ] Create a NoSQL Data Model for Hotel Reservations using Cassandra [[source code](04-serving/cassandra-hotel-reservations/)]
* [ ] Create a NoSQL Data Model for Investment Accounts or Portfolios using Cassandra [[source code](04-serving/cassandra-investment-data-model/)]
* [ ] Create a NoSQL Data Model for Temperature Monitoring Sensor Networks using Cassandra [[source code](04-serving/cassandra-sensor-data-model/)]
* [ ] Create a NoSQL Data Model for Online Shopping Carts using Cassandra [[source code](04-serving/cassandra-shopping-cart-data-model/)]
* [ ] Ingest Movies data into CouchDB database [[source code](02-storage/nosql-databases/couchdb/lab-couchdb-movies-data-migration/)]

#### Visualization

* [ ] Streaming Analytics and Dashboards - Connect to a BigQuery data source, Create reports and charts to visualize BigQuery data [[source code](08-visualization/looker-studio/lab-gcp-streaming-analytics.md/)]

### Data Extraction

#### API

* [ ] archive.org [[source code](03-processing/pubsub/lab-gcp-pubsub.md/)]
* [ ] dummyjson [[source code](05-extraction/api/lab-dummyjson/)]
* [ ] exchangerates [[source code](05-extraction/api/lab-exchangerates/)]
* [ ] coinmarketcap [[source code](05-extraction/api/lab-extract-coinmarketcap/)]
* [ ] opennotify [[source code](05-extraction/api/lab-extract-opennotify/)]
* [ ] git [[source code](05-extraction/api/lab-processing-rest-payloads-git/)]
* [ ] saveonfoods [[source code](05-extraction/api/lab-saveonfoods/)]
* [ ] twitter [[source code](05-extraction/api/lab-twitter/)]
* [ ] datausa [[source code](05-extraction/api/lab-uspopulation/)]
* [ ] git and Hacker News [[source code](05-extraction/api/lab-hackernews-git-api/)]

#### Faker

* [ ] Extract synthetic data using Faker library in python [[source code](05-extraction/faker/lab-generate-data-with-faker/)]

#### Scraping

* [ ] Extract data using Web Scraping from Finance websites [[source code](05-extraction/webscraping/lab-finance-extract-load/)]

### Data Pipelines

* [ ] Getting started with Airflow [[source code](06-orchestration/airflow/lab-airflow-getting-started/)]
  * [ ] Install Airflow in local system
  * [ ] Starting Airflow Web server and Scheduler
  * [ ] Building a BASH commands execution pipeline in Airflow
  * [ ] Building a CSV to JSON pipeline in Airflow
* [ ] Integrate email notifications in Airflow with AWS SNS/SES service [[source code](06-orchestration/airflow/lab-airflow-email-notifications/)]
* [ ] Copying BigQuery Tables Across Different Locations using Cloud Composer [[source code](02-storage/warehouses/bigquery/lab-gcp-bigquery-composer/)]
* [ ] Bike Sharing Service Data Pipeline using Cloud Composer [[source code](06-orchestration/airflow/lab-bike-sharing-service-pipeline/)]
* [ ] Forex ETL with Airflow [[source code](06-orchestration/airflow/lab-forex-etl/)]
* [ ] Building an Airflow ETL pipeline to pull NFT data from Github and store in SQLite database [[source code](06-orchestration/airflow/github-nft/)]
* [ ] IMDB Spark ETL [[source code](06-orchestration/airflow/lab-imdb-spark-etl/)]
  * [ ] Build a data pipeline that download data
  * [ ] Process it
  * [ ] Calculate the hight profit movies
  * [ ] Save the processed data into Postgres database
* [ ] Building Data Ingestion Pipelines using Azure Data Factory [[Source code](06-orchestration/azure-data-factory/lab-data-ingestion-pipeline/)]
  * [ ] This lab covers ingesting data using Azure Data Factory and copying data between Azure SQL Database and Azure Data Lake
  * [ ] Recipe 1 - Provisioning Azure Data Factory
  * [ ] Recipe 2 - Copying files to a database from a data lake using a control flow and copy activity
  * [ ] Recipe 3 - Triggering a pipeline in Azure Data Factory
  * [ ] Recipe 4 - Copying data from a SQL Server virtual machine to a data lake using the Copy data wizard
* [ ] Incremental Data Loading using Azure Data Factory [[Source code](06-orchestration/azure-data-factory/lab-adf-incremental-loading/)]
  * [ ] This lab covers various methods to perform data loading in incremental fashion
  * [ ] Recipe 1 - Using Watermarking
  * [ ] Recipe 2 - Using File Timestamps
  * [ ] Recipe 3 - Using File partitions and folder structures
* [ ] Assignment - Build ETL Pipeline in Airflow using Toll data [[source code](06-orchestration/airflow/lab-tolldata/)]
* [ ] Develop Batch Processing Solution using Azure Data Factory [[Source code](06-orchestration/azure-data-factory/lab-batch-processing-solution/)]
  * [ ] In this lab, we design an end-to-end batch processing solution by using Data Factory, Data Lake, Spark, Azure Synapse Pipelines, PolyBase, and Azure Databricks
  * [ ] Recipe 1 - Data Ingestion using Data Flow
  * [ ] Recipe 2 - Data Transformation using Azure Databricks
  * [ ] Recipe 3 - Data Serving using PolyBase
  * [ ] Recipe 4 - Data Pipeline using Azure Data Factory Pipeline
  * [ ] Recipe 5 - End to end data processing with Azure Batch
* [ ] Building and Executing a Pipeline Graph with Data Fusion [[source code](06-orchestration/datafusion/lab-datafusion-pipeline/)]
* [ ] Prefect Getting Started [[source code](06-orchestration/prefect/lab-prefect-getting-started/)]
* [ ] Athena Query Orchestration with AWS Step Functions with SNS notifications [[source code](06-orchestration/stepfunctions/lab-stepfunction-athena-sns/)]
* [ ] AWS Step Functions and Amazon SQS to design and run a serverless workflow that orchestrates a message queue-based microservice [[source code](06-orchestration/stepfunctions/lab-stepfunction-ecomm-sqs/)]

### DevOps

* [ ] Introduction to Infra-as-code [[link to note](07-devops/infra-as-code.md/)]
* [ ] Introduction to Dockers [[link to note](07-devops/docker/)]
* [ ] Deploy docker in Amazon ECS [[source code](07-devops/ecs/lab-deploy-simple-docker-ecs/)]
* [ ] Create and managing Cloudformation stacks with AWS CLI [[source code](07-devops/cloudformation/)]
* [ ] Building your first FastAPI application [[source code](07-devops/fastapi/lab-simple-api/)]
* [ ] Building FastAPI application and Dockerize it [[source code](07-devops/fastapi/lab-simple-api-docker/)]
* [ ] FastAPI applications [[source code](07-devops/fastapi/)]
  * [ ] Online Academic Discussion Forum API
  * [ ] Online Book Reselling System API
  * [ ] Auction System
  * [ ] ERP System
  * [ ] Todo App
  * [ ] Task Planner System
  * [ ] Fitness Club Management System API
  * [ ] NewsStand Manegement System API
  * [ ] Poverty Analysis System API
  * [ ] Online Recipe System API
  * [ ] Online Restaurant Review System API
  * [ ] Intelligent Tourist System API
* [ ] FastAPI DevOps [[source code](07-devops/fastapi/lab-fastapi-devops/)]
  * [ ] Build and deploy a FastAPI
  * [ ] Serverless deploy using AWS's SAM framework
  * [ ] Use Cloudformation stack to automate the pipeline CICD
* [ ] Build and deploy NodeJS Kubia app in Kubernetes [[source code](07-devops/kubernetes/lab-kubernetes-kubia-app/)]
* [ ] Build Address parsing system in python and dockerize it [[source code](07-devops/docker/lab-assignment-etl-docker/)]

### Data Science & Machine Learning

* [ ] Basics of Regression and Classification models on Tabular data
* [ ] Getting started with NLP Deep Learning
  * [ ] Text Classification
  * [ ] Topic Modeling
  * [ ] Chatbots
  * [ ] Language Modeling
  * [ ] Named Entity Recognition
  * [ ] Text Clearning
  * [ ] Text Embedding
  * [ ] Text Generation
  * [ ] Text Similarity
  * [ ] Text Summarization
  * [ ] Transformers
  * [ ] Word2vec
* [ ] Getting started with Recommender Systems
  * [ ] Content-based
  * [ ] Collaborative
  * [ ] Hybrid
  * [ ] Session-based
  * [ ] Candidate Retrieval Model
  * [ ] Scoring and Ranking Model

#### Computer Vision

* [ ] Common Use Cases [[link to note](19-computer-vision/)]
  * [ ] Face Detection and Recognition
  * [ ] Image Classification
  * [ ] Image Similairty
  * [ ] Image Segmentation
  * [ ] Object Detection
  * [ ] Pose Estimation
  * [ ] Object Tracking
  * [ ] Scene Text Recognition
  * [ ] Video Classification
  * [ ] Video Action Recognition
* [ ] Video Classification Modeling with X3D Model [[source code](19-computer-vision/lab-video-classification/)]

### Capstones

* [ ] ACLED ETL Data Pipeline for war and conflict analysis (Airflow, Postgres, Glue, Spark) [[source code](12-capstones/acled/)]
* [ ] Sales & Orders ELT Data Pipeline (dbt, Redshift, SQL, Jinja) [[source code](12-capstones/dbt-redshift/)]
* [ ] Building End to end data pipeline in AWS [[source code](12-capstones/cloudmaze/)]
  * [ ] Activity 1: Ingestion with DMS
  * [ ] Activity 2: Data Lake Hydration
  * [ ] Activity 3: DMS Migration
  * [ ] Activity 4: Transforming data with Glue - Data Validation and ETL
  * [ ] Activity 5: Query and Visualize
* [ ] Funflix - Australian media company [[source code](12-capstones/funflix/)]
  * [ ] Design the data warehouse for Funflix
  * [ ] Build and deploy the data pipeline for Funflix's multi-region business
  * [ ] Build a data lake for the organization
* [ ] Datalake Schema Correction (AWS S3, Glue, Athena) [[source code](12-capstones/hmc/)]
* [ ] Kortex [[source code](12-capstones/kortex/)]
  * [ ] Design a data platform - MySQL (OLTP) and MongoDB (NoSQL)
  * [ ] Design and implement a data warehouse and generate reports from the data
  * [ ] Design a reporting dashboard that reflects the key metrics of the business
  * [ ] Extract data from OLTP, and NoSQL databases
  * [ ] Transform it and load it into the data warehouse
  * [ ] Create an ETL pipeline
  * [ ] Create a Spark connection to the data warehouse, and then deploy a machine learning model
* [ ] Movie Review Sentiment Analysis Pipeline [[source code](12-capstones/movie-sentiment/)]
* [ ] Building Recommender System from Scratch [[source code](12-capstones/recofront/)]
  * [ ] Front-end website built with Plotly Dash
  * [ ] Clickstream data collection using Divolte pipeline
  * [ ] Model building in python
  * [ ] Recommendation Serving
* [ ] Reddit Submissions, Authors and Subreddits analysis [[source code](12-capstones/reddit/)]
* [ ] Data Pipeline with dbt, Airflow and Great Expectations [[source code](12-capstones/robust-data-pipeline/)]
* [ ] Sparkify [[source code](12-capstones/spectrum/)]
  * [ ] SQL Data Modeling with Postgres
  * [ ] NoSQL Data Modeling with Cassandra
  * [ ] Data Lake with AWS and PySpark
  * [ ] Data Warehouse with Redshift
  * [ ] Data Pipeline with Airflow
* [ ] US Immigration analysis and data pipeline [[source code](12-capstones/us-immigration/)]
  * [ ] Data Load into S3
  * [ ] Data Preprocessing with PySpark
  * [ ] Data Modeling and Warehousing with Amazon Redshift
  * [ ] Advanced analytics using Python and Matplotlib
  * [ ] Convert the whole process into an airflow pipeline
* [ ] CitiBike Trip Histories Data Pipeline [[source code](12-capstones/citibike-trip-histories/)]
  * [ ] Build an end-to-end data pipeline
  * [ ] Cloud: GCP
  * [ ] Data Lake (DL): GCS
  * [ ] Data Warehouse (DWH): BigQuery
  * [ ] Infrastructure as code (IaC): Terraform
  * [ ] Workflow orchestration: Airflow
  * [ ] Transforming data: DBT
  * [ ] Data Visualization: Google Data Studio
* [ ] Global Historical Climatology Network Daily Data Pipeline [[source code](12-capstones/climate/)]
  * [ ] Build a global historical climatology network data pipeline that runs daily
  * [ ] Cloud: GCP
  * [ ] Infrastructure as code (IaC): Terraform
  * [ ] Workflow orchestration: Airflow (ingestion pipeline and transformation pipeline)
  * [ ] Data Warehouse: BigQuery
  * [ ] Data Lake: GCS
  * [ ] Batch processing/Transformations: dbt cloud or DataProc/Spark (transformation pipeline)
  * [ ] Dashboard: Google Data Studio

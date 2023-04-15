# Recohut Data Bootcamps

Hit the ⭐️ button if you like the repo

![bigpicture drawio](https://user-images.githubusercontent.com/62965911/226115094-3ca039b1-0ee6-48f6-85b2-7303bb9c9cf8.svg)

- Programming

  - Python
    - Lab: Lists and dictionaries
    - Lab: For loops and while loops
    - Lab: Functions and Inline functions
    - Lab: Reading data from flat files - csv, json, parquet, avro, excel, txt
    - Lab: Read/Write and Manipulate Data using Pandas
    - Lab: Pulling data from APIs using requests library
    - Lab: Reading and writing data to databases using psycopg2 and sqlalchemy library
    - Lab: Reading data from S3 and athena using aws data wrangler library
    - Lab: Pull credentials from Secrets Manager using boto3 library

  - PySpark
    - Lab: Create your first databricks cluster
    - Lab: Create your first databricks notebook

- Storages

  - Databases
    - [Lab: db2 BookShop and PetSale Data Ingestion and Stored Procedure](docs/02-storage/db2/lab-dbt-bookshop-petsale-data-ingestion/)
    - [Lab: OLAP Analytics on bank, TPCH and NYC Taxi datasets using DuckDB](docs/02-storage/duckdb/lab-analytics-bank-tpch-nyctaxi/)
    - [Lab: Extract from Hipolabs API, Transform and Load into SQLite database](docs/02-storage/lab-sqlite-hipolabs-api/)

  - NoSQL Databases
    - [Apache Cassandra](docs/02-storage/cassandra.md)
    - [GCP BigTable](docs/02-storage/gcp-bigtable.md)
    - [AWS DynamoDB](docs/02-storage/aws-dynamodb.md)
    - [Apache CouchDB](docs/02-storage/apache-couchdb.md)
    - [MongoDB](docs/02-storage/mongodb.md)
    - [Lab: Getting started with Cassandra](docs/02-storage/lab-getting-started-with-cassandra/)
    - [Lab: Streaming Data Processing - Streaming Data Pipelines into GCP Bigtable](docs/02-storage/bigtable/lab-gcp-streaming-bigtable/)
    - [Lab: Cassandra on Cloud with Amazon Keyspaces](docs/02-storage/lab-amazon-keyspaces/)
    - [Lab: Fundamentals of DynamoDB](docs/02-storage/lab-intro-to-dynamodb/)
    - [Lab: Getting started with MongoDB](docs/02-storage/lab-mongodb-basics/)
    - [Lab: Ingest Movies data into CouchDB database](docs/02-storage/lab-couchdb-movies-data-migration/)

  - Warehouses
    - [Data Warehouses](docs/02-storage/data-warehouses.md)
    - [Amazon Athena](docs/02-storage/athena.md)
    - [Project: Athena Federated](docs/02-storage/project-athena-federated/)
    - [Amazon Redshift](docs/02-storage/redshift.md)
    - [Lab: Data Loading into Redshift](docs/02-storage/lab-redshift-data-loading.md)
    - [Lab: Data Loading into Redshift using Python](docs/02-storage/lab-redshift-data-loading-python.md)
    - [Lab: Data Loading into Redshift and Analysis](docs/02-storage/lab-redshift-data-loading-analysis.md)
    - [Lab: Redshift Table Design and Query Tuning](lab-redshift-table-design-query-tuning.md)
    - [Lab: Implement a slowly changing dimension in Redshift](docs/02-storage/lab-redshift-scd.md)
    - [Lab: Implement a slowly changing dimension in Redshift 2](docs/02-storage/lab-redshift-scd-2.md)
    - [Lab: Redshift Ongoing Load - ELT](docs/02-storage/lab-redshift-ongoing-load-elt.md)
    - [Lab: Redshift Spectrum Query Data Lake](docs/02-storage/lab-redshift-spectrum-query-datalake.md)
    - [Lab: Redshift Spectrum Query Tuning](docs/02-storage/lab-redshift-spectrum-query-tuning.md)
    - [Accelerate Application Development with Real Time Streams in Amazon Redshift](https://bit.ly/3Se99Ur)
    - [GCP BigQuery](docs/02-storage/bigquery.md)
    - [Snowflake](docs/02-storage/snowflake.md)

  - Data Lakes
    - [What is a Data Lake?](docs/02-storage/datalakes.md)
    - [Why we need Data Lakes?](docs/02-storage/why-datalakes.md)
    - [On-premises Hadoop cluster vs Cloud data lakes](hadoop-vs-datalake.md)
    - [Components of the cloud data lake architecture](docs/02-storage/datalake-components.md)
    - [Azure Data Lakes](azure-datalake.md)
    - [Google Cloud Storage (GCS)](gcs.md)
    - Lab: Working with S3 using Boto3 in Python
    - [Lab: Building a data lake for a healthcare company with AWS, S3 and Athena](docs/02-storage/lab-datalake-healthcare-s3-glue-athena/)
    - [Lab: Creating and Managing Data in Azure Data Lake](docs/02-storage/lab-adl-create-manage-data/)
    - [Lab: Securing and Monitoring Data in Azure Data Lake](docs/02-storage/lab-adl-securing-monitoring-lakes/)

  - Lakehouses
    - [Data Lakehouses](docs/02-storage/data-lakehouses.md)
    - [Deltalake](docs/02-storage/deltalake.md)
    - [Apache Hudi](docs/02-storage/apache-hudi.md)
    - [Apache Iceberg](docs/02-storage/apache-iceberg.md)
    - [Lab: Read Delta Tables stored in Amazon S3 with Python](docs/02-storage/lab-read-s3-delta-in-python/)
    - [Lab: Build a serverless transactional data lake with Apache Iceberg, Amazon EMR Serverless, and Amazon Athena](docs/02-storage/lab-glue-emr-iceberg-serverless-lakehouse/)
    - [Lab: The Easy Ways to Clean Up Production Messes](docs/02-storage/lab-production-cleaning-deltalake/)
    - [Lab: Implement slowly changing dimensions in a data lake using AWS Glue and Delta](docs/02-storage/lab-scd-glue-delta)

  - Data Meshes
    - [What is Data Mesh?](docs/02-storage/data-mesh-basics.md)
    - [Case Study: Messflix (hypothetical)](docs/02-storage/casestudy-messflix-hypothetical.md)

- Data Processing

  - Databricks
    - [Databricks Getting Started Guide](03-processing/databricks/)
    - [Lab: Building a Cybersecurity Lakehouse for CrowdStrike Falcon Events in Databricks](03-processing/databricks/lab-cybersecurity-databricks/)
    - [Lab: Databricks AWS Integration and Clickstream Analysis](03-processing/databricks/lab-databricks-clickstream/)
    - [Lab: Create an elementary Data Lakehouse using Databricks and the Delta lake technology](03-processing/databricks/lab-databricks-deltalake/)
    - [Lab: Delta Lake Optimizations](03-processing/databricks/lab-deltalake-optimizations/)
    - [Lab: Compare dbt and Delta Live Tables (dlt) for data transformation](03-processing/databricks/lab-dlt-dbt/)
    - [Lab: Unlocking the Power of Health Data With a Modern Data Lakehouse](03-processing/databricks/lab-healthcare-databricks/)
    - [Lab: Real-time Health Tracking and Monitoring System](03-processing/databricks/lab-iot-health-tracker/)
    - [Lab: Simplifying Data Engineering and Analytics with Delta](03-processing/databricks/lab-loan-application/)
    - [Lab: Real-Time Point-of-Sale Analytics With the Data Lakehouse](03-processing/databricks/lab-retail-pos-databricks/)
    - [Lab: Processing Data Using Azure Databricks](03-processing/databricks/lab-data-processing-azure-db/)
    - [Project: Data Engineering with Databricks](03-processing/databricks/project-databricks-de/)
    - [Project: Data Engineer Learner Path with Databricks](03-processing/databricks/project-learnerbricks/)
    - [Project: Advanced Data Engineering with Databricks](03-processing/databricks/project-advancedbricks/)
    - [Project: Databricks PySpark Ecommerce Data Processing Case Study](03-processing/databricks/project-bedbricks/)
    - [Project: Data Pipeline with Databricks PySpark and Superset](03-processing/databricks/project-databricks-superset/)

  - AWS EMR
    - [AWS EMR Getting Started Guide](03-processing/aws-emr.md)
    - [Lab: Creating and submitting Word count Spark Job in EMR Serverless](03-processing/lab-emr-serverless/)

  - AWS Glue Studio
    - [Lab: Advanced Data Engineering and Data Processing with AWS Glue Jobs](03-processing/lab-glue-advanced/)
    - [Lab: Handle UPSERT data operations using open-source Delta Lake and AWS Glue](03-processing/lab-glue-deltalake-cdc-upsert/)
    - [Lab: Create your own reusable visual transforms for AWS Glue Studio](03-processing/lab-glue-studio-custom-transforms/)
    - [Lab: Tickets ETL with Glue Studio](03-processing/lab-glue-studio-tickets/)
    - [Lab: CSV to Parquet Transformation with Glue Studio](03-processing/lab-csv-to-parquet-conversion/)

  - AWS Lambda Function
    - [AWS Lambda Function Getting Started Guide](03-processing/aws-lambda.md)
    - [AWS Lambda Snippets](03-processing/aws-lambda-snippets.md)
    - [Lab: Building a near real-time serverless data pipeline with AWS lambda function](03-processing/lab-lambda-csv-parquet/)

  - Amazon Kinesis
    - [Amazon Kinesis Getting Started Guide](03-processing/aws-kinesis.md)
    - [Lab: Real Time Apache Log Analytics with Kinesis](03-processing/lab-kinesis-apache-logs/)
    - [Lab: Real-Time Clickstream Anomaly Detection with Kinesis](03-processing/lab-kinesis-clickstream-anomaly/)

  - Apache Beam
    - [Apache Beam Getting Started Guide](03-processing/apache-beam.md)
    - [Lab: Getting started with Apache Beam](03-processing/lab-getting-started-with-beam/)
    - [Lab: MapReduce in Beam using Python](03-processing/lab-gcp-beam-mapreduce/)

  - GCP Dataflow
    - [Lab: Build a simple Dataflow Pipeline (Python)](03-processing/lab-gcp-dataflow-pipeline.md)
    - [Lab: Batch Analytics Pipelines with Cloud Dataflow (Python)](03-processing/lab-gcp-dataflow-batch-pipeline.md)
    - [Lab: Providing Side Inputs in Dataflow (Python)](03-processing/lab-gcp-dataflow-side-inputs.md)
    - [Lab: Using Dataflow for Streaming Analytics (Python)](03-processing/lab-gcp-dataflow-stream-pipeline.md)
    - [Lab: Writing an ETL Pipeline using Apache Beam and Cloud Dataflow (Python)](03-processing/lab-gcp-serverless-dataflow.md)
    - [Lab: ETL Processing on Google Cloud Using Dataflow and BigQuery](03-processing/lab-dataflow-bigquery-etl.md)

  - Ray
    - [Ray Getting Started Guide](03-processing/ray.md)
    - [Lab: Ray Core Basics](03-processing/lab-ray-core-basics/)
    - [Lab: Ray AIR Basics](03-processing/lab-ray-air-basics/)

  - GCP Dataproc
    - [GCP Dataproc Getting Started Guide](03-processing/gcp-dataproc.md)
    - [Lab: Running Apache Spark jobs on Cloud Dataproc](03-processing/lab-gcp-dataproc/)

  - Azure HDInsight
    - [Lab: Build Data Pipeline with HDInsight](03-processing/lab-azure-hdinsight-simple-data-processing/)

  - Azure Synapse Analytics
    - [Azure Synapse Analytics Getting Started Guide](03-processing/azure-synapse-analytics.md)
    - [Lab: Transforming Data Using Azure Synapse Dataflows](03-processing/lab-azure-synapse-dataflows/)
    - [Lab: Processing Data Using Azure Synapse Analytics](03-processing/lab-azure-synapse-data-processing/)
    - [Lab: Implementing the Serving Layer Star Schema](03-processing/lab-azure-synapse-implementing-star-schema/)

  - GCP Dataprep
    - [Lab: Creating a Data Transformation Pipeline with Cloud Dataprep](03-processing/lab-gcp-dataprep.md)

  - GCP PubSub
    - [GCP PubSub Getting Started Guide](03-processing/gcp-pubsub.md)
    - [Lab: Streaming Data Pipelines with GCP PubSub](03-processing/lab-gcp-pubsub-processing.md/)
    - [Lab: Publish Streaming Data into PubSub](03-processing/lab-gcp-pubsub.md/)

  - Apache Kafka
    - [Apache Kafka Getting Started Guide](03-processing/apache-kafka.md)
    - [Lab: Getting started with Confluent Kafka and Python](03-processing/lab-confluent-python/)
    - [Lab: Real-time CDC-enabled Extract and Load Pipeline with Kafka on Cloud](03-processing/lab-confluent-kafka-faker/)
    - [Lab: Real-time fraud detection by applying filter in Kafka topic](03-processing/lab-kafka-fraud-detection/)
    - [Lab: Kafka Streams for NYC Taxi data](03-processing/lab-kafka-nyctaxi/)
    - [Lab: Kafka on Cloud with Amazon ECS and Container Orchestration](03-processing/lab-kafka-python-ecs/)
    - [Lab: Realtime Streaming analytics with Apache Kafka and Spark Streaming](03-processing/lab-kafka-spark-streaming/)
    - [Lab: Stock Market Kafka Real Time](03-processing/lab-kafka-stock-market/)
    - [Lab: Data Streaming Pipeline with Kafka for livetolldata](03-processing/lab-kafka-toll-analysis/)
    - [Lab: Building an event-driven IKEA app with Kafka](03-processing/project-ikea/)
    - [Lab: Getting started with Kafka and CLI](03-processing/lab-kafka-cli/)
    - [Lab: Getting started with Kafka and Python](03-processing/lab-kafka-python/)
    - [Project: Building an event-driven IKEA app with Kafka](03-processing/project-kafka-ikea)

  - Apache Druid
    - [Apache Druid Getting Started Guide](03-processing/apache-druid.md)

  - Apache Flink
    - [Apache Flink Getting Started Guide](03-processing/apache-flink.md)
    - [Lab: Real-time Taxi Price Model based Prediction using Flink](03-processing/lab-flink-taxi-pricing/)
    - [Lab: Real-time Twitter Stream Wordcount using Flink](03-processing/lab-flink-twitter-stream-processing/)
    - [Lab: Flink Kafka Sink](03-processing/lab-flink-kafka-sink/)
    - [Lab: Flink Kafka Source](03-processing/lab-flink-kafka-source/)

  - Snowpark
    - [Snowpark Getting Started Guide](03-processing/lab-snowpark.md)
    - [Lab: Churn Analytics Demo with dbt Snowpark Python models](03-processing/lab-snowpark-churnpark/)
    - [Lab: Getting started with dbt and Snowpark](03-processing/lab-snowpark-dbtsnowpy/)
    - [Lab: FIFA prediction model with dbt and Snowpark](03-processing/lab-snowpark-fifapark/)
    - [Lab: Jaffle shop analytics modeling with dbt and Snowpark](03-processing/lab-snowpark-jafflepark/)
    - [Lab: Knoema Regression with dbt Snowpark and Streamlit](03-processing/lab-snowpark-knoema-regression/)

  - dbt
    - [dbt Getting Started Guide](03-processing/dbt.md)
    - [Lab: Building an ELT pipeline for a cab service company using dbt and Postgres](03-processing/lab-dbt-nyctaxi/)
    - [Lab: dbt Postgres on Jaffle Shop data](03-processing/lab-dbt-jaffle-shop/)
    - [Lab: dbt Snowflake on Knoema data](03-processing/lab-dbt-knoema/)
    - [Lab: dbt Postgres on Olist Retail data](03-processing/lab-dbt-olist/)
    - [Lab: dbt BigQuery on Stack Exchange data](03-processing/lab-dbt-stackexchnge/)
    - [Lab: Building an ELT Pipeline with dbt and Amazon Redshift on TICKIT data](03-processing/lab-dbt-tickit/)
    - [Lab: dbt Snowflake on TPCH data](03-processing/lab-dbt-tpch/)

- Data Modeling

  - SQL Data Modeling
    - [SQL Data Modeling](04-data-modeling/sql-data-modeling.md)
    - [Inmon versus the Kimball data model](04-data-modeling/inmon-vs-kimball.md)
    - [Stages of Data Modeling](04-data-modeling/data-modeling-stages.md)
    - [3NF/ Relational Modeling](04-data-modeling/3nf-data-modeling.md)
    - [Dimensional Modeling](04-data-modeling/dimensional-modeling.md)
    - [Data Vault Modeling](04-data-modeling/data-vault-modeling.md)
    - [Steps of Building Data Models](04-data-modeling/data-modeling-steps.md)
    - [Designing SCDs](04-data-modeling/designing-scd.md)
    - [Designing for incremental loading](04-data-modeling/designing-incremental-loading.md)
    - [Data Warehousing](04-data-modeling/data-warehousing.md)
    - [Normalization vs Denormalization](04-data-modeling/normalization-vs-denormalization.md)
    - [CAP Theorem](04-data-modeling/cap-theorem.md)
    - [Data Modeling Quiz](04-data-modeling/quiz.md)
    - [Lab: Build a Star Schema based Data Model in Postgres on the AirBnB dataset](04-data-modeling/lab-airbnb-postgres-datamodel/)
    - [Lab: Car company Data Model in MySQL](04-data-modeling/lab-cars-mysql-datamodel/)
    - [Lab: Create a star schema from 3NF schema on DVD rental Pagila dataset](04-data-modeling/lab-dvd-rental-datamodel/)
    - [Lab: Create a Postgres data model of Google Playstore dataset](04-data-modeling/lab-google-playstore-datamodel/)
    - [Lab: Inegi Snowflake Data Model](04-data-modeling/lab-inegi-snowflake-datamodel/)
    - [Lab: Northwind Data Model in MySQL](04-data-modeling/lab-mysql-northwind-datamodel/)
    - [Lab: Retail Store Data Model in MySQL](04-data-modeling/lab-mysql-retail-store-datamodel/)
    - [Lab: Creating a Bus Rapid Transit (BRT) Database in Postgres](04-data-modeling/lab-postgres-busrapid-transit/)
    - [Lab: Create Fact and Dimension Tables from Denormalized Raw Data](04-data-modeling/lab-postgres-elt-datamodel/)
    - [Lab: Postgres e-Wallet Data Model](04-data-modeling/lab-postgres-ewallet-datamodel/)
    - [Lab: Housing Data Model with CDC and SCD Type 2](04-data-modeling/lab-postgres-housing-cdc-scd/)
    - [Lab: Credit Debit Finance Data Model in Snowflake](04-data-modeling/lab-snowflake-creditdebit-datamodel/)
    - [Lab: Sparkify Music Company Data Model in Postgres](04-data-modeling/lab-sparkify-data-model-postgres/)

  - NoSQL Data Modeling
    - [NoSQL Data Modeling](04-data-modeling/nosql-data-modeling.md)
    - [Lab: Create a NoSQL Data Model for a Digital Music Library using Cassandra](04-data-modeling/lab-cassandra-digital-music-library/)
    - [Lab: Create a NoSQL Data Model for an Email System using Cassandra](04-data-modeling/lab-cassandra-email-data-model/)
    - [Lab: Create a NoSQL Data Model for Hotel Reservations using Cassandra](04-data-modeling/lab-cassandra-hotel-reservations/)
    - [Lab: Create a NoSQL Data Model for Investment Accounts or Portfolios using Cassandra](04-data-modeling/lab-cassandra-investment-data-model/)
    - [Lab: Create a NoSQL Data Model for Temperature Monitoring Sensor Networks using Cassandra](04-data-modeling/lab-cassandra-sensor-data-model/)
    - [Lab: Create a NoSQL Data Model for Online Shopping Carts using Cassandra](04-data-modeling/lab-cassandra-shopping-cart-data-model/)

- Data Extraction

  - [API](05-extraction/api/)
  - [Faker](05-extraction/faker/)
  - [Web Scraping](05-extraction/webscraping/)

- Data Pipelines

  - [Airflow](06-orchestration/airflow/)
  - [Azure Data Factory](06-orchestration/azure-data-factory/)
  - [GCP Cloud DataFusion](06-orchestration/datafusion/)
  - [AWS Step Functions](06-orchestration/stepfunctions/)

- Data Visualization

  - [Flask](08-visualization/flask/)
  - [Looker Studio](08-visualization/looker-studio/)
  - [Preset](08-visualization/preset/)
  - [Streamlit](08-visualization/streamlit/)
  - AWS Quicksight

- System Design

  - [Getting Started](system-design/README.md)
  - [System Design Examples](system-design/examples.md)
  - [Databricks Case Studies](system-design/databricks-case-studies.md)

- DevOps

  - [FastAPI](07-devops/fastapi/)
  - [Containers](07-devops/containers/)
  - [Infra as Code](07-devops/iac/)

- Mathematics

  - [Getting Started](mathematics/)
  - [Probability](mathematics/probability/)
  - [Statistics](mathematics/statistics/)

- Data Science & Machine Learning

  - Basics
    - [The data science origin story](docs/docs/01-foundations/basics/origin.md)
    - [Use Cases](docs/docs/01-foundations/basics/use-cases.md)
    - [Model Deployment](docs/docs/01-foundations/basics/deployment.md)
    - [Data Splits - Train/Valid/Test sets](10-datascience/data-splits.md)
    - [Lab: Data Splits - Train/Valid/Test sets](https://nbviewer.org/gist/sparsh-ai/4eb2f3d2b4ce9643db8a319864fe9cb6)
    - [Bias-Variance Trade-Off](10-datascience/bias-variance-tradeoff.md)
    - [Metrics and Evaluation](10-datascience/metrics-and-evaluation.md)
    - [Lab: Metrics and Evaluation](https://nbviewer.org/gist/sparsh-ai/a2a8d441d00f1421e208fa88b879aab9)
    - [Lab: Optimization and Gradient Descent](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/Optimization_and_Gradient_Descent.ipynb)
    - [Lab: Feature Space and the Curse of Dimensionality](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/Feature_Space_and_the_Curse_of_Dimensionality.ipynb)
    - [Data Preparation](10-datascience/data-preparation.md)
    - [Data Encoding](10-datascience/data-encoding.md)
    - [Lab: Data Encoding](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/Data_Encoding.ipynb)
    - [Feature Selection](10-datascience/feature-selection.md)
    - [Lab: Feature Selection](https://nbviewer.org/gist/sparsh-ai/0fe63e864eaa43d7085f2b29ff859f9a)
    - [Lab: Tensorflow Datasets](https://nbviewer.org/gist/sparsh-ai/bc7dcd94e30ccacc5934b2170d34fc2d)

  - Algorithms
    - [Regression](10-datascience/regression/)
    - [K-Nearest Neighbors](10-datascience/algorithms/knn.md)
    - [Lab: K-Nearest Neighbors](https://nbviewer.org/gist/sparsh-ai/98a7e2db1bb09d4d06fa809d3b977c3a)
    - [Linear Regression](10-datascience/algorithms/linear-regression.md)
    - [Lab: Linear Regression](https://nbviewer.org/gist/sparsh-ai/4f941d5523240a17354573438c45bf65)
    - [Logistic Regression](10-datascience/algorithms/logistic-regression.md)
    - [Lab: Logistic Regression](https://nbviewer.org/gist/sparsh-ai/0ea0ae3f6ef4dc283cc6412c96175672)
    - [Decision Trees](10-datascience/algorithms/decision-trees.md)
    - [Lab: Decision Trees](https://nbviewer.org/gist/sparsh-ai/d0ff7d95e5a8ffbe2e146328a5fa4133)
    - [Random Forest](10-datascience/algorithms/random-forest.md)
    - [Gradient Boosting](10-datascience/algorithms/gradient-boosting.md)
    - [Lab: Gradient Boosting](https://nbviewer.org/gist/sparsh-ai/3ddba63345c40a323021e04ea05def21)

  - Time-Series Forecasting
    - [Prophet](docs/10-datascience/timeseries/prophet.md)
    - [Atmospheric CO2-level Prediction with Prophet](https://nbviewer.org/gist/sparsh-ai/2649176341669f493c9eeec6fb1aa7ba)

- Deep Learning

  - Basics
    - [What is Deep Learning?](10-datascience/deep-learning/deep-learning-basics.md)
    - [The Rosenblatt Perceptron](10-datascience/deep-learning/perceptron.md)
    - [Lab: Deep Learning Basics with Keras](https://nbviewer.org/github/sparsh-ai/notebooks/blob/main/deep-learning-basics-with-keras.ipynb)
    - [NLP](10-datascience/nlp/)
    - [Computer Vision](10-datascience/computer-vision/)
    - [Recommender Systems](10-datascience/recsys/)
    - [Challenges](10-datascience/challenges/)

- MLOps

    - [Concepts](17-mlops/)
    - [Code Snippets](17-mlops/code-snippets.md)

- Add-ons

    - [Capstones](12-capstones/README.md)
    - [Interview Preparation](a1-interviewprep/)
    - [Extras](b3-misc/extras.md)
    - [Resources](b3-misc/resources.md)

- Case Studies

  - [Data Engineering at Udem](https://www.slideshare.net/ankarabigdata/data-engineering-at-udemy?qid=d835f0e3-f290-4445-bd19-d6ac6824e24c&v=&b=&from_search=5)
  - [Fair - Data Ingestion with a Cloud Data Platform](a3-casestudies/fair.md)
  - [Harmony - Responsive Data Pipeline](a3-casestudies/harmony.md)
  - [Panoramic - Simplifying Data Ingestion, Transformation, And Delivery](a3-casestudies/panoramic.md)
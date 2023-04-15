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

  - Data Lakes
    - Lab: Working with S3 using Boto3 in Python

- Data Processing

  - AWS EMR
    - [AWS EMR Getting Started Guide](docs/03-processing/aws-emr.md)
    - [Lab: Creating and submitting Word count Spark Job in EMR Serverless](docs/03-processing/lab-emr-serverless/)

  - AWS Glue Studio
    - [Lab: Advanced Data Engineering and Data Processing with AWS Glue Jobs](docs/03-processing/lab-glue-advanced/)
    - [Lab: Handle UPSERT data operations using open-source Delta Lake and AWS Glue](docs/03-processing/lab-glue-deltalake-cdc-upsert/)
    - [Lab: Create your own reusable visual transforms for AWS Glue Studio](docs/03-processing/lab-glue-studio-custom-transforms/)
    - [Lab: Tickets ETL with Glue Studio](docs/03-processing/lab-glue-studio-tickets/)
    - [Lab: CSV to Parquet Transformation with Glue Studio](docs/03-processing/lab-csv-to-parquet-conversion/)

  - AWS Lambda Function
    - [AWS Lambda Function Getting Started Guide](docs/03-processing/aws-lambda.md)
    - [AWS Lambda Snippets](docs/03-processing/aws-lambda-snippets.md)
    - [Lab: Building a near real-time serverless data pipeline with AWS lambda function](docs/03-processing/lab-lambda-csv-parquet/)

  - Amazon Kinesis
    - [Amazon Kinesis Getting Started Guide](docs/03-processing/aws-kinesis.md)
    - [Lab: Real Time Apache Log Analytics with Kinesis](docs/03-processing/lab-kinesis-apache-logs/)
    - [Lab: Real-Time Clickstream Anomaly Detection with Kinesis](docs/03-processing/lab-kinesis-clickstream-anomaly/)

  - Apache Beam
    - [Apache Beam Getting Started Guide](docs/03-processing/apache-beam.md)
    - [Lab: Getting started with Apache Beam](docs/03-processing/lab-getting-started-with-beam/)
    - [Lab: MapReduce in Beam using Python](docs/03-processing/lab-gcp-beam-mapreduce/)

  - GCP Dataflow
    - [Lab: Build a simple Dataflow Pipeline (Python)](docs/03-processing/lab-gcp-dataflow-pipeline.md)
    - [Lab: Batch Analytics Pipelines with Cloud Dataflow (Python)](docs/03-processing/lab-gcp-dataflow-batch-pipeline.md)
    - [Lab: Providing Side Inputs in Dataflow (Python)](docs/03-processing/lab-gcp-dataflow-side-inputs.md)
    - [Lab: Using Dataflow for Streaming Analytics (Python)](docs/03-processing/lab-gcp-dataflow-stream-pipeline.md)
    - [Lab: Writing an ETL Pipeline using Apache Beam and Cloud Dataflow (Python)](docs/03-processing/lab-gcp-serverless-dataflow.md)
    - [Lab: ETL Processing on Google Cloud Using Dataflow and BigQuery](docs/03-processing/lab-dataflow-bigquery-etl.md)

  - Ray
    - [Ray Getting Started Guide](docs/03-processing/ray.md)
    - [Lab: Ray Core Basics](docs/03-processing/lab-ray-core-basics/)
    - [Lab: Ray AIR Basics](docs/03-processing/lab-ray-air-basics/)

  - GCP Dataproc
    - [GCP Dataproc Getting Started Guide](docs/03-processing/gcp-dataproc.md)
    - [Lab: Running Apache Spark jobs on Cloud Dataproc](docs/03-processing/lab-gcp-dataproc/)

  - Azure HDInsight
    - [Lab: Build Data Pipeline with HDInsight](docs/03-processing/lab-azure-hdinsight-simple-data-processing/)

  - Azure Synapse Analytics
    - [Azure Synapse Analytics Getting Started Guide](docs/03-processing/azure-synapse-analytics.md)
    - [Lab: Transforming Data Using Azure Synapse Dataflows](docs/03-processing/lab-azure-synapse-dataflows/)
    - [Lab: Processing Data Using Azure Synapse Analytics](docs/03-processing/lab-azure-synapse-data-processing/)
    - [Lab: Implementing the Serving Layer Star Schema](docs/03-processing/lab-azure-synapse-implementing-star-schema/)

  - GCP Dataprep
    - [Lab: Creating a Data Transformation Pipeline with Cloud Dataprep](docs/03-processing/lab-gcp-dataprep.md)

  - GCP PubSub
    - [GCP PubSub Getting Started Guide](docs/03-processing/gcp-pubsub.md)
    - [Lab: Streaming Data Pipelines with GCP PubSub](docs/03-processing/lab-gcp-pubsub-processing.md/)
    - [Lab: Publish Streaming Data into PubSub](docs/03-processing/lab-gcp-pubsub.md/)

  - Apache Kafka
    - [Apache Kafka Getting Started Guide](docs/03-processing/apache-kafka.md)
    - [Lab: Getting started with Confluent Kafka and Python](docs/03-processing/lab-confluent-python/)
    - [Lab: Real-time CDC-enabled Extract and Load Pipeline with Kafka on Cloud](docs/03-processing/lab-confluent-kafka-faker/)
    - [Lab: Real-time fraud detection by applying filter in Kafka topic](docs/03-processing/lab-kafka-fraud-detection/)
    - [Lab: Kafka Streams for NYC Taxi data](docs/03-processing/lab-kafka-nyctaxi/)
    - [Lab: Kafka on Cloud with Amazon ECS and Container Orchestration](docs/03-processing/lab-kafka-python-ecs/)
    - [Lab: Realtime Streaming analytics with Apache Kafka and Spark Streaming](docs/03-processing/lab-kafka-spark-streaming/)
    - [Lab: Stock Market Kafka Real Time](docs/03-processing/lab-kafka-stock-market/)
    - [Lab: Data Streaming Pipeline with Kafka for livetolldata](docs/03-processing/lab-kafka-toll-analysis/)
    - [Lab: Building an event-driven IKEA app with Kafka](docs/03-processing/project-ikea/)
    - [Lab: Getting started with Kafka and CLI](docs/03-processing/lab-kafka-cli/)
    - [Lab: Getting started with Kafka and Python](docs/03-processing/lab-kafka-python/)
    - [Project: Building an event-driven IKEA app with Kafka](docs/03-processing/project-kafka-ikea)

  - Apache Druid
    - [Apache Druid Getting Started Guide](docs/03-processing/apache-druid.md)

  - Apache Flink
    - [Apache Flink Getting Started Guide](docs/03-processing/apache-flink.md)
    - [Lab: Real-time Taxi Price Model based Prediction using Flink](docs/03-processing/lab-flink-taxi-pricing/)
    - [Lab: Real-time Twitter Stream Wordcount using Flink](docs/03-processing/lab-flink-twitter-stream-processing/)
    - [Lab: Flink Kafka Sink](docs/03-processing/lab-flink-kafka-sink/)
    - [Lab: Flink Kafka Source](docs/03-processing/lab-flink-kafka-source/)

  - Snowpark
    - [Snowpark Getting Started Guide](docs/03-processing/lab-snowpark.md)
    - [Lab: Churn Analytics Demo with dbt Snowpark Python models](docs/03-processing/lab-snowpark-churnpark/)
    - [Lab: Getting started with dbt and Snowpark](docs/03-processing/lab-snowpark-dbtsnowpy/)
    - [Lab: FIFA prediction model with dbt and Snowpark](docs/03-processing/lab-snowpark-fifapark/)
    - [Lab: Jaffle shop analytics modeling with dbt and Snowpark](docs/03-processing/lab-snowpark-jafflepark/)
    - [Lab: Knoema Regression with dbt Snowpark and Streamlit](docs/03-processing/lab-snowpark-knoema-regression/)

  - dbt
    - [dbt Getting Started Guide](docs/03-processing/dbt.md)
    - [Lab: Building an ELT pipeline for a cab service company using dbt and Postgres](docs/03-processing/lab-dbt-nyctaxi/)
    - [Lab: dbt Postgres on Jaffle Shop data](docs/03-processing/lab-dbt-jaffle-shop/)
    - [Lab: dbt Snowflake on Knoema data](docs/03-processing/lab-dbt-knoema/)
    - [Lab: dbt Postgres on Olist Retail data](docs/03-processing/lab-dbt-olist/)
    - [Lab: dbt BigQuery on Stack Exchange data](docs/03-processing/lab-dbt-stackexchnge/)
    - [Lab: Building an ELT Pipeline with dbt and Amazon Redshift on TICKIT data](docs/03-processing/lab-dbt-tickit/)
    - [Lab: dbt Snowflake on TPCH data](docs/03-processing/lab-dbt-tpch/)

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
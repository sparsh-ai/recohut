# BigQuery

## Steps

1. [Lab: Bigquery basics command line operations](./lab-bigquery-commandline/)
1. [Lab: Creating a Data Warehouse Through Joins and Unions](./lab-bigquery-data-warehousing/)
1. [Lab: Using BigQuery to do Analysis](./lab-bigquery-analysis/)
1. [Lab: Build and Optimize Data Warehouses with BigQuery](./lab-bigquery-optimization/)
1. [Lab: Optimizing your BigQuery Queries for Performance](./lab-bigquery-query-optimization/)
1. [Lab: Predict Visitor Purchases with a Classification Model in BigQuery ML](./lab-gcp-bigquery-ml/)
1. [Lab: Copying BigQuery Tables Across Different Locations using Cloud Composer](./lab-gcp-bigquery-composer/)
1. [Assignment: Process NYC Taxi data on BigQuery](./lab-gcp-bigquery-nyctaxi/)

## Note

> Serverless enterprise data warehouse

BigQuery is server-less, highly scalable, and cost-effective Data warehouse designed for Google cloud Platform (GCP) to store and query petabytes of data. The query engine is capable of running SQL queries on terabytes of data in a matter of seconds, and petabytes in only minutes. You get this performance without having to manage any infrastructure and without having to create or rebuild indexes. 

BigQuery supports standard SQL, so if you ever develop with relational database like Oracle, PostgreSQL, MySQL, Microsoft SQL Server, etc, it is easy to familiarize yourself with BigQuery. There are a few BigQuery functions to support modern-day requirements, and learning about them will make your job easier.

There is no infrastructure required. We don’t need to worry about the size of storage, number of processors, or memory allocation for processing query. BigQuery scales automatically to run query, and then release the resource when it is done. We don't even charged for memory or processor allocation.

Storing and querying massive datasets can be time consuming and expensive without the right hardware and infrastructure. BigQuery is a serverless, highly scalable [cloud data warehouse](https://cloud.google.com/solutions/bigquery-data-warehouse) that solves this problem by enabling super-fast SQL queries using the processing power of Google's infrastructure. Simply move your data into BigQuery and let us handle the hard work. You can control access to both the project and your data based on your business needs, such as giving others the ability to view or query your data.

### ETL, EL, and ELT

The traditional way to work with data warehouses is to start with an Extract, Transform, and Load (ETL) process, wherein raw data is extracted from its source location, transformed, and then loaded into the data warehouse. Indeed, BigQuery has a native, highly efficient columnar storage format9 that makes ETL an attractive methodology. The data pipeline, typically written in either Apache Beam or Apache Spark, extracts the necessary bits from the raw data (either streaming data or batch files), transforms what it has extracted to do any necessary cleanup or aggregation, and then loads it into BigQuery. The reference architecture for ETL into BigQuery uses Apache Beam pipelines executed on Cloud Dataflow and can handle both streaming and batch data using the same code.

Even though building an ETL pipeline in Apache Beam or Apache Spark tends to be quite common, it is possible to implement an ETL pipeline purely within BigQuery. Because BigQuery separates compute and storage, it is possible to run BigQuery SQL queries against CSV (or JSON or Avro) files that are stored as-is on Google Cloud Storage; this capability is called federated querying. You can take advantage of federated queries to extract the data using SQL queries against data stored in Google Cloud Storage, transform the data within those SQL queries, and then materialize the results into a BigQuery native table.

If transformation is not necessary, BigQuery can directly ingest standard formats like CSV, JSON, or Avro into its native storage—an EL (Extract and Load) workflow, if you will. The reason to end up with the data loaded into the data warehouse is that having the data in native storage provides the most efficient querying performance.

We strongly recommend that you design for an EL workflow if possible, and drop to an ETL workflow only if transformations are needed. If possible, do those transformations in SQL, and keep the entire ETL pipeline within BigQuery. If the transforms will be difficult to implement purely in SQL, or if the pipeline needs to stream data into BigQuery as it arrives, build an Apache Beam pipeline and have it executed in a serverless fashion using Cloud Dataflow. Another advantage of implementing ETL pipelines in Beam/Dataflow is that, because this is programmatic code, such pipelines integrate better with Continuous Integration (CI) and unit testing systems.

Besides the ETL and EL workflows, BigQuery makes it possible to do an Extract, Load, and Transform (ELT) workflow. The idea is to extract and load the raw data as-is and rely on BigQuery views to transform the data on the fly. An ELT workflow is particularly useful if the schema of the raw data is in flux. For example, you might still be carrying out exploratory work to determine whether a particular timestamp needs to be corrected for the local time zone. The ELT workflow is useful in prototyping and allows an organization to start deriving insights from the data without having to make potentially irreversible decisions too early.

### Where does BigQuery fit in the data lifecycle?

BigQuery is part of Google Cloud’s comprehensive data analytics platform that covers the entire analytics value chain including ingesting, processing, and storing data, followed by advanced analytics and collaboration. BigQuery is deeply integrated with GCP analytical and data processing offerings, allowing customers to set up an enterprise ready cloud-native data warehouse.

At each stage of the data lifecycle, GCP provides multiple services to manage data. This means customers can select a set of services tailored to their data and workflow.

![](https://user-images.githubusercontent.com/62965911/214002602-9d841ba2-318e-4688-aa9c-f524671590e3.png)

### Ingesting data into BigQuery

BigQuery supports several ways to ingest data into its managed storage. The specific ingestion method depends on the origin of the data. For example, some data sources in GCP, like Cloud Logging and Google Analytics, support direct exports to BigQuery.

BigQuery Data Transfer Service enables data transfer to BigQuery from Google SaaS apps (Google Ads, Cloud Storage), Amazon S3, and other data warehouses (Teradata, Redshift).

Streaming data, such as logs or IoT device data, can be written to BigQuery using Cloud Dataflow pipelines, Cloud Dataproc jobs, or directly using the BigQuery stream ingestion API.

You can access BigQuery by using the [Console](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-web-ui), [Web UI](https://console.cloud.google.com/bigquery?utm_source=bqui&utm_medium=link&utm_campaign=classic&project=cloud-solutions-group) or a [command-line tool](https://cloud.google.com/bigquery/docs/cli_tool) using a variety of [client libraries](https://cloud.google.com/bigquery/docs/reference/libraries) such as Java, .NET, or Python. There are also a variety of [solution providers](https://cloud.google.com/bigquery/providers) that you can use to interact with BigQuery.

### BigQuery Architecture

BigQuery’s serverless architecture decouples storage and compute and allows them to scale independently on demand. This structure offers both immense flexibility and cost controls for customers because they don’t need to keep their expensive compute resources up and running all the time. This is very different from traditional node-based cloud data warehouse solutions or on-premise massively parallel processing (MPP) systems. This approach also allows customers of any size to bring their data into the data warehouse and start analyzing their data using Standard SQL without worrying about database operations and system engineering.

![](https://user-images.githubusercontent.com/62965911/214002594-10e8a071-7a25-4bc7-94d1-57d111cc114a.png)

### Watch the video

Watch this video: https://www.youtube.com/watch?v=2UGA6b5MFI0

### Exploring a BigQuery Public Dataset

Storing and querying massive datasets can be time consuming and expensive without the right hardware and infrastructure. BigQuery is an enterprise data warehouse that solves this problem by enabling super-fast SQL queries using the processing power of Google's infrastructure. Simply move your data into BigQuery and let it handle the hard work. You can control access to both the project and your data based on your business needs, such as giving others the ability to view or query your data.

You access BigQuery through the Cloud Console, the command-line tool, or by making calls to the BigQuery REST API using a variety of client libraries such as Java, .NET, or Python. There are also a variety of third-party tools that you can use to interact with BigQuery, such as visualizing the data or loading the data. In this lab, you access BigQuery using the web UI.

You can use the BigQuery web UI in the Cloud Console as a visual interface to complete tasks like running queries, loading data, and exporting data. This hands-on lab shows you how to query tables in a public dataset and how to load sample data into BigQuery through the Cloud Console.

### Watch the videos

#### Introduction to BigQuery

Watch this video: https://www.youtube.com/watch?v=xuuXXmvRLWQ

#### Demo: Querying TB of data in seconds

Watch this video: https://www.youtube.com/watch?v=DAPiUo3sAFA

#### Analytic window functions

Watch this video: https://www.youtube.com/watch?v=B6FhilGH6NA

#### GIS functions

Watch this video: https://www.youtube.com/watch?v=9K2hTGv3SSc
# AWS Glue

[AWS Glue](https://aws.amazon.com/glue/) is a serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development. AWS Glue provides all the capabilities needed for data integration so that you can start analyzing your data and put it to use in minutes instead of months.

![key_capabilities](https://user-images.githubusercontent.com/62965911/214893307-67708ea2-5f96-4332-9c30-907a6cdfda78.png)

## Glue Data Catalog

The AWS Glue Data Catalog is a central repository to store structural and operational metadata for all your data assets. For a given data set, you can store its table definition, physical location, add business relevant attributes, as well as track how this data has changed over time. AWS Glue provides a number of ways to populate metadata into the AWS Glue Data Catalog. AWS Glue Data Catalog is Apache Hive Metastore compatible. You can point to the Glue Data Catalog endpoint and use it as an Apache Hive Metastore replacement. The metadata stored in the AWS Glue Data Catalog can be readily accessed from Glue ETL, Amazon Athena, Amazon EMR, Amazon Redshift Spectrum, and third-party services.

## Glue Crawler

AWS Glue crawler connects to a data store, progresses through a prioritized list of classifiers to extract the schema of your data and other statistics, and then populates the Glue Data Catalog with this metadata. Crawlers can run periodically to detect the availability of new data as well as changes to existing data, including table definition changes. Crawlers automatically add new tables, new partitions to existing tables, and new versions of table definitions. You can customize Glue crawlers to classify your own file types.

When you define a crawler, you choose one or more classifiers that evaluate the format of your data to infer a schema. When the crawler runs, the first classifier in your list to successfully recognize your data store is used to create a schema for your table. You can use built-in classifiers or define your own. You define your custom classifiers in a separate operation, before you define the crawlers. AWS Glue provides built-in classifiers to infer schemas from common files with formats that include JSON, CSV, and Apache Avro.

## Glue Studio

AWS Glue Studio is a new graphical interface that makes it easy to create, run, and monitor extract, transform, and load (ETL) jobs in AWS Glue. You can visually compose data transformation workflows and seamlessly run them on AWS Glue’s Apache Spark-based serverless ETL engine. You can inspect the schema and data results in each step of the job.

AWS Glue Studio is designed not only for tabular data, but also for semi-structured data, which is difficult to render in spreadsheet-like data preparation interfaces. Examples of semi-structured data include application logs, mobile events, Internet of Things (IoT) event streams, and social feeds.

When creating a job in AWS Glue Studio, you can choose from a variety of data sources that are stored in AWS services. You can quickly prepare that data for analysis in data warehouses and data lakes. AWS Glue Studio also offers tools to monitor ETL workflows and validate that they are operating as intended. You can preview the dataset for each node. This helps you to debug your ETL jobs by displaying a sample of the data at each step of the job.

AWS Glue Studio provides a visual interface that makes it easy to:

- Pull data from an Amazon S3, Amazon Kinesis, or JDBC source.
- Configure a transformation that joins, samples, or transforms the data.
- Specify a target location for the transformed data.
- View the schema or a sample of the dataset at each point in the job.
- Run, monitor, and manage the jobs created in AWS Glue Studio.

## Glue Studio Notebook

AWS Glue Studio Job Notebooks allows you to interactively author extract-transform-and-load (ETL) jobs in a notebook interface based on Jupyter Notebooks. AWS Glue Studio Job Notebooks requires minimal setup so developers can get started quickly, and feature one-click conversion of notebooks into AWS Glue data integration jobs. Notebooks also support live data integration, fast startup times, and built-in cost management.

## Glue ETL job

An AWS Glue job encapsulates a script that connects to your source data, processes it, and then writes it out to your data target. Typically, a job runs extract, transform, and load (ETL) scripts. Jobs can also run general-purpose Python scripts (Python shell jobs.) AWS Glue triggers can start jobs based on a schedule or event, or on demand. You can monitor job runs to understand runtime metrics such as completion status, duration, and start time.

You can use scripts that AWS Glue generates, or you can provide your own. Given a source schema and target location or schema, the AWS Glue code generator can automatically create an Apache Spark API (PySpark) script. You can use this script as a starting point and edit it to meet your needs.

## Monitoring with Glue Studio

The Glue Studio Monitor dashboard provides an overall summary of the job runs, with totals for the jobs with a status of Running, Canceled, Success, or Failed. Additional tiles provide the overall job run success rate, the estimated DPU usage for jobs, a breakdown of the job status counts by job type, worker type, and by day.

## Glue interactive sessions

With AWS Glue interactive sessions, you can rapidly build, test, and run data preparation and analytics applications. Interactive Sessions provides a programmatic and visual interface for building and testing extract, transform, and load (ETL) scripts for data preparation. Interactive sessions run Apache Spark analytics applications and provide on-demand access to a remote Spark runtime environment. AWS Glue transparently manages serverless Spark for these interactive sessions.

Unlike AWS Glue development endpoints, AWS Glue interactive sessions are serverless with no infrastructure to manage. You can start interactive sessions very quickly. Interactive sessions have a 1-minute billing minimum with cost-control features. This reduces the cost of developing data preparation applications.

Because interactive sessions are flexible, you can build and test applications from the environment of your choice. You can create and work with interactive sessions through the AWS Command Line Interface and the API. You can use Jupyter-compatible notebooks to visually author and test your notebook scripts. Interactive sessions provide an open-source Jupyter kernel that integrates almost anywhere that Jupyter does, including integrating with IDEs such as PyCharm, IntelliJ, and VS Code. This enables you to author code in your local environment and run it seamlessly on the interactive sessions backend.

Using the Interactive Sessions API, customers can programmatically run applications that use Apache Spark analytics without having to manage Spark infrastructure. You can run one or more Spark statements within a single interactive session.

Interactive sessions therefore provide a faster, cheaper, more-flexible way to build and run data preparation and analytics applications.

:::note
AWS Glue provides multiple options to develop and test Spark code. Data engineers and data scientists can use tools of their choice to author Glue ETL scripts before deploying them to production. Data scientists can continue to work with Sagemaker notebooks connected to Glue Dev Endpoint, others can use Glue Job Notebooks to quickly launch and use jupyter-based fully-managed notebooks directly in browser. If you prefer to work locally, you can use Glue interactive sessions.
:::

## Glue Workflows

In AWS Glue, you can use workflows to create and visualize complex extract, transform, and load (ETL) activities involving multiple crawlers, jobs, and triggers. Each workflow manages the execution and monitoring of all its components. As a workflow runs each component, it records execution progress and status, providing you with an overview of the larger task and the details of each step. The AWS Glue console provides a visual representation of a workflow as a graph.

## Glue Trigger

AWS Glue manages dependencies between two or more jobs or dependencies on external events using triggers. Triggers can watch one or more jobs as well as invoke one or more jobs. You can have a scheduled trigger that invokes jobs periodically, an on-demand trigger, or a job completion trigger. Multiple jobs can be triggered in parallel or sequentially by triggering them on a job completion event. You can also trigger one or more Glue jobs from an external source such as an AWS Lambda function.

## Glue Streaming Job

You can create Glue Streaming extract, transform, and load (ETL) jobs that run continuously, consume data from streaming sources like Amazon Kinesis Data Streams, Apache Kafka, and Amazon Managed Streaming for Apache Kafka (Amazon MSK). The jobs cleanse and transform the data, and then load the results into Amazon S3 data lakes or JDBC data stores. Glue streaming is built based on Spark streaming which is micro-batch oriented and inherits all features of Spark Streaming. Spark Streaming seamlessly integrates with other Spark components like MLlib and Spark SQL. It is different from other systems that either have a processing engine designed only for streaming, or have similar batch and streaming APIs but compile internally to different engines. Spark’s single execution engine and unified programming model for batch and streaming data leads to some unique benefits over other traditional streaming systems.

## Glue Databrew

AWS Glue DataBrew is a visual data preparation tool that makes it easy for data analysts and data scientists to prepare data with an interactive, point-and-click visual interface without writing code. With Glue DataBrew, you can easily visualize, clean, and normalize terabytes, and even petabytes of data directly from your data lake, data warehouses, and databases, including Amazon S3, Amazon Redshift, Amazon Aurora, and Amazon RDS.

AWS Glue DataBrew is built for users who need to clean and normalize data for analytics and machine learning. Data analysts and data scientists are the primary users. For data analysts, examples of job functions are business intelligence analysts, operations analysts, market intelligence analysts, legal analysts, financial analysts, economists, quants, or accountants. For data scientists, examples of job functions are materials scientists, bioanalytical scientists, and scientific researchers.

## Glue DataBrew Project

The interactive data preparation workspace in DataBrew is called a project. Using a data project, you manage a collection of related items: data, transformations, and scheduled processes. As part of creating a project, you choose or create a dataset to work on. Next, you create a recipe, which is a set of instructions or steps that you want DataBrew to act on. These actions transform your raw data into a form that is ready to be consumed by your data pipeline.

A recipe is a set of instructions or steps for data that you want DataBrew to act on. A recipe can contain many steps, and each step can contain many actions. You use the transformation tools on the toolbar to set up all the changes that you want to make to your data. Later, when you're ready to see the finished product of your recipe, you assign this job to DataBrew and schedule it. DataBrew stores the instructions about the data transformation, but it doesn't store any of your actual data. You can download and reuse recipes in other projects. You can also pubish multiple versions of a recipe.

## Glue DataBrew Job

DataBrew takes on the job of transforming your data by running the instructions that you set up when you made a recipe. The process of running these instructions is called a job. A job can put your data recipes into action according to a preset schedule. But you aren't confined to a schedule. You can also run jobs on demand. If you want to profile some data, you don't need a recipe. In that case, you can just set up a profile job to create a data profile.

## Explore further

1. [Data Preparation on AWS: Comparing ELT Options to Cleanse and Normalize Data](https://knowledgetree.notion.site/Data-Preparation-on-AWS-Comparing-ELT-Options-to-Cleanse-and-Normalize-Data-Shared-5a16da581ef845d2a7e38f06ca0b35c0)
2. [Transform JSON / CSV files to Parquet through Aws Glue](https://hkdemircan.medium.com/how-can-we-json-css-files-transform-to-parquet-through-aws-glue-465773b43dad)
3. [Data Transformation at scale with AWS Glue](https://knowledgetree.notion.site/Data-Transformation-at-scale-with-AWS-Glue-Shared-65b9c00215bf42e69d94365a07a82f5a)
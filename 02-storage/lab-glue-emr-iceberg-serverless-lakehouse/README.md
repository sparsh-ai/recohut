# Build a serverless transactional data lake with Apache Iceberg, Amazon EMR Serverless, and Amazon Athena

Since the deluge of big data over a decade ago, many organizations have learned to build applications to process and analyze petabytes of data. Data lakes have served as a central repository to store structured and unstructured data at any scale and in various formats. However, as data processing at scale solutions grow, organizations need to build more and more features on top of their data lakes. One important feature is to run different workloads such as business intelligence (BI), Machine Learning (ML), Data Science and data exploration, and Change Data Capture (CDC) of transactional data, without having to maintain multiple copies of data. Additionally, the task of maintaining and managing files in the data lake can be tedious and sometimes complex.

Table formats like Apache Iceberg provide solutions to these issues. They enable transactions on top of data lakes and can simplify data storage, management, ingestion, and processing. These transactional data lakes combine features from both the data lake and the data warehouse. You can simplify your data strategy by running multiple workloads and applications on the same data in the same location. However, using these formats requires building, maintaining, and scaling infrastructure and integration connectors that can be time-consuming, challenging, and costly.

In this lab, we show how you can build a serverless transactional data lake with Apache Iceberg on [Amazon Simple Storage Service](http://aws.amazon.com/s3) (Amazon S3) using [Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/) and [Amazon Athena](http://aws.amazon.com/athena). We provide an example for data ingestion and querying using an ecommerce sales data lake.

## Build your transactional data lake on AWS

You can build your modern data architecture with a scalable data lake that integrates seamlessly with an [Amazon Redshift](http://aws.amazon.com/redshift) powered cloud warehouse. Moreover, many customers are looking for an architecture where they can combine the benefits of a data lake and a data warehouse in the same storage location. In the following figure, we show a comprehensive architecture that uses the modern data architecture strategy on AWS to build a fully featured transactional data lake. AWS provides flexibility and a wide breadth of features to ingest data, build AI and ML applications, and run analytics workloads without having to focus on the undifferentiated heavy lifting.

Data can be organized into three different zones, as shown in the following figure. The first zone is the raw zone, where data can be captured from the source as is. The transformed zone is an enterprise-wide zone to host cleaned and transformed data in order to serve multiple teams and use cases. Iceberg provides a table format on top of Amazon S3 in this zone to provide ACID transactions, but also to allow seamless file management and provide time travel and rollback capabilities. The business zone stores data specific to business cases and applications aggregated and computed from data in the transformed zone.

![bdb-2850-image001](https://user-images.githubusercontent.com/62965911/224493008-fbe32641-6c75-41cd-8977-37c28a373822.jpg)

One important aspect to a successful data strategy for any organization is data governance. On AWS, you can implement a thorough governance strategy with fine-grained access control to the data lake with [AWS Lake Formation](https://aws.amazon.com/lake-formation/).

## Serverless architecture overview

In this section, we show you how to ingest and query data in your transactional data lake in a few steps. EMR Serverless is a serverless option that makes it easy for data analysts and engineers to run Spark-based analytics without configuring, managing, and scaling clusters or servers. You can run your Spark applications without having to plan capacity or provision infrastructure, while paying only for your usage. EMR Serverless supports Iceberg natively to create tables and query, merge, and insert data with Spark. In the following architecture diagram, Spark transformation jobs can load data from the raw zone or source, apply the cleaning and transformation logic, and ingest data in the transformed zone on Iceberg tables. Spark code can run instantaneously on an EMR Serverless application, which we demonstrate later in this lab.

![bdb-2850-image002](https://user-images.githubusercontent.com/62965911/224493010-5d573dee-e20f-4fbb-978e-5c309cb87e75.jpg)

The Iceberg table is synced with the [AWS Glue](https://aws.amazon.com/glue) Data Catalog. The Data Catalog provides a central location to govern and keep track of the schema and metadata. With Iceberg, ingestion, update, and querying processes can benefit from atomicity, snapshot isolation, and managing concurrency to keep a consistent view of data.

Athena is a serverless, interactive analytics service built on open-source frameworks, supporting open-table and file formats. Athena provides a simplified, flexible way to analyze petabytes of data where it lives. To serve BI and reporting analysis, it allows you to build and run queries on Iceberg tables natively and integrates with a variety of BI tools.

## Sales data model

[Star schema](https://aws-samples.github.io/aws-dbs-refarch-edw/src/star-schema/) and its variants are very popular for modeling data in data warehouses. They implement one or more fact tables and dimension tables. The fact table stores the main transactional data from the business logic with foreign keys to dimensional tables. Dimension tables hold additional complementary data to enrich the fact table.

In this lab, we take the example of sales data from the [TPC-DS benchmark](https://www.tpc.org/tpc_documents_current_versions/pdf/tpc-ds_v2.13.0.pdf). We zoom in on a subset of the schema with the `web_sales` fact table, as shown in the following figure. It stores numeric values about sales cost, ship cost, tax, and net profit. Additionally, it has foreign keys to dimensional tables like `date_dim`, `time_dim`, `customer`, and `item`. These dimensional tables store records that give more details. For instance, you can show when a sale took place by which customer for which item.

![bdb-2850-image003](https://user-images.githubusercontent.com/62965911/224493011-b3da90b0-96d2-4e77-b66e-19e32c13c824.png)

Dimension-based models have been used extensively to build data warehouses. In the following sections, we show how to implement such a model on top of Iceberg, providing data warehousing features on top of your data lake, and run different workloads in the same location. We provide a complete example of building a serverless architecture with data ingestion using EMR Serverless and Athena using TPC-DS queries.

## Code

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/02-storage/lab-glue-emr-iceberg-serverless-lakehouse/main.ipynb)

## Conclusion

In this lab, we created a serverless transactional data lake with Iceberg tables, EMR Serverless, and Athena. We used TPC-DS sales data with 10 GB data and more than 7 million records in the fact table. We demonstrated how straightforward it is to rely on SQL and Spark to run serverless jobs for data ingestion and upserts. Moreover, we showed how to run complex BI queries directly on Iceberg tables from Athena for reporting.

You can start building your serverless transactional data lake on AWS today, and dive deep into the features and optimizations Iceberg provides to build analytics applications more easily. Iceberg can also help you in the future to improve performance and reduce costs.

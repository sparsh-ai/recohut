# Amazon Athena

> Athena is a Serverless Query Service from Amazon based on Presto engine

Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.

Athena is easy to use. Simply point to your data in Amazon S3, define the schema, and start querying using standard SQL. Most results are delivered within seconds. With Athena, there’s no need for complex ETL jobs to prepare your data for analysis. This makes it easy for anyone with SQL skills to quickly analyze large-scale datasets.

![](https://user-images.githubusercontent.com/62965911/214001856-3d835c43-3eef-42a0-8e6f-ad1eca4e807f.png)

Athena is out-of-the-box integrated with AWS Glue Data Catalog, allowing you to create a unified metadata repository across various services, crawl data sources to discover schemas and populate your Catalog with new and modified table and partition definitions, and maintain schema versioning.

Presto (or PrestoDB) is an open source, distributed SQL query engine, designed from the ground up for fast analytic queries against data of any size. It supports both non-relational sources, such as the Hadoop Distributed File System (HDFS), Amazon S3, Cassandra, MongoDB, and HBase, and relational data sources such as MySQL, PostgreSQL, Amazon Redshift, Microsoft SQL Server, and Teradata.

Presto can query data where it is stored, without needing to move data into a separate analytics system. Query execution runs in parallel over a pure memory-based architecture, with most results returning in seconds. You’ll find it used by many well-known companies like Facebook, Airbnb, Netflix, Atlassian, and Nasdaq.

Amazon Athena lets you deploy Presto using the AWS Serverless platform, with no servers, virtual machines, or clusters to setup, manage, or tune. Simply point to your data at Amazon S3, define the schema, and start querying using the built-in query editor, or with your existing Business Intelligence (BI) tools. Athena automatically parallelizes your query, and dynamically scales resources for queries to run quickly. You pay only for the queries that you run.

Athena is "Managed Presto"

Athena doesn't support

1. DML Operations
2. Stored Procedures or MQT

### Benefits

#### Start querying instantly

**Serverless, no ETL**

Athena is serverless. You can quickly query your data without having to setup and manage any servers or data warehouses. Just point to your data in Amazon S3, define the schema, and start querying using the built-in query editor. Amazon Athena allows you to tap into all your data in S3 without the need to set up complex processes to extract, transform, and load the data (ETL).

#### Open, powerful, standard

**Built on Presto, runs standard SQL**

Amazon Athena uses Presto with ANSI SQL support and works with a variety of standard data formats, including CSV, JSON, ORC, Avro, and Parquet. Athena is ideal for interactive querying and can also handle complex analysis, including large joins, window functions, and arrays. Amazon Athena is highly available; and executes queries using compute resources across multiple facilities and multiple devices in each facility. Amazon Athena uses Amazon S3 as its underlying data store, making your data highly available and durable.

tip:

Presto: Released as open source by Facebook, it’s an open source distributed SQL query engine for running interactive analytic queries against data sources of all sizes. Presto allows querying data where it lives, including Hive, Cassandra, relational databases and file systems. It can perform queries on large data sets in a manner of seconds. It is independent of Hadoop but integrates with most of its tools, especially Hive to run SQL queries.

#### Pay per query

**Only pay for data scanned**

With Amazon Athena, you pay only for the queries that you run. You are charged $5 per terabyte scanned by your queries. You can save from 30% to 90% on your per-query costs and get better performance by compressing, partitioning, and converting your data into columnar formats. Athena queries data directly in Amazon S3. There are no additional storage charges beyond S3.

#### Fast, really fast

**Interactive performance even for large datasets**

With Amazon Athena, you don't have to worry about having enough compute resources to get fast, interactive query performance. Amazon Athena automatically executes queries in parallel, so most results come back within seconds.

### Athena Federation

Run federated queries against relational databases, data warehouses, object stores, and non-relational data stores. Federated SQL queries allow you to query the data in-place from wherever it resides. You can use familiar SQL to JOIN data across multiple data sources for quick analysis, and store results in Amazon S3 for subsequent use. Athena federated query also introduces a new Query Federation SDK that allows you to write your own data source connectors to query custom data stores.

Athena uses data source connectors that run on AWS Lambda to execute federated queries. A data source connector is a piece of code that can translate between your target data source and Athena. You can think of a connector as an extension of Athena's query engine. When a query is submitted against a data source, Athena invokes the corresponding connector to identify parts of the tables that need to be read, manages parallelism, and pushes down filter predicates. Based on the user submitting the query, connectors can provide or restrict access to specific data elements.

### Athena ACID Transactions

ACID transactions enable multiple users to concurrently and reliably add and delete Amazon S3 objects in an atomic manner, while isolating any existing queries by maintaining read consistency for queries against the data lake. Athena ACID transactions add single-table support for write, delete, update, and time travel operations to the Athena SQL data manipulation language (DML). You and multiple concurrent users can use Athena ACID transactions to make reliable, row-level modifications to Amazon S3 data. Athena transactions automatically manage locking semantics and coordination and do not require a custom record locking solution.

Athena ACID transactions and familiar SQL syntax simplify updates to your business and regulatory data. For example, to respond to a data erasure request, you can perform a SQL DELETE operation. To make manual record corrections, you can use a single UPDATE statement. To recover data that was recently deleted, you can issue time travel queries using a SELECT statement.

Athena supports read, time travel, and write queries for Apache Iceberg tables that use the Apache Parquet format for data and the AWS Glue catalog for their metastore.

### Watch these videos

- https://www.youtube.com/watch?v=whR4J5Arj78
- https://www.youtube.com/watch?v=M5ptG0YaqAs
- https://www.youtube.com/watch?v=1lzpeVV2hDQ

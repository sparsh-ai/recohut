# Snowflake

Snowflake is the Data Cloud that enables you to build data-intensive applications without operational burden, so you can focus on data and analytics instead of infrastructure management.

> Snowflake is the next big thing, and it is becoming a full-blown data ecosystem. With the level of scalability and efficiency in handling massive volumes of data and also with several new concepts in it, this is the right time to wrap your head around Snowflake and have it in your toolkit.

Snowflake started out because its founders understood and knew the truth about how users suffered with traditional relational OLAP solutions. Makes sense, they came from Oracle. They also understood how the cloud works. The founders didn't want to port an Oracle-like database over to the cloud as is. That would not solve the problems that the user base was experiencing. What were users suffering from: scale, performance, concurrency, and tons of expensive resources to keep the lights on! So they built Snowflake to solve these problems by taking all the good of a relational database platform and applying it to the cloud. The cloud allows for simple manifestation of environments with elasticity for size or scale.

Who competes with Snowflake directly? All cloud-based OLAP databases like: Redshift, Teradata, Oracle, Synapse, and Databricks. Yes, dare I say it Cloudera. Snowflake is starting to blur the lines a bit with Iceberg (Data Lake), SnowPark(Data Science/Data Engineering), Data Sharing/Marketplace(Third Party Data), and coming soon: Unistore (OLTP).

### Architecture

Even the improved traditional data platforms, especially those that were implemented on premises, couldn’t adequately address modern data problems or solve the long-standing scalability issue. The Snowflake team made the decision to take a unique approach. Rather than trying to incrementally improve or transform existing software architectures, they built an entirely new, modern data platform, just for the cloud, that allows multiple users to concurrently share live data.

The unique Snowflake design physically separates but logically integrates storage and compute along with providing services such as security and management. As we explore the many unique Snowflake features throughout the upcoming chapters, you’ll be able to see for yourself why the Snowflake architecture is the only architecture that can enable the Data Cloud.

The Snowflake hybrid-model architecture is composed of three layers, which are shown in the following image: the cloud services layer, the compute layer, and the data storage layer.

![](https://user-images.githubusercontent.com/62965911/214011273-c6c43e89-1b73-4d0f-9a59-4b42f3a9933e.png)

Watch this video: https://www.youtube.com/watch?v=ZOqmqfe8WvM

### Object hierarchy

![](https://user-images.githubusercontent.com/62965911/214011288-13335fff-954f-40fd-9b26-ea4cb231cfea.png)

### Snowpark

With Snowpark, developers can program using a familiar construct like the DataFrame, and bring in complex transformation logic through UDFs, and then execute directly against Snowflake’s processing engine, leveraging all of its performance and scalability characteristics in the Data Cloud.

Snowpark provides several benefits over how developers have designed and coded data-driven solutions in the past:

- Simplifies architecture and data pipelines by bringing different data users to the same data platform, and processes against the same data without moving it around.
- Accelerates data pipeline workloads by executing with performance, reliability, and scalability with Snowflake’s elastic performance engine.
- Eliminates maintenance and overhead with managed services and near-zero maintenance.
- Creates a single governance framework and a single set of policies to maintain by using a single platform.
- Provides a highly secure environment with administrators having full control over which libraries are allowed to execute inside the Java/Scala runtimes for Snowpark.

### Snowflake Data Ingestion/Loading and Extraction

![](https://user-images.githubusercontent.com/62965911/214011557-32f11577-390b-45e0-85b1-7ca33afdafee.png)

As the diagram above shows, Snowflake supports a wide range of use-cases including:

- Data File Loading: Which is the most common and highly efficient data loading method in Snowflake. This involves using SnowSQL to execute SQL commands to rapidly load data into a landing table. Using this technique it’s possible to quickly load terabytes of data, and this can be executed on a batch or micro-batch basis. Once the data files are held in a cloud stage (EG. S3 buckets), the COPY command can be used to load the data into Snowflake. For the majority of large volume batch data ingestion this is the most common method, and it’s normally good practice to size data files at around 100–250 megabytes of compressed data optionally breaking up very large data files were appropriate.
- Replication from on Premises Databases: Snowflake supports a range of data replication and ETL tools including HVR, Stitch, Fivetran and Qlik Replicate which will seamlessly replicate changes from operational or legacy warehouse systems with zero impact upon the source system. Equally there are a huge range of data integration tools which support Snowflake in addition to other database platforms and these can be used to extract and load data. Equally, some customers choose to write their own data extract routines and use the Data File Loading and COPY technique described above.
- Data Streaming: Options to stream data into Snowflake include using the Snowflake Kafka Connector to automatically ingest data directly from a Kafka topic as demonstrated by this video demonstration. Unlike the COPY command which needs a virtual warehouse, Snowpipe is an entirely serverless process, and Snowflake manages the operation entirely, scaling out the compute as needed. Equally, the option exists to simply trigger Snowpipe to automatically load data files when they arrive on cloud storage.
- Inserts using JDBC and ODBC: Although not the most efficient way to bulk load data into Snowflake (using COPY or Snowpipe is always faster and more efficient), the Snowflake JDBC and ODBC connectors are available in addition to a range of Connectors and Drivers including Python, Node.js and Go.
- Ingestion from a Data Lake: While Snowflake can be used to host a Data Lake, customers with an existing investment in a cloud data lake can make use of Snowflake External Tables to provide a transparent interface to data in the lake. From a Snowflake perspective, the data appears to be held in a read-only table, but the data is transparently read from the underlying files on cloud storage.
- Data Sharing: For customers with multiple Snowflake deployments, the Data Exchange provides a seamless way to share data across the globe. Using the underlying Snowflake Data Sharing technology, customers can query and join data in real time from multiple sources without the need to copy. Existing in-house data can also be enriched with additional attributes from externally sourced data using the Snowflake Data Marketplace.

**Batch/Bulk Data Ingestion**

1. Write/load the data into your staging location (S3 bucket)
2. Ingest the data into Snowflake in batches at frequent time intervals using:
   1. Snowflake copy commands scheduled using Snowflake tasks
   2. Trigger copy commands using Python/Glue/Airflow running at specified time intervals

**Real-time Data Ingestion**

1. Write/load the data into your staging location (S3 bucket) and ingest the data in real-time using:
   1. Snowpipe (continuous data ingestion)
   2. Airflow S3 sensors/triggers
2. Kafka-Snowflake Connector for real-time data ingestion

### SnowSQL

SnowSQL is the command line client for connecting to Snowflake to execute SQL queries and perform all DDL and DML operations, including loading data into and unloading data out of database tables. It is a modern command line tool designed for Snowflake Cloud data warehouse that is built on high security standards and has tight integration with Snowflake core architecture. It has very powerful scripting capability, and it can be further enhanced when used along with Python. Also, to upload/download any files to Snowflake internal stage you need SnowSql as put and get command work only with command line and not Web UI.

### SnowPipe

> Getting the volume and variety of today’s data into your data warehouse is paramount to obtain immediate, data-driven insight. Unfortunately, legacy data warehouses require batch-oriented loading and scheduling at off-peak times to avoid contention with the crucial needs of data analytics users. Snowpipe is a new data loading service for Snowflake that significantly improves the process of making data available for analysis.

Snowpipe is an event based data ingest tool. Snowpipe provides two main methods for triggering a data loading event. This trigger could be a cloud storage notification (i.e. AWS S3 ObjectCreated event) or by directly calling the Snowpipe insertFiles REST API.

When building data applications, your users count on seeing the latest. Stale data is less actionable and could lead to costly errors. That's why continuously generated data is essential. Snowflake provides a data loading tool to drive updates, ensuring your databases are accurate by updating tables in micro-batches.

### Best Practices for Data Engineering on Snowflake

1. Follow the standard ingestion pattern: This involves the multi-stage process of landing the data files in cloud storage and then loading to a landing table before transforming the data. Breaking the overall process into predefined steps makes it easier to orchestrate and test.
2. Retain history of raw data: Unless your data is sourced from a raw data lake, it makes sense to keep the raw data history which should ideally be stored using the [VARIANT](https://docs.snowflake.com/en/sql-reference/data-types-semistructured.html#variant) data type to benefit from automatic schema evolution. This means you have the option of truncating and re-processing data if bugs are found in the transformation pipeline and provides an excellent raw data source for Data Scientists. While you may not yet have any machine learning requirements, it's almost certain you will, if not now, then in the years to come. Keep in mind that Snowflake data storage is remarkably cheap, unlike on-premises solutions.
3. Use multiple data models: On-premises data storage was so expensive it was not feasible to store multiple copies of data with each using a different data model to match the need. However, using Snowflake it makes sense to store raw data history in either structured or variant format, cleaned and conformed data in [3rd Normal Form](https://dwbi1.wordpress.com/2011/03/28/storing-history-on-3rd-normal-form/) or using a [Data Vault](https://www.analytics.today/blog/when-should-i-use-data-vault) model and finally data ready for consumption in a [Kimball Dimensional Data model](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/). Each data model has unique benefits and storing the results of intermediate steps has huge architectural benefits, not least, the ability to reload and reprocess the data in the event of mistakes.
4. Use the right tool: As the quote above implies, if you only know one tool, you'll use it inappropriately. The decision should be based upon a range of factors including, the existing skill set in the team, whether you need rapid near real-time delivery, whether you're doing a once off data load or a regular repeating process. Be aware, Snowflake can natively handle a range of file formats including Avro, Parquet, ORC, JSON and CSV and there is extensive guidance on [loading data into Snowflake](https://docs.snowflake.com/en/user-guide-data-load.html#loading-data-into-snowflake) on the online documentation.
5. Use COPY or SNOWPIPE to load data: Around 80% of data loaded into a data warehouse is either ingested using a regular batch process or increasingly, immediately the data files arrive. By far the fastest, most cost efficient way to load data is using COPY and SNOWPIPE, so avoid the temptation to use other methods (for example queries against external tables) for regular data loads. Effectively, this is another example of *use the right tool*.
6. Avoid JDBC or ODBC for regular large data loads: Another *right tool* recommendation. While a JDBC or ODBC interface may be fine to load a few megabytes of data, these interfaces will not scale to the massive throughput of COPY and SNOWPIPE. Use them by all means, but not for large regular data loads.
7. Avoid Scanning Files: When using the COPY command to ingest data, use [partitioned staged data](https://docs.snowflake.com/en/user-guide/data-load-considerations-manage.html#partitioning-staged-data-files) files which is described as step 1 in the [Top 3 Snowflake Performance Tuning Tactics](https://www.analytics.today/blog/top-3-snowflake-performance-tuning-tactics). This reduces the effort of scanning large numbers of data files in cloud storage.
8. Choose a sensible Virtual Warehouse size: Another tip from the [Top 3 Snowflake Performance Tuning Tactics](https://www.analytics.today/blog/top-3-snowflake-performance-tuning-tactics), don't assume an X6-LARGE virtual warehouse will load massive data files any faster than an X-SMALL. Each physical file is loaded sequentially, and it therefore pays to follow the [Snowflake File Sizing Recommendations](https://docs.snowflake.com/en/user-guide/data-load-considerations-prepare.html#general-file-sizing-recommendations) and either split multi-gigabyte files into chunks of 100--250Mb or load multiple concurrent data files in parallel.
9. Ensure 3rd party tools push down: ETL tools like Ab Initio, Talend and Informatica were originally designed to extract data from source systems into an ETL server, transform the data and write them to the warehouse. As Snowflake can draw upon massive on-demand compute resources and automatically scale out, it makes no sense to use have data copied to an external server. Instead, use the ELT (Extract, Load and Transform) method, and ensure the tools generate and execute SQL statements on Snowflake to maximise throughput and reduce costs.
10. Transform data in Steps: A common mistake by inexperienced data engineers is to write huge SQL statements that join, summarise and process lots of tables in the mistaken belief this is an efficient way of working. In reality the code becomes over-complex and difficult to maintain and worst still, often performs poorly. Instead, break the transformation pipeline into multiple steps and write results to intermediate tables. This makes it easier to test intermediate results, simplifies the code and often produces simple SQL code that runs faster.
11. Use Transient tables for intermediate results: During a complex ELT pipeline, write intermediate results to a [transient table](https://docs.snowflake.com/en/user-guide/tables-temp-transient.html#transient-tables) which may be truncated prior to the next load. This reduces the time-travel storage to just one day and avoids an additional 7 days of fail-safe storage. By all means use [temporary tables](https://docs.snowflake.com/en/user-guide/tables-temp-transient.html#temporary-tables) if sensible, but it's often helpful to check the results of intermediate steps in a complex ELT pipeline.
12. Avoid row-by-row processing: Modern analytics platforms like Snowflake are designed to ingest, process and analyse billions of rows at amazing speed using simple SQL statements which act upon the data *set-at-a-time*. However, people tend to think in terms of row-by-row processing and this sometimes leads to programming loops which fetch and update rows, one at a time. Be aware, [row-by-row processing](https://www.sqlskills.com/blogs/paul/reconciling-set-based-operations-with-row-by-row-iterative-processing/) is by far the single biggest way of killing query performance. Use SQL statements to process all table entries at a time and avoid row-by-row processing at all cost.
13. Use Query Tags: When you start any multi-step transformation task set the [session query tag using](https://docs.snowflake.com/en/sql-reference/sql/alter-session.html#alter-session): ALTER SESSION SET QUERY_TAG = 'XXXXXX' and ALTER SESSION UNSET QUERY_TAG. This stamps every SQL statement until reset with an identifier and is invaluable to System Administrators. As every SQL statement (and QUERY_TAG) is recorded in the [QUERY_HISTORY](https://docs.snowflake.com/en/sql-reference/account-usage/query_history.html#query-history-view) view you can then track the job performance over time. This can be used to quickly identify when a task change has resulted in poor performance, identify inefficient transformation jobs or indicate when a job would be better executed on a larger or smaller warehouse.
14. Keep it Simple: Probably the best indicator of an experienced data engineer is the value they place on *simplicity*. You can always make a job 10% faster or generic or more elegant and it *may* be beneficial but it's *always* beneficial to simplify a solution. Simple solutions are easier to understand, easier to diagnose problems and are therefore easier to maintain. Around 50% of the performance challenges I face are difficult to resolve because the solution is a single, monolithic complex block of code. The first thing I do, is to break down the solution into steps and only then identify the root cause.

Watch this video: https://www.youtube.com/watch?v=jKJTqfvwFOg
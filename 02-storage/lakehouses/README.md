# Data Lakehouses

![lakehouse-architecture](https://user-images.githubusercontent.com/62965911/216760249-832980a9-2e58-4c7f-8dcf-a482cadc2415.png)

Table formats are instrumental for getting the scalability benefits of the data lake and the underlying object store, while at the same time getting the data quality and governance associated with data warehouses. Previously, users had to pick one or the other, or replicate data from a lake to the warehouse and hope (or pray) that it stays up-to-date. But by using a table format, lakehouse users don’t have to accept tradeoffs and get the benefits of both.

Three table formats have emerged over the past few years to power data lakehouses. Apache Iceberg was created by engineers at Netflix and Apple who were tired of trying to use Apache Hive’s metastore to track data updates and manage transactions. [Databricks](https://www.databricks.com/) created its own table format to live at the heart of its Delta Lake offering, and then open sourced it. Apache Hudi, meanwhile, was created by engineers at Uber to provide support for transactions for a massive data lake running on Hadoop.

The whole elevator pitch for lakehouse is ACID transactions. Not to turn it into an OLTP database, but is the data that we’re doing these analytics on or building these machine learning models on–is this valid data? Is it consistent? Or are we basically chasing our tail? That was the real driver of this. From that, you then get all the other goodies, like now with a table structure, we can do much more granular governance. Arguably there are ways to basically accelerate processing Parquet. But basically with tables, you can get much better performance that you can through file scans than you can with something like Impala.

## Deltalake

> An open format storage layer for your lakehouses

Delta Lake  is an open source storage layer that enables building a Lakehouse architecture on top of data lakes. It provides functionalities to data in the data lake that only exist in data warehouses. When combined with cloud storage, Databricks and Delta Lake lead to the formation of a Lakehouse. A Lakehouse simply provides the best of both worlds – data lakes and data warehouses. In today's world, a Lakehouse provides the same set of capabilities as a traditional data warehouse and at a much lower cost. This is made possible due to cheap cloud storage such as Azure Data Lake/S3, Spark as the processing engine, and data being stored in the Delta Lake format.

Delta Lake guarantees data atomicity, consistency, isolation, and durability in the lake. In short, a Delta Lake is ACID compliant. In addition to providing ACID transactions, scalable metadata handling, and more, Delta Lake runs on an existing data lake and is compatible with Apache Spark APIs. Delta Lake also offers unifies streaming and batch data processing on top of existing data lakes, such as S3 and HDFS.

There are a few methods of getting started with Delta Lake. Databricks offers notebooks along with compatible Apache Spark APIs to create and manage Delta Lakes.

Specifically, Delta Lake offers:

- ACID transactions on Spark: Serializable isolation levels ensure that readers never see inconsistent data.
- Scalable metadata handling: Leverages Spark distributed processing power to handle all the metadata for petabyte-scale tables with billions of files at ease.
- Streaming and batch unification: A table in Delta Lake is a batch table as well as a streaming source and sink. Streaming data ingest, batch historic backfill, interactive queries all just work out of the box.
- Schema enforcement: Automatically handles schema variations to prevent insertion of bad records during ingestion.
- Time travel: Data versioning enables rollbacks, full historical audit trails, and reproducible machine learning experiments.
- Upserts and deletes: Supports merge, update and delete operations to enable complex use cases like change-data-capture, slowly-changing-dimension (SCD) operations, streaming upserts, and so on.

### Why an ACID Delta Lake

There are many advantages to introducing Delta Lake into a modern cloud data architecture. Traditionally, data lakes and Apache Spark are not ACID compliant. Delta Lake introduces this ACID compliance to solve many the following ACID compliance issues:

1. **Atomicity**: *Write either all data or nothing*. Apache Spark *save modes* do not utilize any locking and are not atomic. With this, a failed job may leave an incomplete file and may corrupt data. Additionally, a failing job may remove the old file and corrupt the new file. While this seems concerning, Spark does have built-in data frame writer APIs that are not atomic but behave so for append operations. This however does come with performance overhead for use with cloud storage. The currently available Apache Spark save modes include ErrorIfExists, Append, Overwrite, and Ignore.
2. **Consistency**: *Data is always in a valid state*. If the Spark API writer deletes an old file and creates a new one and the operation is not transactional, then there will always be a period of time when the file does not exist between the deletion of the old file and creation of the new. In that scenario, if the overwrite operation fails, this will result in data loss of the old file. Additionally, the new file may not be created. This is a typical Spark overwrite operation issue related to consistency.
3. **Isolation**: *Multiple transactions occur independently without interference*. This means that when writing to a dataset, other concurrent reads or writes on the same dataset should not be impacted by the write operation. Typical transactional databases offer multiple isolation levels, such as read uncommitted, read committed, repeatable read, snapshot, and serializable. While Spark has task- and job-level commits, since it lacks atomicity, it does not have isolation types.
4. **Durability**: *Committed data is never lost.* When Spark does not correctly implement a commit, then it overwrites all the great durability features offered by cloud storage options and either corrupts and/or loses the data. This violates data durability.

## Apache Hudi

> Bring transactions, record-level updates/deletes and change streams to data lakes

Apache Hudi is an open-source data management framework used to simplify incremental data processing and data pipeline development by providing record-level insert, update, upsert, and delete capabilities. Upsert refers to the ability to insert records into an existing dataset if they do not already exist or to update them if they do. By efficiently managing how data is laid out in Amazon S3, Hudi allows data to be ingested and updated in near real time. Hudi carefully maintains metadata of the actions performed on the dataset to help ensure that the actions are atomic and consistent.

Hudi is a rich platform to build streaming data lakes with incremental data pipelines
on a self-managing database layer, while being optimized for lake engines and regular batch processing.

![](https://user-images.githubusercontent.com/62965911/213927494-a34ab9fe-0bdb-4b7e-a39a-23e8275e196d.png)

## Apache Iceberg

> The open table format for analytic datasets

Apache Iceberg is an open table format for very large analytic datasets. Iceberg manages large collections of files as tables, and it supports modern analytical data lake operations such as record-level insert, update, delete, and time travel queries. The Iceberg specification allows seamless table evolution such as schema and partition evolution, and its design is optimized for usage on Amazon S3. Iceberg also helps guarantee data correctness under concurrent write scenarios.

Iceberg is an open-source table format that brings the power of SQL tables to big data files. It enables ACID transactions on tables, allowing for concurrent data ingestion, updates, and queries, all while using familiar SQL. Iceberg employs internal metadata management that keeps track of data and empowers a set of rich features at scale. It allows you to time travel and roll back to old versions of committed data transactions, control the table’s schema evolution, easily compact data, and employ hidden partitioning for fast queries.

Iceberg manages files on behalf of the user and unlocks use cases such as:

- Concurrent data ingestion and querying, including streaming and CDC
- BI and reporting with expressive simple SQL
- Empowering ML feature stores and training sets
- Compliance and regulations workloads, such as GDPR find and forget
- Reinstating late-arriving data, which is dimensions data arriving later than the fact data. For example, the reason for a flight delay may arrive well after the fact that the fligh is delayed.
- Tracking data changes and rollback

For more information about Apache Iceberg, see https://iceberg.apache.org/.

## Medallion Architecture

A medallion architecture is a data design pattern used to logically organize data in a lakehouse, with the goal of incrementally and progressively improving the structure and quality of data as it flows through each layer of the architecture (from Bronze ⇒ Silver ⇒ Gold layer tables). Medallion architectures are sometimes also referred to as "multi-hop" architectures.

![](https://user-images.githubusercontent.com/62965911/213927430-13be2919-ad25-4094-8488-17048701f745.png)

A lakehouse is a new data platform architecture paradigm that combines the best features of data lakes and data warehouses. A modern lakehouse is a highly scalable and performant data platform hosting both raw and prepared data sets for quick business consumption and to drive advanced business insights and decisions. It breaks data silos and allows seamless, secure data access to authorized users across the enterprise on one platform.

### Benefits of a lakehouse architecture

- Simple data model
- Easy to understand and implement
- Enables incremental ETL
- Can recreate your tables from raw data at any time
- ACID transactions, time travel

### Layers

#### Landing area

An optional layer that is often seen at organizations implementing a data platform is a landing area or landing zone. A landing area is an intermediate location in which data from various source systems will be stored before moving it into the Bronze layer. This layer is often needed in situations in which it's hard to extract data from the target source system. For example, when working with external customers or SaaS vendors. In such scenarios, you have a dependency or sometimes receive data in an unpreferred (file) format or structure.

The solution design of a landing zone varies between organizations. Often, it's a simple Blob storage account. In other cases, the landing zone is part of the data lake services, for example, container, bucket, or specific folder in which the data is ingested. Data within landing zones is often highly diverse. File formats could be CSV, JSON, XML, Parquet, Delta, and so on.

#### Bronze layer

The bronze layer is usually a reservoir that stores data in its natural and original state. It contains unvalidated data (without having to first define schemas). In this layer you either get data using full loads or delta loads. Data that is stored in bronze has usually the following characteristics:

- Maintains the raw state of the data source in the structure "as-is".
- Data is immutable (read-only).
- Managed using interval partitioned tables, for example, using a YYYYMMDD or datetime folder structure.
- Retains the full (unprocessed) history of each dataset in an efficient storage format, for example, Parquet or Delta.
- For transactional data: Can be appended incrementally and grow over time.
- Provides the ability to recreate any state of a given data system.
- Can be any combination of streaming and batch transactions.
- May include extra metadata, such as schema information, source file names or recording the time data was processed.

The question that I often hear is "What is the best file format? Should I use Delta or Parquet?" Delta is faster, but since data is already versioned or historized using a folder structure, I don't see any compelling benefits for maintaining a transaction log or apply versioning. Data in Bronze is generally new data or being appended. So, if you would like to go for Parquet, that's fine. Alternatively, you use Delta in line with all other layers.

Some people say that data in Bronze is useful for business users for querying or ad-hoc analysis. In my experience, while working with customers, I rarely see raw data being used as input for running queries or ad-hoc analysis. Raw data is hard to work with. It requires in-depth understanding of how the source system has been designed. It requires you to work out complex business logic that has been encapsulated with the data itself. It often has many small tables, hence it's impossible to secure. To conclude: Bronze is a staging layer and input for other layers. It's mainly accessed by technical accounts.

#### Silver layer

The Silver layer provides a refined structure over data that has been ingested. It represents a validated, enriched version of our data that can be trusted for downstream workloads, both operational and analytical. In addition to that, Silver may have the following characteristics:

- Uses data quality rules for validating and processing data.
- Typically contains only functional data. So, technical data or irrelevant data from Bronze is filtered out.
- Historization is usually applied by merging all data. Data is processed using slowly changing dimensions (SCD), either type 2 or type 4. This means additional columns are added, such as start, end and current columns.
- Data is stored in an efficient storage format; preferably Delta, alternatively Parquet.
- Uses versioning for rolling back processing errors.
- Handles missing data, standardizes clean or empty fields.
- Data is usually enriched with reference and/or master data.
- Data is often cluttered around certain subject areas.
- Data is often still source-system aligned and organized.

For Silver there are a couple of attention points:

Some people say that Silver can act as a temporary storage layer. Thus, older data can be wiped out or storage accounts can be created on the fly. Customers question me, do you see this as well? Well, it depends. If you aren't planning on using data in the original context for operational reporting or operational analytics, then Silver can be a temporal layer. However, if you plan on retaining history and use this data for operational reporting and analytics, then, I encourage you to make Silver a persistent layer.

Data in Silver is queryable. From a data modeling standpoint, this means that for Silver it's recommended to follow a more denormalized data model. Why? Because such a design better utilizes the distributed column-based storage that is separated from compute. Does this mean that you shouldn't use a 3rd-normal form or Data Vault-like data model? Well, you could implement a design that is heavier normalized. On the flip side, I don't see any compelling arguments. Delta already provides isolation and protection. For example, you can turn on merge schema for handling changes. Besides that, you have history in Silver and also history in your Bronze layer from which you can (re)load data again. Thus, flexibility is already provided. So, then why add increased complexity, slow down performance and add more expensive runtimes to your design? It's a trade-off you should make. If you would like to learn more on this subject, then I recommend you to watch the [video from Simon Whiteley](https://www.youtube.com/watch?v=RNMoWnSWcTo) in which he provides many considerations.

Another discussion that I sometimes have is on whether you should already join or integrate data between applications and source systems. Here the situation is a bit more nuanced. I recommend, if possible, breaking things apart for better managing and isolating concerns. For facilitating scenarios in which you utilize Silver for operational reporting or operational analytics, this consequently means that it's recommended to not already combine and integrate data between source systems. If you would do so, then you would create unnecessary coupling points between applications. For example, for another consumer or user that is only interested in data from a single source, there's also coupling to other systems, because data first is combined in a harmonized layer, and then served out. So, such data consumers are more likely to see potential impact from other systems. If you aim for such an isolated design, then consequently the combination or integration of data between sources moves up one layer.

The same above argument holds true when aligning your lake houses with the source-system side of your architecture. If you plan on building data products and strongly want to align data ownership, then I wouldn't encourage your engineers to already cross-join data between applications from other domains.

For the enrichments, such as calculations, there are also considerations you should make. If you plan to facilitate operational reporting and for that, enrichments are needed, then I recommend already enriching your data in the Silver layer. This potentially could result in some extra calibration when combining data at a later stage in Gold. Yes, this might be additional work, but it's worth having the benefits of flexibility.

#### Gold layer

Data in the Gold layer, according to the principles of a Lakehouse architecture, is typically organized in consumption-ready "project-specific" databases. From from this perspective, you could argue that data ownership changes, because data is no longer source-system is aligned. Instead, it has been integrated and combined with other data.

For Gold, depending on your use cases, I recommend a more de-normalized and read-optimized data model with fewer joins. So, a Kimball-style star schema. In addition to that, expect the following characteristics:

- Gold tables represent data that has been transformed for consumption or use cases.
- Data is stored in an efficient storage format, preferably Delta.
- Gold uses versioning for rolling back processing errors.
- Historization is applied only for the set of use cases or consumers. So, Gold can be a selection or aggregation of data that's found in Silver.
- In Gold you apply complex business rules. So, it uses many post-processing activities, calculations, enrichments, use-case specific optimizations, etc.
- Data is highly governed and well-documented.

Gold is often the most complex layer because its design varies on the scope of your architecture. In the simplest scenario, your Lakehouses are only aligned with the source-system side. If so, data that sits in Gold will represent "data product" data. Thus, data is generic and user-friendly for broad distribution to many other domains. Then, and after distribution, you expect data to land in another platform. This could be a Lakehouse again. If so, you would expect Gold in these platform to match the precise requires of analytical consumers. Thus, data has been modelled. Its shape and structure is highly specific for the use case you're working on. The upper way of working could lead to principles in which you allow domains to only operate on internal data that is not directly served to other domains. So, there might be tables that are flexible and can be adjusted at any times. And there are other tables with a formal status that are being consumed by other parties.

If your Lakehouse scope is larger and targets both sides, then, extra layers are expected. Some people call these extra layers workspace or presentation layers. In such a design, data in Gold is more generic. It's integrated and prepared for a set of use cases. Then, within these workspace or presentation layers you see subsets. Such a design is very similar to how you usually do data modeling within data warehousing. Gold behaves like a generic integration layer from which data marts or subsets can be populated.

Some companies also use these workspace or presentation layers for sharing data across to other platforms or teams. So, they make selections and/or prefilter data for specific use cases. Other customers apply tokenization, which means that they replace sensitive values with randomized data strings. Other use additional services for data anonymization. You could argue that this data in a way behaves as "data product" data.

### Medallion architecture and data mesh

The Medallion architecture is compatible with the concept of a data mesh. Bronze and silver tables can be joined together in a "one-to-many" fashion, meaning that the data in a single upstream table could be used to generate multiple downstream tables.

## Labs

1. Introduction to Data Lakehouses - Delta, Iceberg and Hudi
2. Working with AWS S3 and Delta lake in Databricks

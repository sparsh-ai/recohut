# Deltalake

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

An open-source storage format that brings ACID transactions to Apache Spark™ and big data workloads.

* **Open format**: Stored as Parquet format in blob storage.
* **ACID Transactions**: Ensures data integrity and read consistency with complex, concurrent data pipelines.
* **Schema Enforcement and Evolution**: Ensures data cleanliness by blocking writes with unexpected.
* **Audit History**: History of all the operations that happened in the table.
* **Time Travel**: Query previous versions of the table by time or version number.
* **Deletes and upserts**: Supports deleting and upserting into tables with programmatic APIs.
* **Scalable Metadata management**: Able to handle millions of files are scaling the metadata operations with Spark.
* **Unified Batch and Streaming Source and Sink**: A table in Delta Lake is both a batch table, as well as a streaming source and sink. Streaming data ingest, batch historic backfill, and interactive queries all just work out of the box.

![](https://www.databricks.com/wp-content/uploads/2022/06/db-247-blog-img-3.png)

Watch these videos:

- https://www.youtube.com/watch?v=yumysN3XwbQ
- https://www.youtube.com/watch?v=PftRBoqjhZM
- https://www.youtube.com/watch?v=BMO90DI82Dc
- https://www.youtube.com/watch?v=H5nMHhlh5N0
- https://www.youtube.com/watch?v=fApTba65Dnk

### Why an ACID Delta Lake

There are many advantages to introducing Delta Lake into a modern cloud data architecture. Traditionally, data lakes and Apache Spark are not ACID compliant. Delta Lake introduces this ACID compliance to solve many the following ACID compliance issues:

1. **Atomicity**: *Write either all data or nothing*. Apache Spark *save modes* do not utilize any locking and are not atomic. With this, a failed job may leave an incomplete file and may corrupt data. Additionally, a failing job may remove the old file and corrupt the new file. While this seems concerning, Spark does have built-in data frame writer APIs that are not atomic but behave so for append operations. This however does come with performance overhead for use with cloud storage. The currently available Apache Spark save modes include ErrorIfExists, Append, Overwrite, and Ignore.
2. **Consistency**: *Data is always in a valid state*. If the Spark API writer deletes an old file and creates a new one and the operation is not transactional, then there will always be a period of time when the file does not exist between the deletion of the old file and creation of the new. In that scenario, if the overwrite operation fails, this will result in data loss of the old file. Additionally, the new file may not be created. This is a typical Spark overwrite operation issue related to consistency.
3. **Isolation**: *Multiple transactions occur independently without interference*. This means that when writing to a dataset, other concurrent reads or writes on the same dataset should not be impacted by the write operation. Typical transactional databases offer multiple isolation levels, such as read uncommitted, read committed, repeatable read, snapshot, and serializable. While Spark has task- and job-level commits, since it lacks atomicity, it does not have isolation types.
4. **Durability**: *Committed data is never lost.* When Spark does not correctly implement a commit, then it overwrites all the great durability features offered by cloud storage options and either corrupts and/or loses the data. This violates data durability.

### Seperation of Compute and Storage Layer

![Evolution from cloud data warehouses to cloud data lakehouses (courtesy of Tomer Shiran)](https://user-images.githubusercontent.com/62965911/213930654-e49a4550-0e1d-42e2-9813-344e7728cfec.png)
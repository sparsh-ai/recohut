# Apache Iceberg

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
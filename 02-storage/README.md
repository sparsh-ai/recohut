# Data Storages

Storage is the core piece of a data platform around which everything else is built. Data gets ingested into the storage layer and is distributed from there. All workloads (data processing, analytics, and machine learning) access this layer.

![CH02_F01_Riscutia2](https://user-images.githubusercontent.com/62965911/218320138-c3c04f51-8ed7-4872-893a-a1d60a159839.png)

## Postgres vs MySQL

When it comes to choosing a relational database management system (RDBMS), two popular options are PostgreSQL and MySQL. Both have been around for decades and have proven to be highly reliable, secure, and scalable. However, they have different strengths and weaknesses that make one more suitable for certain use cases than the other.

Follow [this](https://dbconvert.com/blog/mysql-vs-postgresql/?utm_source=pocket_reader) link for more information.

#### When should you use a data lake?

We can consider using data lakes for the following scenarios:

- If you have data that is too big to be stored in structured storage systems like data warehouses or SQL databases
- When you have raw data that needs to be stored for further processing, such as an ETL system or a batch processing system
- Storing continuous data such as **Internet of Things** (**IoT**) data, sensor data, tweets, and so on for low latency, high throughput streaming scenarios
- As the staging zone before uploading the processed data into an SQL database or data warehouse
- Storing videos, audios, binary blob files, log files, and other semi-structured data such as **JavaScript Object Notation** (**JSON**), **Extensible Markup Language** (**XML**), or **YAML Ain't Markup Language** (**YAML**) files for short-term or long-term storage.
- Storing processed data for advanced tasks such as ad hoc querying, **machine learning** (**ML**), data exploration, and so on.

## SQL vs NoSQL

|                            | SQL                                                                                                                             | NoSQL                                                                                                                                                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Definition                 | SQL databases are primarily called RDBMSs or relational databases.                                                              | NoSQL databases are primarily called as non-relational or distributed databases.                                                                                                             |
| Designed for               | Traditional RDBMS uses SQL syntax and queries to analyze and get the data for further insights. They are used for OLAP systems. | NoSQL database system consists of various kinds of database technologies. These databases were developed in response to the demands presented for the development of the modern application. |
| Query language             | Structured Query Language (SQL)                                                                                                 | No declarative query language                                                                                                                                                                |
| Type                       | SQL databases are table-based databases.                                                                                        | NoSQL databases can be document-based, key-value pair, graph databases.                                                                                                                      |
| Schema                     | SQL databases have a predefined schema.                                                                                         | NoSQL databases use a dynamic schema for unstructured data.                                                                                                                                  |
| Ability to scale           | SQL databases are vertically scalable.                                                                                          | NoSQL databases are horizontally scalable.                                                                                                                                                   |
| Examples                   | Oracle, Postgres, and MS SQL.                                                                                                   | MongoDB, Redis, Neo4j, Cassandra, HBase.                                                                                                                                                     |
| Best suited for            | An ideal choice for the complex query-intensive environment.                                                                    | It is not a good fit for complex queries.                                                                                                                                                    |
| Hierarchical data storage | SQL databases are not suitable for hierarchical data storage.                                                                   | More suitable for the hierarchical data store as it supports key-value pair methods.                                                                                                         |
| Variations                 | One type with minor variations.                                                                                                 | Many different types that include key-value stores, document databases, and graph databases.                                                                                                 |
| Development year           | It was developed in the 1970s to deal with issues with flat file storage.                                                       | Developed in the late 2000s to overcome issues and limitations of SQL databases.                                                                                                             |
| Consistency                | It should be configured for strong consistency.                                                                                 | It depends on DBMS as some offer strong consistency like MongoDB, whereas others offer only eventual consistency, like Cassandra.                                                            |
| Best used for              | RDBMS is the right option for solving ACID problems.                                                                            | NoSQL is best used for solving data availability problems.                                                                                                                                   |
| Importance                 | It should be used when data validity is super important.                                                                        | Use when it’s more important to have fast data than correct data.                                                                                                                           |
| Best option                | When you need to support dynamic queries.                                                                                       | Use when you need to scale based on changing requirements.                                                                                                                                   |
| ACID vs. BASE model       | ACID (Atomicity, Consistency, Isolation, and Durability) is a standard for RDBMS.                                               | BASE (Basically Available, Soft state, Eventually consistent) is a model of many NoSQL systems.                                                                                              |

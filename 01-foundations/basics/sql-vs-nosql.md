# SQL vs NoSQL

As you design large systems ( or even smaller ones), you need to decide the inflow-processing and outflow of data coming- and getting processed in the system.

Data is generally organized in tables as rows and columns where columns represents attributes and rows represent records and keys have logical relationships. The SQL db schema always shows relational, tabular data following the ACID properties.

SQL databases have predefined schema and the data is organized/displayed in the form of tables. These databases use SQL ( Structured Query Language) to define, manipulate, update the data.

Relational databases like MS SQL Server, PostgreSQL, Sybase, MySQL Database, Oracle, etc. use SQL.

NoSQL databases on the other side, have no predefined schema which adds to more flexibility to use the formats that best suits the data - Work with graphs, column-oriented data, key-value and documents etc. They are generally preferred for hierarchical data, graphs ( e.g. social network) and to work with large data.

Some examples - Wide-column use Cassandra and HBase, Graph use Neo4j, Document use MongoDB and CouchDB, Key-value use Redis and DynamoDB.

![sql-nosql](https://user-images.githubusercontent.com/62965911/222883560-23c9b9d1-1105-4f34-acf4-d175ea41161e.png)

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

**SQL**

- Ensure ACID compliance.
  - Reduce anomalies.
  - Protect database integrity.
- Data is structured and unchanging.

**NoSQL**

- Data has little or no structure.
- Make the most of cloud computing and storage.
  - Cloud-based storage requires data to be easily spread across multiple servers to scale up.
- Rapid development.
  - Frequent updates to the data structure.

### Storage

- SQL: store data in tables.
- NoSQL: have different data storage models.

### Schema

- SQL
  - Each record conforms to a fixed schema.
  - Schema can be altered, but it requires modifying the whole database.
- NoSQL:
  - Schemas are dynamic.

### Querying

- SQL
  - Use SQL (structured query language) for defining and manipulating the data.
- NoSQL
  - Queries are focused on a collection of documents.
  - UnQL (unstructured query language).
  - Different databases have different syntax.

### Scalability

- SQL
  - Vertically scalable (by increasing the horsepower: memory, CPU, etc) and expensive.
  - Horizontally scalable (across multiple servers); but it can be challenging and time-consuming.
- NoSQL
  - Horizontablly scalable (by adding more servers) and cheap.

### ACID

- Atomicity, consistency, isolation, durability
- SQL
  - ACID compliant
  - Data reliability
  - Gurantee of transactions
- NoSQL
  - Most sacrifice ACID compliance for performance and scalability.

### Common types of NoSQL

#### Key-value stores

- Array of key-value pairs. The "key" is an attribute name.
- Redis, Vodemort, Dynamo.

#### Document databases

- Data is stored in documents.
- Documents are grouped in collections.
- Each document can have an entirely different structure.
- CouchDB, MongoDB.

#### Wide-column / columnar databases

- Column families - containers for rows.
- No need to know all the columns up front.
- Each row can have different number of columns.
- Cassandra, HBase.

#### Graph database

- Data is stored in graph structures
  - Nodes: entities
  - Properties: information about the entities
  - Lines: connections between the entities
- Neo4J, InfiniteGraph
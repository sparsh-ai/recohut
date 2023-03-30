# Data Engineering

## What is Data Engineering?

There are tons of definitions but you have to stick to one and understand it deeply. Here is one such good definition:

![](https://user-images.githubusercontent.com/62965911/213917818-65a2146a-5eb3-4818-861f-5bad0155b8d0.svg)

Data engineers have a key role in a modern data organization. It is a multidisciplinary role, so it needs knowledge of programming, data transformation, and mathematics, among other areas. To support these important activities, there are several open source and cloud tools to help data engineers perform their day-to-day operations.

The following are some examples of tasks that are the responsibility of the data engineer:

- Developing data ingestion pipelines
- Setting connectivity standards in data sources with proper security and latency
- Maintaining data pipelines creating scripts for data structures with versioning control
- Applying modern data exploration languages and libraries to generate insights
- Supporting database administrators in the necessary analytical database maintenance routines
- Modeling and implementing data consumption structures aligned with the business area needs
- Supporting the automation of data analysis processes, model creation, and databases (DataOps)

## How It Works?

Make sure you watch this short 15-mins video, as it explains a lot of concepts with great examples:

<iframe width="80%" height="280" src="https://www.youtube.com/embed/qWru-b6m030" title="How Data Engineering Works" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Landscape

![](./img/bigpicture.drawio.svg)

> For more info - https://youtu.be/bFC1MBijB-c

## Role of a Data Engineer

![img](https://user-images.githubusercontent.com/62965911/213917822-612d86ce-85f9-4565-8f3c-47405ae57e4c.svg)

- Big Data Engineers design and build complex data pipelines and have expert knowledge in coding using Python, etc. These professionals collaborate and work closely with data scientists to run the code using various tools such as the Hadoop ecosystem, etc.
- Data Architects are typically the database administrators and are responsible for data management. These professionals have in-depth knowledge in databases, and they also help in business operations.
- Business Intelligence Engineers are skilled in data warehousing and create dimension models for loading data for large scale enterprise reporting solutions. These professionals are experts in using ELT tools and SQL.
- Data Warehouse Engineers are responsible for looking after the ETL processes, performance administration, dimensional design, etc. These professionals take care of the full back-end development and dimensional design of the table structure.
- Technical Architects design and define the overall structure of a system with an aim to improve the business of an organization. The job role of these professionals involves breaking large projects into manageable pieces.

## Skills You Need

1. **SQL** - Querying data using SQL is an essential skill for anyone who works with data. Listed as one of the top technologies on data engineer job listings, SQL is a standardized programming language used to manage relational databases (not exclusively) and perform various operations on the data in them. Data Engineering using Spark SQL.
1. **Python Programming** - As a data engineer you'll be writing a lot of code to handle various business cases such as ETLs, data pipelines, etc. The de facto standard language for data engineering is Python (not to be confused with R or nim that are used for data science, they have no use in data engineering). Python helps data engineers to build efficient data pipelines as many data engineering tools use Python in the backend. Moreover, various tools in the market are compatible with Python and allow data engineers to integrate them into their everyday tasks by simply learning Python.
1. **Cloud Computing** - Data engineers are expected to be able to process and handle data efficiently. Many companies prefer the cloud solutions to the on-premise ones. Amazon Web Services (AWS) is the world's most comprehensive and broadly adopted cloud platform, offering over 200 fully featured services. Data engineers need to meet various requirements to build data pipelines. This is where AWS data engineering tools come into the scenario. AWS data engineering tools make it easier for data engineers to build AWS data pipelines, manage data transfer, and ensure efficient data storage.
1. **Shell Scripting** - Unix machines are used everywhere these days and as a data engineer, they are something we interact with every single day. Understanding common shell tools and how to use them to manipulate data will increase your flexibility and speed when dealing with day to day data activities.
1. **Relational and NoSQL Databases** - RDBMS are the basic building blocks for any application data. A data engineer should know how to design and architect their structures, and learn about concepts that are related to them. NoSQL is a term for any non-relational database model: key-value, document, column, graph, and more. A basic acquaintance is required, but going deeper into any model depends on the job. Column databases are a kind of nosql databases. They deserve their own section as they are essential for the data engineer as working with Big Data online (as opposed to offline batching) usually requires a columnar back-end.
1. **Data Lakes and Warehouses** - Understand the concepts behind data warehouses and familiarize youself with common data warehouse solutions. Also make yourself famliar with data lakes and lakehouse concepts like medallion architecture and delta format.
1. **OLAP Data Modeling** - OLAP (analytical) databases (used in data warehouses) data modeling concepts, modeling the data correctly is essential for a functioning data warehouse.
1. **Batch and Stream Data Processing** - Batch Data processing using Python, SQL and Spark. Everyone should know how it works, but going deep into the details and operations are recommended only if necessary. Stream Data Processing is the data processing on the fly. Suggested to get a good grasp of the subject and then dive deep into a specific tool like Kafka, Spark, Flink, etc.
1. **Pipeline / Workflow Management** - Data engineers should have experience with data pipeline and ETL (extract, transform, load) tools, such as Apache NiFi, Apache Kafka, Apache Airflow, Talend etc. These tools are used to build data pipelines that collect, store, and process data. Airflow is considered to be the defacto standard, but any understanding of DAGs - directed acyclical graphs for tasks will be good.
1. **Spark and Distributed Computing** - Data engineers should understand distributed systems, such as how data is stored and processed across multiple machines. This knowledge is essential for designing and implementing big data systems that can handle large amounts of data.

**Soft skills**

1. Strong analytical and problem-solving skills: Data engineers should have strong analytical and problem-solving skills, as they are responsible for designing and implementing data pipelines, troubleshooting issues, and ensuring data quality.
2. Understanding of data governance and security: Data engineers should be familiar with the best practices and how to implement them in the data pipeline, such as data encryption, access control, and data masking.
3. Strong communication and collaboration skills: Data engineers often work with cross-functional teams and must be able to communicate effectively with data scientists, analysts, internal and external customers and other stakeholders.

**Other Skills**

1. Developer tools - Git, VSCode and Jupyter Notebook
1. DevOps - Infra as Code, Container Orchestration, API Management, CICD Pipelines
1. Basic ML/AI Skills - Machine Learning Basics, NLP & Computer Vision, Recommender Systems, MLOps Pipelines

## Key Concepts

1. Data Warehousing: The process of collecting, storing, and managing large sets of data in a central repository for reporting and analysis. Data warehousing allows organizations to store and access large amounts of data in a structured and efficient manner. This enables users to easily query and extract insights from the data, and it also supports the creation of data-driven reports and dashboards.
2. Data Modeling: The process of designing and creating a conceptual representation of data and its relationships, typically using diagrams or other tools. Data modeling is an important step in the data warehousing process, as it helps to ensure that data is stored in a logical and consistent manner. This makes it easier for users to understand and navigate the data, and it also supports the creation of efficient data queries.
3. Data Integration: The process of combining data from different sources into a single, unified view. Data integration is a critical step in the data warehousing process, as it allows organizations to combine data from different systems and sources into a single repository. This enables users to access and analyze data from multiple sources in a single location, and it also supports the creation of data-driven reports and dashboards.
4. Data Pipelines: The process of creating a series of steps to automatically extract, transform, and load data from one system to another. Data pipelines are an essential component of data warehousing and integration, as they automate the process of moving data from one system to another. This reduces the need for manual data entry and improves the accuracy and efficiency of data processing.
5. Data Quality: The process of ensuring that data is accurate, complete, and relevant, and that it meets the needs of the users and systems that rely on it. Data quality is a critical consideration for data engineers, as it helps to ensure that data is usable and valuable for decision making. This includes tasks such as data validation, data cleaning, and data standardization.
6. Data Governance: The process of creating policies and procedures to manage data throughout its lifecycle, including data security and compliance. Data governance is an important consideration for data engineers, as it helps to ensure that data is used and stored in a secure and compliant manner. This includes tasks such as data security, data privacy, and data compliance.
7. Data Processing: The process of applying algorithms and other methods to extract insights and value from data. Data processing is a critical step in the data warehousing process, as it allows organizations to extract insights and value from their data. This includes tasks such as data analysis, data mining, and machine learning.
8. Data Visualization: The process of creating graphical representations of data to help users understand and explore the data. Data visualization is an important step in the data warehousing process, as it allows users to easily explore and understand their data. This includes creating charts, graphs, and other visualizations that make it easy to see patterns and trends in the data.

## Data Pipelines

![img](https://user-images.githubusercontent.com/62965911/213917834-967b67bb-89e6-483a-bbbe-db8cf5ddf36c.svg)

### ELTL Pipeline

This pipeline is one of the most common process companies are following. In this pipeline, we first extract and load the data from multiple data sources into data lake and then transform it using distributed compute engines like spark and then load the transformed data into warehouses.

![](https://user-images.githubusercontent.com/62965911/213917819-7afbfc9c-b35b-4459-a86c-c28c09f4a429.svg)

> Check out animated flow [here](https://user-images.githubusercontent.com/62965911/213917792-c61931fb-c440-4ea3-b133-edf8bfbc40e0.gif)

## OLTP vs OLAP

#### Transactional databases (OLTP)

Transactional databases are used by systems for basic operations: creating, reading, updating, and deleting. Transactional systems are considered the core of the informatization of business processes. With these basic operations, we can create entities such as customers, products, stores, and sales transactions, among others, to store important data. A transactional database is commonly known as online transaction processing (OLTP) considering that this type of database serves online transactional operations between the application and the database. For an organization, transactional databases usually have their data segmented into entities, which can be tables (or not), with or without a relationship between these entities to facilitate the correlation between this data. For example, an e-commerce database can be structured with a table called Shopping_Cart, which represents the products that are being selected in the store during user navigation, and another called Purchases with the completed transaction records. The process of segmenting entities in a database is called normalization. The format of a normalized transactional database is optimized for transactional operations, but it is not the best format for data exploration and analysis.

The following is an example of a relational transactional database:

![B18569_01_04](https://user-images.githubusercontent.com/62965911/218830276-44ecdb83-3c85-4de2-8479-a5aedc7f8ce2.jpeg)

The preceding figure demonstrates a relational database of transactional workloads in a sales and delivery system. We can see the main entity, Orders, joined to Employees, Shippers, Customers, and Order Details, which then detail all products of this order in the relationship with the Products entity, which looks for information in the Categories and Suppliers entities.

#### Analytical databases (OLAP)

When the data solution requires a good interface for queries, explorations, and data analysis, the data storage organization is different from transactional databases. To meet this requirement, we prioritize the data aggregations and relationships for data consumption and exploration; this specialized data storage is called an **analytical database**.

Analytical databases use a process called **online analytical processing** (**OLAP**) and have undergone a great evolution in recent years with the emergence of data warehouses and big data platforms.

Analytical databases are constituted through a process of data ingestion, and they are responsible for processing and transforming the data into insights and information and then making this processed information available for consumption. The following steps describe this process:

1. **Data ingestion** -- The process responsible for connecting to transactional databases or other data sources to collect raw transaction information and include it in the analytical database
2. **Data processing** -- The process performed by the OLAP platform to create a data model, organize entities, perform indicator calculations, and define metrics for data consumption
3. **Data query** -- After the data model is loaded with the proper organization for querying, data manipulation and reporting tools can connect to the OLAP platform to perform your queries

The following diagram is an example of a structured data model in an OLAP database:

![B18569_01_05](https://user-images.githubusercontent.com/62965911/218830680-16962fc7-0cc1-4d79-bc11-f5c77b44b2a4.jpeg)

The following diagram is a simple comparison of OLTP and OLAP databases:

![B18569_01_06](https://user-images.githubusercontent.com/62965911/218830688-a6fb6ff1-8778-4fb3-9150-3d77526aff55.jpeg)

The preceding figure demonstrates the traditional flow of data, which is sourced and stored in transactional OLTP databases and then moved to OLAP analytical databases for data intelligence generation.

IMPORTANT NOTE

> There are modern data storage platforms that aim to unite OLTP and OLAP on the same platform, but these databases, often called NewSQL, still need to mature their structures to deliver the best of transactional and analytical worlds in the same database. The industry standard is to keep transactional and analytical data structures separate.

#### A transactional workload

Relational and non-relational databases can be used as solutions for transactional workloads, which are the databases used to perform basic data storage operations: **create, read, update, and delete** (**CRUD**). Transactional operations must be done in sequence, with a transaction control that only confirms the conclusion of this transaction (a process called a **commit**) when the entire operation is successfully executed. If this does not occur, the transaction is canceled, and all processes are not performed, thus generating a process called **rollback**.

An important idea to help understand the difference between relational and non-relational databases is ACID, present in most database technologies. These properties are as follows:

- **Atomicity**: This is the property that controls the transaction and defines whether it was successfully performed completely to commit or must be canceled by performing a rollback. Database technology should ensure atomicity.
- **Consistency**: For a running transaction, it is important to evaluate consistency between the database state *before* receiving the data and the database state *after* receiving the data. For example, in a bank transfer, when funds are added to an account, those funds must have a source. Therefore, it is important to know this source and whether the fund's source exit process has already been performed before confirming the inclusion in this new account.
- **Isolation**: This property evaluates whether there are multiple executions of transactions similar to the current one and if so, it keeps the database in the same state. It then evaluates whether the execution of transactions was sequential. In the bank transfer example, if multiple transactions are sent simultaneously, it checks whether the amounts have already left the source for all transactions, or you need to review one by one, transaction per transaction.
- **Durability**: This is responsible for evaluating whether a transaction remains in the committed database even if there is a failure during the process, such as a power outage or latency at the time of recording the record.

ACID properties are not unique to transactional databases; they are also found in analytic databases. At this point, the most important thing is to understand that these settings exist, and you can adjust them as per the requirements of your data solution use case.

##### Database management systems

**Database management systems** (**DBMSs**), which are database software, have ACID properties within their architecture, and in addition to performing these controls, they need to manage several complex situations. For example, if multiple users or systems try to access or modify database records, the database systems need to isolate transactions, perform all necessary validations quickly, and maintain the consistency of the data stored after the transaction is committed. For this, some DBMS technologies work with temporary transaction locks, so that actions are done sequentially. This lock is done during the process of an action executing in that record; for example, in an edit of a field in a table, the lock ends as soon as the commit is executed, confirming that transaction.

Some DBMSs are called **distributed databases**. These databases have their architecture distributed in different storage and processing locations, which can be on-premises in the company's data center or a different data center in the cloud. Distributed database solutions are widely used to maintain consistency in databases that will serve applications in different geographic locations, but this consistency doesn't need to be synchronous. For example, a mobile game can be played in the United States and Brazil, and the database of this game has some entities (categories, game modes, and so on) that must be shared among all players. But the transactions from the United States player do not necessarily need to appear to the player in Brazil in a real-time way; this transactional data will be synchronized from the United States to Brazil, but in an asynchronous process. Let's understand this process next.

##### Eventual consistency

All transactions in distributed databases take longer to process than in undistributed databases because it is necessary to replicate the data across all nodes in this distributed system. So, to maintain an adequate replication speed, the distributed databases only synchronize the data that is needed. This is the concept of *eventual consistency*, which configures ACID to perform replication between the distributed nodes asynchronously, after the confirmation of the transaction on the main node of the database is created. This technique can lead to temporary inconsistencies between database nodes. Ideally, the application connected to a distributed database does not require a guarantee of data ordering. It means that the data relating to this eventual consistency may appear to users with an eventual delay as well. Distributed databases are widely used by social media platforms, for news feeds, likes, and shares, among other features.

In addition to transactional, relational, or non-relational databases, we also have another data workload, the analytical workload, which we will address in the next section.

#### An analytical workload

The second category of data solutions is the analytical workloads. These analytical solutions are based on high-volume data processing platforms, optimized for querying and exploring, and not for CRUD transactions or with ACID properties. In analytical databases, we aggregate various data sources, such as more than one transactional database, as well as logs, files, images, videos, and everything that can generate information for a business analyst.

This raw data is processed and aggregated, thus generating summaries, trends, and predictions that can support decision-making.

An analytical workload can be based on a specific time or a sequence of dated events. In these workloads, it's common to evaluate only the data that is relevant to the analysis. For example, if you have a sales system with a transactional database (source) with several tables recording all sales, products, categories, and customers, among others, it is important to evaluate which of these tables can be used for the analytical database (destination) and then perform the data connections.

To create an analytical database, it is necessary to perform data ingestion, a process of copying data from sources to the analytical base. For this, a technique called **extract, transform, and load** (**ETL**), or the more recent **extract, load, and transform** (**ELT**), is used. The following figure demonstrates this process with an example of a transactional database as the data source and the analytical database as the destination:

![B18569_01_11](https://user-images.githubusercontent.com/62965911/218831832-7efbefdb-f234-478b-8140-f2cc31cfb491.jpeg)

In the preceding diagram, we can see that transactional databases are storages of information systems that automate business processes. Analytical databases act on simple and advanced data analysis, using, for example, statistical models with the application of machine learning, a branch of artificial intelligence. The data ingestion process is an important process for assembling an analytical database that meets the data solution.


## Data Storage Solutions

| **Architecture**          | **Total cost of solution**                                                                                                                                                  | **Flexibility of scenarios**                                                                                                                                                                      | **Complexity of development**                                                                                                                                                     | **Maturity of ecosystem**                                                                                                                                                                         | **Organizational maturity required**                                                                                                                                                            |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cloud data warehouse**  | **High** - given cloud data warehouses rely on proprietary data formats and offer an end to end solution together, the cost is high                                        | **Low** - Cloud data warehouses are optimized for BI/SQL based scenarios, there is some support for data science/exploratory scenarios which is restrictive due to format constraints            | **Low** - there is less moving parts and you can get started almost immediately with an end to end solution                                                                      | **High** - for SQL/BI scenarios, Low - for other scenarios                                                                                                                                       | **Low** - the tools and ecosystem are largely well understood and ready to be consumed by organizations of any shape/size.                                                                     |
| **Modern data warehouse** | **Medium** - the data preparation and historical data can be moved to the data lake at lower cost, still need a cloud warehouse which is expensive                         | **Medium** - diverse ecosystem of tools nad more exploratory scenarios supported in the data lake, correlating data in the warehouse and data lake needs data copies                             | **Medium** - the data engineering team needs to ensure that the data lake design is efficient and scalable, plenty of guidance and considerations available, including this book | **Medium** - the data preparation and data engineering ecosystem, such as Spark/Hadoop has a higher maturity, tuning for performance and scale needed, High - for consumption via data warehouse | **Medium** - the data platform team needs to be skilled up to understand the needs of the organization and make the right design choices at the least to support the needs of the organization |
| **Data lakehouse**        | **Low** - the data lake storage acts as the unified repository with no data movement required, compute engines are largely stateless and can be spun up and down on demand | **High** - flexibility of running more scenarios with a diverse ecosystem enabling more exploratory analysis such as data science, and ease of sharing of data between BI and data science teams | **Medium to High** - careful choice of right datasets and the open data format needed to support the lakehouse architecture                                                      | **Medium to High** - while technologies such as Delta Lake, Apache Iceberg, and Apache Hudi are gaining maturity and adoption, today, this architecture requires thoughtful design               | **Medium to High** - the data platform team needs to be skilled up to understand the needs of the organization and the technology choices that are still new                                   |
| **Data mesh**             | **Medium** - while the distributed design ensures cost is lower, lot of investment required in automation/blueprint/data governance solutions                              | **High** - flexibility in supporting different architectures and solutions in the same organization, and no bottlenecks on a central lean organization                                           | **High** - this relies on an end to end automated solution and an architecture that scales to 10x growth and sharing across architectures/cloud solutions                        | **Low** - relatively nascent in guidance and available toolsets                                                                                                                                  | **High** - data platform team and product/domain teams need to be skilled up in data lakes.                                                                                                    |

**Cost versus complexity of cloud data lake architectures**

![](https://user-images.githubusercontent.com/62965911/213930648-3e63ea81-b214-411a-9e4a-39a403ed35df.png)

## SQL vs NoSQL

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


## Big Data

![Six Vs of big data](https://user-images.githubusercontent.com/62965911/213918079-10af46d9-f906-4c3e-9b84-ddc47708bd15.png)


#### Lambda Architecture

Lambda architecture comprises Batch Layer, Speed Layer (also known as Stream layer), and Serving Layer.

The batch layer operates on the complete data and thus allows the system to produce the most accurate results. However, the results come at the cost of high latency due to high computation time. The batch layer stores the raw data as it arrives and computes the batch views for consumption. Naturally, batch processes will occur at some interval and will be long-lived. The scope of data is anywhere from hours to years.

The speed layer generates results in a low-latency, near real-time fashion. The speed layer is used to compute the real-time views to complement the batch views. The speed layer receives the arriving data and performs incremental updates to the batch layer results. Thanks to the incremental algorithms implemented at the speed layer, the computation cost is significantly reduced.

The batch views may be processed with more complex or expensive rules and may have better data quality and less skew, while the real-time views give you up-to-the-moment access to the latest possible data.

Finally, the serving layer enables various queries of the results sent from the batch and speed layers. The outputs from the batch layer in the form of batch views and the speed layer in the form of near-real-time views are forwarded to the serving layer, which uses this data to cater to the pending queries on an ad-hoc basis.

![](https://user-images.githubusercontent.com/62965911/213918086-32e76d06-a398-40ad-9271-16b9ffc3bb6b.png)

**Pros**

- It is a good balance of speed, reliability, and scalability. The batch layer of Lambda architecture manages historical data with the fault-tolerant, distributed storage, ensuring a low possibility of errors even if the system crashes.
- Access to both real-time and offline results in covering many data analysis scenarios very well.
- Having access to a complete data set in a batch window may yield specific optimizations that make Lambda better performing and perhaps even simpler to implement.

**Cons**

- Although the offline layer and the real-time stream face different scenarios, their internal processing logic is the same, so there are many duplicate modules and coding overhead.
- Reprocesses every batch cycle, which is not beneficial in specific scenarios.
- A data set modeled with Lambda architecture is difficult to migrate or reorganize.

**Use Cases**

- User queries are required to be served on an ad-hoc basis using immutable data storage.
- Quick responses are required, and the system should handle various updates in new data streams.
- None of the stored records shall be erased, and it should allow the addition of updates and new data to the database.

#### Kappa Architecture

The Kappa architecture solves the redundant part of the Lambda architecture. It is designed with the idea of replaying data. Kappa architecture avoids maintaining two different code bases for the batch and speed layers. The key idea is to handle real-time data processing, and continuous data reprocessing using a single stream processing engine and avoid a multi-layered Lambda architecture while meeting the standard quality of service.

![](https://user-images.githubusercontent.com/62965911/213918082-56da8775-caee-4db4-b515-7c20ee2bc6bd.png)

**Pros**

- Applications can read and write directly to Kafka (or other message queue) as developed. For existing event sources, listeners are used to stream writes directly from database logs (or datastore equivalents), eliminating the need for batch processing during ingress, resulting in fewer resources.
- Treating every data point in your organization as a streaming event also provides you the ability to 'time travel' to any point and see the state of all data in your organization.
- Queries only need to look in a single serving location instead of going against batch and speed views.

**Cons**

- The complication of this architecture mainly revolves around having to process this data in a stream, such as handling duplicate events, cross-referencing events, or maintaining order - operations that are generally easier to do in batch processing.
- Although the Kappa architecture looks concise, it isn't easy to implement, especially for the data replay.
- For Lambda, catalog services can auto-discover and document file and database systems. Kafka doesn't align with this tooling, so supporting scaling to enterprise-sized environments strongly infers implementing confluent enterprise with a schema registry that attempts to play the role of a catalog service.

**Use Cases**

- When the algorithms applied to the real-time data and the historical data are identical, it is very beneficial to use the same code base to process historical and real-time data and, therefore, implement the use-case using the Kappa architecture.
- Kappa architecture can be used to develop data systems that are online learners and therefore don't need the batch layer.
- The order of the events and queries is not predetermined. Stream processing platforms can interact with the database at any time.

Kappa is not a replacement for Lambda as some use-cases deployed using the Lambda architecture cannot be migrated.

When you seek an architecture that is more reliable in updating the data lake as well as efficient in training the machine learning models to predict upcoming events robustly, then use the Lambda architecture as it reaps the benefits of both the batch layer and speed layer to ensure few errors and speed.

On the other hand, when you want to deploy big data architecture using less expensive hardware and require it to deal effectively with unique events occurring continuously, then select the Kappa architecture for your real-time data processing needs.

Check out [this whitepaper](https://www.qlik.com/us/resource-library/modernizing-your-data-architecture-to-unlock-business-value) and [related webinar](https://videos.qlik.com/watch/mm2p55sd3zvdYHqkzhqRaH?_ga=2.269188596.401343546.1664008674-358725923.1664008674) to deep dive into this topic.

## Batch vs Incremental Data Processing

The idea behind incremental processing is quite simple. Incremental processing extends the semantics of processing streaming data to batch processing pipelines by processing only new data each run and then incrementally updating the new results. This unlocks great cost savings due to much shorter batch pipelines as well as data freshness speedups due to being able to run them much more frequently as well. 

> :eyeglasses: Case Study: <a href="https://www.uber.com/en-IN/blog/ubers-lakehouse-architecture/" target="_blank">Setting Uber’s Transactional Data Lake in Motion with Incremental ETL Using Apache Hudi</a>

## Quizzes

> :game_die: Quiz: <a href="#/a1-interviewprep/50-most-common-interview-questions.md" target="_blank">50 Most Common Interview Questions</a>
>
> :game_die: Quiz: <a href="#/a1-interviewprep/25-most-common-interview-questions.md" target="_blank">25 Most Common Interview Questions</a>

## Case Studies

> :eyeglasses: Case Study: <a href="#/a3-casestudies/fair.md" target="_blank">Fair - Data Ingestion with a Cloud Data Platform</a>
>
> :eyeglasses: Case Study: <a href="#/a3-casestudies/harmony.md" target="_blank">Harmony - Responsive Data Pipeline</a>
>
> :eyeglasses: Case Study: <a href="#/a3-casestudies/panoramic.md" target="_blank">Panoramic - Simplifying Data Ingestion, Transformation, And Delivery</a>

## Explore Further

1. [Data Contract](01-foundations/data-engineering/data-contract.md)
1. [Data Management](01-foundations/data-engineering/data-management.md)
1. [Data Quality](01-foundations/data-engineering/data-quality.md)
1. [Data Engineering Roadmap](https://knowledgetree.notion.site/Data-Engineering-Roadmap-6e543497f9074aba89520b45b678d32f)
1. [Approaching the data pipeline architecture](https://knowledgetree.notion.site/Approaching-the-data-pipeline-architecture-214bdf596037454ca3f879894035c83f)
1. [The Data Engineering Megatrend: A Brief History](https://www.rudderstack.com/blog/the-data-engineering-megatrend-a-brief-history)
1. [How to gather requirements for your data project](https://www.startdataengineering.com/post/n-questions-data-pipeline-req/)
1. [Five Steps to land a high paying data engineering job](https://www.startdataengineering.com/post/n-steps-high-pay-de-job/)
1. [Functional Data Engineering - A Set of Best Practices](https://youtu.be/4Spo2QRTz1k)
1. [4 Key Aspects for Designing Distributed Systems](https://betterprogramming.pub/4-key-aspects-for-designing-distributed-systems-dc8fec7b8c5b)
1. [Big Data](https://www.alura.com.br/artigos/big-data)
1. [Data Lake vs Data Warehouse](https://www.alura.com.br/artigos/data-lake-vs-data-warehouse)
1. [Data Mesh: indo além do Data Lake e Data Warehouse](https://medium.com/data-hackers/data-mesh-indo-al%C3%A9m-do-data-lake-e-data-warehouse-465d57539d89)
1. [Data as a product vs data products. What are the differences?](https://towardsdatascience.com/data-as-a-product-vs-data-products-what-are-the-differences-b43ddbb0f123)
1. [Data Mesh Principles and Logical Architecture](https://martinfowler.com/articles/data-mesh-principles.html)
1. [Data Mesh and Governance](https://www.thoughtworks.com/en-us/about-us/events/webinars/core-principles-of-data-mesh/data-mesh-and-governance)
1. [Data Engineering Challenges](https://www.youtube.com/watch?v=VxZu4B8wIbQ)
1. [Data Lake / Lakehouse Guide: Powered by Data Lake Table Formats (Delta Lake, Iceberg, Hudi)](https://airbyte.com/blog/data-lake-lakehouse-guide-powered-by-table-formats-delta-lake-iceberg-hudi)
2. https://martinfowler.com/bliki/DataLake.html
3. [Top Delta Lake Interview Questions](https://www.analyticsvidhya.com/blog/2022/07/top-10-delta-lake-interview-questions/)
4. https://www.databricks.com/blog/2021/08/30/frequently-asked-questions-about-the-data-lakehouse.html
5. http://www.igfasouza.com/blog/what-is-data-lake
6. https://40uu5c99f3a2ja7s7miveqgqu-wpengine.netdna-ssl.com/wp-content/uploads/2017/02/Understanding-data-lakes-EMC.pdf
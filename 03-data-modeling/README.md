# Data Modeling

## Sub-modules

1. [SQL Data Modeling](./sql-data-modeling/)
2. [NoSQL Data Modeling](./nosql-data-modeling/)

## Concepts

The data model helps us design our database. When building a plane, you don’t start with building the engine. You start by creating a blueprint anschematic. Creating database is just the same, you start with modelling the data. Model is a representation of real data that provide us with characteristic, relation and rules that apply to our data. It doesn’t actually contain any data in it.

In the classical sense, a data model is simply metadata that described the structure, content, and relationships that exist within a group of related data assets. Maintaining a data model has long been a standard practice for OLTP workloads built on SQL. Typically maintained by data engineers & data architects, they help manage the evolution of assets, remove unnecessary duplication & enforce conventions to maintain an intuitive and consistent layout. A key additional benefit is to inform consumers (ex. data analysts) about assets and how best to use them. For this reason, maintaining data models is also a common practice for managing the evolution of large SQL data warehouses. Without data models, end users would find it challenging to navigate around a library of hundreds (if not thousands) of data assets and correctly leverage them.

### Stages of Data Modeling

#### Conceptual Data Model

Define **WHAT** the system contains. Used by business stakeholders. The purpose is to organize, scope and define business concepts and rules.

#### Logical Data Model

Defines **HOW** the system should be implemented regardless of the DBMS. Used by data architects and business analysts. The purpose is to develop technical map of rules and data structures.

#### Physical Data Model

Describes **HOW** the system will be implemented using a specific DBMS system. Used by DBA and developers. The purpose is actual implementation of the database.

### Types of Data Modeling

#### 3NF/ Relational Modeling

Owing its origins to the entity-relationship modeling methodology, 3NF is also widely used in data warehousing to serve as a normalized layer to the further layers. It provides tremendous flexibility but can end up having really verbose queries. It is usually found in OLTP systems.

#### Dimensional Modeling

Dimensional modeling is a bottom-up approach to designing data warehouses in order to optimize them for analytics. Dimensional models are used to denormalize business data into **dimensions** (like time and product) and **facts** (like transactions in amounts and quantities), and different subject areas are connected via conformed dimensions to navigate to different fact tables. It is usually found in OLAP systems.

The most common form of dimensional modeling is the [star schema](https://www.databricks.com/glossary/star-schema). A star schema is a multi-dimensional data model used to organize data so that it is easy to understand and analyze, and very easy and intuitive to run reports on. Kimball-style star schemas or dimensional models are pretty much the gold standard for the presentation layer in data warehouses and data marts, and even semantic and reporting layers. The star schema design is optimized for querying large data sets. The most popular exponents of this method are the star schema and snowflake schema.

![star-schema-datamodel](https://user-images.githubusercontent.com/62965911/216760155-70c45f6e-7599-47a3-a337-183262bdff6d.png)

#### Data Vault Modeling

A hybrid between 3NF and dimensional modeling, the Data Vault model is much closer to 3NF than to the dimensional model. It tries to keep the best features of 3NF, such as ease of querying highly granular, historical data, and still restructures the data into new types of tables, such as satellites, links, hubs, bridges, and PITs. A [Data Vault](https://www.databricks.com/glossary/data-vault) is a more recent data modeling design pattern used to build data warehouses for enterprise-scale analytics compared to Kimball and Inmon methods. Data Vaults organize data into three different types: ** hubs** ,  **links** , and  **satellites** . Hubs represent core business entities, links represent relationships between hubs, and satellites store attributes about hubs or links. Data Vault focuses on agile data warehouse development where scalability, data integration/ETL and development speed are important.

![data-vault-datamodel](https://user-images.githubusercontent.com/62965911/216759991-593de2e9-2777-4ba1-8915-1674b97cbf37.png)

### Steps of Building Data Models

#### Gathering requirements

Before designing the warehouse table(s), you should always clearly define the end objectives.

Some questions you need answered/explored are

- What does this data represent and why is it needed?
- Who is the end-user of the table(s)?
- What is the business process that generates this data? How is this data generated?
- A few (>= 3) different example queries that the end-user is expected to run?
- What is the expected number of read queries per minute?
- What is an acceptable query execution time for reading from the table(s)?
- What is the expected number of daily records?
- What is the general date range (and/or other) filters for the read queries?
- What is the historical range of data that needs to be available for querying?

Answers to these questions will determine how you model and transform the data.

#### Exploration

The next step is to explore the data, check for any data issues, validate assumptions, approximate data size growth, validate business rules, check for missing/duplicate rows on joins, etc

You will need to load the raw data into your data warehouse. There are multiple ways to ingest data into a data warehouse. For exploration, dump the data into a cloud storage system and use a COPY INTO command to load raw data into your data warehouse.

Some points you need answered/explored are:

1. Data schema checks

- Are data types consistent with the columns?
- Are column names consistent?

2. Data quality checks

- Were all the records in the raw file loaded into the raw table? Use wc -l input_data_file.csv to count the number of lines in the input data.
- Check for absence of column values such as NULL, null, 'null', '', N/A, etc
- Do any of the column values have a field delimiter within them? Most data warehouses have options to handle these, e.g. quote_character, FIELD_OPTIONALLY_ENCLOSED_BY.

3. Validate business assumptions

- If you join this data with other business-relevant tables, do you get unexpected duplicates or missing rows? If so, why?
- If you aggregate by some id and aggregate numeric columns in a fact table, are the aggregates accurate? Or does it cause doubles/undercounting? If so, how can you prevent it?
- Does the number of rows per day (and/or other business entities) show clear patterns? (including seasonality)
- Do all the tables have a unique id?
- For every business entity table (aka dimension), is there a table that records every update made to that table?
- Be aware of values with specific meaning. E.g. sometimes -9999 (or similar) can be used to denote NULL or other values.

This will be an ongoing process. Since the data generation process upstream can change, you may find additional data issues, etc.

#### Modeling

With knowledge of the requirement and data issues, you are all set to model the end-user table(s). The standard approach is to have fact and dimension table(s). This type of data modeling has the advantage of being able to answer most queries. The downside is that this may require multiple joins, and can be a lot of work to manage.

Note:

> Dimensional/Data modeling always uses the concepts of facts (measures), and dimensions (context). Facts are typically (but not always) numeric values that can be aggregated, and dimensions are groups of hierarchies and descriptors that define the facts. For example, sales amount is a fact; timestamp, product, register#, store#, etc. are elements of dimensions. Dimensional models are built by business process area, e.g. store sales, inventory, claims, etc. Because the different business process areas share some but not all dimensions, efficiency in design, operation, and consistency, is achieved using conformed dimensions, i.e. using one copy of the shared dimension across subject areas.

Some points you need answered/explored are

- Naming conventions: Each company has its standard naming convention. If you don’t, make sure to establish this standard. (e.g. naming standard).
- Slowly changing dimensions: Most business entity tables (aka dimensions) have attributes that change over time. Consider creating an SCD2 table to capture historical changes.
- In-correct aggregates: Running aggregates on any numeric values of the fact table(s) should not produce duplicate/inaccurate results. This is usually a result of having the data representing different columns in one column.
- Pre-aggregating data: At times, the expected query pattern requires data to be rolled up to a higher granularity. In these cases, if your read time is longer than the requirement, you may want to pre-aggregate your data on a set schedule. Pre-aggregating the data will allow “read queries” to be much faster but introduces the additional overhead of creating, scheduling, and maintaining a data pipeline.
- Flat tables: Although the Kimball Model is very popular, it can get tedious for the end-user to query and join multiple tables. A way for the data team to provide a clean interface for the end-user is to create a wide flat table (or view). A flat table is a table with all the facts and dimensional columns. The end-user does not need to worry about joining multiple tables and can concentrate on analyzing the data.

Note:

> In a flat table, if some dimensional attributes change over time, then running a group-by query on those may produce inaccurate results. You can circumvent this by having 2 tables/views one with point-in-time dimensional attributes and the other with the most recent dimensional attribute.

#### Data storage

Storing data in the right format can significantly impact your query performance. When modeling your end-user tables, make sure to consider the impact of data storage on read-type queries.

It’s crucial to understand the following concepts.

- Partitioning: Partitioning/Clustering, can significantly reduce the amount of data scanned and hence reduce the cost.
- Storage formats: Such as Parquet, or ORC formats can significantly reduce data size and speed up transformations.
- Sorting: Sorting can also reduce the amount of data to be read and make transformations efficient.
- Cloud storage: External tables allow for data to be stored in a cloud storage system and read when necessary.

Every data warehouse has different naming/implementation/caveats concerning the above, e.g. Snowflake automatically does most of these are for you, while Redshift requires a more hands on approach.

### Normalization vs Denormalization

Normalization is Trying to increase data integrity by reducing the number of copies of the data. Data that needs to be added or updated will be done in as few places as possible. Denormalization is Trying to increase performance by reducing the number of joins between tables (as joins can be slow). Data integrity will take a bit of a potential hit, as there will be more copies of the data (to reduce JOINS).

### Star vs Snowflake Schema

Star Schema (introduced by Ralph Kimball) is the most widely used approach to organize data in database to make it easy to understand, read (fast data retrieval) and analyze. It is the underlying structure of dimensional model and also one of the methods used in dimensional modeling.

In practice, Star Schema is used to denormalize business data. It separates business process data into:

1. Fact tables that hold quantitative information about the business, such as quantity, unit price, sales amount, etc.
2. Dimension tables that hold descriptive information of the fact table, such as store, product, customer, etc.

With this design, the end-users are able to easily find the data they need, slice and dice the data however they see fit and evolve the schema if the business changes.

It is called a star schema because the fact table sits at the center of the logical diagram, and the small dimensional tables branch off to form the points of the star.

![](https://user-images.githubusercontent.com/62965911/214235541-66b537aa-4903-40ae-9587-57768efa1bd8.png)

In fact tables, you will have the foreign keys to dimension tables as well as aggregate or numeric information. We do not want descriptions or attributes in fact tables since those are reserved for dimension tables. We will use the foreign keys in a fact table to "*join"* the information in dimension tables.

Dimension tables are generally [denormalized](https://en.wikipedia.org/wiki/Denormalization) (may hold redundant data) and do not contain any foreign keys nor do they have any *"sub-dimension tables"*. Dimension table contains primary key and descriptive information of the fact table.

So how do we build a Star Schema? [As proposed by Kimball](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/four-4-step-design-process/#:~:text=Select%20the%20business%20process.,Identify%20the%20facts.), there are 4 steps in designing of a dimensional model.

1. Select the business process. The first step is to identify the business process that you want to model. Model the processes that are most significant or relevant to the business first.
2. Declare the grain. Grain refers to the level of detail of the information that you will store in the fact table. The grain should be at the most atomic or lowest level possible. For example, A line item on a grocery receipt. The grocery owner might want to ask questions such as *"what are the items that sold the best during the day in our grocery store?"*, and to answer this question we need to dig into line-item level instead of the order-level.
3. Identify the dimensions. You can identify the dimensions by looking at the descriptive information or attributes that exist in your business process and provide context to your measurable events. For example: payment method, customers, locations, etc.
4. Identify the facts. Facts are the quantitative measures in your business process that are always in numeric. For example: price, minutes, speed, etc. You should identify/select the measures that are true to your selected grain.

### [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem)

- Consistency: every read receives the most recent write or an error.
- Availability: every request receives a response that is not an error.
- Partition tolerance: the system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes
- CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability
- CAP is frequently misunderstood as if one has to choose to abandon one of the three guarantees at all times. In fact, the choice is really between consistency and availability only when a network partition or failure happens; at all other times, no trade-off has to be made.
- [ACID](https://en.wikipedia.org/wiki/ACID) databases choose consistency over availability.
- [BASE](https://en.wikipedia.org/wiki/Eventual_consistency) systems choose availability over consistency.

## Check your understanding

1. What is Data Normalization?
2. What is Data Denormalization?
3. What are the Pros and Cons of Data Normalization?
4. What are the Pros and Cons of Data Denormalization?
5. What is the difference among 1NF, 2NF and 3NF?
6. What are the different categories of NoSQL Databases?
7. What are the ACID properties and where these are applied?
8. What are the BASE properties and where these are applied?
9. What are the differences between SQL and NoSQL data modeling?
10. What is OLTP?
11. What is OLAP?
12. What are the differences between OLTP and OLAP?
13. What are the Pros and Cons of OLTP?
14. What are the Pros and Cons of OLAP?
15. What is CAP theorem?
16. What is Data Modeling and Why you should care?
17. What are the advantages of Data Modeling?
18. What is Conceptual Data Model?
19. What is Logical Data Model?
20. What is Physical Data Model?
21. What is Entity-Relation (ER) Model?
22. What is Star Schema?
23. What are the differences between Star Schema and Snowflake Schema?
24. Explain the Relational Data Modeling with an example
25. Explain the Non-Relational Data Modeling with an example
26. Explain the Kimball's Four Step Process to Dimensional Data Modeling
27. What is Inmon Data Modeling Approach?
28. What are the differences between Kimball and Inmon Data Modeling Approach?
29. What is the difference between Fact and Dimension Tables?
30. What are Slowly Changing Dimensions (SCDs)?
31. Explain Different Types of Slowly Changing Dimensions (SCDs)
32. What is Data Warehouse?
33. Why is Data Warehouse needed?
34. What are the differences between Databases and Data Warehouses?
35. What are the differences between Operational and Analytical Systems?
36. What is Data Mart?
37. Explain how the Cargo Shipping Company Created its Data Model?

## Resources

1. [Data Modeling by Packt](https://subscription.packtpub.com/book/big-data-and-business-intelligence/9781783989188/1/ch01lvl1sec03/data-modeling)
2. https://knowledgetree.notion.site/Data-Modeling-92b0646bc2674a23a6203d9309bf414f
3. [Database Schema Design Examples](https://blog.panoply.io/database-schema-design-examples)
4. [Data Modeling Layer &amp; Concepts](https://www.holistics.io/books/setup-analytics/data-modeling-layer-and-concepts/)
5. [Kimball’s Dimensional Data Modeling](https://www.holistics.io/books/setup-analytics/kimball-s-dimensional-data-modeling/)
6. [Modeling Example: A Real-world Use Case](https://www.holistics.io/books/setup-analytics/modeling-example-a-real-world-use-case/)
7. [Kimball Dimensional Modeling Techniques](https://bit.ly/3DPllXo)
8. [Designing a dimensional model for a cargo shipper](https://www.techshashank.com/data-warehousing/shipping-dimensional-modeling)
9. [5 Database Design Schema Example: Critical Practices &amp; Designs](https://hevodata.com/learn/schema-example/)
10. [Kimball’s 4-Step Dimensional Design Process](https://bit.ly/3LTUtHY)
11. [Introduction to Data Warehouse](https://knowledgetree.notion.site/Brief-Introduction-to-Data-Warehouses-Shared-83ead0962c7a4c1cb7f165995f58e122)
12. [Data Warehouse Schemas](https://knowledgetree.notion.site/Data-Warehousing-Schemas-Shared-a03264b8ab6d4a50b6be0d73a82f8c8c)
13. [Know Data Warehouse Essential Concepts](https://www.1keydata.com/datawarehousing/datawarehouse.html)
14. [Fundamental Data modeling and Data warehousing](https://medium.com/nerd-for-tech/fundamental-data-modeling-and-data-warehousing-b599183d998a)

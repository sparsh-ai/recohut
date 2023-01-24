# Data Modeling

## Steps

1. [SQL Data Modeling](./sql-data-modeling/)
1. [NoSQL Data Modeling](./nosql-data-modeling/)

## Note

The data model helps us design our database. When building a plane, you don’t start with building the engine. You start by creating a blueprint anschematic. Creating database is just the same, you start with modelling the data. Model is a representation of real data that provide us with characteristic, relation and rules that apply to our data. It doesn’t actually contain any data in it.

In the classical sense, a data model is simply metadata that described the structure, content, and relationships that exist within a group of related data assets. Maintaining a data model has long been a standard practice for OLTP workloads built on SQL. Typically maintained by data engineers & data architects, they help manage the evolution of assets, remove unnecessary duplication & enforce conventions to maintain an intuitive and consistent layout. A key additional benefit is to inform consumers (ex. data analysts) about assets and how best to use them. For this reason, maintaining data models is also a common practice for managing the evolution of large SQL data warehouses. Without data models, end users would find it challenging to navigate around a library of hundreds (if not thousands) of data assets and correctly leverage them.

### Types of data modeling

1. Conceptual Data Model - Define **WHAT** the system contains. Used by business stakeholders. The purpose is to organize, scope and define business concepts and rules.
2. Logical Data Model - Defines **HOW** the system should be implemented regardless of the DBMS. Used by data architects and business analysts. The purpose is to develop technical map of rules and data structures.
3. Physical Data Model - Describes **HOW** the system will be implemented using a specific DBMS system. Used by DBA and developers. The purpose is actual implementation of the database.

You can use several data modeling techniques when creating a data warehouse:

1. 3NF (third normal form) modeling — owing its origins to the entity-relationship modeling methodology, 3NF is also widely used in data warehousing to serve as a normalized layer to the further layers. It provides tremendous flexibility but can end up having really verbose queries.
2. Dimensional modeling — a modeling technique that restructures the data into denormalized fact and dimension tables to make analytic workloads easier to run. The most popular exponents of this method are the star schema and snowflake schema.
3. Data Vault modeling — a hybrid between 3NF and dimensional modeling, the Data Vault model is much closer to 3NF than to the dimensional model. It tries to keep the best features of 3NF, such as ease of querying highly granular, historical data, and still restructures the data into new types of tables, such as satellites, links, hubs, bridges, and PITs.

### Process of building the data models

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

:::note
Dimensional/Data modeling always uses the concepts of facts (measures), and dimensions (context). Facts are typically (but not always) numeric values that can be aggregated, and dimensions are groups of hierarchies and descriptors that define the facts. For example, sales amount is a fact; timestamp, product, register#, store#, etc. are elements of dimensions. Dimensional models are built by business process area, e.g. store sales, inventory, claims, etc. Because the different business process areas share some but not all dimensions, efficiency in design, operation, and consistency, is achieved using conformed dimensions, i.e. using one copy of the shared dimension across subject areas.
:::

Some points you need answered/explored are

- Naming conventions: Each company has its standard naming convention. If you don’t, make sure to establish this standard. (e.g. naming standard).
- Slowly changing dimensions: Most business entity tables (aka dimensions) have attributes that change over time. Consider creating an SCD2 table to capture historical changes.
- In-correct aggregates: Running aggregates on any numeric values of the fact table(s) should not produce duplicate/inaccurate results. This is usually a result of having the data representing different columns in one column.
- Pre-aggregating data: At times, the expected query pattern requires data to be rolled up to a higher granularity. In these cases, if your read time is longer than the requirement, you may want to pre-aggregate your data on a set schedule. Pre-aggregating the data will allow “read queries” to be much faster but introduces the additional overhead of creating, scheduling, and maintaining a data pipeline.
- Flat tables: Although the Kimball Model is very popular, it can get tedious for the end-user to query and join multiple tables. A way for the data team to provide a clean interface for the end-user is to create a wide flat table (or view). A flat table is a table with all the facts and dimensional columns. The end-user does not need to worry about joining multiple tables and can concentrate on analyzing the data.

:::note
In a flat table, if some dimensional attributes change over time, then running a group-by query on those may produce inaccurate results. You can circumvent this by having 2 tables/views one with point-in-time dimensional attributes and the other with the most recent dimensional attribute.
:::

#### Data storage

Storing data in the right format can significantly impact your query performance. When modeling your end-user tables, make sure to consider the impact of data storage on read-type queries.

It’s crucial to understand the following concepts.

- Partitioning: Partitioning/Clustering, can significantly reduce the amount of data scanned and hence reduce the cost.
- Storage formats: Such as Parquet, or ORC formats can significantly reduce data size and speed up transformations.
- Sorting: Sorting can also reduce the amount of data to be read and make transformations efficient.
- Cloud storage: External tables allow for data to be stored in a cloud storage system and read when necessary.

Every data warehouse has different naming/implementation/caveats concerning the above, e.g. Snowflake automatically does most of these are for you, while Redshift requires a more hands on approach.

:::tip Normalization vs Denormalization
**Normalization:** Trying to increase data integrity by reducing the number of copies of the data. Data that needs to be added or updated will be done in as few places as possible.

**Denormalization:** Trying to increase performance by reducing the number of joins between tables (as joins can be slow). Data integrity will take a bit of a potential hit, as there will be more copies of the data (to reduce JOINS).
:::

### [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem)

- Consistency: every read receives the most recent write or an error.
- Availability: every request receives a response that is not an error.
- Partition tolerance: the system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes
- CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability
- CAP is frequently misunderstood as if one has to choose to abandon one of the three guarantees at all times. In fact, the choice is really between consistency and availability only when a network partition or failure happens; at all other times, no trade-off has to be made.
- [ACID](https://en.wikipedia.org/wiki/ACID) databases choose consistency over availability.
- [BASE](https://en.wikipedia.org/wiki/Eventual_consistency) systems choose availability over consistency.

### Check your understanding

1. What is Data Normalization?
1. What is Data Denormalization?
2. What are the Pros and Cons of Data Normalization?
2. What are the Pros and Cons of Data Denormalization?
3. What is the difference among 1NF, 2NF and 3NF?
4. What are the different categories of NoSQL Databases?
5. What are the ACID properties and where these are applied?
6. What are the BASE properties and where these are applied?
7. What are the differences between SQL and NoSQL data modeling?
8. What is OLTP?
9. What is OLAP?
10. What are the differences between OLTP and OLAP?
11. What are the Pros and Cons of OLTP?
12. What are the Pros and Cons of OLAP?
13. What is CAP theorem?
14. What is Data Modeling and Why you should care?
15. What are the advantages of Data Modeling?
16. What is Conceptual Data Model?
17. What is Logical Data Model?
18. What is Physical Data Model?
19. What is Entity-Relation (ER) Model?
20. What is Star Schema?
21. What are the differences between Star Schema and Snowflake Schema?
22. Explain the Relational Data Modeling with an example
23. Explain the Non-Relational Data Modeling with an example
24. Explain the Kimball's Four Step Process to Dimensional Data Modeling
25. What is Inmon Data Modeling Approach?
26. What are the differences between Kimball and Inmon Data Modeling Approach?
27. What is the difference between Fact and Dimension Tables?
28. What are Slowly Changing Dimensions (SCDs)?
29. Explain Different Types of Slowly Changing Dimensions (SCDs)
30. What is Data Warehouse?
31. Why is Data Warehouse needed?
32. What are the differences between Databases and Data Warehouses?
33. What are the differences between Operational and Analytical Systems?
34. What is Data Mart?
35. Explain how the Cargo Shipping Company Created its Data Model?

## Resources

1. https://bit.ly/3Sco9SY
2. https://knowledgetree.notion.site/Data-Modeling-92b0646bc2674a23a6203d9309bf414f
3. [Database Schema Design Examples](https://blog.panoply.io/database-schema-design-examples)
4.  [Data Modeling Layer & Concepts](https://www.holistics.io/books/setup-analytics/data-modeling-layer-and-concepts/)
5.  [Kimball’s Dimensional Data Modeling](https://www.holistics.io/books/setup-analytics/kimball-s-dimensional-data-modeling/)
6.  [Modeling Example: A Real-world Use Case](https://www.holistics.io/books/setup-analytics/modeling-example-a-real-world-use-case/)
7.  [Kimball Dimensional Modeling Techniques](https://bit.ly/3DPllXo)
8.  [Designing a dimensional model for a cargo shipper](https://www.techshashank.com/data-warehousing/shipping-dimensional-modeling)
9.  [5 Database Design Schema Example: Critical Practices & Designs](https://hevodata.com/learn/schema-example/)
10. [Kimball’s 4-Step Dimensional Design Process](https://bit.ly/3LTUtHY)
12. [Introduction to Data Warehouse](https://knowledgetree.notion.site/Brief-Introduction-to-Data-Warehouses-Shared-83ead0962c7a4c1cb7f165995f58e122)
13. [Data Warehouse Schemas](https://knowledgetree.notion.site/Data-Warehousing-Schemas-Shared-a03264b8ab6d4a50b6be0d73a82f8c8c)
14. [Know Data Warehouse Essential Concepts](https://www.1keydata.com/datawarehousing/datawarehouse.html)
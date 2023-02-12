# Data Modeling

The data model helps us design our database. When building a plane, you don’t start with building the engine. You start by creating a blueprint anschematic. Creating database is just the same, you start with modelling the data. Model is a representation of real data that provide us with characteristic, relation and rules that apply to our data. It doesn’t actually contain any data in it.

In the classical sense, a data model is simply metadata that described the structure, content, and relationships that exist within a group of related data assets. Maintaining a data model has long been a standard practice for OLTP workloads built on SQL. Typically maintained by data engineers & data architects, they help manage the evolution of assets, remove unnecessary duplication & enforce conventions to maintain an intuitive and consistent layout. A key additional benefit is to inform consumers (ex. data analysts) about assets and how best to use them. For this reason, maintaining data models is also a common practice for managing the evolution of large SQL data warehouses. Without data models, end users would find it challenging to navigate around a library of hundreds (if not thousands) of data assets and correctly leverage them.

**Data modeling** is a process of designing how data will be represented in data stores. Many data modeling techniques were originally designed for databases and warehouses. Since the Serving layers are usually built with relational data stores such as data warehouses, some of the data modeling techniques can be applied for the Serving layer design too. Serving layer could be built using other storage technologies such as document databases, key-value stores, and so on, based on the customer requirements.

Unlike data lakes, in databases or data warehouses we don't have the luxury of storing huge volumes of data in the format we like. Databases and data warehouses can perform querying exceptionally fast, provided the data is stored in predetermined formats and is limited in size. Hence, while designing the Serving layer, we need to identify the specifics of which data needs to be stored, which format to store it in, and how much data to store. To be specific, we need to decide on which SQL tables are required, what would be the relationship between these tables, and which restrictions need to be imposed on these tables.

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

Schemas are guidelines for arranging data entities such as SQL tables in a data store. Designing a schema refers to the process of designing the various tables and the relationships among them. Star and Snowflake schemas are two of the most commonly used schemas in the data analytics and BI world. In fact, Star schemas are used more frequently than Snowflake schemas. Both have their own advantages and disadvantages.

**Star Schema**

Star Schema (introduced by Ralph Kimball) is the most widely used approach to organize data in database to make it easy to understand, read (fast data retrieval) and analyze. It is the underlying structure of dimensional model and also one of the methods used in dimensional modeling.

In practice, Star Schema is used to denormalize business data. It separates business process data into:

1. Fact tables that hold quantitative information about the business, such as quantity, unit price, sales amount, etc.
2. Dimension tables that hold descriptive information of the fact table, such as store, product, customer, etc.

With this design, the end-users are able to easily find the data they need, slice and dice the data however they see fit and evolve the schema if the business changes.

It is called a star schema because the fact table sits at the center of the logical diagram, and the small dimensional tables branch off to form the points of the star.

![](https://user-images.githubusercontent.com/62965911/214235541-66b537aa-4903-40ae-9587-57768efa1bd8.png)

A star schema is a multi-dimensional data model used to organize data so that it is easy to understand and analyze, and very easy and intuitive to run reports on. Kimball-style star schemas or dimensional models are pretty much the gold standard for the presentation layer in data warehouses and data marts, and even semantic and reporting layers. The star schema design is optimized for querying large data sets. Star schema has two sets of tables: one that stores quantitative information such as transactions happening at a retail outlet or trips happening at a cab company, and another that stores the context or descriptions of events that are stored in the quantitative table. The quantitative tables are called fact tables and the descriptive or context tables are called dimension tables.

![star-schema-datamodel](https://user-images.githubusercontent.com/62965911/216760155-70c45f6e-7599-47a3-a337-183262bdff6d.png)

Dimensional modeling focuses on easier and faster information retrieval, whereas other models usually focus on storage optimization. Since the relationship diagram of the Star schema is in the shape of a star, it is called a Star schema. The fact table at the middle is the center of the star, and the dimension tables are the arms of the star.

Let's look at some important points about Star schemas, as follows:

- Fact tables are usually of much higher volume than dimension tables.
- Dimension tables are not connected; they are independent of each other.
- Data is not normalized in a Star schema. It is very common to find data replicated in multiple tables. The tables are designed for speed and ease of use.
- They are optimized for **BI** queries. The queries are usually very simple as it just has one level of joins.
- Queries are usually much faster too due to the lesser number of joins.

In fact tables, you will have the foreign keys to dimension tables as well as aggregate or numeric information. We do not want descriptions or attributes in fact tables since those are reserved for dimension tables. We will use the foreign keys in a fact table to "*join"* the information in dimension tables.

Dimension tables are generally [denormalized](https://en.wikipedia.org/wiki/Denormalization) (may hold redundant data) and do not contain any foreign keys nor do they have any *"sub-dimension tables"*. Dimension table contains primary key and descriptive information of the fact table.

So how do we build a Star Schema? [As proposed by Kimball](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/four-4-step-design-process/#:~:text=Select%20the%20business%20process.,Identify%20the%20facts.), there are 4 steps in designing of a dimensional model.

1. Select the business process. The first step is to identify the business process that you want to model. Model the processes that are most significant or relevant to the business first.
2. Declare the grain. Grain refers to the level of detail of the information that you will store in the fact table. The grain should be at the most atomic or lowest level possible. For example, A line item on a grocery receipt. The grocery owner might want to ask questions such as *"what are the items that sold the best during the day in our grocery store?"*, and to answer this question we need to dig into line-item level instead of the order-level.
3. Identify the dimensions. You can identify the dimensions by looking at the descriptive information or attributes that exist in your business process and provide context to your measurable events. For example: payment method, customers, locations, etc.
4. Identify the facts. Facts are the quantitative measures in your business process that are always in numeric. For example: price, minutes, speed, etc. You should identify/select the measures that are true to your selected grain.

**Snowflake Schema**

A snowflake schema is an extension of the Star schema. In this model, the fact table remains the same, but the dimension tables are further split into their normalized forms, which are referenced using foreign keys. There could be multiple levels of hierarchy among the dimension tables.

![CH05_F05_Riscutia2](https://user-images.githubusercontent.com/62965911/218325714-f1e5bd1b-6153-4b6f-95dc-097837916a4f.png)

The following diagram shows how the same example used for a Star schema can be extended to a Snowflake schema:

![B17525_04_001](https://user-images.githubusercontent.com/62965911/218277646-2a914b1e-2a71-4bb9-8d67-a8a70ddb41c9.jpeg)
![Figure_4 2_-_Example_of_Snowflake_Schema](https://user-images.githubusercontent.com/62965911/218277647-ead2f682-4e1c-4462-87d2-a5457373ba94.jpg)

As you will notice from the preceding diagram, the DimDriver table has been normalized to have the license details separately. Similarly, we have normalized the address details away from the DimCustomer table.

You can choose a Snowflake schema if you have both BI and non-BI applications sharing the same data warehouse. In such cases, from an overall perspective, it might be better to have normalized data.

Let's look at some important points about Snowflake schemas, as follows:

- Fact tables, here again, are similar to Star schemas and are of much higher volume than dimension tables.
- Dimension data is normalized, thereby avoiding any redundant data.
- Dimensions could be connected to each other.
- The data is optimized for storage and integrity, but not speed.
- The schema is more complex than a Star schema, so this might not be the most preferred option for BI and reporting use cases.
- Queries are usually slower compared to Star schemas due to the multi-level joins required.

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

### Designing SCDs

SCDs refer to data in dimension tables that changes slowly over time and not at a regular cadence. A common example for SCDs is customer profiles—for example, an email address or the phone number of a customer doesn't change that often, and these are perfect candidates for SCD.

Here are some of the main aspects we will need to consider while designing an SCD:

- Should we keep track of the changes? If yes, how much of the history should we maintain?
- Or, should we just overwrite the changes and ignore the history?

Based on our requirements for maintaining the history, there are about seven ways in which we can accomplish keeping track of changes. They are named SCD1, SCD2, SCD3, and so on, up to SCD7.

Among these, SCD1, SCD2, SCD3, SCD4, and SCD6 are the most important ones.

#### Designing SCD1

In SCD type 1, the values are overwritten and no history is maintained, so once the data is updated, there is no way []()to find out what the previous value was. The new queries will always return the most recent value. Here is an example of an SCD1 table:

| Customer ID | Name | City     | Email | ... |
| ----------- | ---- | -------- | ----- | --- |
| 1           | Adam | New York | Adam  | ... |

| Customer ID | Name | City       | Email | ... |
| ----------- | ---- | ---------- | ----- | --- |
| 1           | Adam | New Jersey | Adam  | ... |

In this example, the value of the City column is changing from New York to New Jersey. The value just gets overwritten.

#### Designing SCD2

In SCD2, we maintain a complete history of changes. Every time there is a change, we add a new row with all the details without deleting the previous values. There are multiple ways in which we can accomplish this. Let's take a look at the most common approaches.

**Using a flag**

In this approach, we use a flag to indicate if a particular value is active or if it is current. Here is an example of this:

| SurrogateID | CustomerID | Name | City     | isActive | ... |
| ----------- | ---------- | ---- | -------- | -------- | --- |
| 1           | 1          | Adam | New York | True     | ... |

| SurrogateID | CustomerID | Name | City       | isActive | ... |
| ----------- | ---------- | ---- | ---------- | -------- | --- |
| 1           | 1          | Adam | New York   | False    | ... |
| 2           | 1          | Adam | New Jersey | False    | ... |
| 3           | 1          | Adam | Miami      | True     | ... |

In the second table, every time there is a change, we add a new row and update the isActive column of the previous rows to False. That way, we can easily query the active values by filtering on the isActive=True criteria.

NOTE

> Surrogate keys are secondary row identification keys. They are added in all SCD2 cases because the primary identification key will not be unique anymore with newly added rows.

**Using version numbers**

In this approach, we use version numbers to keep track of changes. The row with the highest version is the most current value. Here is an example of this:

| SurrogateID | CustomerID | Name | City     | Version | ... |
| ----------- | ---------- | ---- | -------- | ------- | --- |
| 1           | 1          | Adam | New York | 0       | ... |

| SurrogateID | CustomerID | Name | City       | Version | ... |
| ----------- | ---------- | ---- | ---------- | ------- | --- |
| 1           | 1          | Adam | New York   | 0       | ... |
| 2           | 1          | Adam | New Jersey | 1       | ... |
| 3           | 1          | Adam | Miami      | 2       | ... |

In the previous example, we need to filter on the MAX(Version) column to get the current values.

**Using date ranges**

In this approach, we use date ranges to show the period a particular record (row) was active, as illustrated in the following example:

| SurrogateID | CustomerID | Name | City     | StartDate   | EndDate | ... |
| ----------- | ---------- | ---- | -------- | ----------- | ------- | --- |
| 1           | 1          | Adam | New York | 01-Jan-2020 | NULL    | ... |

| SurrogateID | CustomerID | Name | City       | StartDate   | EndDate     | ... |
| ----------- | ---------- | ---- | ---------- | ----------- | ----------- | --- |
| 1           | 1          | Adam | New York   | 01-Jan-2020 | 25-Mar-2020 | ... |
| 2           | 1          | Adam | New Jersey | 25-Mar-2020 | 01-Dec-2020 | ... |
| 3           | 1          | Adam | Miami      | 01-Dec-2020 | NULL        | ... |

In the previous example, every time we change a field, we add a new record to the table. Along with that, we update the EndDate column of the previous record and the StartDate column for the new record with today's date. In order to fetch the current record, we have to filter on the EndDate=NULL criteria, or, instead, we could just fill in a very futuristic date instead of NULL—something such as 31-Dec-2100.

As a variation to the date-range approach, we could also add a flag column to easily identify active or current records. The following example shows this approach:

| SurrogateID | CustomerID | Name | City       | StartDate   | EndDate     | isActive | ... |
| ----------- | ---------- | ---- | ---------- | ----------- | ----------- | -------- | --- |
| 1           | 1          | Adam | New York   | 01-Jan-2020 | 25-Mar-2020 | False    | ... |
| 2           | 1          | Adam | New Jersey | 25-Mar-2020 | 01-Dec-2020 | False    | ... |
| 3           | 1          | Adam | Miami      | 01-Dec-2020 | NULL        | True     | ... |

#### Designing SCD3

In SCD3, we maintain only a partial history and not a complete history. Instead of adding additional rows, we add an extra column that stores the previous value, so only one version of historic data will be preserved. As with the SCD2 option, here again, we can choose to add date columns to keep track of modified dates, but we don't need surrogate keys in this case as the identification key of the record doesn't change. Here is an example of this:

| CustomerID | Name | City     | PrevCity | ... |
| ---------- | ---- | -------- | -------- | --- |
| 1          | Adam | New York | NULL     | ... |

| CustomerID | Name | City       | PrevCity | ... |
| ---------- | ---- | ---------- | -------- | --- |
| 1          | Adam | New Jersey | New York | ... |

In the previous example, we have added a new column called PrevCity. Every time the value of City changes, we add the previous value to PrevCity and update the City column with the current city.

#### Designing SCD4

SCD4 was introduced for dimension attributes that change relatively frequently. In type 4, we split the fast-changing attributes of the dimension table into another smaller dimension table and also reference the new dimension table directly from the fact table.

For example, in the following diagram, if we assume that the carpool (also known as High occupancy vehicles) pass needs to be purchased every month, we can move that field to a smaller mini-dimension and reference it directly from the fact table:

![B17525_04_009](https://user-images.githubusercontent.com/62965911/218293241-5d41063b-5dc9-45ac-bcf7-77c9fc41532b.jpeg)

We can split the table into a mini DimCarPool dimension, as in the following diagram:

![B17525_04_010](https://user-images.githubusercontent.com/62965911/218293244-d9892da4-f4cf-4010-8188-f040f0d5d784.jpeg)

This sub-division helps in modifying only a smaller amount of data frequently instead of the complete row.

#### Designing SCD5, SCD6, and SCD7

The rest of the SCDs—SCD5, SCD6, and SCD7—are derivatives of the previous four SCDs. Among these derived ones, SCD6 is a relatively important one, so we will be exploring that as part of the next sub-section.

**Designing SCD6**

Type 6 is a combination of 1, 2, and 3. In this type, along with the addition of new rows, we also update the latest value in all the rows, as illustrated below:

| SurrogateID | CustomerID | Name | CurrCity | PrevCity   | StartDate   | EndDate     | isActive | ... |
| ----------- | ---------- | ---- | -------- | ---------- | ----------- | ----------- | -------- | --- |
| 1           | 1          | Adam | Miami    | NULL       | 01-Jan-2020 | 25-Mar-2020 | False    | ... |
| 2           | 1          | Adam | Miami    | New York   | 25-Mar-2020 | 01-Dec-2020 | False    | ... |
| 3           | 1          | Adam | Miami    | New Jersey | 01-Dec-2020 | NULL        | True     | ... |

In the previous example, you would have noticed that the CurrCity value for all the records belonging to customer Adam has been updated. This is just another benefit of extracting the latest values.

That explains SCD type 6. If you are interested in learning about SCDs 5 and 7, you can find more information at the following links:

SCD5: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-5/

SCD7: https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/type-7

### Designing for incremental loading

Incremental loading or delta loading refers to the process of loading smaller increments of data into a storage solution—for example, we could have daily data that is being loaded into a data lake or hourly data flowing into an extract, transform, load (ETL) pipeline, and so on. During data-ingestion scenarios, it is very common to do a bulk upload followed by scheduled incremental loads.

There are different ways in which we can design incremental loading. Based on the type of data source, we can have different techniques to implement incremental loading. Some of them are listed here:

#### Watermarks

Watermarking is a very simple technique whereby we just keep track of the last record loaded (our watermark) and load all the new records beyond the watermark in the next incremental run.

In relational storage technologies such as SQL databases, we can store the watermark details as just another simple table and automatically update the watermark with stored procedures. Every time a new record is loaded, the stored procedure should get triggered, which will update our watermark table. The next incremental copy pipeline can use this watermark information to identify the new set of records that need to be copied.

### Normalization vs Denormalization

Normalization is Trying to increase data integrity by reducing the number of copies of the data. Data that needs to be added or updated will be done in as few places as possible. Denormalization is Trying to increase performance by reducing the number of joins between tables (as joins can be slow). Data integrity will take a bit of a potential hit, as there will be more copies of the data (to reduce JOINS).

### [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem)

- Consistency: every read receives the most recent write or an error.
- Availability: every request receives a response that is not an error.
- Partition tolerance: the system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes
- CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability
- CAP is frequently misunderstood as if one has to choose to abandon one of the three guarantees at all times. In fact, the choice is really between consistency and availability only when a network partition or failure happens; at all other times, no trade-off has to be made.
- [ACID](https://en.wikipedia.org/wiki/ACID) databases choose consistency over availability.
- [BASE](https://en.wikipedia.org/wiki/Eventual_consistency) systems choose availability over consistency.

### Best Practices

**Database design** is a critical aspect of any software system. It determines the overall performance, scalability, and security of a system. Here are 9 best practices for designing a database that ensures the longevity and success of your system:

1. **Normalization:** Normalization is the process of organizing data in a relational database so that data redundancies are minimized and data anomalies are prevented. Normalization helps ensure data consistency and eliminates data duplications.
2. **Proper indexing:** Indexing is the process of adding an index to a database column to speed up the search process. Proper indexing helps improve the performance of queries and makes data retrieval faster.
3. **Use appropriate data types:** It is important to use appropriate data types for each column in your database. This helps ensure data accuracy and consistency.
4. **Avoid over-normalization:** While normalization is important, over-normalization can lead to complicated and slow-performing queries. It is important to strike a balance between normalization and efficiency.
5. **Use appropriate keys:** Keys are used to identifying a unique record in a database. It is important to choose the appropriate key for each table, such as primary keys, foreign keys, or composite keys.
6. **Document your design:** Documenting your database design helps ensure that it is clear, consistent, and easy to understand. This documentation also makes it easier to maintain and modify the database in the future.
7. **Test your design:** It is important to test your database design thoroughly before deploying it to production. This helps catch any potential problems and ensures that the design meets all requirements.
8. **Consider security:** Security is a critical aspect of database design. It is important to consider security from the beginning of the design process to ensure that the database is protected from unauthorized access.
9. **Plan for scalability:** As your system grows, so will your database. It is important to plan for scalability from the beginning so that the database can easily handle increasing amounts of data.

Following these 9 best practices for database design will help ensure that your system has a strong foundation for success. Proper planning, documentation, testing, and security considerations will help ensure that your database is efficient, secure, and scalable.

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

## Case Studies

### Relational/3NF Data Models

1. [Spotify](https://medium.com/towards-data-engineering/design-the-database-for-a-system-like-spotify-95ffd1fb5927)
2. [LinkedIn](https://medium.com/towards-data-engineering/database-design-for-a-system-like-linkedin-3c52a5ab28c0)
3. [Zomato/Swiggy](https://medium.com/towards-data-engineering/database-design-for-a-food-delivery-app-like-zomato-swiggy-86c16319b5c5)

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

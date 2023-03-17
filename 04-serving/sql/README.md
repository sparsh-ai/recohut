# Relational (SQL) Data Modeling

What is data modeling? **Data modeling** is a process for representing the database objects in our real-world or business perspective. Objects in warehouses can be datasets, tables, or views. Representing the objects as close as possible to the real world is important because the end users of the data are human. Some of the most common end users are business analysts, data analysts, data scientists, BI users, or any other roles that require access to the data for business purposes.

The data model helps us design our database. When building a plane, you don’t start with building the engine. You start by creating a blueprint anschematic. Creating database is just the same, you start with modelling the data. Model is a representation of real data that provide us with characteristic, relation and rules that apply to our data. It doesn’t actually contain any data in it.

In the classical sense, a data model is simply metadata that described the structure, content, and relationships that exist within a group of related data assets. Maintaining a data model has long been a standard practice for OLTP workloads built on SQL. Typically maintained by data engineers & data architects, they help manage the evolution of assets, remove unnecessary duplication & enforce conventions to maintain an intuitive and consistent layout. A key additional benefit is to inform consumers (ex. data analysts) about assets and how best to use them. For this reason, maintaining data models is also a common practice for managing the evolution of large SQL data warehouses. Without data models, end users would find it challenging to navigate around a library of hundreds (if not thousands) of data assets and correctly leverage them.

**Data modeling** is a process of designing how data will be represented in data stores. Many data modeling techniques were originally designed for databases and warehouses. Since the Serving layers are usually built with relational data stores such as data warehouses, some of the data modeling techniques can be applied for the Serving layer design too. Serving layer could be built using other storage technologies such as document databases, key-value stores, and so on, based on the customer requirements.

Unlike data lakes, in databases or data warehouses we don't have the luxury of storing huge volumes of data in the format we like. Databases and data warehouses can perform querying exceptionally fast, provided the data is stored in predetermined formats and is limited in size. Hence, while designing the Serving layer, we need to identify the specifics of which data needs to be stored, which format to store it in, and how much data to store. To be specific, we need to decide on which SQL tables are required, what would be the relationship between these tables, and which restrictions need to be imposed on these tables.

What's the main difference between designing a data model in a data warehouse and designing an **OLTP** database (transactional database) for applications. In the application database, the end users of the database are applications, not humans. In the data warehouse, you serve humans. So, as data engineers, we need to think from their perspective.

Since modern data engineers realize the non-relevancy of the old principles and, at the same time, the demand to insert any data in data warehouses is growing tremendously, they tend to skip the data modeling steps, and that's bad. Skipping the data warehouse principles means ignoring the fact that we need to maintain data consistency. This fact may lead to some bad results. Take the following common example:

- Data is duplicated in many locations.
- Some values are not consistent across different users and reports.
- The cost of processing is highly inefficient.
- The end user doesn't understand how to use the data warehouse objects.
- The business doesn't trust the data.

In my opinion, a modern data warehouse is still a data warehouse. The objective of a data warehouse is to build a centralized and trustworthy data storage that can be used for business. Data engineers need to take more time to do proper data modeling in data warehouses compared to the data lake concept in order to meet this objective.

Let's look at this example. We want to represent people in a table object. Which of the following two tables, A or B, do you think better represents people? Here is People table A:

![B16851_03_35](https://user-images.githubusercontent.com/62965911/219542322-e4437269-6cba-4f29-aa32-5cd23d1d8c71.jpg)
Try and compare this with People table B:

![B16851_03_36](https://user-images.githubusercontent.com/62965911/219542327-4e45a493-a827-4e30-944d-66a623c7ea41.jpg)

If we look back at the objective, we want to represent people. Then I think we can all agree that *People table A* is better at representing people because this table represents people clearly. It's very natural to imagine people having names, ages, hair colors, and genders. A good data model is self-explanatory, like *People table A*. This means that even without anyone explaining to you how to read the table, you already know what the table is about.

Now, why is *table B* bad? There are a few reasons:

- The lists of attributes don't really represent people; for example, **postal code**. Even though we know people may have houses, and houses have postal codes, it's difficult to imagine people as entities having a postal code as part of them. 
- What is **NULL** in relation to **postal code**? Does that mean Barb doesn't have a house? Or maybe he forgot his postal code? Or perhaps this is just a bug. The table can't really tell you that.
- Still on the subject of the postal code, how about if one of the people here has more than one house? Should we add new records to this table? It will become complicated.
- Gender is inconsistent. **Female** and **Woman**, and **Male** and **Man**, may have the same meanings, but may not.
- The wealthy column has **yes** and **no** values. What does this mean? How can this column be justified?

It is not that the information is wrong - we often need to store such information. Now the question is, can we store the same information, but with a better data model? 

Let's take another example. Perhaps this better represents the real world for the required information:

![B16851_03_37](https://user-images.githubusercontent.com/62965911/219542328-65d0e5a7-f59a-4afe-b18a-6929a0f01d0e.jpg)

Maybe this *Alternative C* is better. We still have the people table, but only with people-related attributes, for example, **gender**. Then, **postal code** is part of the **Address** table. It may have other address information, but in this example, we will keep it simple with just the postal code. And if someone such as **Barb** doesn't have a postal code, then we don't need to put the **NULL** record there. And lastly, we may assume that wealth is driven by salary (just for example purposes), so we had better just store the salary information, and later use queries to put the **wealthy** logic on top of the salary information. This is more natural and closer to the real world.

What could happen with a bad data model? It is often the case that the end user will have too much dependency on the data engineering team. Unable to understand the table shapes, end users need to keep posing the following questions to the data engineering team, for example:

1. What does **NULL** mean?
2. How should I join the tables?
3. Why are there duplications?
4. Why do some records have the attribute X while others don't?

In the worst-case scenario, the end user doesn't trust the data in the data warehouse, so the goal of using the data for a business impact has failed. 

In the best-case scenario, a perfect data model is where the end user doesn't need to put any questions to the data engineering team. They can answer any business questions just by looking at the table structures and trust the data 100%. And that's our goal as data engineers.

But, at the end of the day, it's very difficult to design a perfect data model because there are other aspects that a data engineer needs to think about when designing a data model.

**Other purposes of the data model**

Besides representing data in a real-world scenario, there are three other reasons why we require a data model in a data warehouse:

- **Data consistency**
- **Query performance**
- **Storage efficiency**

Let's start with the latest point first: *Storage efficiency*. How can we improve storage efficiency by the data model? 

Take a look at this example again. Which one is more storage-efficient? Perhaps a table with **name** and **gender**, where **gender** is written in a string data type as **Man or Woman**:

![B16851_03_38](https://user-images.githubusercontent.com/62965911/219542329-0af81eb2-394a-4241-af5f-12533db98706.jpg)

Or perhaps *option B*? We create a gender reference table, and the main table will only store one character, **gender_id**, as a reference. The user can later join both tables for the same result as *option A*.

![B16851_03_39](https://user-images.githubusercontent.com/62965911/219542332-906ff971-1b6d-47c6-b72b-19f9775bd577.jpg)

*Option B* is definitely better, as we don't need to repeat storing **Female** and **Male** strings in our storage. It looks like a small difference, but the same technique applies to all categorical string attributes, and that can have a significant impact.

Using the same technique, we can also improve data consistency. For example, we can use the gender reference table for other tables, as in the following example user table:

![B16851_03_40](https://user-images.githubusercontent.com/62965911/219542334-b975bb7d-415e-43d4-ad03-97cbd62f3784.jpg)

With that, we avoid data inconsistency; for example, the People table uses Female-Male, and the User table uses Man-Woman. This is a very common practice, and the common terminology in the data warehouse world to refer to this is normalized and denormalized. 

*Storage efficiency option A* is a denormalized table, while *Storage efficiency option B* is a normalized table.

Last but not least, one reason why we need a data model is for query performance. In a big data system where data is stored in distributed storage, there is a general rule of thumb regarding which operation is the most resource-intensive, which is **JOIN**. **JOIN** in general is a very expensive operation, especially when we need to join multiple large-volume tables. And if you look back at the normalized and denormalized approaches, you will realize that even normalized data is good for storage efficiency and data consistency, but it's bad for performance because you require a lot of **Join** operations. 

At the end of the day, we need to find a balance between all the factors. There will be no right or wrong answer for a data model in a complex data warehouse. In a complex data warehouse, this may involve thousands to millions of tables. So, everyone will have a different approach for designing the data model. However, there are some theories that we can use as reference.

#### Inmon versus the Kimball data model

If you look at the internet, there will be many references to data modeling, but two of the most famous approaches are the **Inmon** method (data-driven) and the **Kimball** method (user-driven).

We will take a quick look at these methods, but we won't spend much time or go into too much detail in this note since there are so many details to explain regarding the framework. I suggest you do some more in-depth research from other resources regarding these two methods to better understand the step-by-step approaches and the frameworks. What we want to learn from them are the differences and the thinking processes behind them.

At a very high level, the Inmon method focuses on building a central data warehouse or single source of truth. To achieve that, the data model must be highly normalized to the lowest level, so the data can be highly consistent. The Inmon data model follows a top-down approach, which means the data warehouse is built as the central data source for all the downstream data marts, sometimes referred to as the **Enterprise Data Warehouse**. The downstream data marts need to follow the rules from the data warehouse, as in this figure. Imagine the gray boxes are tables. 

![B16851_03_41](https://user-images.githubusercontent.com/62965911/219542336-5dc33337-2996-4feb-abc7-89b178c9ec9d.jpg)

Compared to the Inmon method, the Kimball method focuses on answering user questions and follows a bottom-up approach. This method keeps end user questions in mind and uses the questions as a basis to build necessary tables. The goal is to ease end user accessibility and provide a high level of performance improvement.

The tables may contain the entity's basic information and its measurements. This is what are now known as fact and dimension tables. A **fact table** is a collection of measurements or metrics in a predefined granularity. A **dimension table** is a collection of entity attributes that support the fact tables. This collection of fact and dimension tables will later be the data warehouse. 

Here is an example of a fact table. The fact table has two measurements that measure customers in daily granularity:

![B16851_03_42](https://user-images.githubusercontent.com/62965911/219542340-a84d6156-e7ed-49d8-b97a-85644f3de1f9.jpg)

Here is an example of a dimension table with **Customer ID** as the primary key and the attributes:

![B16851_03_43](https://user-images.githubusercontent.com/62965911/219542343-d63c8ffc-d3b7-4409-99c1-788025412491.jpg)

As you can see from the examples, the facts and dimension tables are different. So how do they relate together as a data model?

One of the most well-known data models for the Kimball method is the star schema. The star schema follows the fact and dimension table relations. There is a rule of thumb regarding the star schema that a dimension table can't have parent tables, which means the dimension is a denormalized table. Check the following diagram, which provides a high-level illustration of a data warehouse using the Kimball approach. Imagine that all the gray boxes are tables:

![B16851_03_44](https://user-images.githubusercontent.com/62965911/219542344-c9fcd477-c631-451c-b0f9-ed8b17b731dc.jpg)

The pros and cons of both methods are summarized as follows:

![B16851_03_45](https://user-images.githubusercontent.com/62965911/219542350-d8a15c63-644d-4dac-8032-3c321258265b.jpg)

Use the table comparison as your reference when deciding between the Inmon or Kimball methods. This is usually not a straightforward and quick decision to make. It's a difficult decision because choosing one of them means your entire organization needs to commit to the data model for the long term. An experienced data modeler is usually the best person to decide this.

### Stages of Data Modeling

#### Conceptual Data Model

Define **WHAT** the system contains. Used by business stakeholders. The purpose is to organize, scope and define business concepts and rules.

- Entity Relationship Diagram
- Data Dictionaries

#### Logical Data Model

Defines **HOW** the system should be implemented regardless of the DBMS. Used by data architects and business analysts. The purpose is to develop technical map of rules and data structures.

- Notmalization and De-Normalization
- Object-oriented Data Modeling

#### Physical Data Model

Describes **HOW** the system will be implemented using a specific DBMS system. Used by DBA and developers. The purpose is actual implementation of the database.

- Implementation of a data model in a database management system
- Indexing
- Partitioning

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

Whereas operational source systems contain only the latest version of [master data](https://en.wikipedia.org/wiki/Master_data), the star schema enables time travel queries to reproduce dimension attribute values on past dates when the fact transaction or event actually happened. The star schema data model allows analytical users to query historical data tying metrics to corresponding dimensional attribute values over time. Time travel is possible because dimension tables contain the exact version of the associated attributes at different time ranges. Relative to the metrics data that keeps changing on a daily or even hourly basis, the dimension attributes change less frequently. Therefore, dimensions in a star schema that keeps track of changes over time are referred to as [slowly changing dimensions](https://en.wikipedia.org/wiki/Slowly_changing_dimension) (SCDs).

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

There are mainly two types of data loading which includes Full load and Incremental load.

Full load: The entire dataset is replaced or overwritten with the new dataset. Performing full load is easy in terms of implementation and design. However, the full load process will consume a lot of time when size of data increases.

![](https://user-images.githubusercontent.com/62965911/213924400-566f123a-73b5-413d-9b21-269a74611dd3.png)

Incremental Load: Instead of overwriting the old data, incremental data load identifies the difference between the source data and target data and append the difference to the target data thus increasing the performance significantly especially when one is dealing with huge volume of data. The maintenance is a bit complex.

![](https://user-images.githubusercontent.com/62965911/213924401-5a4b5d49-c5df-46f2-88e8-a937790800dd.png)

There are different ways in which we can design incremental loading. Based on the type of data source, we can have different techniques to implement incremental loading. Some of them are listed here:

#### Watermarks

Watermarking is a very simple technique whereby we just keep track of the last record loaded (our watermark) and load all the new records beyond the watermark in the next incremental run.

In relational storage technologies such as SQL databases, we can store the watermark details as just another simple table and automatically update the watermark with stored procedures. Every time a new record is loaded, the stored procedure should get triggered, which will update our watermark table. The next incremental copy pipeline can use this watermark information to identify the new set of records that need to be copied.

## Data Warehousing

In today's data-driven world, businesses need to have the ability to store and analyze large amounts of data in order to make informed decisions. One way to achieve this is by designing and developing a data warehouse. A data warehouse is a centralized repository that allows organizations to store and manage data from various sources in a structured manner. In this note, we will discuss seven key steps involved in designing and developing a data warehouse.

Designing and developing a data warehouse involves several steps, including:

1. Identify business requirements
2. Create a conceptual model
3. Develop a logical model
4. Define the physical model
5. Extract, transform, and load (ETL) processes
6. Develop reporting and analysis tools
7. Implement data quality and data governance processes

*let's begin to explain each and every step in more detail*

### Identify business requirements

Identifying business requirements is a critical step in designing and developing a data warehouse. It involves understanding the business goals, data sources, data types, data volumes, and the frequency of data updates.

To identify business requirements, you need to work closely with business stakeholders, such as executives, analysts, and subject matter experts. You may conduct interviews, workshops, and surveys to gather information about the business requirements.

Some of the key areas to consider when identifying business requirements include:

1. Business goals: Understanding the business goals is essential to align the data warehouse design with the organization's strategic objectives. This involves understanding the key performance indicators (KPIs) and metrics that are important to the business.
2. Data sources: Identifying the data sources is essential to determine the types of data that will be loaded into the data warehouse. This may include transactional systems, operational databases, flat files, and external sources such as social media and web analytics.
3. Data types: Understanding the data types is critical to determine the appropriate data models and database structures for the data warehouse. This may include structured data such as customer information, sales data, and financial data, as well as unstructured data such as emails, documents, and images.
4. Data volumes: Understanding the data volumes is essential to determine the hardware and software requirements for the data warehouse. This includes estimating the amount of data that will be processed and stored, and the frequency of data updates.
5. Frequency of data updates: Understanding the frequency of data updates is essential to determine the appropriate data loading and refresh strategies for the data warehouse. This may include batch processing, real-time processing, or a combination of both.

By identifying business requirements, you can develop a data warehouse that meets the needs of the business and provides valuable insights for decision-making.

### Create a conceptual model

The conceptual model represents the high-level view of the data warehouse and provides a framework for organizing and understanding the data.

To create a conceptual model, you need to work closely with business stakeholders to understand the business entities, relationships, and attributes that are relevant to the data warehouse. The goal is to create a logical structure that is intuitive, easy to understand, and aligned with the business goals.

Here are some of the key steps involved in creating a conceptual model:

1. Identify business entities: The first step in creating a conceptual model is to identify the business entities that are relevant to the data warehouse. This may include customers, products, transactions, and other entities that are important to the business.
2. Define entity relationships: Once the business entities are identified, you need to define the relationships between the entities. This involves understanding how the entities are related to each other and how they are used in the business processes.
3. Determine attributes: For each entity, you need to determine the attributes that are relevant to the data warehouse. This may include data such as customer name, address, email, and purchase history.
4. Organize entities and relationships: After identifying the entities and relationships, you need to organize them into a conceptual model. This may involve using diagrams, flowcharts, or other visual tools to represent the entities, relationships, and attributes.
5. Validate the conceptual model: Once the conceptual model is created, it is important to validate it with business stakeholders to ensure that it accurately represents the business entities, relationships, and attributes.

By creating a conceptual model, you can establish a common understanding of the data warehouse structure and provide a foundation for the logical and physical design of the data warehouse.

### Develop a logical model

Developing a logical model is an important step in designing a data warehouse as it provides a more detailed representation of the data warehouse structure than the conceptual model. The logical model represents the structure of the data warehouse in terms of tables, columns, keys, and relationships.

Here are some key steps involved in developing a logical model:

1. Normalize the data: The first step in developing a logical model is to normalize the data. Normalization is the process of organizing the data into tables to reduce redundancy and improve data integrity. This involves breaking down the data into its smallest logical parts and organizing it into tables.
2. Identify entities and relationships: Once the data is normalized, you can identify the entities and relationships that are relevant to the data warehouse. This involves understanding the relationships between the tables and how they are used in the business processes.
3. Define primary and foreign keys: For each table, you need to define the primary key, which is a unique identifier for each record in the table. You also need to define foreign keys, which are used to establish relationships between tables.
4. Determine column attributes: For each table, you need to determine the attributes that are relevant to the data warehouse. This may include data such as customer name, address, email, and purchase history.
5. Validate the logical model: Once the logical model is developed, it is important to validate it with business stakeholders to ensure that it accurately represents the business entities, relationships, and attributes.

By developing a logical model, you can create a more detailed and structured representation of the data warehouse. This provides a foundation for the physical design of the data warehouse, which involves implementing the data warehouse on a specific database platform.

### Define the physical model

The physical model is the implementation of the logical model on a specific database platform. It involves defining the database schema, creating tables and columns, and establishing relationships between tables. The physical model is the final step in the data warehouse design process and represents the actual structure of the data warehouse that will be used to store and analyze data.

Here are some key steps involved in defining the physical model:

1. Choose a database platform: The first step in defining the physical model is to choose a database platform. The database platform should be compatible with the requirements of the data warehouse and provide the necessary performance, scalability, and security features.
2. Define the database schema: Once the database platform is chosen, you need to define the database schema. The database schema is the structure of the database that defines the tables, columns, keys, and relationships. It is based on the logical model but is optimized for the specific database platform.
3. Create tables and columns: After defining the database schema, you need to create the tables and columns in the database. This involves translating the logical model into SQL statements that can be executed on the database platform.
4. Establish relationships between tables: Once the tables and columns are created, you need to establish relationships between the tables. This involves defining primary and foreign keys and creating indexes to optimize query performance.
5. Load data into the data warehouse: Once the physical model is defined, you can load data into the data warehouse. This involves extracting data from the source systems, transforming the data to conform to the data warehouse schema, and loading the data into the data warehouse.

By defining the physical model, you can create a structure for the data warehouse that is optimized for the specific database platform. This provides a foundation for data analysis and reporting and enables users to extract insights from the data warehouse.

### Extract, transform, and load (ETL) processes

Extract, Transform, and Load (ETL) is a data integration process that is commonly used in data warehousing. The ETL process involves extracting data from multiple sources, transforming the data to conform to a common format, and loading the data into a target data warehouse. Here is an overview of each stage of the ETL process:

1. Extract: In the extract stage, data is extracted from various source systems such as operational databases, files, or APIs. This data is usually in a raw format and may be stored in different formats or structures.
2. Transform: In the transform stage, the extracted data is transformed into a format that is consistent with the target data warehouse. This involves cleaning the data, removing duplicates, and transforming data values to a common format. Transformations can be simple, such as changing the format of a date field, or complex, such as aggregating data from multiple sources.
3. Load: In the load stage, the transformed data is loaded into the target data warehouse. This involves inserting the data into tables in the data warehouse while maintaining data integrity, ensuring that there are no data conflicts and that data is consistent across all tables.

The ETL process is critical in ensuring that data is accurate, consistent, and ready for analysis in the data warehouse. It is often an iterative process, where data quality issues are identified during the transform stage and remedied before the data is loaded into the target data warehouse.

The ETL process is often automated using ETL tools that provide an interface for building and managing ETL processes. These tools provide a graphical interface for designing ETL processes, as well as scheduling, monitoring, and managing ETL workflows. ETL processes can also be built using programming languages such as Python or SQL.

### Develop reporting and analysis tools

Developing reporting and analysis tools is a crucial step in utilizing the data stored in a data warehouse. These tools enable users to extract insights from the data and gain valuable business intelligence. Here are some key steps involved in developing reporting and analysis tools:

1. Define user requirements: The first step in developing reporting and analysis tools is to define user requirements. This involves understanding the needs of the users and the types of reports and analyses they require.
2. Choose a reporting and analysis tool: Once the user requirements are defined, you need to choose a reporting and analysis tool that meets those requirements. There are many reporting and analysis tools available, ranging from simple tools such as Microsoft Excel to more complex tools such as Tableau, Power BI, or QlikView.
3. Create reports and dashboards: After selecting a reporting and analysis tool, you can create reports and dashboards that provide insights into the data stored in the data warehouse. Reports can be static or interactive and can be designed to meet specific user requirements. Dashboards can provide an overview of key metrics and KPIs and can be customized to provide different views of the data.
4. Analyze data: Reporting and analysis tools enable users to analyze data in different ways, such as through ad hoc queries, OLAP cubes, or data mining techniques. These tools enable users to gain insights into the data and identify trends and patterns.
5. Ensure data quality: To ensure the accuracy and reliability of the reports and analyses, it is important to ensure data quality. This involves establishing data governance policies and procedures, implementing data validation checks, and monitoring data quality over time.
6. Train users: Finally, it is important to train users on how to use the reporting and analysis tools effectively. This involves providing training and documentation on how to use the tools and interpret the data, as well as ongoing support and troubleshooting.

In summary, developing reporting and analysis tools is a crucial step in utilizing the data stored in a data warehouse. It involves understanding user requirements, selecting a reporting and analysis tool, creating reports and dashboards, analyzing data, ensuring data quality, and training users on how to use the tools effectively. By providing users with the tools they need to extract insights from the data, organizations can gain valuable business intelligence and make data-driven decisions.

### Implement data quality and data governance processes

Implementing data quality and data governance processes is critical to ensuring the accuracy, consistency, and reliability of data stored in a data warehouse. Here are some key steps involved in implementing data quality and data governance processes:

1. Define data governance policies: The first step in implementing data quality and data governance processes is to define data governance policies that outline how data will be managed, stored, and secured. These policies should include data quality standards, data access, and security policies, and data retention policies.
2. Establish data quality metrics: To ensure data quality, you need to establish data quality metrics that measure the accuracy, completeness, consistency, and timeliness of the data. These metrics should be based on user requirements and should be regularly monitored and reviewed.
3. Implement data validation checks: To ensure data quality, you need to implement data validation checks that validate data as it is loaded into the data warehouse. These checks can include checks for data type, range, and consistency.
4. Monitor data quality: It is important to monitor data quality over time to ensure that data continues to meet the established data quality metrics. This involves implementing data quality monitoring processes and regularly reviewing data quality reports.
5. Establish data governance roles and responsibilities: To ensure that data governance policies are implemented effectively, you need to establish data governance roles and responsibilities. This includes assigning data stewards, data custodians, and data owners who are responsible for managing data quality and data governance processes.
6. Train users: Finally, it is important to train users on data quality and data governance processes to ensure that they understand their roles and responsibilities and are able to comply with data governance policies.

Implementing data quality and data governance processes is critical to ensuring the accuracy, consistency, and reliability of data stored in a data warehouse. It involves defining data governance policies, establishing data quality metrics, implementing data validation checks, monitoring data quality, establishing data governance roles and responsibilities, and training users.

In *conclusion, designing and developing a data warehouse is a complex process that requires careful planning, attention to detail, and collaboration between different teams. By following the seven steps outlined in this article, organizations can create a data warehouse that meets their specific needs and provides valuable insights into their data. A well-designed data warehouse can help organizations make better-informed decisions, improve operational efficiency, and gain a competitive edge in today's data-driven business environment.*

## Normalization vs Denormalization

Normalization is Trying to increase data integrity by reducing the number of copies of the data. Data that needs to be added or updated will be done in as few places as possible. Denormalization is Trying to increase performance by reducing the number of joins between tables (as joins can be slow). Data integrity will take a bit of a potential hit, as there will be more copies of the data (to reduce JOINS).

## [CAP Theorem](https://en.wikipedia.org/wiki/CAP_theorem)

- Consistency: every read receives the most recent write or an error.
- Availability: every request receives a response that is not an error.
- Partition tolerance: the system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes
- CAP theorem implies that in the presence of a network partition, one has to choose between consistency and availability
- CAP is frequently misunderstood as if one has to choose to abandon one of the three guarantees at all times. In fact, the choice is really between consistency and availability only when a network partition or failure happens; at all other times, no trade-off has to be made.
- [ACID](https://en.wikipedia.org/wiki/ACID) databases choose consistency over availability.
- [BASE](https://en.wikipedia.org/wiki/Eventual_consistency) systems choose availability over consistency.

## Best Practices

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

## Labs

1. Build a Star Schema based Data Model in Postgres on the AirBnB dataset [[source code](04-serving/sql/lab-airbnb-postgres-datamodel/)]
2. Car company Data Model in MySQL [[source code](04-serving/sql/lab-cars-mysql-datamodel/)]
3. Create a star schema from 3NF schema on DVD rental Pagila dataset [[source code](04-serving/sql/lab-dvd-rental-datamodel/)]
4. Create a Postgres data model of Google Playstore dataset [[source code](04-serving/sql/lab-google-playstore-datamodel/)]
5. Inegi Snowflake Data Model [[source code](04-serving/sql/lab-inegi-snowflake-datamodel/)]
6. Northwind Data Model in MySQL [[source code](04-serving/sql/lab-mysql-northwind-datamodel/)]
7. Retail Store Data Model in MySQL [[source code](04-serving/sql/lab-mysql-retail-store-datamodel/)]
8. Creating a Bus Rapid Transit (BRT) Database in Postgres [[source code](04-serving/sql/lab-postgres-busrapid-transit/)]
9. Create Fact and Dimension Tables from Denormalized Raw Data [[source code](04-serving/sql/lab-postgres-elt-datamodel/)]
10. Postgres e-Wallet Data Model [[source code](04-serving/sql/lab-postgres-ewallet-datamodel/)]
11. Housing Data Model with CDC and SCD Type 2 [[source code](04-serving/sql/lab-postgres-housing-cdc-scd/)]
12. Credit Debit Finance Data Model in Snowflake [[source code](04-serving/sql/lab-snowflake-creditdebit-datamodel/)]
13. Sparkify Music Company Data Model in Postgres [[source code](04-serving/sql/lab-sparkify-data-model-postgres/)]

## Case Studies

1. [Spotify](https://medium.com/towards-data-engineering/design-the-database-for-a-system-like-spotify-95ffd1fb5927)
2. [LinkedIn](https://medium.com/towards-data-engineering/database-design-for-a-system-like-linkedin-3c52a5ab28c0)
3. [Zomato/Swiggy](https://medium.com/towards-data-engineering/database-design-for-a-food-delivery-app-like-zomato-swiggy-86c16319b5c5)

### Mobile Phone Billing System Relational Model

![](./img/mobilephone-billing-system-data-model.svg)

### Whatnot Dimensional Data Modeling

![img](https://user-images.githubusercontent.com/62965911/224901453-45944e6b-4467-4f3c-89c2-c5b1a8f6040f.png)

**Data model types:**

- **Facts** are (generally) transaction-like records that should not change after the transaction is completed. They tend to be high velocity (there are a lot of them) and have measurements associated with them, such as price or duration.
- **Dimensions** describe the objects in a fact table. For example, many orders might come from the same livestream, so the livestream would be considered a “dimension” of the order.
- **Bridge Tables** — map two entities together when they have a one-to-many or many-to-many relationship. For example, we will have a category dimension and a livestream watches fact. Live streams can have many categories.
- **Map Tables** — Different from bridge tables, map tables can be thought of as upstream of facts and dimensions. These are intermediary tables that map an ID to a categorization.

**Slowly Changing Dimensions:**

SCDs are dimensions with tracked changes using `valid_from` and `valid_to columns`. For example, a user’s address can change over time and each time a change occurs, a new record is created (Type 2 SCD).

**Natural Keys vs Surrogate Keys:**

Earlier, data users relied on a model’s natural keys to join, which is intuitive and simple, but sometimes confusing — string or int? — and, with the introduction of SCD, could lead to exploding joins. Whatnot decided all data models in their core schema would have a `varchar` surrogate key. They generate this for each table using  `dbt_utils.generate_surrogate_key([entity_id, valid_from])`. By always using a hashed surrogate key, we avoid potential integer-to-varchar join issues. The downside to surrogate keys is that they can be confusing for developers, who are used to joining on “id” columns rather than “keys”.

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

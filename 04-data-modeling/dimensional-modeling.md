# Dimensional Modeling

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
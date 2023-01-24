# Star Schema

Star Schema (introduced by Ralph Kimball) is the most widely used approach to organize data in database to make it easy to understand, read (fast data retrieval) and analyze. It is the underlying structure of dimensional model and also one of the methods used in dimensional modeling.

In practice, Star Schema is used to denormalize business data. It separates business process data into:

1.  Fact tables that hold quantitative information about the business, such as quantity, unit price, sales amount, etc.
2.  Dimension tables that hold descriptive information of the fact table, such as store, product, customer, etc.

With this design, the end-users are able to easily find the data they need, slice and dice the data however they see fit and evolve the schema if the business changes.

It is called a star schema because the fact table sits at the center of the logical diagram, and the small dimensional tables branch off to form the points of the star.

![](https://user-images.githubusercontent.com/62965911/214235541-66b537aa-4903-40ae-9587-57768efa1bd8.png)

In fact tables, you will have the foreign keys to dimension tables as well as aggregate or numeric information. We do not want descriptions or attributes in fact tables since those are reserved for dimension tables. We will use the foreign keys in a fact table to "*join"* the information in dimension tables.

Dimension tables are generally [denormalized](https://en.wikipedia.org/wiki/Denormalization) (may hold redundant data) and do not contain any foreign keys nor do they have any *"sub-dimension tables"*. Dimension table contains primary key and descriptive information of the fact table.

So how do we build a Star Schema? [As proposed by Kimball](https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/four-4-step-design-process/#:~:text=Select%20the%20business%20process.,Identify%20the%20facts.), there are 4 steps in designing of a dimensional model.

1.  Select the business process. The first step is to identify the business process that you want to model. Model the processes that are most significant or relevant to the business first.
2.  Declare the grain. Grain refers to the level of detail of the information that you will store in the fact table. The grain should be at the most atomic or lowest level possible. For example, A line item on a grocery receipt. The grocery owner might want to ask questions such as *"what are the items that sold the best during the day in our grocery store?"*, and to answer this question we need to dig into line-item level instead of the order-level.
3.  Identify the dimensions. You can identify the dimensions by looking at the descriptive information or attributes that exist in your business process and provide context to your measurable events. For example: payment method, customers, locations, etc.
4.  Identify the facts. Facts are the quantitative measures in your business process that are always in numeric. For example: price, minutes, speed, etc. You should identify/select the measures that are true to your selected grain.
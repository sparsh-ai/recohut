# SQL Data Modeling

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

## Data Modeling Best Practices

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

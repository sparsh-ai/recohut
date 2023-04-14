# Views

A *view* can be considered a virtual table because it is composed of rows and columns of data, the results of a **SELECT** SQL instruction in one or more database tables. Views are great resources for organizing information from different tables to create reports.

The following is a *view* example, with the name **High_price_products**, which is constructed with a **SELECT** statement in the **PRODUCTS** table, filtering the **Price** field by the average greater than that of the other products in the table:

```sql
CREATE VIEW [High_price_products] AS
SELECT Product_Name, Product_Price
FROM Products
WHERE Product_Price > (SELECT AVG(Product_Price) FROM Products);
```

Views are important features, especially for generating reports. But another object that's also widely used in SQL databases, and which can help in the development of solutions, is a stored procedure, which we'll look at in the following section.

Both tables and views have advantages and disadvantages. There are two advantages to using a view. First, the view costs no additional storage. If you create a view, the data won't be stored anywhere; it will just save the SQL formula. The second advantage is real time; if you access the view, then every time the underlying table changes, the view will get the latest update.

However, there are reasons as to why you would want to avoid using too many views physicalized into a new table. Sometimes, views can be heavy, and when the underlying tables are large and there are many joins and aggregations in the view's query, you may end up having very heavy processing. 

IMPORTANT NOTE

> A physicalized table means using the query result to create a new table.

Imagine you have 5 upstream raw tables, each 1 PB in size, and your downstream consists of 1,000 views accessing the 5 tables. You may end up processing the PBs of data repeatedly, and that's bad in terms of both cost and performance.
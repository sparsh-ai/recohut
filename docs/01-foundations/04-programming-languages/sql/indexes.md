# Indexes

An *index* is created by a table or view to define a field that can be used to optimize queries.

The best way to understand an *index* is to observe the index section typically present in a book. This section summarizes the main topics in the book and references the page each topic begins on. This is exactly what an index does in a database table or view.

Some database platforms have an *auto index*; others use the primary key of the tables to create their indexes.

You can create multiple *indexes* in each table. Each *index* generates a record in an internal database table, with a copy of the data in order and pointers that indicate the fastest way to get to the information, which help the database search system find that record.

To create an *index* in a table, the SQL statement is very simple:

```sql
CREATE INDEX IDX_CUSTOMERNAME
ON CUSTOMERS(Name);
```

This way, we create an index called **IDX_CUSTOMERNAME** in the **CUSTOMERS** table, using the **Name** field to help the database organize queries for customer names.

So, we close the main SQL commands used in relational databases. Of course, all commands are used in a large database, but by understanding the statement and how they work, you will surely be able to implement your commands at the right time.

A database index is a data structure that improves the speed of operations in a table. Indexes can be created using one or more columns, providing the basis for both rapid random lookups and efficient ordering of access to records.

While creating index, it should be taken into consideration which all columns will be used to make SQL queries and create one or more indexes on those columns.

Practically, indexes are also a type of tables, which keep primary key or index field and a pointer to each record into the actual table.

The users cannot see the indexes, they are just used to speed up queries and will be used by the Database Search Engine to locate records very fast.

The INSERT and UPDATE statements take more time on tables having indexes, whereas the SELECT statements become fast on those tables. The reason is that while doing insert or update, a database needs to insert or update the index values as well.
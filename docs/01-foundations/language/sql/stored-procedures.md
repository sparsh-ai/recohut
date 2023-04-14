# Stored Procedures

A *stored procedure* is a set of SQL statements stored in a database. These statements can request data entry parameters, which are used as variables during execution, and can constitute a data output.

In the following example, we can see the creation of a *stored SQL procedure* called **All_Customers**, which requests two variables, **City** and **PostalCode**, to filter the results in the query:

```sql
CREATE PROCEDURE All_Customers
@City nvarchar(30), @PostalCode nvarchar(10)
AS
SELECT * FROM Customers WHERE City = @City AND PostalCode = @PostalCode
GO;
```

Objects in a database need a trigger to be called and start executing. For this reason, there is an object in relational databases called a *trigger*. Let's analyze it now.


If you want to save your SQL query on the database server for execution later, one way to do it is to use a stored procedure.

The first time you invoke a stored procedure, MySQL looks up for the name in the database catalog, compiles the stored procedure's code, place it in a memory area known as a cache, and execute the stored procedure.

If you invoke the same stored procedure in the same session again, MySQL just executes the stored procedure from the cache without having to recompile it.

A stored procedure can have [parameters](https://www.mysqltutorial.org/stored-procedures-parameters.aspx) so you can pass values to it and get the result back. For example, you can have a stored procedure that returns customers by country and city. In this case, the country and city are parameters of the stored procedure.

A stored procedure may contain control flow statements such as [IF](https://www.mysqltutorial.org/mysql-if-statement/), [CASE](https://www.mysqltutorial.org/mysql-case-statement/), and `LOOP` that allow you to implement the code in the procedural way.

A stored procedure can call other stored procedures or [stored functions](https://www.mysqltutorial.org/mysql-stored-function/), which allows you to modulize your code.

Typically, a stored procedure contains multiple statements separated by semicolons (;). To compile the whole stored procedure as a single compound statement, you need to temporarily change the delimiter from the semicolon (;) to another delimiter such as `$$` or `//`.

**MySQL stored procedures advantages**

The following are the advantages of stored procedures.

1. Reduce network traffic - Stored procedures help reduce the network traffic between applications and MySQL Server. Because instead of sending multiple lengthy SQL statements, applications have to send only the name and parameters of stored procedures.
2. Centralize business logic in the database - You can use the stored procedures to implement business logic that is reusable by multiple applications. The stored procedures help reduce the efforts of duplicating the same logic in many applications and make your database more consistent.
3. Make database more secure - The database administrator can grant appropriate privileges to applications that only access specific stored procedures without giving any privileges on the underlying tables.

**MySQL stored procedures disadvantages**

Besides those advantages, stored procedures also have disadvantages:

1. Resource usages - If you use many stored procedures, the memory usage of every connection will increase substantially. Besides, overusing a large number of logical operations in the stored procedures will increase the CPU usage because the MySQL is not well-designed for logical operations.
2. Troubleshooting - It's difficult to debug stored procedures. Unfortunately, MySQL does not provide any facilities to debug stored procedures like other enterprise database products such as Oracle and SQL Server.
3. Maintenances - Developing and maintaining stored procedures often requires a specialized skill set that not all application developers possess. This may lead to problems in both application development and maintenance.
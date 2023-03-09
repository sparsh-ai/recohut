# SQL

**Structured Query Language** (**SQL**) is the most widely used language in relational database platforms for recording, editing, re-editing, and querying operations. SQL was created by Donald D. Chamberlin and Raymond F. Boyce in 1974 in an innovation lab at IBM and has since evolved with DBMSs that use it with Microsoft SQL Server, Oracle Database, MySQL, PostgreSQL, and MariaDB.

SQL has been standardized by ANSI and the **International Organization for Standardization** (**ISO**), but each of the RDBMS has some exclusive extended SQL standard instructions, primarily for administration, monitoring, and other operations unique to that RDM.

These unique patterns have names such as the following:

- T-SQL or Transact-SQL is the version used by Microsoft SQL Server and Azure SQL versions
- pgSQL is the default of PostgreSQL databases

SQL is a must-have skill for data engineers. They use the querying language to perform essential tasks like modeling data, extracting performance metrics, and developing reusable data structures.

Data engineer SQL questions tend to mirror the work that engineers do.

Therefore, data engineers need to be proficient not just in querying data and pulling metrics, but also in data structures, manipulation and security within SQL. Broadly, a data engineer may face SQL questions in these categories:

- SQL queries - Using SQL data query language (DQL) statements to pull metrics and analyze data. Commands to know: SELECT
- Data modeling - Using DDL commands to create database schema and define data structures. Commands to know: CREATE, ALTER, DROP, RENAME, TRUNCATE, COMMENT
- Data manipulation - Using DML statements to retrieve and manipulate data. Commands to know: INSERT, UPDATE, DELETE, MERGE, CALL, EXPLAIN PLAN, LOCK TABLE
- Data security - Using DCL (data control language) commands to manage database security. Commands to know: GRANT, REVOKE

This data engineering SQL questions guide provides an overview of the types of questions you might face, as well as an example data engineer interview questions to help you prepare for your interview.

Watch this video: https://www.youtube.com/embed/AK7_m-aThfw

[This](https://techtfq.com/blog/top-20-sql-interview-questions) is the blog link for the above video.

We will now list some of the additional advantages that made the SQL language the standard used in relational databases.

## Key Concepts

1. **Data definition:** The ability to create and modify the structure of a database, including creating tables, defining columns and data types, and setting constraints.
2. **Data manipulation:** The ability to add, update, and delete data within a database, as well as retrieve specific data using SELECT statements.
3. **Data integrity:** Ensuring that the data within a database is accurate, consistent, and free of errors, through the use of constraints, keys, and indexes.
4. **Data querying:** Retrieving specific data from a database using SELECT statements, filtering and sorting the data, and joining tables to combine data from multiple sources.
5. **Data modeling:** The ability to represent real-world entities and relationships in a database through the use of tables, columns, and keys.*
6. **Data normalization:** The process of organizing data in a database to minimize data redundancy and improve data integrity.*
7. **Data security:** Techniques for protecting a database from unauthorized access, such as through the use of user accounts, passwords, and access controls.
8. **Data maintenance:** The ability to backup, restore, and optimize a database to ensure its ongoing performance and stability.*

## Advantages

The list of advantages is very long, but the main points are as follows:

- **Standardization**: As mentioned, SQL has been standardized by *ANSI* and is still used in many database systems. This is why SQL is one of the most documented languages today, easier to learn, and useful for day-to-day activities.
- **Simplicity with scalability**: SQL is an easy-to-understand language with simple syntax fundamentals, answering high-scalability database scenarios by processing millions of pieces of data.
- **Portability**: Because it is standard in several *DBMSs*, SQL is portable between these different types of database managers, even though there are some particularities in the SQL of each.
- **Multiple data views**: With SQL, it is possible to define different views of the database structure for different user needs. For example, you might have users who are only allowed to explore the data and perform **SELECT** commands, whereas other users can add columns in tables but cannot delete any columns. This granularity of permissions makes databases more fully configurable.

## Disadvantages

Of course, we can find more disadvantages when we know about NoSQL databases, but the disadvantages most encountered by data architects to justify an analysis of other databases are these:

- **Database processing cost**: In general, the cost of processing a database that uses the SQL language is high compared to more modern database languages. This means that the database needs a robust infrastructure for data processing. Compared to a NoSQL database, a SQL database uses compute power, RAM, and storage speed more intensively.
- **Pre-build and fixed schema**: A SQL database must be planned and implemented (the creation of tables, columns, relationships, and so on) before implementing the software. Your schema should be created and, once created, only changed upon a general impact analysis of the database.

This generates a lack of flexibility and more time spent at the beginning of a project in the planning and implementation of the database.

## Understanding the categories of SQL commands

To understand the structure of SQL, it is subdivided into five categories of commands:

- **Data Query Language** (**DQL**): Defines the command used so that we can query (**SELECT**) the data stored in the database
- **Data Manipulation Language** (**DML**): Defines the commands used for manipulating data in the database (**INSERT**, **UPDATE**, and **DELETE**)
- **Data Definition Language** (**DDL**): Defines the commands used for creating tables, views, and indexes, updating these structures (**ALTER**), as well as removal (**DROP**)
- **Data Control Language** (**DCL**): Defines the commands used to control access to database data by adding (**GRANT**) and removing (**REVOKE**) access permissions
- **Data Transaction Language** (**DTL**): Defines the commands used to manage transactions executed in the database, such as starting a transaction (**BEGIN**), confirming it (**COMMIT**), or undoing it (**ROLLBACK**)

The following diagram demonstrates the categories of the SQL language and their main commands for quick reference:

![B18569_03_03](https://user-images.githubusercontent.com/62965911/218838205-321df2ab-06b7-4737-8570-6d8c52e5e543.jpeg)

These five categories contain all the necessary syntaxes of SQL commands for operations in a database.

SQL was initially created to be the language for generating, manipulating, and retrieving data from relational databases, which have been around for more than 40 years. Over the past decade or so, however, other data platforms such as Hadoop, Spark, and NoSQL have gained a great deal of traction, eating away at the relational database market. However, the SQL language has been evolving to facilitate the retrieval of data from various platforms, regardless of whether the data is stored in tables, documents, or flat files.

Whether you will be using a relational database or not, if you are working in data engineering, business intelligence, or some other facet of data analysis, you will likely need to know SQL, along with other languages/platforms such as Python and R. Data is everywhere, in huge quantities, and arriving at a rapid pace, and people who can extract meaningful information from all this data are in big demand.

### Aggregation, Grouping, Ordering & Filtering

The aggregation functions perform calculations on multiple rows and return the result as one value, collapsing the individual rows in the process. When an aggregation function is used, you need to group the data on fields which are not aggregated by using a GROUP BY clause.

Filtering is used when you need to extract a subset of data by using a specific condition. You can use WHERE and HAVING clauses to filter the data as per your needs.

### Joins and Unions

Data Engineers are typically responsible for collating different data sources together and providing a cleaner source of information for the Data Scientists or Data Analysts. In order to collate data from different sources, they need a good understanding of SQL Joins and Unions.

### CTEs, Sub Queries, and Window Functions

As the queries become more complex, it’s not always possible to write a single query and do all the analysis. Sometimes, it’s necessary to create a temporary table and use the results in a new query to perform analysis at different levels. We can use a subquery, a CTE (Common Table Expression), or a TEMP (Temporary) table for this. As a Data Engineer, you need to understand these concepts to write better and optimized SQL queries.

### Query breakdown

| Statement | How to Use It               | Other Details                                         |
| --------- | --------------------------- | ----------------------------------------------------- |
| SELECT    | SELECT Col1, Col2, ...      | Provide the columns you want                          |
| FROM      | FROM Table                  | Provide the table where the columns exist             |
| LIMIT     | LIMIT 10                    | Limits based number of rows returned                  |
| ORDER BY  | ORDER BY Col                | Orders table based on the column. Used with DESC.     |
| WHERE     | WHERE Col > 5               | A conditional statement to filter your results        |
| LIKE      | WHERE Col LIKE '%me%'       | Only pulls rows where column has 'me' within the text |
| IN        | WHERE Col IN ('Y', 'N')     | A filter for only rows with column of 'Y' or 'N'      |
| NOT       | WHERE Col NOT IN ('Y', 'N') | NOT is frequently used with LIKE and IN               |
| AND       | WHERE Col1 > 5 AND Col2 < 3 | Filter rows where two or more conditions must be true |
| OR        | WHERE Col1 > 5 OR Col2 < 3  | Filter rows where at least one condition must be true |
| BETWEEN   | WHERE Col BETWEEN 3 AND 5   | Often easier syntax than using an AND                 |

## Key Commands

Important Commands that you must know:

- CREATE - To create table or view or database
- SELECT - To select the data values from the table in a database
- FROM - To specify table name from where we are retrieving the records
- WHERE - To filter the results based on the condition specified in the where clause
- LIMIT - To limit the number of rows returned as the result
- DROP - To delete the table or database
- UPDATE - To update the data in the table
- DELETE - To delete the rows in the table
- ALTER TABLE - To add or remove columns from the table
- AS - To rename column with an alias name
- JOIN - To combine the rows of 2 or more tables
- AND - To combine rows in which records from both/more table are evaluated using And condition
- OR - To combine rows in which records from both/more table are evaluated using Or condition
- IN - To specify multiple values using the where clause/condition
- LIKE - To search/identify the patterns in the column
- IS NULL - To check and return those rows that contains NULL values
- CASE - To return values after evaluating the specified condition
- GROUP BY - To group rows which consist of same values into the summary rows/columns
- ORDER BY - To specify the order of the result returned ( ASC or DESC)
- HAVING - To specify conditions for aggregate functions
- COUNT - To count the number of rows
- SUM - To return sum of the column
- AVG - To return average of the column
- MIN - To return min value in the column
- MAX - To return max value in the column

## Key Functions

* **Aggregate functions:** These functions are used to summarize data, such as counting the number of rows, calculating the sum or average of a column, or finding the minimum or maximum value. Examples include COUNT(), SUM(), AVG(), MIN(), and MAX().
* **Window functions:** These functions are used to perform calculations across rows within a specific window or frame of a query result set. Examples include ROW_NUMBER(), RANK(), DENSE_RANK() and NTILE().
* **String functions:** These functions are used to manipulate and extract information from strings. Examples include SUBSTRING(), LENGTH(), CONCAT(), UPPER(), and LOWER().
* **Date and time functions:** These functions are used to work with date and time data. Examples include CURRENT_DATE(), CURRENT_TIME(), CURRENT_TIMESTAMP(), and EXTRACT().
* **Conversion functions:** These functions are used to convert data from one type to another. Examples include CAST() and CONVERT().
* **Conditional functions:** These functions are used to perform conditional calculations. Examples include CASE(), COALESCE() and NULLIF().
* **Analytic functions:** These functions are used to perform complex calculations over a group of rows. Examples include RANK(), DENSE_RANK(), ROW_NUMBER(), and LEAD() and LAG().

## Describing the database components

There are components in a relational database that are important to maintain the organization and productivity. The four most common components among database systems are as follows:

- **Views**
- **Stored Procedures**
- **Triggers**
- **Indexes**

Let's take a look at each of them in detail in the following sections.

### Views

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

### Stored procedures

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

### Triggers

*Triggers* are a type of stored procedure, configured to call whenever an event occurs. This trigger can be used, for example, to signalize the execution of some statements whenever new data is included in a table, or a record is edited in the table.

Many *trigger* use cases are about creating transaction audit tables and maintaining data consistency, by reviewing relationships before confirming any type of transaction. We can use a trigger in the data definition and for data manipulation instructions.

In the following, we will use the **DDL CREATE** statement, which we have already seen in this note to create tables, but now we will use it to create a **TRIGGER**:

```sql
CREATE TRIGGER LOG_PRICE_HISTORY before update
on PRODUCTS_SERVICES
for each row
insert into PRICE_HISTORY
values(old.PRODUCTID, old.BASEPRICE, old.DISCOUNT, old.FINALPRICE, old.DATELASTUPDATE);
```

Executing this command, the **LOG_PRICE_HISTORY** trigger will be created and linked to the **PRODUCTS_SERVICES** table, with the following condition: whenever an item is edited in this table, a new record will be created in the **PRICE_HISTORY** table with the data from this table before the change.

This makes it possible for you to keep a history of this table and know exactly the changes that were made.

Sometimes, tables become very large, with thousands and even millions of records. This size can cause performance problems in database operations, and one of the methods used to mitigate these problems was indexes, which we are going to look at now.

### Indexes

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

## Basics

### SQL SELECT

There are two required ingredients in any SQL query: `SELECT` and `FROM`---and they have to be in that order. `SELECT` indicates which columns you'd like to view, and `FROM` identifies the table that they live in.

### SQL LIMIT

As you might expect, the limit restricts how many rows the SQL query returns.

**Why should you limit your results?**

Many analysts use limits as a simple way to keep their queries from taking too long to return. The aim of many of your queries will simply be to see what a particular table looks like—you'll want to scan the first few rows of data to get an idea of which fields you care about and how you want to manipulate them. If you query a very large table (such as one with hundreds of thousands or millions of rows) and don't use a limit, you could end up waiting a long time for all of your results to be displayed, which doesn't make sense if you only care about the first few.

### SQL WHERE

Once you know how to view some data using SELECT and FROM, the next step is filtering the data using the WHERE clause.

### SQL Comparison Operators

**Comparison operators on numerical data**

The most basic way to filter data is using comparison operators. The easiest way to understand them is to start by looking at a list of them:

| Equal to                 | `=`              |
| ------------------------ | ------------------ |
| Not equal to             | `<>` or `!=` |
| Greater than             | `>`              |
| Less than                | `<`              |
| Greater than or equal to | `>=`             |
| Less than or equal to    | `<=`             |

These comparison operators make the most sense when applied to numerical columns.

**Comparison operators on non-numerical data**

All of the above operators work on non-numerical data as well. `=` and `!=` make perfect sense—they allow you to select rows that match or don't match any value, respectively.

There are some important rules when using these operators, though. If you're using an operator with values that are non-numeric, you need to put the value in single quotes: 'value'.

You can use `>`, `<`, and the rest of the comparison operators on non-numeric columns as well---they filter based on alphabetical order.

If you're using `>`, `<`, `>=`, or `<=`, you don't necessarily need to be too specific about how you filter.

**Arithmetic in SQL**

You can perform arithmetic in SQL using the same operators you would in Excel: `+`, `-`, `*`, `/`. However, in SQL you can only perform arithmetic across columns on values in a given row. To clarify, you can only add values in multiple columns *from the same row* together using `+`---if you want to add values across multiple rows, you'll need to use aggregate functions.

The columns that contain the arithmetic functions are called "derived columns" because they are generated by modifying the information that exists in the underlying data.

As in Excel, you can use parentheses to manage the order of operations.

It occasionally makes sense to use parentheses even when it's not absolutely necessary just to make your query easier to read.

### SQL Logical Operators

You'll likely also want to filter data using several conditions---possibly more often than you'll want to filter by only one condition. Logical operators allow you to use multiple comparison operators in one query.

Each logical operator is a special snowflake, so we'll go through them individually in the following lessons. Here's a quick preview:

- `LIKE` allows you to match similar values, instead of exact values.
- `IN` allows you to specify a list of values you'd like to include.
- `BETWEEN` allows you to select only rows within a certain range.
- `IS NULL` allows you to select rows that contain no data in a given column.
- `AND` allows you to select only rows that satisfy two conditions.
- `OR` allows you to select rows that satisfy either of two conditions.
- `NOT` allows you to select rows that do not match a certain condition.

### SQL LIKE

LIKE is a logical operator in SQL that allows you to match on similar values rather than exact ones.

### SQL IN

IN is a logical operator in SQL that allows you to specify a list of values that you'd like to include in the results.

As with comparison operators, you can use non-numerical values, but they need to go inside single quotes. Regardless of the data type, the values in the list must be separated by commas.

### SQL BETWEEN

BETWEEN is a logical operator in SQL that allows you to select only rows that are within a specific range.

### SQL IS NULL

IS NULL is a logical operator in SQL that allows you to exclude rows with missing data from your results.

Some tables contain null values—cells with no data in them at all. This can be confusing for heavy Excel users, because the difference between a cell having no data and a cell containing a space isn't meaningful in Excel. In SQL, the implications can be pretty serious.

You can select rows that contain no data in a given column by using IS NULL.

### SQL AND

AND is a logical operator in SQL that allows you to select only rows that satisfy two conditions.

You can use SQL's AND operator with additional AND statements or any other comparison operator, as many times as you want.

### SQL OR

OR is a logical operator in SQL that allows you to select rows that satisfy either of two conditions. It works the same way as AND, which selects the rows that satisfy both of two conditions.

You can combine AND with OR using parenthesis.

### SQL NOT

NOT is a logical operator in SQL that you can put before any conditional statement to select rows for which that statement is false.

NOT is commonly used with LIKE.

NOT is also frequently used to identify non-null rows, but the syntax is somewhat special—you need to include IS beforehand.

### SQL ORDER BY

The ORDER BY clause allows you to reorder your results based on the data in one or more columns.

You can also order by mutiple columns. This is particularly useful if your data falls into categories and you'd like to organize rows by date, for example, but keep all of the results within a given category together.

When using ORDER BY with a row limit (either through the check box on the query editor or by typing in LIMIT), the ordering clause is executed first. This means that the results are ordered before limiting to only a few rows.

### Comments

You can "comment out" pieces of code by adding combinations of characters. In other words, you can specify parts of your query that will not actually be treated like SQL code. It can be helpful to include comments that explain your thinking so that you can easily remember what you intended to do if you ever want to revisit your work. Commenting can also be useful if you want to test variations on your query while keeping all of your code intact.

You can use-- (two dashes) to comment out everything to the right of them on a given line.

You can also leave comments across multiple lines using /* to begin the comment and */ to close it.

## Intermediate

### SQL Aggregate Functions

| Aggregate function                                               | Description                                                            |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------- |
| [AVG()](https://www.mysqltutorial.org/mysql-avg/)                   | Return the average of non-NULL values.                                 |
| BIT_AND()                                                        | Return bitwise AND.                                                    |
| BIT_OR()                                                         | Return bitwise OR.                                                     |
| BIT_XOR()                                                        | Return bitwise XOR.                                                    |
| [COUNT()](https://www.mysqltutorial.org/mysql-count/)               | Return the number of rows in a group, including rows with NULL values. |
| [GROUP_CONCAT()](https://www.mysqltutorial.org/mysql-group_concat/) | Return a concatenated string.                                          |
| JSON_ARRAYAGG()                                                  | Return result set as a single JSON array.                              |
| JSON_OBJECTAGG()                                                 | Return result set as a single JSON object.                             |
| [MAX()](https://www.mysqltutorial.org/mysql-max-function/)          | Return the highest value (maximum) in a set of non-NULL values.        |
| [MIN()](https://www.mysqltutorial.org/mysql-min/)                   | Return the lowest value (minimum) in a set of non-NULL values.         |
| [STDEV()](https://www.mysqltutorial.org/mysql-standard-deviation/)  | Return the population standard deviation.                              |
| STDDEV_POP()                                                     | Return the population standard deviation.                              |
| STDDEV_SAMP()                                                    | Return the sample standard deviation.                                  |
| [SUM()](https://www.mysqltutorial.org/mysql-sum/)                   | Return the summation of all non-NULL values a set.                     |
| VAR_POP()                                                        | Return the population standard variance.                               |
| VARP_SAM()                                                       | Return the sample variance.                                            |
| VARIANCE()                                                       | Return the population standard variance.                               |

SQL is excellent at aggregating data the way you might in a pivot table in Excel. You will use aggregate functions all the time, so it's important to get comfortable with them. The functions themselves are the same ones you will find in Excel or any other analytics program.

- COUNT counts how many rows are in a particular column.
- SUM adds together all the values in a particular column.
- MIN and MAX return the lowest and highest values in a particular column, respectively.
- AVG calculates the average of a group of selected values.

### SQL COUNT

COUNT is a SQL aggregate function for counting the number of rows in a particular column. COUNT is the easiest aggregate function to begin with because verifying your results is extremely simple.

Things start to get a little bit tricky when you want to count individual columns.

One nice thing about COUNT is that you can use it on non-numerical columns.

### SQL SUM

SUM is a SQL aggregate function. that totals the values in a given column. Unlike COUNT, you can only use SUM on columns containing numerical values.

### SQL MIN/MAX

MIN and MAX are SQL aggregation functions that return the lowest and highest values in a particular column.

They're similar to COUNT in that they can be used on non-numerical columns. Depending on the column type, MIN will return the lowest number, earliest date, or non-numerical value as close alphabetically to "A" as possible. As you might suspect, MAX does the opposite—it returns the highest number, the latest date, or the non-numerical value closest alphabetically to "Z."

### SQL AVG

AVG is a SQL aggregate function that calculates the average of a selected group of values. It's very useful, but has some limitations. First, it can only be used on numerical columns. Second, it ignores nulls completely.

### SQL GROUP BY

SQL aggregate function like COUNT, AVG, and SUM have something in common: they all aggregate across the entire table. But what if you want to aggregate only part of a table? For example, you might want to count the number of entries for each year.

In situations like this, you'd need to use the GROUP BY clause. GROUP BY allows you to separate data into groups, which can be aggregated independently of one another.

You can group by multiple columns, but you have to separate column names with commas—just as with ORDER BY).

As with ORDER BY, you can substitute numbers for column names in the GROUP BY clause. It's generally recommended to do this only when you're grouping many columns, or if something else is causing the text in the GROUP BY clause to be excessively long.

The order of column names in your GROUP BY clause doesn't matter—the results will be the same regardless. If you want to control how the aggregations are grouped together, use ORDER BY.

### SQL HAVING

You'll often encounter datasets where GROUP BY isn't enough to get what you're looking for. Let's say that it's not enough just to know aggregated stats by month. After all, there are a lot of months in this dataset. Instead, you might want to find every month during which AAPL stock worked its way over $400/share. The WHERE clause won't work for this because it doesn't allow you to filter on aggregate columns—that's where the HAVING clause comes in.

### Query clause order

The order in which you write the clauses is important. Here's the order for everything you've learned so far:

1. SELECT
2. FROM
3. WHERE
4. GROUP BY
5. HAVING
6. ORDER BY
7. LIMIT

### SQL CASE

The CASE statement is SQL's way of handling if/then logic. The CASE statement is followed by at least one pair of WHEN and THEN statements—SQL's equivalent of IF/THEN in Excel. Because of this pairing, you might be tempted to call this SQL CASE WHEN, but CASE is the accepted term.

Every CASE statement must end with the END statement. The ELSE statement is optional, and provides a way to capture values not specified in the WHEN/THEN statements.

You can also define a number of outcomes in a CASE statement by including as many WHEN/THEN statements as you'd like.

You can also string together multiple conditional statements with AND and OR the same way you might in a WHERE clause.

CASE's slightly more complicated and substantially more useful functionality comes from pairing it with aggregate functions. For example, let's say you want to only count rows that fulfill a certain condition. Since COUNT ignores nulls, you could use a CASE statement to evaluate the condition and produce null or non-null values depending on the outcome.

Combining CASE statements with aggregations can be tricky at first. It's often helpful to write a query containing the CASE statement first and run it on its own.

### SQL DISTINCT

You'll occasionally want to look at only the unique values in a particular column. You can do this using SELECT DISTINCT syntax.

DISTINCT can be particularly helpful when exploring a new data set. In many real-world scenarios, you will generally end up writing several preliminary queries in order to figure out the best approach to answering your initial question. Looking at the unique values on each column can help identify how you might want to group or filter the data.

You can use DISTINCT when performing an aggregation. You'll probably use it most commonly with the COUNT function.

It's worth noting that using DISTINCT, particularly in aggregations, can slow your queries down quite a bit.

### SQL Joins

It might be helpful to refer to this JOIN visualization by Patrik Spathon.

[![](https://user-images.githubusercontent.com/62965911/213920018-c8eece0a-b772-40f6-85bd-f6c0159f903e.png)](https://joins.spathon.com/)

Let's say we want to figure out which conference has the highest average weight. Given that information is in two separate tables, how do you do that? A join!

```sql
SELECT teams.conference AS conference,
    AVG(players.weight) AS average_weight
FROM college_football_players players
    JOIN college_football_teams teams ON teams.school_name = players.school_name
GROUP BY teams.conference
ORDER BY AVG(players.weight) DESC
```

### SQL INNER JOIN

Returns only the rows from both the dataframes that have matching values in both columns specified as the join keys. In mathematical terms, an inner join is the intersection of the two tables.

### SQL LEFT/LEFT OUTER JOIN

Returns all the rows from the left dataframe and the matching rows from the right dataframe. If there are no matching values in the right dataframe, then it returns a null.

### SQL RIGHT/RIGHT OUTER JOIN

Returns all the rows from the right dataframe and the matching rows from the left dataframe. If there are no matching values in the left dataframe, then it returns a null.

### SQL OUTER/FULL JOIN

Returns all the rows from both the dataframes, including the matching and non-matching rows. If there are no matching values, then the result will contain a NULL value in place of the missing data.

### SQL CROSS JOIN

Returns all possible combinations of rows from both the dataframes. In other words, it takes every row from one dataframe and matches it with every row in the other dataframe. The result is a new dataframe with all possible combinations of the rows from the two input dataframes.

A cross-join is used when we want to perform a full outer join but in a more computationally efficient manner. Cross joins are not recommended for large datasets as they can produce a very large number of records, leading to memory issues and poor performance.

### SQL LEFT ANTI JOIN

A left anti join is a type of left join operation that returns only the rows from the left dataframe that do not have matching values in the right dataframe. It is used to find the rows in one dataframe that do not have corresponding values in another dataframe.

The result of a left anti join is a dataframe that contains only the rows from the left dataframe that do not have matching values in the right dataframe. If a row from the left dataframe has matching values in the right dataframe, it will not be included in the result.

### SQL SELF JOIN

A self join is a join operation in which a dataframe is joined with itself. It is used to compare the values within a single dataframe and return the rows that match specified criteria.

For example, a self join could be used to find all pairs of rows in a dataframe where the values in two columns are equal. The result would be a new dataframe that contains only the rows that meet the specified criteria.

### SQL UNION

SQL joins allow you to combine two datasets side-by-side, but UNION allows you to stack one dataset on top of the other. Put differently, UNION allows you to write two separate SELECT statements, and to have the results of one statement display in the same table as the results from the other statement.

SQL has strict rules for appending data:

- Both tables must have the same number of columns
- The columns must have the same data types in the same order as the first table

While the column names don't necessarily have to be the same, you will find that they typically are. This is because most of the instances in which you'd want to use UNION involve stitching together different parts of the same dataset.

## Advanced

### SQL Date

Assuming you've got some dates properly stored as a date or time data type, you can do some pretty powerful things. Maybe you'd like to calculate a field of dates a week after an existing field. Or maybe you'd like to create a field that indicates how many days apart the values in two other date fields are. These are trivially simple, but it's important to keep in mind that the data type of your results will depend on exactly what you are doing to the dates.

When you perform arithmetic on dates (such as subtracting one date from another), the results are often stored as the interval data type—a series of integers that represent a period of time.

| Function                                                         | Description                                                               |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [CURDATE](https://www.mysqltutorial.org/mysql-curdate/)             | Returns the current date.                                                 |
| [DATEDIFF](https://www.mysqltutorial.org/mysql-datediff.aspx)       | Calculates the number of days between two DATE values.                    |
| [DAY](https://www.mysqltutorial.org/mysql-day/)                     | Gets the day of the month of a specified date.                            |
| [DATE_ADD](https://www.mysqltutorial.org/mysql-date_add/)           | Adds a time value to date value.                                          |
| [DATE_SUB](https://www.mysqltutorial.org/mysql-date_sub/)           | Subtracts a time value from a date value.                                 |
| [DATE_FORMAT](https://www.mysqltutorial.org/mysql-date_format/)     | Formats a date value based on a specified date format.                    |
| [DAYNAME](https://www.mysqltutorial.org/mysql-dayname/)             | Gets the name of a weekday for a specified date.                          |
| [DAYOFWEEK](https://www.mysqltutorial.org/mysql-dayofweek/)         | Returns the weekday index for a date.                                     |
| [EXTRACT](https://www.mysqltutorial.org/mysql-extract/)             | Extracts a part of a date.                                                |
| [LAST_DAY](https://www.mysqltutorial.org/mysql-last_day/)           | Returns the last day of the month of a specified date                     |
| [NOW](https://www.mysqltutorial.org/mysql-now/)                     | Returns the current date and time at which the statement executed.        |
| [MONTH](https://www.mysqltutorial.org/mysql-month/)                 | Returns an integer that represents a month of a specified date.           |
| [STR_TO_DATE](https://www.mysqltutorial.org/mysql-str_to_date/)     | Converts a string into a date and time value based on a specified format. |
| [SYSDATE](https://www.mysqltutorial.org/mysql-sysdate/)             | Returns the current date.                                                 |
| [TIMEDIFF](https://www.mysqltutorial.org/mysql-timediff/)           | Calculates the difference between two TIME or DATETIME values.            |
| [TIMESTAMPDIFF](https://www.mysqltutorial.org/mysql-timestampdiff/) | Calculates the difference between two DATE or DATETIME values.            |
| [WEEK](https://www.mysqltutorial.org/mysql-week/)                   | Returns a week number of a date.                                          |
| [WEEKDAY](https://www.mysqltutorial.org/mysql-weekday/)             | Returns a weekday index for a date.                                       |
| [YEAR](https://www.mysqltutorial.org/mysql-year/)                   | Return the year for a specified date                                      |

### Using SQL String Functions to Clean Data

| Name                                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| [CONCAT](https://www.mysqltutorial.org/sql-concat-in-mysql.aspx)                                        | Concatenate two or more strings into a single string                                     |
| [INSTR](https://www.mysqltutorial.org/mysql-instr/)                                                     | Return the position of the first occurrence of a substring in a string                   |
| [LENGTH](https://www.mysqltutorial.org/mysql-string-length/)                                            | Get the length of a string in bytes and in characters                                    |
| [LEFT](https://www.mysqltutorial.org/mysql-left-function/)                                              | Get a specified number of leftmost characters from a string                              |
| [LOWER](https://www.mysqltutorial.org/mysql-string-functions/mysql-lower/)                              | Convert a string to lowercase                                                            |
| [LTRIM](https://www.mysqltutorial.org/mysql-string-functions/mysql-ltrim-function/)                     | Remove all leading spaces from a string                                                  |
| [REPLACE](https://www.mysqltutorial.org/mysql-string-replace-function.aspx)                             | Search and replace a substring in a string                                               |
| [RIGHT](https://www.mysqltutorial.org/mysql-string-functions/mysql-right-function/)                     | Get a specified number of rightmost characters from a string                             |
| [RTRIM](https://www.mysqltutorial.org/mysql-string-functions/mysql-rtrim-function/)                     | Remove all trailing spaces from a string                                                 |
| [SUBSTRING](https://www.mysqltutorial.org/mysql-substring.aspx)                                         | Extract a substring starting from a position with a specific length.                     |
| [SUBSTRING_INDEX](https://www.mysqltutorial.org/mysql-string-functions/mysql-substring_index-function/) | Return a substring from a string before a specified number of occurrences of a delimiter |
| [TRIM](https://www.mysqltutorial.org/mysql-trim/)                                                       | Remove unwanted characters from a string.                                                |
| [FIND_IN_SET](https://www.mysqltutorial.org/mysql-find_in_set/)                                         | Find a string within a comma-separated list of strings                                   |
| [FORMAT](https://www.mysqltutorial.org/mysql-format-function/)                                          | Format a number with a specific locale, rounded to the number of decimals                |
| [UPPER](https://www.mysqltutorial.org/mysql-string-functions/mysql-upper/)                              | Convert a string to uppercase                                                            |

**LEFT, RIGHT, and LENGTH**

You can use LEFT to pull a certain number of characters from the left side of a string and present them as a separate string. The syntax is LEFT(string, number of characters).

When using functions within other functions, it's important to remember that the innermost functions will be evaluated first, followed by the functions that encapsulate them.

**TRIM**

The TRIM function is used to remove characters from the beginning and end of a string.

The TRIM function takes 3 arguments. First, you have to specify whether you want to remove characters from the beginning ('leading'), the end ('trailing'), or both ('both', as used above). Next you must specify all characters to be trimmed. Any characters included in the single quotes will be removed from both beginning, end, or both sides of the string. Finally, you must specify the text you want to trim using FROM.

**POSITION**

POSITION allows you to specify a substring, then returns a numerical value equal to the character number (counting from left) where that substring first appears in the target string.

Importantly, POSITION function is case-sensitive. If you want to look for a character regardless of its case, you can make your entire string a single by using the UPPER or LOWER functions.

**SUBSTR**

LEFT and RIGHT both create substrings of a specified length, but they only do so starting from the sides of an existing string. If you want to start in the middle of a string, you can use SUBSTR. The syntax is SUBSTR(*string*, *starting character position*, *# of characters*):

**CONCAT**

You can combine strings from several columns together (and with hard-coded values) using CONCAT. Simply order the values you want to concatenate and separate them with commas. If you want to hard-code values, enclose them in single quotes.

**Changing case with UPPER and LOWER**

Sometimes, you just don't want your data to look like it's screaming at you. You can use LOWER to force every character in a string to become lower-case. Similarly, you can use UPPER to make all the letters appear in upper-case:

**Turning strings into dates**

Dates are some of the most commonly screwed-up formats in SQL. This can be the result of a few things:

- The data was manipulated in Excel at some point, and the dates were changed to MM/DD/YYYY format or another format that is not compliant with SQL's strict standards.
- The data was manually entered by someone who use whatever formatting convention he/she was most familiar with.
- The date uses text (Jan, Feb, etc.) instead of numbers to record months.

In order to take advantage of all of the great date functionality, you need to have your date field formatted appropriately. This often involves some text manipulation, followed by a CAST.

**Turning dates into more useful dates**

Once you've got a well-formatted date field, you can manipulate in all sorts of interesting ways.

What if you want to include today's date or time? You can instruct your query to pull the local date and time at the time the query is run using any number of functions. Interestingly, you can run them without a FROM clause:

**COALESCE**

Occasionally, you will end up with a dataset that has some nulls that you'd prefer to contain actual values. This happens frequently in numerical data (displaying nulls as 0 is often preferable), and when performing outer joins that result in some unmatched rows. In cases like this, you can use COALESCE to replace the null values:

### Subqueries

Subqueries (also known as inner queries or nested queries) are a tool for performing operations in multiple steps. For example, if you wanted to take the sums of several columns, then average all of those values, you'd need to do each aggregation in a distinct step.

Subqueries can be used in several places within a query, but it's easiest to start with the FROM statement.

Subqueries are required to have names, which are added after parentheses the same way you would add an alias to a normal table.

A quick note on formatting: The important thing to remember when using subqueries is to provide some way for the reader to easily determine which parts of the query will be executed together. Most people do this by indenting the subquery in some way.

### Window Functions

| Name                                                                                           | Description                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [CUME_DIST](https://www.mysqltutorial.org/mysql-window-functions/mysql-cume_dist-function/)       | Calculates the cumulative distribution of a value in a set of values.                                                                                                                                                                            |
| [DENSE_RANK](https://www.mysqltutorial.org/mysql-window-functions/mysql-dense_rank-function/)     | Assigns a rank to every row within its partition based on the `ORDER BY` clause. It assigns the same rank to the rows with equal values. If two or more rows have the same rank, then there will be no gaps in the sequence of ranked values. |
| [FIRST_VALUE](https://www.mysqltutorial.org/mysql-window-functions/mysql-first_value-function/)   | Returns the value of the specified expression with respect to the first row in the window frame.                                                                                                                                                 |
| [LAG](https://www.mysqltutorial.org/mysql-window-functions/mysql-lag-function/)                   | Returns the value of the Nth row before the current row in a partition. It returns NULL if no preceding row exists.                                                                                                                             |
| [LAST_VALUE](https://www.mysqltutorial.org/mysql-window-functions/mysql-last_value-function/)     | Returns the value of the specified expression with respect to the last row in the window frame.                                                                                                                                                  |
| [LEAD](https://www.mysqltutorial.org/mysql-window-functions/mysql-lead-function/)                 | Returns the value of the Nth row after the current row in a partition. It returns NULL if no subsequent row exists.                                                                                                                             |
| [NTH_VALUE](https://www.mysqltutorial.org/mysql-window-functions/mysql-nth_value-function/)       | Returns value of argument from Nth row of the window frame                                                                                                                                                                                       |
| [NTILE](https://www.mysqltutorial.org/mysql-window-functions/mysql-ntile-function/)               | Distributes the rows for each window partition into a specified number of ranked groups.                                                                                                                                                         |
| [PERCENT_RANK](https://www.mysqltutorial.org/mysql-window-functions/mysql-percent_rank-function/) | Calculates the percentile rank of a row in a partition or result set                                                                                                                                                                             |
| [RANK](https://www.mysqltutorial.org/mysql-window-functions/mysql-rank-function/)                 | Similar to the `DENSE_RANK()` function except that there are gaps in the sequence of ranked values when two or more rows have the same rank.                                                                                                  |
| [ROW_NUMBER](https://www.mysqltutorial.org/mysql-window-functions/mysql-row_number-function/)     | Assigns a sequential integer to every row within its partition                                                                                                                                                                                   |

A window function performs a calculation across a set of table rows that are somehow related to the current row. This is comparable to the type of calculation that can be done with an aggregate function. But unlike regular aggregate functions, use of a window function does not cause rows to become grouped into a single output row — the rows retain their separate identities. Behind the scenes, the window function is able to access more than just the current row of the query result.

If you'd like to narrow the window from the entire dataset to individual groups within the dataset, you can use PARTITION BY to do so.

Note: You can't use window functions and standard aggregations in the same query. More specifically, you can't include window functions in a GROUP BY clause.

**The usual suspects: SUM, COUNT, and AVG**

When using window functions, you can apply the same aggregates that you would under normal circumstances—SUM, COUNT, and AVG.

**ROW_NUMBER()**

ROW_NUMBER() does just what it sounds like—displays the number of a given row. It starts with 1 and numbers the rows according to the ORDER BY part of the window statement. ROW_NUMBER() does not require you to specify a variable within the parentheses.

Using the PARTITION BY clause will allow you to begin counting 1 again in each partition. The following query starts the count over again for each terminal:

**RANK() and DENSE_RANK()**

RANK() is slightly different from ROW_NUMBER().

You can also use DENSE_RANK() instead of RANK() depending on your application. Imagine a situation in which three entries have the same value. Using either command, they will all get the same rank.

**NTILE**

You can use window functions to identify what percentile (or quartile, or any other subdivision) a given row falls into. The syntax is NTILE(*# of buckets*). In this case, ORDER BY determines which column to use to determine the quartiles (or whatever number of 'tiles you specify). For example:

**LAG and LEAD**

It can often be useful to compare rows to preceding or following rows, especially if you've got the data in an order that makes sense. You can use LAG or LEAD to create columns that pull values from other rows—all you need to do is enter which column to pull from and how many rows away you'd like to do the pull. LAG pulls from previous rows and LEAD pulls from following rows.

This is especially useful if you want to calculate differences between rows.

**Defining a window alias**

If you're planning to write several window functions in to the same query, using the same window, you can create an alias.

The WINDOW clause, if included, should always come after the WHERE clause.

### CTE (Common Table Expressions)

A common table expression is a named temporary result set that exists only within the execution scope of a single SQL statement e.g.,[`SELECT`](https://www.mysqltutorial.org/mysql-select-statement-query-data.aspx), [`INSERT`](https://www.mysqltutorial.org/mysql-insert-statement.aspx), [`UPDATE`](https://www.mysqltutorial.org/mysql-update-data.aspx), or [`DELETE`](https://www.mysqltutorial.org/mysql-delete-statement.aspx).

Similar to a [derived table](https://www.mysqltutorial.org/mysql-derived-table/), a CTE is not stored as an object and last only during the execution of a query. A Common Table Expression (CTE) is the result set of a query which exists temporarily and for use only within the context of a larger query. Much like a derived table, the result of a CTE is not stored and exists only for the duration of the query.

CTEs, like database views and derived tables, enable users to more easily write and maintain complex queries via increased readability and simplification. This reduction in complexity is achieved by deconstructing ordinarily complex queries into simple blocks to be used, and reused if necessary, in rewriting the query. Example use cases include:

- Needing to reference a derived table multiple times in a single query
- An alternative to creating a view in the database
- Performing the same calculation multiple times over across multiple query components

Unlike a derived table, a CTE can be self-referencing (a [recursive CTE](https://www.mysqltutorial.org/mysql-recursive-cte/)) or can be referenced multiple times in the same query. In addition, a CTE provides better readability and performance in comparison with a derived table.

The structure of a CTE includes the name, an optional column list, and a query that defines the CTE. After the CTE is defined, you can use it as a view in a `SELECT`, `INSERT`, `UPDATE`, `DELETE`, or `CREATE VIEW` statement.

The following illustrates the basic syntax of a CTE:

```sql
WITH cte_name (column_list) AS (
    query
) 
SELECT * FROM cte_name;
```

### Indexes

A database index is a data structure that improves the speed of operations in a table. Indexes can be created using one or more columns, providing the basis for both rapid random lookups and efficient ordering of access to records.

While creating index, it should be taken into consideration which all columns will be used to make SQL queries and create one or more indexes on those columns.

Practically, indexes are also a type of tables, which keep primary key or index field and a pointer to each record into the actual table.

The users cannot see the indexes, they are just used to speed up queries and will be used by the Database Search Engine to locate records very fast.

The INSERT and UPDATE statements take more time on tables having indexes, whereas the SELECT statements become fast on those tables. The reason is that while doing insert or update, a database needs to insert or update the index values as well.

### Performance Tuning

SQL tuning is the process of improving SQL queries to accelerate your servers performance. It's general purpose is to reduce the amount of time it takes a user to receive a result after issuing a query, and to reduce the amount of resources used to process a query.

A database is a piece of software that runs on a computer, and is subject to the same limitations as all software---it can only process as much information as its hardware is capable of handling. The way to make a query run faster is to reduce the number of calculations that the software (and therefore hardware) must perform. To do this, you'll need some understanding of how SQL actually makes calculations. First, let's address some of the high-level things that will affect the number of calculations you need to make, and therefore your querys runtime:

- Table size: If your query hits one or more tables with millions of rows or more, it could affect performance.
- Joins: If your query joins two tables in a way that substantially increases the row count of the result set, your query is likely to be slow.
- Aggregations: Combining multiple rows to produce a result requires more computation than simply retrieving those rows.

Query runtime is also dependent on some things that you can't really control related to the database itself:

- Other users running queries: The more queries running concurrently on a database, the more the database must process at a given time and the slower everything will run. It can be especially bad if others are running particularly resource-intensive queries that fulfill some of the above criteria.
- Database software and optimization: This is something you probably can't control, but if you know the system you're using, you can work within its bounds to make your queries more efficient.

**Reducing table size**

Filtering the data to include only the observations you need can dramatically improve query speed. How you do this will depend entirely on the problem you're trying to solve. For example, if you've got time series data, limiting to a small time window can make your queries run much more quickly:

```sql
SELECT *
  FROM sample_event_table
 WHERE event_date >= '2014-03-01'
   AND event_date <  '2014-04-01'
```

Keep in mind that you can always perform exploratory analysis on a subset of data, refine your work into a final query, then remove the limitation and run your work across the entire dataset. The final query might take a long time to run, but at least you can run the intermediate steps quickly.

This is why we enforces a LIMIT clause by default—100 rows is often more than you need to determine the next step in your analysis, and it's a small enough dataset that it will return quickly.

It's worth noting that LIMIT doesn't quite work the same way with aggregations—the aggregation is performed, then the results are limited to the specified number of rows. So if you're aggregating into one row as below, LIMIT 100 will do nothing to speed up your query:

```sql
SELECT COUNT(*)
  FROM sample_event_table
 LIMIT 100
```

If you want to limit the dataset before performing the count (to speed things up), try doing it in a subquery:

```sql
SELECT COUNT(*)
  FROM (
    SELECT *
      FROM sample_event_table
     LIMIT 100
       ) sub
```

Note: Using LIMIT this will dramatically alter your results, so you should use it to test query logic, but not to get actual results.

In general, when working with subqueries, you should make sure to limit the amount of data you're working with in the place where it will be executed first. This means putting the LIMIT in the subquery, not the outer query. Again, this is for making the query run fast so that you can test—NOT for producing good results.

**EXPLAIN**

You can add EXPLAIN at the beginning of any (working) query to get a sense of how long it will take. It's not perfectly accurate, but it's a useful tool.

**Use Column Names Instead of * in a SELECT Statement**

If you are selecting only a few columns from a table there is no need to use SELECT *. Though this is easier to write, it will cost more time for the database to complete the query. By selecting only the columns you need, you are reducing the size of the result table, reducing the network traffic and also in turn boosting the overall performance of the query.

**Example:**

Original query:

```sql
SELECT * FROM SH.sales
```

Improved query:

```sql
SELECT s.prod_id FROM SH.sales s
```

**Avoid including a HAVING clause in SELECT statements**

The HAVING clause is used to filter the rows after all the rows are selected and it is used like a filter. It is quite useless in a SELECT statement. It works by going through the final result table of the query parsing out the rows that don’t meet the HAVING condition.

Example:

Original query:

```sql
SELECT s.cust_id, count(s.cust_id) FROM SH.sales s GROUP BY s.cust_id HAVING s.cust_id != '1660' AND s.cust_id != '2'
```

Improved query:

```sql
SELECT s.cust_id,count(cust_id) FROM SH.sales s WHERE s.cust_id != '1660' AND s.cust_id !='2' GROUP BY s.cust_id
```

**Eliminate Unnecessary DISTINCT Conditions**

Considering the case of the following example, the DISTINCT keyword in the original query is unnecessary because the table_name contains the primary key p.ID, which is part of the result set.

**Example:**

Original query:

```sql
SELECT DISTINCT * FROM SH.sales s JOIN SH.customers c ON s.cust_id= c.cust_id WHERE c.cust_marital_status = 'single'
```

Improved query:

```sql
SELECT * FROM SH.sales s JOIN SH.customers c ON s.cust_id = c.cust_id WHERE c.cust_marital_status='single'
```

**Un-nest sub queries**

Rewriting nested queries as joins often leads to more efficient execution and more effective optimization. In general, sub-query un-nesting is always done for correlated sub-queries with, at most, one table in the FROM clause, which are used in ANY, ALL, and EXISTS predicates. A uncorrelated sub-query, or a sub-query with more than one table in the FROM clause, is flattened if it can be decided, based on the query semantics, that the sub-query returns at most one row.

**Example:**

Original query:

```sql
SELECT * FROM SH.products p WHERE p.prod_id = (SELECT s.prod_id FROM SH.sales s WHERE s.cust_id = 100996 AND s.quantity_sold = 1)
```

Improved query:

```sql
SELECT p.* FROM SH.products p, sales s WHERE p.prod_id = s.prod_id AND s.cust_id = 100996 AND s.quantity_sold = 1
```

**Consider using an IN predicate when querying an indexed column**

The IN-list predicate can be exploited for indexed retrieval and also, the optimizer can sort the IN-list to match the sort sequence of the index, leading to more efficient retrieval. Note that the IN-list must contain only constants, or values that are constant during one execution of the query block, such as outer references.

**Example:**

Original query:

```sql
SELECT s.* FROM SH.sales s WHERE s.prod_id = 14 OR s.prod_id = 17
```

Improved query:

```sql
SELECT s.* FROM SH.sales s WHERE s.prod_id IN (14, 17)
```

**Use EXISTS instead of DISTINCT when using table joins that involves tables having one-to-many relationships**

The DISTINCT keyword works by selecting all the columns in the table then parses out any duplicates.Instead, if you use sub query with the EXISTS keyword, you can avoid having to return an entire table.

**Example:**

Original query:

```sql
SELECT DISTINCT c.country_id, c.country_name FROM SH.countries c,SH.customers e WHERE e.country_id = c.country_id
```

Improved query:

```sql
SELECT c.country_id, c.country_name FROM SH.countries c WHERE EXISTS (SELECT 'X' FROM SH.customers e WHERE e.country_id = c.country_id)
```

**Try to use UNION ALL in place of UNION**

The UNION ALL statement is faster than UNION, because UNION ALL statement does not consider duplicate s, and UNION statement does look for duplicates in a table while selection of rows, whether or not they exist.

**Example:**

Original query:

```sql
SELECT cust_id FROM SH.sales UNION SELECT cust_id FROM customers
```

Improved query:

```sql
SELECT cust_id FROM SH.sales UNION ALL SELECT cust_id FROM customers
```

**Avoid using OR in join conditions**

Any time you place an ‘OR’ in the join condition, the query will slow down by at least a factor of two.

**Example:**

Original query:

```sql
SELECT * 
FROM SH.costs c 
INNER JOIN SH.products p 
ON c.unit_price = p.prod_min_price OR c.unit_price = p.prod_list_price
```

Improved query:

```sql
SELECT * 
FROM SH.costs c 
INNER JOIN SH.products p 
ON c.unit_price = p.prod_min_price 
UNION ALL 
SELECT * 
FROM SH.costs c 
INNER JOIN SH.products p 
ON c.unit_price = p.prod_list_price
```

**Avoid functions on the right hand side of the operator**

Functions or methods are used very often with their SQL queries. Rewriting the query by removing aggregate functions will increase the performance tremendously.

**Example:**

Original query:

```sql
SELECT * 
FROM SH.sales 
WHERE EXTRACT (YEAR FROM TO_DATE (time_id, ‘DDMON-RR’)) = 2001 AND EXTRACT (MONTH FROM TO_DATE (time_id, ‘DD-MON-RR’)) = 12
```

Improved query:

```sql
SELECT * 
FROM SH.sales 
WHERE TRUNC (time_id) BETWEEN TRUNC(TO_DATE(‘12/01/2001’, ’mm/dd/yyyy’)) AND TRUNC (TO_DATE (‘12/30/2001’,’mm/dd/yyyy’))
```

**Remove any redundant mathematics**

There will be times where you will be performing mathematics within an SQL statement. They can be a drag on the performance if written improperly. For each time the query finds a row it will recalculate the math. So eliminating any unnecessary math in the statement will make it perform faster.

**Example:**

Original query:

```sql
SELECT * FROM SH.sales s WHERE s.cust_id + 10000 < 35000
```

Improved query:

```sql
SELECT * FROM SH.sales s WHERE s.cust_id < 25000
```

**Some of the most Query Optimizations techniques are —**

1. **Use indexes:** Indexes can greatly improve the performance of your queries by allowing the database to quickly locate the data it needs.
2. **Limit the number of rows returned:** Use the "LIMIT" clause to limit the number of rows returned by a query. This can improve performance and reduce memory usage.
3. **Use the right join type:** Use the appropriate join type (e.g. inner join, left join, right join) based on the specific needs of your query.
4. **Use subqueries wisely:** Subqueries can be useful, but they can also slow down a query if used excessively. Use subqueries sparingly and make sure they are optimized.
5. **Avoid using "SELECT"**: Instead of using "SELECT", specify the specific columns you need in your query. This can improve performance and reduce memory usage.
6. **Avoid using functions on indexed columns:** Avoid using functions on indexed columns in the WHERE clause.
7. **Use Temporary table:** Use temporary tables to store intermediate results and then join them with other tables.
8. **Use Explain plan:** Use the "EXPLAIN PLAN" statement to analyze the execution plan of a query and identify any potential performance bottlenecks.
9. **Use Partitioning:** Use partitioning to divide large tables into smaller, more manageable pieces.
10. **Use caching:** Use caching to store the results of frequently-run queries in memory, so they can be retrieved quickly without the need to re-run the query.

### Stored Procedures

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

### Cursor

To handle a result set inside a [stored procedure](https://www.mysqltutorial.org/mysql-stored-procedure-tutorial.aspx "MySQL Stored Procedure"), you use a cursor. A cursor allows you to [iterate ](https://www.mysqltutorial.org/stored-procedures-loop.aspx "How to use loop in stored procedure")a set of rows returned by a query and process each row individually.

MySQL cursor is read-only, non-scrollable and asensitive.

- Read-only: you cannot update data in the underlying table through the cursor.
- Non-scrollable: you can only fetch rows in the order determined by the [SELECT](https://www.mysqltutorial.org/mysql-select-statement-query-data.aspx) statement. You cannot fetch rows in the reversed order. In addition, you cannot skip rows or jump to a specific row in the result set.
- Asensitive: there are two kinds of cursors: asensitive cursor and insensitive cursor. An asensitive cursor points to the actual data, whereas an insensitive cursor uses a temporary copy of the data. An asensitive cursor performs faster than an insensitive cursor because it does not have to make a temporary copy of data. However, any change that made to the data from other connections will affect the data that is being used by an asensitive cursor, therefore, it is safer if you do not update the data that is being used by an asensitive cursor. MySQL cursor is asensitive.

You can use MySQL cursors in [stored procedures](https://www.mysqltutorial.org/getting-started-with-mysql-stored-procedures.aspx), [stored functions](https://www.mysqltutorial.org/mysql-stored-function/), and [triggers](https://www.mysqltutorial.org/mysql-triggers.aspx "MySQL Triggers").

First, declare a cursor by using the `DECLARE` statement:

```sql
DECLARE cursor_name CURSOR FOR SELECT_statement;
```

The cursor declaration must be after any [variable ](https://www.mysqltutorial.org/variables-in-stored-procedures.aspx "MySQL Variables in Stored Procedures")declaration. If you declare a cursor before the variable declarations, MySQL will issue an error. A cursor must always associate with a `SELECT` statement.

Next, open the cursor by using the `OPEN` statement. The `OPEN` statement initializes the result set for the cursor, therefore, you must call the `OPEN` statement before fetching rows from the result set.

```sql
OPEN cursor_name;
```

Then, use the `FETCH` statement to retrieve the next row pointed by the cursor and move the cursor to the next row in the result set.

```sql
FETCH cursor_name INTO variables list;
```

After that, check if there is any row available before fetching it.

Finally, deactivate the cursor and release the memory associated with it  using the `CLOSE` statement:

```sql
CLOSE cursor_name;
```

It is a good practice to always close a cursor when it is no longer used.

When working with MySQL cursor, you must also declare a `NOT FOUND` handler to handle the situation when the cursor could not find any row.

Because each time you call the `FETCH` statement, the cursor attempts to read the next row in the result set. When the cursor reaches the end of the result set, it will not be able to get the data, and a condition is raised. The handler is used to handle this condition.

To declare a `NOT FOUND` handler, you use the following syntax:

```sql

DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = 1;
```

The `finished` is a variable to indicate that the cursor has reached the end of the result set. Notice that the handler declaration must appear after variable and cursor declaration inside the stored procedures.

The following diagram illustrates how MySQL cursor works:

![mysql-cursor](https://user-images.githubusercontent.com/62965911/222632160-ccbd8671-684e-4176-8273-5baab4d4eed3.png)

### Triggers

In MySQL, a trigger is a stored program invoked automatically in response to an event such as [insert](https://www.mysqltutorial.org/mysql-insert-statement.aspx), [update](https://www.mysqltutorial.org/mysql-update-data.aspx), or [delete](https://www.mysqltutorial.org/mysql-delete-statement.aspx) that occurs in the associated table. For example, you can define a trigger that is invoked automatically before a new row is inserted into a table.

MySQL supports triggers that are invoked in response to the [INSERT](https://www.mysqltutorial.org/mysql-insert-statement.aspx), [UPDATE](https://www.mysqltutorial.org/mysql-update-data.aspx) or [DELETE](https://www.mysqltutorial.org/mysql-delete-statement.aspx) event.

The SQL standard defines two types of triggers: row-level triggers and statement-level triggers.

- A row-level trigger is activated for each row that is inserted, updated, or deleted.  For example, if a table has 100 rows inserted, updated, or deleted, the trigger is automatically invoked 100 times for the 100 rows affected.
- A statement-level trigger is executed once for each transaction regardless of how many rows are inserted, updated, or deleted.

**Advantages of triggers**

- Triggers provide another way to check the integrity of data.
- Triggers handle errors from the database layer.
- Triggers give an alternative way to [run scheduled tasks](https://www.mysqltutorial.org/mysql-triggers/working-mysql-scheduled-event/). By using triggers, you don't have to wait for the [scheduled events](https://www.mysqltutorial.org/mysql-triggers/working-mysql-scheduled-event/) to run because the triggers are invoked automatically *before* or *after* a change is made to the data in a table.
- Triggers can be useful for auditing the data changes in tables.

**Disadvantages of triggers**

- Triggers can only provide extended validations, not all validations. For simple validations, you can use the [NOT NULL](https://www.mysqltutorial.org/mysql-not-null-constraint/), [UNIQUE](https://www.mysqltutorial.org/mysql-unique-constraint/), [CHECK](https://www.mysqltutorial.org/mysql-check-constraint/) and [FOREIGN KEY](https://www.mysqltutorial.org/mysql-foreign-key/) constraints.
- Triggers can be difficult to troubleshoot because they execute automatically in the database, which may not invisible to the client applications.
- Triggers may increase the overhead of the MySQL Server.

## SQL vs. NoSQL

**SQL**

- Ensure ACID compliance.
  - Reduce anomalies.
  - Protect database integrity.
- Data is structured and unchanging.

**NoSQL**

- Data has little or no structure.
- Make the most of cloud computing and storage.
  - Cloud-based storage requires data to be easily spread across multiple servers to scale up.
- Rapid development.
  - Frequent updates to the data structure.

### Storage

- SQL: store data in tables.
- NoSQL: have different data storage models.

### Schema

- SQL
  - Each record conforms to a fixed schema.
  - Schema can be altered, but it requires modifying the whole database.
- NoSQL:
  - Schemas are dynamic.

### Querying

- SQL
  - Use SQL (structured query language) for defining and manipulating the data.
- NoSQL
  - Queries are focused on a collection of documents.
  - UnQL (unstructured query language).
  - Different databases have different syntax.

### Scalability

- SQL
  - Vertically scalable (by increasing the horsepower: memory, CPU, etc) and expensive.
  - Horizontally scalable (across multiple servers); but it can be challenging and time-consuming.
- NoSQL
  - Horizontablly scalable (by adding more servers) and cheap.

### ACID

- Atomicity, consistency, isolation, durability
- SQL
  - ACID compliant
  - Data reliability
  - Gurantee of transactions
- NoSQL
  - Most sacrifice ACID compliance for performance and scalability.

### Common types of NoSQL

#### Key-value stores

- Array of key-value pairs. The "key" is an attribute name.
- Redis, Vodemort, Dynamo.

#### Document databases

- Data is stored in documents.
- Documents are grouped in collections.
- Each document can have an entirely different structure.
- CouchDB, MongoDB.

#### Wide-column / columnar databases

- Column families - containers for rows.
- No need to know all the columns up front.
- Each row can have different number of columns.
- Cassandra, HBase.

#### Graph database

- Data is stored in graph structures
  - Nodes: entities
  - Properties: information about the entities
  - Lines: connections between the entities
- Neo4J, InfiniteGraph

## Labs

1. [Ingest data from CSV file into MySQL database table](01-foundations/language/sql/lab-mysql-data-ingestion/)
2. [SQL Basics to Advanced Primer](01-foundations/language/sql/lab-basic-to-advanced/)
   1. SQL Basics - Select, Limit, Where, Comparison and Logical operators, Order by
   2. SQL Intermediate - Aggregations, Group by, Case statements, Joins
   3. SQL Advanced - Dates, Text, Subqueries, Window functions, Optimizations
3. [Postgres SQL basics to advanced](01-foundations/language/sql/lab-postgres-queries/)
4. [Running Dates, String and Advanced queries in Postgres on Sales data](01-foundations/language/sql/lab-postgres-sales/)
5. [Working with Book dataset on SQLite database](01-foundations/language/sql/lab-sqlite-basics/)
6. [Challenge - Yammer Advanced Analytics](01-foundations/language/sql/challenges/yammer/)
7. [Challenge - BrainTree SQL Code Challenge](01-foundations/language/sql/challenges/braintree/)

## SQL Interview Questions

[Click here](01-foundations/language/sql/sql-interviews-questions.md)

## Resources

1. [SQL Cheat Sheet](https://www.interviewbit.com/sql-cheat-sheet/)
2. [What I realized after solving 100 leetcode SQL questions](https://towardsdatascience.com/sql-questions-summary-df90bfe4c9c)
3. [LeetCode SQL Problem Solving Questions With Solutions](https://www.dsfaisal.com/articles/sql/leetcode-sql-problem-solving)
4. [HackerRank SQL Problem Solving Questions With Solutions](https://www.dsfaisal.com/articles/sql/hackerrank-sql-problem-solving#1-revising-the-select-query-i--easy--hackerrank)
5. [SQL Interview Questions](https://knowledgetree.notion.site/SQL-Interview-Questions-04a1196192a24eb2848e8454af1bd9c7)
6. [Data Engineer Interview Questions](https://www.stratascratch.com/blog/data-engineer-interview-questions/)
7. [10 SQL Queries You Should Know as a Data Engineer](https://knowledgetree.notion.site/10-SQL-Queries-You-Should-Know-as-a-Data-Engineer-4e157d42c4ce4ae08050e99f3b33b82b)
8. [SQL JOIN Interview Questions](https://www.stratascratch.com/blog/sql-join-interview-questions/)
9. [The Ultimate Guide to SQL Window Functions](https://www.stratascratch.com/blog/the-ultimate-guide-to-sql-window-functions/)

## Database Questions

1. [https://leetcode.com/problems/combine-two-tables/](https://leetcode.com/problems/combine-two-tables/)
2. [https://leetcode.com/problems/employees-earning-more-than-their-managers/](https://leetcode.com/problems/employees-earning-more-than-their-managers/)
3. [https://leetcode.com/problems/duplicate-emails/](https://leetcode.com/problems/duplicate-emails/)
4. [https://leetcode.com/problems/customers-who-never-order/](https://leetcode.com/problems/customers-who-never-order/)
5. [https://leetcode.com/problems/delete-duplicate-emails/](https://leetcode.com/problems/delete-duplicate-emails/)
6. [https://leetcode.com/problems/rising-temperature/](https://leetcode.com/problems/rising-temperature/)
7. [https://leetcode.com/problems/find-customer-referee/](https://leetcode.com/problems/find-customer-referee/)
8. [https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/](https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/)
9. [https://leetcode.com/problems/classes-more-than-5-students/](https://leetcode.com/problems/classes-more-than-5-students/)
10. [https://leetcode.com/problems/big-countries/](https://leetcode.com/problems/big-countries/)
11. [https://leetcode.com/problems/top-travellers/](https://leetcode.com/problems/top-travellers/)
12. [https://leetcode.com/problems/second-highest-salary/](https://leetcode.com/problems/second-highest-salary/)
13. [https://leetcode.com/problems/rank-scores/](https://leetcode.com/problems/rank-scores/)
14. [https://leetcode.com/problems/consecutive-numbers/](https://leetcode.com/problems/consecutive-numbers/)
15. [https://platform.stratascratch.com/coding/10164-total-adwords-earnings](https://platform.stratascratch.com/coding/10164-total-adwords-earnings)
16. [https://platform.stratascratch.com/coding/2107-primary-key-violation](https://platform.stratascratch.com/coding/2107-primary-key-violation)
17. [https://platform.stratascratch.com/coding/10308-salaries-differences](https://platform.stratascratch.com/coding/10308-salaries-differences)
18. [https://platform.stratascratch.com/coding/10172-best-selling-item](https://platform.stratascratch.com/coding/10172-best-selling-item)
19. [https://platform.stratascratch.com/coding/2117-employee-with-most-orders](https://platform.stratascratch.com/coding/2117-employee-with-most-orders)
20. [https://platform.stratascratch.com/technical/2354-common-table-expression](https://platform.stratascratch.com/technical/2354-common-table-expression)
21. [https://platform.stratascratch.com/technical/2084-delete-and-truncate](https://platform.stratascratch.com/technical/2084-delete-and-truncate)
22. [https://platform.stratascratch.com/technical/2074-linked-list-and-array](https://platform.stratascratch.com/technical/2074-linked-list-and-array)
23. [https://pgexercises.com/](https://pgexercises.com/)
24. [https://www.hackerrank.com/domains/sql](https://www.hackerrank.com/domains/sql)
25. [https://www.hackerrank.com/domains/databases](https://www.hackerrank.com/domains/databases)

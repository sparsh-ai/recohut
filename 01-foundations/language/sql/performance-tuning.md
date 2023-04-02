
# Performance Tuning

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

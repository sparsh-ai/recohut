# SQL

## Concepts

1. <a href="#/01-foundations/language/sql/window-functions.md" target="_blank">Window Functions</a>
1. <a href="#/01-foundations/language/sql/sql-basics.md" target="_blank">SQL Basics</a>
1. <a href="#/01-foundations/language/sql/sql-query.md" target="_blank">SQL Query</a>
1. <a href="#/01-foundations/language/sql/views.md" target="_blank">Views</a>
1. <a href="#/01-foundations/language/sql/stored-procedures.md" target="_blank">Stored Procedures</a>
1. <a href="#/01-foundations/language/sql/triggers.md" target="_blank">Triggers</a>
1. <a href="#/01-foundations/language/sql/indexes.md" target="_blank">Indexes</a>
1. <a href="#/01-foundations/language/sql/comparison-operators.md" target="_blank">Comparison Operators</a>
1. <a href="#/01-foundations/language/sql/logical-operators.md" target="_blank">Logical Operators</a>
1. <a href="#/01-foundations/language/sql/aggregate-functions.md" target="_blank">Aggregate Functions</a>
1. <a href="#/01-foundations/language/sql/string-functions.md" target="_blank">String Functions</a>
1. <a href="#/01-foundations/language/sql/joins.md" target="_blank">Joins</a>
1. <a href="#/01-foundations/language/sql/comments.md" target="_blank">Comments</a>
1. <a href="#/01-foundations/language/sql/select.md" target="_blank">SELECT</a>
1. <a href="#/01-foundations/language/sql/limit.md" target="_blank">LIMIT</a>
1. <a href="#/01-foundations/language/sql/where.md" target="_blank">WHERE</a>
1. <a href="#/01-foundations/language/sql/like.md" target="_blank">LIKE</a>
1. <a href="#/01-foundations/language/sql/in.md" target="_blank">IN</a>
1. <a href="#/01-foundations/language/sql/between.md" target="_blank">BETWEEN</a>
1. <a href="#/01-foundations/language/sql/isnull.md" target="_blank">IS NULL</a>
1. <a href="#/01-foundations/language/sql/and.md" target="_blank">AND</a>
1. <a href="#/01-foundations/language/sql/or.md" target="_blank">OR</a>
1. <a href="#/01-foundations/language/sql/not.md" target="_blank">NOT</a>
1. <a href="#/01-foundations/language/sql/like.md" target="_blank">LIKE</a>
1. <a href="#/01-foundations/language/sql/like.md" target="_blank">LIKE</a>
1. <a href="#/01-foundations/language/sql/orderby.md" target="_blank">ORDER BY</a>
1. <a href="#/01-foundations/language/sql/groupby.md" target="_blank">GROUP BY</a>
1. <a href="#/01-foundations/language/sql/cursor.md" target="_blank">Cursor</a>
1. <a href="#/01-foundations/language/sql/performance-tuning.md" target="_blank">Performance Tuning</a>
1. <a href="#/01-foundations/language/sql/date-functions.md" target="_blank">Date Functions</a>

### SQL HAVING

You'll often encounter datasets where GROUP BY isn't enough to get what you're looking for. Let's say that it's not enough just to know aggregated stats by month. After all, there are a lot of months in this dataset. Instead, you might want to find every month during which AAPL stock worked its way over $400/share. The WHERE clause won't work for this because it doesn't allow you to filter on aggregate columns—that's where the HAVING clause comes in.

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

### SQL UNION

SQL joins allow you to combine two datasets side-by-side, but UNION allows you to stack one dataset on top of the other. Put differently, UNION allows you to write two separate SELECT statements, and to have the results of one statement display in the same table as the results from the other statement.

SQL has strict rules for appending data:

- Both tables must have the same number of columns
- The columns must have the same data types in the same order as the first table

While the column names don't necessarily have to be the same, you will find that they typically are. This is because most of the instances in which you'd want to use UNION involve stitching together different parts of the same dataset.

### Subqueries

Subqueries (also known as inner queries or nested queries) are a tool for performing operations in multiple steps. For example, if you wanted to take the sums of several columns, then average all of those values, you'd need to do each aggregation in a distinct step.

Subqueries can be used in several places within a query, but it's easiest to start with the FROM statement.

Subqueries are required to have names, which are added after parentheses the same way you would add an alias to a normal table.

A quick note on formatting: The important thing to remember when using subqueries is to provide some way for the reader to easily determine which parts of the query will be executed together. Most people do this by indenting the subquery in some way.

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

## Challenge - Employee Analytics

Small dataset | 6 Questions

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/01-foundations/language/sql/lab-employee/main.ipynb)
[![Google Colab](https://img.shields.io/static/v1?style=for-the-badge&message=Google+Colab&color=222222&logo=Google+Colab&logoColor=F9AB00&label=)](https://colab.research.google.com/github/sparsh-ai/recohut/blob/main/tree/main/01-foundations/language/sql/lab-employee/main.ipynb)

## Explore Further

1. [SQL Interview Questions](01-foundations/language/sql/sql-interviews-questions.md)
2. [SQL Cheat Sheet](https://www.interviewbit.com/sql-cheat-sheet/)
3. [What I realized after solving 100 leetcode SQL questions](https://towardsdatascience.com/sql-questions-summary-df90bfe4c9c)
4. [LeetCode SQL Problem Solving Questions With Solutions](https://www.dsfaisal.com/articles/sql/leetcode-sql-problem-solving)
5. [HackerRank SQL Problem Solving Questions With Solutions](https://www.dsfaisal.com/articles/sql/hackerrank-sql-problem-solving#1-revising-the-select-query-i--easy--hackerrank)
6. [SQL Interview Questions](https://knowledgetree.notion.site/SQL-Interview-Questions-04a1196192a24eb2848e8454af1bd9c7)
7. [Data Engineer Interview Questions](https://www.stratascratch.com/blog/data-engineer-interview-questions/)
8. [10 SQL Queries You Should Know as a Data Engineer](https://knowledgetree.notion.site/10-SQL-Queries-You-Should-Know-as-a-Data-Engineer-4e157d42c4ce4ae08050e99f3b33b82b)
9. [SQL JOIN Interview Questions](https://www.stratascratch.com/blog/sql-join-interview-questions/)

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

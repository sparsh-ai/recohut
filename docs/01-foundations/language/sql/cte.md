# CTE (Common Table Expressions)

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
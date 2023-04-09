# SQL Query

## Execution path of a query

![](https://user-images.githubusercontent.com/62965911/226103358-b131be3c-09e7-44a3-8582-a2f2c9084cb3.png)

## Query breakdown

| Statement | How to Use It               | Other Details                                         |
|-----------|-----------------------------|-------------------------------------------------------|
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

## Query clause order

The order in which you write the clauses is important. Here's the order for everything you've learned so far:

1. SELECT
2. FROM
3. WHERE
4. GROUP BY
5. HAVING
6. ORDER BY
7. LIMIT
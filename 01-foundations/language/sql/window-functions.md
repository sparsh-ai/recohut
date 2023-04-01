# Window Functions

There is no official categorisation of Window Functions but based on the usage, we can briefly categorise them in 3 ways:

![1_nf6iu-Jt4XBLefa6Jv6kMQ](https://user-images.githubusercontent.com/62965911/229128540-ad1ebf04-9b0b-490a-ad9a-cd1ec2dfb7a4.png)

- **Aggregate Functions** \- Regular Aggregate Function can be used as a Window Function to calculate aggregations for numeric columns within window partitions such as running total sales, minimum or maximum value within partition etc.
- **Ranking Functions** \- These functions return a ranking value for each row in a partition.
- **Value Functions** \- These functions are useful for generating simple statistics or time series analysis.

If we need to figure out MIN and MAX values of MSRP for each PRODUCTLINE, then how will the result sets differ for both GROUP BY and PARTITION BY clause:

![1_a3yi8-K7JhgXrKNZVAe0dA](https://user-images.githubusercontent.com/62965911/229129245-e5b2384f-218f-4c00-9dc7-794934d82f27.png)

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

## Cheat Sheet

![Window_Functions_Cheat_Sheet_A3 (1)](https://user-images.githubusercontent.com/62965911/229131678-80b65039-4b10-4fd7-9fcc-34dc59528c8c.jpg)

[Click here](https://learnsql.com/blog/sql-window-functions-cheat-sheet/Window_Functions_Cheat_Sheet_A3.pdf) for PDF version

## References

1. [The Ultimate Guide to SQL Window Functions](https://www.stratascratch.com/blog/the-ultimate-guide-to-sql-window-functions/)
1. https://learnsql.com/blog/sql-window-functions-cheat-sheet/
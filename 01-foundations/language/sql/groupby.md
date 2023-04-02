# SQL GROUP BY

SQL aggregate function like COUNT, AVG, and SUM have something in common: they all aggregate across the entire table. But what if you want to aggregate only part of a table? For example, you might want to count the number of entries for each year.

In situations like this, you'd need to use the GROUP BY clause. GROUP BY allows you to separate data into groups, which can be aggregated independently of one another.

You can group by multiple columns, but you have to separate column names with commas—just as with ORDER BY).

As with ORDER BY, you can substitute numbers for column names in the GROUP BY clause. It's generally recommended to do this only when you're grouping many columns, or if something else is causing the text in the GROUP BY clause to be excessively long.

The order of column names in your GROUP BY clause doesn't matter—the results will be the same regardless. If you want to control how the aggregations are grouped together, use ORDER BY.
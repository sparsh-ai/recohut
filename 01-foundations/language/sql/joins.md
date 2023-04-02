# SQL Joins

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
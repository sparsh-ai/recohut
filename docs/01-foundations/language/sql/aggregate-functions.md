# SQL Aggregate Functions

| Aggregate function                                                  | Description                                                            |
|---------------------------------------------------------------------|------------------------------------------------------------------------|
| [AVG()](https://www.mysqltutorial.org/mysql-avg/)                   | Return the average of non-NULL values.                                 |
| BIT_AND()                                                           | Return bitwise AND.                                                    |
| BIT_OR()                                                            | Return bitwise OR.                                                     |
| BIT_XOR()                                                           | Return bitwise XOR.                                                    |
| [COUNT()](https://www.mysqltutorial.org/mysql-count/)               | Return the number of rows in a group, including rows with NULL values. |
| [GROUP_CONCAT()](https://www.mysqltutorial.org/mysql-group_concat/) | Return a concatenated string.                                          |
| JSON_ARRAYAGG()                                                     | Return result set as a single JSON array.                              |
| JSON_OBJECTAGG()                                                    | Return result set as a single JSON object.                             |
| [MAX()](https://www.mysqltutorial.org/mysql-max-function/)          | Return the highest value (maximum) in a set of non-NULL values.        |
| [MIN()](https://www.mysqltutorial.org/mysql-min/)                   | Return the lowest value (minimum) in a set of non-NULL values.         |
| [STDEV()](https://www.mysqltutorial.org/mysql-standard-deviation/)  | Return the population standard deviation.                              |
| STDDEV_POP()                                                        | Return the population standard deviation.                              |
| STDDEV_SAMP()                                                       | Return the sample standard deviation.                                  |
| [SUM()](https://www.mysqltutorial.org/mysql-sum/)                   | Return the summation of all non-NULL values a set.                     |
| VAR_POP()                                                           | Return the population standard variance.                               |
| VARP_SAM()                                                          | Return the sample variance.                                            |
| VARIANCE()                                                          | Return the population standard variance.                               |

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
# Methods, Operations and Functions

PySpark provides a variety of methods to work with data, some of the most commonly used are:

- `.show()`: Displays the first 20 rows of a DataFrame
- `.count()`: Counts the number of rows in a DataFrame
- `.describe()`: Computes basic statistics of a DataFrame
- `.head()`: Returns the first n rows of a DataFrame
- `.select()`: Selects specific columns from a DataFrame
- `.filter()`: Filters the rows of a DataFrame based on a condition
- `.groupBy()`: Groups the rows of a DataFrame by a specific column
- `.orderBy()`: Sorts the rows of a DataFrame by one or more columns

PySpark also provides a variety of operations for transforming and processing data, such as:

- `.map()`: Applies a function to each element of an RDD or DataFrame
- `.reduce()`: Combines the elements of an RDD or DataFrame using a specified function
- `.flatMap()`: Applies a function to each element of an RDD or DataFrame, and flattens the results
- `.filter()`: Filters the elements of an RDD or DataFrame based on a condition
- `.distinct()`: Returns a new RDD or DataFrame with distinct elements
- `.union()`: Returns a new RDD or DataFrame with elements from both the source RDD or DataFrame and another RDD or DataFrame

PySpark provides a variety of built-in functions for data manipulation, such as:

- `count()`: Counts the number of rows in a DataFrame
- `sum()`: Sums the values of a specific column
- `avg()`: Computes the average of the values of a specific column
- `min()`: Returns the minimum value of a specific column
- `max()`: Returns the maximum value of a specific column
- `concat()`: Concatenates two or more columns into a single column
- `split()`: Splits a string column into multiple columns
- `substring()`: Returns a substring of a string column

These functions can be used in combination with the PySpark SQL module to perform a variety of data manipulation tasks.

Here is an example of how to use the sum() function to compute the sum of a specific column in a DataFrame:

```py
from pyspark.sql.functions import sum

# Compute the sum of the "value" column
df.select(sum("value")).show()
```

Once you have read your data, you can use Spark to perform various data processing tasks. The following code snippet shows how to perform a simple groupby operation on the data:

```py
from pyspark.sql.functions import count

# Group the data by the "category" column and count the number of occurrences
grouped_data = df.groupBy("category").agg(count("*").alias("count"))
```

In this example, we are using the groupBy() function to group the data by the “category” column and the agg() function to count the number of occurrences in each group. We then store the result in a new DataFrame called grouped_data.

## Using Filter and Where on DataFrame

The `where()` and `filter()` methods are used to select rows from a DataFrame based on one or more conditions. Both methods are used to filter data based on a specified condition, and they are often used interchangeably.

The `where()` method is a synonym for the `filter()` method, and they have the same syntax.

## Different Types of Joins in PySpark

There are several types of joins in PySpark, including inner join, outer join, left join, right join, and cross join.

The most commonly used join in PySpark is the inner join, which returns only the rows that have matching keys in both DataFrames.

## Using Union and Union All on DataFrames

In PySpark, `union()` and `unionAll()` are methods used to combine two or more DataFrames vertically, i.e., they stack rows from one DataFrame on top of another.

The main difference between the two methods is that `union()` removes duplicate rows, while `unionAll()` retains all rows.

## Working with Columns Using withColumn

In PySpark, `withColumn()` is a method used to add a new column to a DataFrame or replace an existing column with a modified version.

The method takes two parameters: the name of the new column, and an expression that defines the values for the new column.

## Where to Use withColumnRenamed

In PySpark, `withColumnRenamed()` is a method used to rename a column in a DataFrame.

The method takes two parameters: the current name of the column, and the new name of the column.

## Aggregation and Filtering Using groupBy

In PySpark, `groupBy()` is a method used to group rows of a DataFrame based on one or more columns, and apply aggregation functions on each group.

This method is useful for summarizing and analyzing data based on certain criteria.

## How to Clean your Data Using drop

In PySpark, `drop()` is a method used to remove one or more columns from a DataFrame.

The method takes one or more column names as parameters and returns a new DataFrame with the specified columns removed.

## How to Pivot in PySpark

In PySpark, `pivot()` is a method used to transform a DataFrame from a long format to a wide format, by rotating values from a column into separate columns.

This method is useful for summarizing and analyzing data in a different format.

## Eliminate Duplicate Data with distinct

In PySpark, `distinct()` is a method used to return a DataFrame with distinct rows based on all columns or a subset of columns.

## How to Use map and mapPartitions

In PySpark, `map()` and `mapPartitions()` are methods used to transform the data in an RDD (Resilient Distributed Dataset).

The `map()` method applies a function to each element of an RDD and returns a new RDD with the transformed elements.

The `mapPartitions()` method applies a function to each partition of an RDD and returns a new RDD with the transformed partitions. This method is more efficient than `map()` when the function you're applying to each element of the RDD requires some setup or teardown work.

## What are foreach and foreachPartition

In PySpark, `foreach()` and `foreachPartition()` are methods used to perform actions on each element of an RDD.

The `foreach()` method applies a function to each element of an RDD, without returning any result. It is typically used for side effects, such as writing the elements to a file or a database.

The `foreachPartition()` method applies a function to each partition of an RDD, instead of each element. This method is useful when you need to perform some expensive initialization or teardown work for each partition, such as establishing a database connection or opening a file.

## Understanding Data Structures Using StructType and StructField

In PySpark, `StructType` and `StructField` are classes used to define the schema of a DataFrame.

`StructType` is a class that represents a schema, which is a collection of `StructField` objects. A schema defines the structure of a DataFrame, including the names, data types, and nullable flags of its columns.

## Collect vs Select in PySpark Best Practices

In PySpark, `collect()` and `select()` are methods used to extract data from a DataFrame or RDD.

`collect()` is a method that returns all the data from a DataFrame or RDD as a list in the driver program. This method should be used with caution because it can potentially cause the driver program to run out of memory if the data is too large.

`select()` is a method that returns a new DataFrame with only the specified columns. This method is used to filter the data and reduce the amount of data that needs to be processed.
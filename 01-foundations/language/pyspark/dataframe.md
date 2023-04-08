# PySpark DataFrame

## Creating a DataFrame in PySpark

The DataFrames are a fundamental data structure in PySpark, and they provide a powerful and flexible way to work with structured and semi-structured data. A DataFrame is a distributed collection of data organized into named columns. It is similar to a table in a relational database or a data frame in R/Python. DataFrames are built on top of RDDs and provide a higher-level abstraction for data processing. They also support a more powerful query optimizer, known as the Catalyst Optimizer, which can greatly improve the performance of Spark queries.

DataFrames can be created from a variety of data sources, including structured data files, Hive tables, external databases, and streaming data sources. The following code snippet shows how to create a DataFrame from a CSV file:

```py
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)
```

Once a DataFrame has been created, it can be transformed and processed using the same functions as an RDD, as well as additional functions specific to DataFrames.
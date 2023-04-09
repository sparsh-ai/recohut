# Lazy Processing

PySpark uses a concept called lazy processing, which means that operations on DataFrames and RDDs are not executed immediately, but rather are recorded in a lineage. The actual execution of the operations is delayed until an action is called. This allows Spark to optimize the execution plan by analyzing the entire lineage of operations, rather than executing each operation individually.

This can significantly improve the performance of Spark jobs by reducing the amount of data that needs to be read and processed.

Here is an example of how lazy processing works in PySpark:

```py
# Define a DataFrame
df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

# Define a transformation on the DataFrame
df = df.filter(df["age"] > 30)

# The transformation is not executed yet

# Perform an action on the DataFrame
df.count()

# The transformation is executed and the DataFrame is filtered
```

In this example, the filter operation on the DataFrame is not executed until the count() action is called. This allows Spark to optimize the execution plan by analyzing the entire lineage of operations before executing them.
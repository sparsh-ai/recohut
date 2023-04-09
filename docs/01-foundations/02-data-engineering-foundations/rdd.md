# Spark RDDs

An RDD (Resilient Distributed Dataset) is the primary data structure in Spark. It is a distributed collection of data that can be processed in parallel. RDDs are immutable, meaning that once an RDD is created, it cannot be modified. Instead, any transformations applied to an RDD will return a new RDD.

RDDs are the low-level representation of datasets processed by a Spark cluster. In early versions of Spark, you had to write code manipulating RDDs directly. In modern versions of Spark you should instead use the higher-level DataFrame APIs, which Spark automatically compiles into low-level RDD operations.

Once an RDD has been created, it can be transformed and processed using a variety of functions, such as map, filter, and reduce.

![rdd-process](https://user-images.githubusercontent.com/62965911/215011129-929b3b1e-ca32-4669-a4de-d40e96b8c272.png)

These are the most fundamental data structures that Spark operates on. RDDs support a wide variety of data formats such as JSON, **comma-separated values** (**CSV**), Parquet, and so on.

### Creating RDDs

An RDD can be created from a variety of data sources, including text files, sequences, and external data sources such as HBase and Cassandra.

The following code snippet shows how to create an RDD from a text file:

```py
rdd = sc.textFile("path/to/file.txt")
```

Here is an easy way using the parallelize() function:

```python
val cities = Seq("New York", "Austin")

val rdd=spark.sparkContext.parallelize(cities)
```
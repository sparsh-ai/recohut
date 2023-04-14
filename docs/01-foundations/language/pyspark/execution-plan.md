# Spark Execution Plan

Spark uses a query optimizer known as Catalyst to optimize the execution plan of Spark jobs. The execution plan is a representation of the physical execution of a query and it can be used to understand how Spark is processing data.

The `explain()` the method can be used to view the execution plan of a query. The `explain()` method can be used on DataFrames and RDDs to view the physical execution plan of a query.

Here is an example of how to view the execution plan of a query:

```py
# View the execution plan of a query
df.filter(df["age"] > 30).explain()
```

In this example, the `explain()` the method is used to view the physical execution plan of a query that filters the DataFrame to include only rows where the "age" column is greater than 30. The output of the `explain()` the method will show the physical execution plan of the query, which can be used to understand how Spark is processing data.

We can express the same query using any interface. The Spark SQL engine generates the same query plan used to optimize and execute on our Spark cluster.

![query execution engine](https://user-images.githubusercontent.com/62965911/214256593-38afbb18-1bc3-405d-916f-9981edb57522.png)

Broadcasting in Spark can greatly improve the performance of Spark jobs by reducing the amount of data that needs to be sent over the network. Understanding the execution plan in Spark can also be helpful to understand how Spark is processing data and to optimize the performance of Spark jobs.

Whenever we execute transformations, Spark prepares a plan, and as soon as an action is called, it performs those transformations. Now, it's time to expand that knowledge. Let's dive deeper into Spark's query execution mechanism.

Every time a query is executed by Spark, it is done with the help of the following four plans:

- **Parsed Logical Plan**: Spark prepares a *Parsed Logical Plan*, where it checks the metadata (table name, column names, and more) to confirm whether the respective entities exist or not.
- **Analyzed Logical Plan**: Spark accepts the Parsed Logical Plan and converts it into what is called the *Analyzed Logical Plan*. This is then sent to Spark's catalyst optimizer, which is an advanced query optimizer for Spark.
- **Optimized Logical Plan**: The catalyst optimizer applies further optimizations and comes up with the final logical plan, called the *Optimized Logical Plan*.
- **Physical Plan**: The *Physical Plan* specifies how the Optimized Logical Plan is going to be executed on the cluster.

Apart from the catalyst optimizer, there is another framework in Spark called the **cost-based optimizer** (**CBO**). The CBO collects statistics on data, such as the number of distinct values, row counts, null values, and more, to help Spark come up with a better Physical Plan. AQE is another optimization technique that speeds up query execution based on runtime statistics. It does this with the help of the following three features:

- **Dynamically coalescing shuffle partitions**
- **Dynamically switching join strategies**
- **Dynamically optimizing skew joins**

To write efficient Spark applications, we need to have some understanding of how Spark executes queries. Having a good understanding of how Spark executes a given query helps big data developers/engineers work efficiently with large volumes of data.

Query execution is a very broad subject, and, in this section, we will understand jobs, stages, and tasks. We will also learn how Spark lazy evaluation works, how to check and understand the execution plan when working with DataFrames or SparkSQL, how joins work in Spark and the different types of join algorithms Spark uses while joining two tables. We will also learn about the input, output, and shuffle partitions and the storage benefits of using different file formats.

Knowing about the internals will help you troubleshoot and debug your Spark applications more efficiently. By the end of this section, you will know how to execute Spark queries, as well as how to write and debug your Spark applications more efficiently.

### Tuning shuffle partitions

Spark uses a technique called **shuffle** to move data between its executors or nodes while performing operations such as **join**, **union**, **groupby**, and **reduceby**. The shuffle operation is very expensive as it involves the movement of data between nodes. Hence, it is usually preferable to reduce the amount of shuffle involved in a Spark query. The number of partition splits that Spark performs while shuffling data is determined by the following configuration:

```python
spark.conf.set("spark.sql.shuffle.partitions",200)
```

**200** is the default value and you can tune it to a number that suits your query the best. If you have too much data and too few partitions, this might result in longer tasks. But, on the other hand, if you have too little data and too many shuffle partitions, the overhead of shuffle tasks will degrade performance. So, you will have to run your query multiple times with different shuffle partition numbers to arrive at an optimum number.

You can learn more about Spark performance tuning and shuffle partitions here: [https://spark.apache.org/docs/latest/sql-performance-tuning.html](https://spark.apache.org/docs/latest/sql-performance-tuning.html).

### Identifying shuffles in a Spark query plan

Similar to SQL, we can use the **EXPLAIN** command to print the plans in Spark. Here is a simple example to generate two sets of numbers, partition them, and then join them. This will cause lot of data movement:

```python
val jump2Numbers = spark.range(0, 100000,2)
val jump5Numbers = spark.range(0, 200000, 5)
val ds1 = jump2Numbers.repartition(3)
val ds2 = jump5Numbers.repartition(5)
val joined = ds1.join(ds2)
joined.explain
```

The **joined.explain** request will print a plan similar to the sample shown as follows:

```
== Physical Plan ==
BroadcastNestedLoopJoin BuildRight, Inner
:- **Exchange** RoundRobinPartitioning(3), [id=#216]
:  +- *(1) Range (0, 100000, step=2, splits=4)
+- BroadcastExchange IdentityBroadcastMode, [id=#219]
   +- **Exchange** RoundRobinPartitioning(5), [id=#218]
      +- *(2) Range (0, 200000, step=5, splits=4)
```

Just search for the **Exchange** keyword to identify the shuffle stages.

Alternatively, you can identify the shuffle stage from the Spark DAG. In the DAG, look for sections named **Exchange**. These are the shuffle sections. Here is an example Spark DAG containing two **Exchange** stages:

![B17525_14_013](https://user-images.githubusercontent.com/62965911/218312617-1624668d-96d7-449d-87ea-60edf79edf2d.jpeg)

If there are very expensive shuffle sections, consider enabling the statistics and checking whether the engine generates a better plan. If not, you will have to rewrite the query to reduce the shuffles as much as possible.

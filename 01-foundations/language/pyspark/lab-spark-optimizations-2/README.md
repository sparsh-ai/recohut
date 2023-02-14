# Spark Optimizations

**Performance tuning** in **Apache** **Spark** plays an instrumental role in running efficient big data workloads. More often than not, the optimization techniques employed to prevent the shuffling and skewing of data drastically improve performance. In this lab, we will learn about the Spark optimization techniques directly related to **Spark Core** that help prevent the shuffling and skewing of data.

We will begin by learning about broadcast joins and how they are different from traditional joins in Spark. Next, we will learn about **Apache** **Arrow**, its integration with the **Python** **pandas** project, and how it improves the performance of Pandas code in **Databricks**. We will also learn about shuffle partitions, Spark caching, and **adaptive query execution** (**AQE**). Shuffle partitions can often become performance bottlenecks, and it is important that we learn how to tune them. Spark caching is another popular optimization technique that helps to speed up queries on the same data without having to re-read it from the source. Last but not least, AQE helps to automatically optimize data engineering workloads. The topics covered in this lab are as follows:

- Learning about broadcast joins
- Learning about Apache Arrow in Pandas
- Understanding shuffle partitions
- Understanding caching in Spark
- Learning about AQE

## Learning about broadcast joins

In **ETL** operations, we need to perform join operations between new data and lookup tables or historical tables. In such scenarios, a join operation is performed between a large DataFrame (millions of records) and a small DataFrame (hundreds of records). A standard join between a large and small DataFrame incurs a shuffle between the worker nodes of the cluster. This happens because all the matching data needs to be shuffled to every node of the cluster. While this process is computationally expensive, it also leads to performance bottlenecks due to network overheads on account of shuffling. Here, **broadcast joins** come to the rescue! With the help of broadcast joins, Spark duplicates the smaller DataFrame on every node of the cluster, thereby avoiding the cost of shuffling the large DataFrame.

We can better understand the difference between a standard join and a broadcast join with the help of the following diagram. In the case of a standard join, the partitions of both the DataFrames need to shuffle across worker nodes or executors so that matching records based on the join condition can be joined. In the case of a broadcast join, Spark sends a copy of the smaller DataFrame to each node or executor so that it can be joined with the respective partition of the larger DataFrame.

![B17782_07_01](https://user-images.githubusercontent.com/62965911/218774587-90b9c572-0866-404b-b75b-e864cd852325.jpeg)

In this lab, we will go through a worked-out example to better understand the performance comparisons of both of these joins.

The catch here is that broadcast joins are not suitable for every join scenario, and there is no set limit on DataFrame size so as to define the smaller DataFrame. But as a best practice, DataFrames sized between 10 MB and 50 MB are usually broadcast. Spark also performs broadcast joins implicitly. This behavior is controlled with the help of the Spark configuration, **spark.sql.autoBroadcastJoinThreshold**. The default threshold is 10 MB for the configuration. To disable the configuration, we can set it to **-1**.

## Learning about Apache Arrow in Pandas

Apache Arrow is an in-memory columnar data format that helps to efficiently store data between clustered **Java Virtual Machines** (**JVMs**) and Python processes. This is highly beneficial for data scientists working with Pandas and **NumPy** in Databricks. Apache Arrow does not produce different results in terms of the data. It is helpful when we are converting Spark DataFrames to Pandas DataFrames, and vice versa. Let's try to better understand the utility of Apache Arrow with an analogy.

Let's say you were traveling to Europe before the establishment of the **European Union** (**EU**). To visit 10 countries in 7 days, you would have has to spend some time at every border for passport control, and money would have always been lost due to currency exchange. Similarly, without using Apache Arrow, inefficiencies exist due to serialization and deserialization processes wasting memory and CPU resources (such as converting a Spark DataFrame to a Pandas DataFrame).

But using Apache Arrow is like traveling to Europe after the establishment of the EU. This means no more waiting at the borders, and the same currency being used everywhere. Therefore, Apache Arrow allows us to use the same in-memory data format for different frameworks and file formats. This highly optimizes data conversions between Spark and Pandas. In Databricks, Apache Arrow is available as an optimization when converting a **PySpark** DataFrame to a Pandas DataFrame with the **toPandas()** function, and when converting a Pandas DataFrame to a PySpark DataFrame using the **createDataFrame()** function.

A point to note here is that even though we are enabling Apache Arrow, working with Pandas still leads to data getting collected on the driver node using the **toPandas()** function. Therefore, it should only be used on a small subset of data.

## Understanding shuffle partitions

Every time Spark performs a wide transformation or aggregations, shuffling of data across the nodes occurs. And during these shuffle operations, Spark, by default, changes the partitions of the DataFrame. For example, when creating a DataFrame, it may have 10 partitions, but as soon as the shuffle occurs, Spark may change the partitions of the DataFrame to 200. These are what we call the shuffle partitions.

This is a default behavior in Spark, but it can be altered to improve the performance of Spark jobs. We can also confirm the default behavior by running the following line of code:

```python
spark.conf.get('spark.sql.shuffle.partitions')
```

This returns the output of **200**. This means that Spark will change the shuffle partitions to **200** by default. To alter this configuration, we can run the following code, which configures the shuffle partitions to **8**:

```python
spark.conf.set('spark.sql.shuffle.partitions',8)
```

You may be wondering why we set the **spark.sql.shuffle.partitions** configuration to **8**. This is because we have eight cores in the cluster we are using. And having the same number of shuffle partitions ensures that during the shuffling process, we will have all the cores' clusters processing the same number of partitions at a time.

## Understanding caching in Spark

Every time we perform an action on a Spark DataFrame, Spark has to re-read the data from the source, run jobs, and provide an output as the result. This may not be a performance bottleneck when reading data for the first time, but if a certain DataFrame needs to be queried repeatedly, Spark will have to re-compute it every time. In such scenarios, Spark caching proves to be highly useful. Spark *caching* means that we store data in the cluster's memory. As we already know, Spark has memory divided for cached DataFrames and performing operations. Every time a DataFrame is cached in memory, it is stored in the cluster's memory, and Spark does not have to re-read it from the source in order to perform computations on the same DataFrame.

NOTE

> Spark caching is a transformation and therefore it is evaluated *lazily*. In order to enforce a cache on a DataFrame, we need to call an *action*.

Now, you may be wondering how this is different from **Delta caching**. The following table illustrates the differences between Delta caching and Spark caching:

![B17782_07_02a](https://user-images.githubusercontent.com/62965911/218777857-8164b86a-40e7-4903-bec7-b248950c8337.jpeg)
![B17782_07_02b](https://user-images.githubusercontent.com/62965911/218777543-caab7170-069d-45fc-82dc-17f237f019d1.jpeg)

Another point to note is that when a Databricks cluster is terminated, the cache is also lost. In this lab, we will go through a worked-out example to better understand Spark caching in Databricks.

## Learning about AQE

We already know how Spark works under the hood. Whenever we execute transformations, Spark prepares a plan, and as soon as an action is called, it performs those transformations. Now, it's time to expand that knowledge. Let's dive deeper into Spark's query execution mechanism.

Every time a query is executed by Spark, it is done with the help of the following four plans:

- **Parsed Logical Plan**: Spark prepares a *Parsed Logical Plan*, where it checks the metadata (table name, column names, and more) to confirm whether the respective entities exist or not.
- **Analyzed Logical Plan**: Spark accepts the Parsed Logical Plan and converts it into what is called the *Analyzed Logical Plan*. This is then sent to Spark's catalyst optimizer, which is an advanced query optimizer for Spark.
- **Optimized Logical Plan**: The catalyst optimizer applies further optimizations and comes up with the final logical plan, called the *Optimized Logical Plan*.
- **Physical Plan**: The *Physical Plan* specifies how the Optimized Logical Plan is going to be executed on the cluster.

Apart from the catalyst optimizer, there is another framework in Spark called the **cost-based optimizer** (**CBO**). The CBO collects statistics on data, such as the number of distinct values, row counts, null values, and more, to help Spark come up with a better Physical Plan. AQE is another optimization technique that speeds up query execution based on runtime statistics. It does this with the help of the following three features:

- **Dynamically coalescing shuffle partitions**
- **Dynamically switching join strategies**
- **Dynamically optimizing skew joins**

Let's discuss these in detail.

### Dynamically coalescing shuffle partitions

When dealing with very large datasets, shuffle has a huge impact on performance. It is an expensive operation that requires data to be moved across nodes so that it can be re-distributed as required by the downstream operations. But two types of issues can occur:

- If the number of partitions is less, then their size will be larger, and this can lead to data spillage during the shuffle. This can slow down Spark jobs.
- If the number of partitions is more, then there could be a chance that the partitions would be small in size, leading to a greater number of tasks. This can put more burden on Spark's task scheduler.

To solve these problems, we can set a relatively large number of shuffle partitions and then coalesce any adjacent small partitions at runtime. This can be achieved with the help of AQE, as it automatically coalesces small partitions at runtime.

### Dynamically switching join strategies

With the help of AQE, Spark can switch join strategies at runtime if they are found to be inefficient. Spark supports various join strategies but usually, the *broadcast hash join* (also called the *broadcast join*) is often considered to be the most performant if one side of the join is small enough to fit in the memory of every node.

### Dynamically optimizing skew joins

*Data skew* occurs when data is unevenly distributed across the partitions of the DataFrame. It has the potential to downgrade query performance. With the help of AQE, Spark can automatically detect data skew while joins are created. After detection, it splits the larger of those partitions into smaller sub-partitions that are joined to the corresponding partition on the other side of the join. This ensures that the Spark job does not get stuck due to a single enormously large partition.

In this recipe, we will go through a worked-out example to learn how AQE actually works in Databricks.

## Conclusion

In this lab, we learned about several optimization techniques concerning Spark Core. We started off by learning about broadcast joins and how they are more performant than a standard join. Then, we learned about the advantages of using Apache Arrow with Pandas. Next, we learned about shuffle partitions and Spark caching.

Finally, we learned about AQE and how it helps to speed up queries during runtime. All these optimization techniques are highly useful for tuning big data workloads in Databricks.

# Delta Lake Optimizations

In this lab, we will learn about various Delta Lake optimizations that help us build a more performant Lakehouse.

We will cover the following topics:

- Working with the **OPTIMIZE** and **ZORDER** commands
- Using **AUTO OPTIMIZE**
- Learning about delta caching
- Learning about dynamic partition pruning
- Understanding bloom filter indexing

Delta Lake is an open source storage layer that provides functionalities to data in the data lake that only exist in data warehouses. When combined with cloud storage, **Databricks** and Delta Lake lead to the formation of a **Lakehouse**. A Lakehouse simply provides the best of both worlds -- **data lakes** and **data warehouses**. In today's world, a Lakehouse provides the same set of capabilities as a traditional data warehouse and at a much lower cost. This is made possible due to cheap cloud storage such as Azure Data Lake, Spark as the processing engine, and data being stored in the Delta Lake format. In this lab, we will learn about various Delta Lake optimizations that help us build a more performant Lakehouse.

In this lab, we will cover the following topics:

- Working with the **OPTIMIZE** and **ZORDER** commands
- Using **AUTO OPTIMIZE**
- Learning about delta caching
- Learning about dynamic partition pruning
- Understanding bloom filter indexing

## Environment Setup

You will find a dbc file in assets folder. Import this in your databricks workspace.

![](https://user-images.githubusercontent.com/62965911/218763268-0f50845e-eb1f-4213-8bf7-4594ff3946ea.png)

## Working with the OPTIMIZE and ZORDER commands

Delta lake on Databricks lets you speed up queries by changing the layout of the data stored in the cloud storage. The algorithms that support this functionality are as follows:

- **Bin-packing**: This uses the **OPTIMIZE** command and helps coalesce small files into larger ones.
- **Z-Ordering**: This uses the **ZORDER** command and helps collocate data in the same set of files. This co-locality helps reduce the amount of data that's read by Spark while processing.

Use `1. Working with OPTIMIZE and ZORDER` notebook for this recipe.

**OPTIMIZE** and **ZORDER** can be used to speed up Databricks queries. As a best practice, **ZORDER** should be used on columns that are commonly used in queries to filter data and have high cardinality. But *Z-Ordering* on too many columns can also degrade performance. Hence, the columns to Z-Order on should be chosen wisely. *Bin-packing* should always be used when different transactions such as inserts, deletes, or updates are being executed on a delta table. Also, it is an idempotent process, meaning that if the **OPTIMIZE** command is run twice on a table, the second run will have no effect.

## Using Auto Optimize

**Auto Optimize** is a feature that helps us automatically compact small files while an individual writes to a delta table. Unlike bin-packing, we do not need to run a command every time Auto Optimize is executed. It consists of two components:

- **Optimized Writes**: Databricks dynamically optimizes Spark partition sizes to write 128 MB chunks of table partitions.
- **Auto Compaction**: Here, Databricks runs an optimized job when the data writing process has been completed and compacts small files. It tries to coalesce small files into 128 MB files. This works on data that has the greatest number of small files.

Use `2. Using AUTO OPTIMIZE` notebook for this recipe.

In this recipe, we will understand how Auto Optimize has been applied to our newly written file in delta format. But Auto Optimize may not always be useful in every scenario. To understand this, we will learn when to opt in and when to opt out of the Auto Optimize features.

### Understanding optimized writes

**Optimized writes** help dynamically optimize Spark partition sizes to write 128 MB chunks of table partitions. Here are some best practices regarding optimized writes:

- Optimized writes involve shuffling data across the executors, so they should only be used if a minutes' worth of latency is acceptable in streaming jobs.
- It should be used when SQL commands such as **UPDATE**, **DELETE**, and more are frequently used.
- It should not be used when terabytes of data is being processed and storage optimized node instances are not available.

Next, let's learn about Auto Compaction.

### Understanding Auto Compaction

**Auto Compaction** tries to coalesce small files into 128 MB files and works on data that has the greatest number of small files. Here are some best practices regarding optimized writes:

- Auto Compaction should be used when a minutes' worth of latency is acceptable in streaming jobs.
- If Bin-Packing is not being done on a delta table, Auto Compaction should be used.
- This feature should not be used when operations such as **DELETE**, **UPDATE**, and more are being applied on a Delta table. This is because Auto Compaction is performed on a table after the write has succeeded. Hence, there could be a transactional conflict between the jobs.

NOTE

> If Auto Compaction fails due to a conflict, Databricks does not fail or retry the compaction.

This concludes this section on Auto Optimize. In the next section, we will learn about delta caching.

## Learning about delta caching

**Delta caching** is an optimization technique that helps speed up queries by storing the data in the cluster node's local storage. The delta cache stores local copies of data that resides in remote locations such as **Azure Data Lake** or **Azure Blob Storage**. It improves the performance of a wide range of queries but cannot store the results of arbitrary subqueries.

Once delta caching has been enabled, any data that is fetched from an external location is automatically added to the cache. This process does not require action. To preload data into the delta cache, the **CACHE** command can be used. Any changes that have been made to the data persisted in the delta cache are automatically detected by the delta cache. The easiest way to use delta caching is to provision a cluster with **Standard_L** series worker types (**Delta Cache Accelerated**).

Use `3. Learning Delta Caching` notebook for this recipe.

## Learning about dynamic partition pruning

**Dynamic partition pruning** is a *data-skipping technique* that can drastically speed up query execution time. Delta lake collects metadata on the partition files it manages so that data can be skipped without the need to access it. This technique is very useful for *star schema* types of queries as it can dynamically skip partitions and their respective files. Using this technique, we can prune the partitions of a fact table during the join to a dimension table. This is made possible when the filter that's applied to a dimension table to prune its partitions is dynamically applied to the fact table.

Use `4. Learning Dynamic Partition Pruning` notebook for this recipe.

## Understanding bloom filter indexing

A **bloom filter index** is a data structure that provides data skipping on columns, especially on fields containing arbitrary text. The filter works by either stating that certain data is definitely not in a file or that it is probably in the file, which is defined by a **false positive probability** (**FPP**). The bloom filter index can help speed up *needle in a haystack* type of queries, which are not speed up by other techniques.

Use `5. Understanding Bloom Filter Indexing` notebook for this recipe.

## Summary

In this lab, we learned about several optimization techniques concerning Databricks Delta Lake. We started with file compaction and clustering techniques and ended with techniques for efficient data skipping. These optimization techniques play a crucial role in making querying and data engineering workloads in Databricks quicker and more efficient.

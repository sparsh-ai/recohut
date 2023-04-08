# Partitioning

A partition in spark is a logical chunk of data mapped to a single node in a cluster. Partitions are basic units of parallelism. Each partition is processed by a single task slot. In a multicore system, total slots for tasks will be `num of executors x number of cores`. Hence the number of partitions decides the task parallelism.

Problem due to inadequate/misconfigured partitions:

- **Too many partitions —** slower data reads
- **Too many small partitions —** waste of resource
- **Overly large partitions** can even cause executor “out of memory” errors.
- **A small number of large partitions** may leave some worker cores idle.
- **Few partitions:** long computation and write times. Also, it can cause skewed data and inefficient resource use. Skewed partition may lead to slow stage/tasks, data spilling to disk, and OOM errors.

In Spark, the number of partitions comes into the picture at three stages of the pipeline:

![partitioning](https://user-images.githubusercontent.com/62965911/223931567-7bc4652d-09a3-430a-9677-e96ec541c069.png)

### Input

The first place where we can decide the number of partitions that get created while we read data from files, DBs, or any other source. We can mention the size of each partition and based on the amount of data that is being read spark will create as many partitions.

For reading files from Parquet, JSON, and ORC we can set the bytes for each partition.

* spark.default.parallelism — how many partitions are read in when doing `spark.read`
* spark.sql.files.maxPartitionBytes — The maximum number of bytes to put into a single partition when reading files
* spark.sql.files.minPartitionNum — minimum number of split file partition
* spark.files.openCostInBytes — estimated cost to open a file

While reading from databases we can ser (`partitionColumn`, `lowerBound`, `upperBound`, `numPartitions` ). These values will divide the data (between lower & upper bound) into partitions (a number equal to numPartitions). So let us say we have an Id column and we set `lowerBound` to 1 and `upperBound` to 40000 with `numPartitions` to 4. Then in the case of equal distribution spark will have 4 partitions with 10000 records each.

NOTE

> While reading from folders containing large number of files, enumeration of datasets is a challenge as it happens on driver. This processing of file listing follows a serial code path and can be slow. There are third party solutions, like RapidFile, to speed up file listing.

### Shuffle

When we perform a wide transformation (group by, join, window function) there is a shuffle of data. During this shuffle, new partitions get created or removed.

The smaller size of partitions (more partitions) will increase the parallel running jobs, which can improve performance, but too small of a partition will cause overhead and increase the GC time. Larger partitions (fewer number of partitions) will decrease the number of jobs running in parallel.

* **spark.sql.shuffle.partitions** — Default number of partitions returned by transformations like `join`, `reduceByKey`, and `parallelize` when not set by user. Default is **200**.

We can manually tweak the number of partitions by coalescing or repartitioning.

* repartition(numPartitions) — Uses RoundRobinPartitioning
* repartition(partitionExprs) — Uses HashPartitioner
* repartitionByRange(partitionExprs) — Uses range partitioning
* coalesce(numPartitions) — Use only to reduce the number of partitions

NOTE

> In most cases, Coalesce should be preferred over repartition while reducing the number of partitions. But Repartition guarantees that the data distribution in the partition is roughly the same size. So in some cases, it may be preferred.

In case where are performing aggregate on unique columns we should control the shuffle by using repartition. Good partitioning of data leads to better speed and fewer OOMs errors. The _repartition_ leads to a full shuffle of data between the executors making the job slower. The _coalesce_ operation doesn’t trigger a full shuffle when it reduces the number of partitions. It only transfers the data from partitions being removed to existing partitions.

We can get partitions and there record count for each one using the following code:

```python
from pyspark.sql.functions import spark\_partition\_id, asc, desc

df.withColumn("partitionId", spark\_partition\_id())\\
    .groupBy("partitionId")\\
    .count()\\
    .orderBy(asc("count"))\\
    .show()
```

With AQE we can dynamically split & coalesce the partitions to have equal-sized partitions.

- spark.sql.adaptive.skewJoin.skewedPartitionFactor
- spark.sql.adaptive.skewJoin.skewedPartitionThresholdInByte
- spark.sql.adaptive.coalescePartitions.enabled
- spark.sql.adaptive.coalescePartitions.minPartitionSize
- spark.sql.adaptive.advisoryPartitionSizeInBytes
- spark.sql.adaptive.coalescePartitions.initialPartitionNum
- spark.sql.shuffle.partitions

### Output

The number of files that get written out is controlled by the parallelization of your DataFrame or RDD. So if your data is split across 10 Spark partitions you cannot write fewer than 10 files without reducing partitioning (e.g. `coalesce` or `repartition`).

* **partitionBy()** — Partitions the output by the given columns on the file system
* **maxRecordsPerFile** — number of records in a single file in each partition. This helps in fixing large file problem

When we write data, using the `maxRecordsPerFile` option, we can limit the number of records that get written per file in each partition.

To get one file per partition, use `repartition()` with the same columns you want the output to be partitioned by. The `partitionBy` method does not trigger any shuffle but it may generate a two many files. Imagine we have 200 partitions, and we want to partition data by date. Each spark task will produce 365 files in which leads to 365×200=73k files.

```python
partition_cols = []
df.repartition(*partition_cols)\
  .write.partitionBy(*partition_cols)\
  .mode(SaveMode.Append).parquet(path)
```

Spark also gives us the option of bucketing while writing data to tables. In bucketing data is divided into smaller portions called “buckets”.

```python
df.write.bucketBy(12, "key").saveAsTable("table\_name")
```

*No of files in bucketing = df.partition * number of bucket*

Also, To use bucket join for tables having buckets multiple of each other we need to set the following:

* _spark.sql.bucketing.coalesceBucketsInJoin.enabled_

## Partition pruning and Predicate pushdown

- **Partition pruning**: When you are dealing with terabytes of data, it is very difficult to retrieve the required data in a performant way. In this case, if files support partition pruning, then data can be retrieved faster. Partition pruning is a performance optimization technique that restricts the number of files and partitions that Spark can read while querying data. When partitioning is done, data is stored according to the partitioning scheme that's been segregated in the hierarchical folder structure and when data is queried, only a particular partition where data is available will be searched.
- **Predicate pushdown**: This is a condition in Spark queries that's used to filter the data that's restricting the number of records being returned from databases, thus improving the query's performance. While writing Spark queries, you need to ensure that the partition key columns are included in the filter condition of the query. Using predicate pushdown lets you skip over huge portions of the data while you're scanning and processing.
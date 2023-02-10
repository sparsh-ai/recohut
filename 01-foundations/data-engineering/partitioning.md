# Data Partitioning

Partitioning and bucketing are used to maximize benefits while minimizing adverse effects. It can reduce the overhead of shuffling, the need for serialization, and network traffic. In the end, it improves performance, cluster utilization, and cost-efficiency.

Partition helps in localizing data and reducing data shuffling across the network nodes, reducing network latency, which is a major component of the transformation operation, thereby reducing the time of completion. A good partitioning strategy knows about data and its structure, and cluster configuration. Bad partitioning can lead to bad performance, mostly in 3 fields:

- Too many partitions regarding your cluster size and you won’t use efficiently your cluster. For example, it will produce intense task scheduling.
- Not enough partitions regarding your cluster size, and you will have to deal with memory and CPU issues: memory because your executor nodes will have to put high volume of data in memory (possibly causing OOM Exception), and CPU because compute across the cluster will be unequal.
- Skewed data in your partitions can occur. When a Spark task is executed in these partitioned, they will be distributed across executor slots and CPUs. If your partitions are unbalanced in terms of data volume, some tasks will run longer compared to others and will slow down the global execution time of the tasks (and a node will probably burn more CPU that others).

## How to decide the partition key(s)?

- Choose low cardinality columns as partition columns (since a HDFS directory will be created for each partition value combination). Generally speaking, the total number of partition combinations should be less than 50K. (For example, don’t use partition keys such as roll_no, employee_ID etc. Instead use the state code, country code, geo_code, etc.)
- Choose the columns used frequently in filtering conditions.
- Use at most 2 partition columns as each partition column creates a new layer of directory.

## Different methods that exist in PySpark

### Repartitioning

The first way to manage partitions is the repartition operation. Repartitioning is the operation to reduce or increase the number of partitions in which the data in the cluster will be split. This process involves a full shuffle. Consequently, it is clear that repartitioning is an expensive process. In a typical scenario, most of the data should be serialized, moved, and deserialized.

```py
repartitioned = df.repartition(8)
```

In addition to specifying the number of partitions directly, you can pass in the name of the column by which you want to partition the data.

```py
repartitioned = df.repartition('country')
```

### Coalesce

The second way to manage partitions is coalesce. This operation reduces the number of partitions and avoids a full shuffle. The executor can safely leave data on a minimum number of partitions, moving data only from redundant nodes. Therefore, it is better to use coalesce than repartition if you need to reduce the number of partitions.

```py
coalesced = df.coalesce(2)
```

### PartitionBy

partitionBy(cols) is used to define the folder structure of data. However, there is no specific control over how many partitions are going to be created. Different from the coalesce andrepartition functions, partitionBy effects the folder structure and does not have a direct effect on the number of partition files that are going to be created nor the partition sizes.

```py
green_df \ 
    .write \ 
.partitionBy("pickup_year", "pickup_month") \ 
    .mode("overwrite") \ 
    .csv("data/partitions/partitionBy.csv", header=True)
```

## Key Points

1. Do not partition by columns with high cardinality.
2. Partition by specific columns that are mostly used during filter and groupBy operations.
3. Even though there is no best number, it is recommended to keep each partition file size between 256MB to 1GB.
4. If you are increasing the number of partitions, use repartition()(performing full shuffle).
5. If you are decreasing the number of partitions, use coalesce() (minimizes shuffles).
6. Default no of partitions is equal to the number of CPU cores in the machine.
7. GroupByKey ,ReduceByKey — by default this operation uses Hash Partitioning with default parameters.


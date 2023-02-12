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

## Benefits of partitioning

Partitioning has several benefits apart from just query performance. Let's take a look at a few important ones.

### Improving performance

Partitioning helps improve the parallelization of queries by splitting massive monolithic data into smaller, easily consumable chunks.

Apart from parallelization, partitioning also improves performance via **data pruning**. Using data pruning queries can ignore non-relevant partitions, thereby reducing the **input/output** (**I/O**) required for queries.

Partitions also help with the archiving or deletion of older data. For example, let's assume we need to delete all data older than 12 months. If we partition the data into units of monthly data, we can delete a full month's data with just a single **DELETE** command, instead of deleting all the files one by one or all the entries of a table row by row.

Let's next look at how partitioning helps with scalability.

### Improving scalability

In the world of big data processing, there are two types of scaling: vertical and horizontal.

**Vertical scaling** refers to the technique of increasing the capacity of individual machines by adding more memory, CPU, storage, or network to improve performance. This usually helps in the short term, but eventually hits a limit beyond which we cannot scale.

The second type of scaling is called **horizontal scaling**. This refers to the technique of increasing processing and storage capacity by adding more and more machines to a cluster, with regular hardware specifications that are easily available in the market (commodity hardware). As and when the data grows, we just need to add more machines and redirect the new data to the new machines. This method theoretically has no upper bounds and can grow forever. Data lakes are based on the concept of horizontal scaling.

Data partitioning helps naturally with horizontal scaling. For example, let's assume that we store data at a per-day interval in partitions, so we will have about 30 partitions per month. Now, if we need to generate a monthly report, we can configure the cluster to have 30 nodes so that each node can process one day's worth of data. If the requirement increases to process quarterly reports (that is, reports every 3 months), we can just add more nodes---say, 60 more nodes to our original cluster size of 30 to process 90 days of data in parallel. Hence, if we can design our data partition strategy in such a way that we can split the data easily across new machines, this will help us scale faster.

Let's next look at how partitioning helps with data management.

### Improving manageability

In many analytical systems, we will have to deal with data from a wide variety of sources, and each of these sources might have different data governance policies assigned to them. For example, some data might be confidential, so we need to restrict access to that; some might be transient data that can be regenerated at will; some might be logging data that can be deleted after a few months; some might be transaction data that needs to be archived for years; and so on. Similarly, there might be data that needs faster access, so we might choose to persist it on premium **solid-state drive** (**SSD**) stores and other data on a **hard disk drive** (**HDD**) to save on cost.

If we store such different sets of data in their own storage partitions, then applying separate rules---such as access restrictions, or configuring different data life cycle management activities such as deleting or archiving data, and so on---for the individual partitions becomes easy. Hence, partitioning reduces the management overhead, especially when dealing with multiple different types of data such as in a data lake.

Let's next look at how data partitioning helps with security.

### Improving security

As we saw in the previous section about improving manageability, confidential datasets can have different access and privacy levels. Customer data will usually have the highest security and privacy levels. On the other hand, product catalogs might not need very high levels of security and privacy.

So, by partitioning the data based on security requirements, we can isolate the secure data and apply independent access-control and audit rules to those partitions, thereby allowing only privileged users to access such data.

Let's next look at how we can improve data availability using partitioning.

### Improving availability

If our data is split into multiple partitions that are stored in different machines, applications can continue to serve at least partial data even if a few partitions are down. Only a subset of customers whose partitions went down might get impacted, while the rest of the customers will not see any impact. This is better than the entire application going down. Hence, physically partitioning the data helps improve the availability of services.

In general, if we plan our partition strategy correctly, the returns could be significant. I hope you have now understood the benefits of partitioning data. Let's next look at some partition strategies from a storage/files perspective.

## Key Points

1. Do not partition by columns with high cardinality.
2. Partition by specific columns that are mostly used during filter and groupBy operations.
3. Even though there is no best number, it is recommended to keep each partition file size between 256MB to 1GB.
4. If you are increasing the number of partitions, use repartition()(performing full shuffle).
5. If you are decreasing the number of partitions, use coalesce() (minimizes shuffles).
6. Default no of partitions is equal to the number of CPU cores in the machine.
7. GroupByKey, ReduceByKey — by default this operation uses Hash Partitioning with default parameters.

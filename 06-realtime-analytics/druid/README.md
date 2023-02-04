# Druid

One database that meets all the criteria for real-time analytics application is Apache Druid. It enables subsecond performance at scale, provides high concurrency at the best value, and easily ingests and combines real-time streaming data and historical batch data. It is a high-performance, real-time analytics database that is flexible, efficient, and resilient.

## Origins of Druid

In 2011, the data team at a technology company had a problem. It needed to quickly aggregate and query real-time data coming from website users across the internet to analyze digital advertising auctions. This created large data sets, with millions or billions of rows.

The data team first implemented its product using relational databases. It worked but needed many machines to scale, and that was too expensive.

The team then tried the NoSQL database HBase, which was populated from Hadoop MapReduce jobs. These jobs took hours to build the aggregations necessary for the product. At one point, adding only three dimensions on a data set that numbered in the low millions of rows took the processing time from 9 hours to 24 hours.

So, in the words of Eric Tschetter, one of Druid’s creators, “we did something crazy: we rolled our own database.” And it worked! The first incarnation of Druid scanned, filtered, and aggregated one billion rows in 950 milliseconds.

Druid became open source a few years later and became a top-level project of the Apache Software Foundation in 2016.

As of 2023, over 1,400 organizations use Druid to generate insights that make data useful, in a wide variety of industries and a wide range of uses. There are over 10,000 developers active in the Druid global community.

## Scalable and Flexible

Druid has an elastic and distributed architecture to build any application at any scale, enabled by a unique storage-compute design with independent services.

During ingestion, data is split into segments, fully indexed, and optionally pre-aggregated. This enables unique value over other analytics databases, which force a choice between the performance of tightly coupled compute and storage or the scalability of loosely coupled compute and storage. Druid gets both performance and cost advantages by storing the segments on cloud storage and also prefetching them so they are ready when requested by the query engine.

Each service in Druid can scale independently of other services. Data nodes, which contain prefetched, indexed, segmented data, can be dynamically added or removed as data quantities change. Meanwhile, query nodes, which manage queries against streams and historical data, can be dynamically added or removed as the number and shape of queries change.

A small Druid cluster can run on a single computer, while large clusters span thousands of servers and are able to ingest multiple millions of stream events per second while querying billions of rows, usually in under one second.

## Efficient and Integrated

Performance is the key to interactivity. In Druid, the key to performance is “if it’s not needed, don’t do it.” This means minimizing the work the cluster has to do.

Druid doesn’t load data from disk to memory, or from memory to CPU, when it isn’t needed for a query. It doesn’t decode data when it can operate directly on encoded data. It doesn’t read the full data set when it can read a smaller index. It doesn’t start up new processes for each query when it can use a long-running process. It doesn’t send data unnecessarily across process boundaries or from server to server.

Druid achieves this level of efficiency through its tightly integrated query engine and storage format, designed in tandem to minimize the amount of work done by each data server. Druid also has a distributed design that partitions tables into segments, balances those segments automatically between servers, quickly identifies which segments (or replicas of segments) are relevant to a query, and then pushes as much computation as possible down to individual data servers.

The result of this unique relationship between compute and storage is very high performance at any scale, even for data sets of multiple petabytes.

## Resilient and Durable

Druid is self healing, self balancing, and fault tolerant. It is designed to run continuously without planned downtime for any reason, even for configuration changes and software updates. It is also durable and will not lose data, even in the event of major systems failures.

Whenever needed, you can add servers to scale out or remove servers to scale down. The Druid cluster rebalances itself automatically in the background without any downtime. When a Druid server fails, the system automatically understands the failure and continues to operate.

As part of ingestion, Druid safely stores a copy of the data segment in deep storage, creating an automated, continuous additional copy of the data in cloud storage or HDFS. It both makes the segment immediately available for queries and creates a replica of each data segment. You can always recover data from deep storage, even in the unlikely case that all Druid servers fail. For a limited failure that affects only a few Druid servers, automatic rebalancing ensures that queries are still possible and data is still available during system recoveries. When using cloud storage, such as Amazon S3, durability is 99.999999999% or greater per year (or a loss of no more than 1 record per 100 billion).

## High Performance

The features of Druid combine to enable high performance at high concurrency by avoiding unneeded work. Pre-aggregated, sorted data avoids moving data across process boundaries or across servers and avoids processing data that isn’t needed for a query. Long-running processes avoid the need to start new processes for each query. Using indexes avoids costly reading of the full data set for each query. Acting directly on encoded, compressed data avoids the need to uncompress and decode. Using only the minimum data needed to answer each query avoids moving data from disk to memory and from memory to CPU.

In a paper published at the 22nd International Conference on Business Information Systems (May 2019), José Correia, Carlos Costa, and Maribel Yasmina Santos benchmarked performance of Hive, Presto, and Druid using a TPC-H-derived test of 13 queries run against a denormalized star schema on a cluster of 5 servers, each with an Intel i5 quad-core processor and 32 GB memory. Druid performance was measured as greater than 98% faster than Hive and greater than 90% faster than Presto in each of six test runs, using different configurations and data sizes. For Scale Factor 100 (a 100 GB database), for example, Druid required 3.72s, compared with 90s for Presto and 424s for Hive.

![Hive  Presto  and Druid results from](https://learning.oreilly.com/api/v2/epubs/urn:orm:book:9781098146597/files/assets/brta_0110.png)

In November 2021, Imply published the results of a benchmark using the same star schema benchmark, with Druid on a single AWS c5.9xlarge instance (36 CPU and 72 GB memory) at Scale Factor 100 (a 100 GB database). The 13 queries executed in a total of 0.747s.

## High Concurrency

High concurrency was one of the original design goals for Druid, and many Druid clusters are supporting hundreds of thousands of queries per second.

The key to Druid concurrency is the unique relationship between storage and compute resources. Data is stored in segments, which are scanned in parallel by scatter/gather queries. Usually, scanning each segment requires about 250ms and rarely more than 500ms.

In Druid, there is no need to lock segments, so when multiple queries are trying to scan the same segment, the resources are released to a new query immediately upon scan completion. This keeps the computation time on each segment very small and enables a very high number of concurrent queries.

In addition, Druid automatically caches query results per segment from historical data while not caching, by default, data from fast-changing stream data. This further reduces query times and computation loads.

One of many examples of Druid concurrency was published by Nielsen Marketing, which compared response time as a function of concurrency in Druid with their previous Elasticsearch architecture.

Note that with 10 concurrent queries, average response time was 280ms. Increasing this twelvefold to 120 concurrent queries in Druid only increased the average response time by 18%. The contrast with Elasticsearch is clear.

## High-Speed Data Ingestion

In Druid,  *ingestion*, sometimes called *indexing*, is loading data into the database. Druid reads data from source systems, whether files or streams, and stores the data in segments.

The ingestion process both creates tables and loads data into them. All tables are always fully indexed, so there is no need to explicitly create or manage indexes.

When data is ingested into Druid, it is automatically indexed, partitioned, and, optionally, partially pre-aggregated. Compressed **bitmap** indexes enable fast filtering and searching across multiple columns. Data is partitioned by time and other fields.

## Stream Ingestion

Druid was specifically created to enable real-time analytics of stream data, which begins with stream ingestion. Druid includes built-in indexing services for both Apache Kafka and Amazon Kinesis, so additional stream connectors are not needed.

Stream data is immediately queryable by Druid as each event arrives.

Supervisor processes run on Druid management nodes to manage the ingestion processes, coordinating indexing processes on data nodes that read stream events and guarantee *exactly-once ingestion*. The indexing processes use the partition and offset mechanisms found in Kafka and the shard and sequence mechanisms found in Kinesis.

If there is a failure during stream ingestion, for example, a server or network outage on a data or management node, Druid automatically recovers and continues to ingest every event exactly once, even events that arrive during the outage. No data is lost.

## Batch Ingestion

It’s often useful to combine real-time stream data with historical data. Batch ingestion is used for loading the latter type of data. This approach to loading data is known as batch ingestion. Some Druid implementations use entirely historical files. Data from any source can take advantage of the interactive data conversations, easy scaling, high performance, high concurrency, and high reliability of Druid.

Druid usually ingests data from object stores—which include HDFS, Amazon S3, Azure Blob, and Google Cloud Storage—or from local storage. The datafiles can be in a number of common formats, including JSON, CSV, TSV, Parquet, ORC, Avro, or Protobuf. Druid can ingest directly from both standard and compressed files, using formats including  *.gz* ,  *.bz2* ,  *.xz* ,  *.zip* ,  *.sz* , and  *.zst* .

The easiest way to ingest batch data is with a SQL statement, using `INSERT INTO`. Since this uses SQL, the ingestion can also include whatever SQL statements are desired to filter, combine, or aggregate the data (`WHERE`, `JOIN`, `GROUP BY`, and others) as part of **ingestion.**

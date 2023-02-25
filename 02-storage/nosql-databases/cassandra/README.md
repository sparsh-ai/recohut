# Cassandra

> *Apache Cassandra is an open source, distributed, decentralized, elastically scalable, highly available, fault-tolerant, tuneably consistent, row-oriented database. Cassandra bases its distribution design on Amazon’s Dynamo and its data model on Google’s Bigtable, with a query language similar to SQL. Created at Facebook, it now powers cloud-scale applications across many industries.*

Cassandra first started as an Incubator project at Apache in January of 2009. Shortly thereafter, the committers, led by Apache Cassandra Project Chair Jonathan Ellis, released version 0.3 of Cassandra, and steadily made releases up to the milestone 3.0 release. Since 2017, the project has been led by Apache Cassandra Project Chair Nate McCall, producing releases 3.1 through the latest 4.0 release. Cassandra is being used in production by some of the biggest companies on the web, including Facebook, Twitter, and Netflix.

Its popularity is due in large part to the outstanding technical features it provides. It is durable, seamlessly scalable, and tuneably consistent. It performs blazingly fast writes, can store hundreds of terabytes of data, and is decentralized and symmetrical so there’s no single point of failure. It is highly available and offers a data model based on the Cassandra Query Language (CQL).

For example, at Netflix, Cassandra runs 30 million ops/second on its most active single cluster and 98% of streaming data is stored on Cassandra. Apple runs 160,000+ Cassandra instances with thousands of clusters.

There are eight features that makes Cassandra powerful:

1. **Big data ready:** Partitioning over distributed architecture makes the database capable of handling data of any size: at petabyte scale. Need more volume? Add more nodes.
2. **Read-write performance:** A single node is very performant, but a cluster with multiple nodes and data centers brings throughput to the next level. Decentralization (leaderless architecture) means that every node can deal with any request, read or write.
3. **Linear scalability:** There are no limitations on volume or velocity and no overhead on new nodes. Cassandra scales with your needs.
4. **Highest availability:** Theoretically, you can achieve 100% uptime thanks to replication, decentralization and topology-aware placement strategy.
5. **Self-healing and automation:** Operations for a huge cluster can be exhausting. Cassandra clusters alleviate a lot of headaches because they are smart — able to scale, change data replacement, and recover — all automatically.
6. **Geographical distribution:** Multi-data center deployments grant an exceptional capability for disaster tolerance while keeping your data close to your clients, wherever they are in the world.
7. **Platform agnostic:** Cassandra is not bound to any platform or service provider, which allows you to build hybrid-cloud and multi-cloud solutions with ease.
8. **Vendor independent:** Cassandra doesn’t belong to any of the commercial vendors but is offered by a non-profit open-source Apache Software Foundation, ensuring both open availability and continued development.

### How does Cassandra work?

In Cassandra, all servers are created equal. Unlike traditional architecture, where there’s a leader server for write/read and follower servers for read-only, leading to a single point of failure, Cassandra’s leader-less (peer to peer) architecture distributes data across multiple nodes within clusters (also known as data centers or rings).

A node represents a single instance of Cassandra, and each node stores a few terabytes of data. Nodes “gossip” or exchange state information about itself and other nodes across the cluster for data consistency. When one node fails, the application contacts another node, ensuring 100% uptime.

In Cassandra, data is replicated. The replication factor (RF) represents the number of nodes used to store your data. If RF = 1, every partition is stored on one node. If RF = 2, then every partition is stored on two nodes, and so on. The industry standard is a replication factor of three, though there are cases that call for using more or fewer nodes.

Cassandra uses key-based partitioning. The main components of Cassandra’s data structure include:

1. **Keyspace:** A container of data, similar to a schema, which contains several tables.
2. **Table:** A set of columns, primary key, and rows storing data in partitions.
3. **Partition:** A group of rows together with the same partition token (a base unit of access in Cassandra).
4. **Row:** A single, structured data item in a table.

Cassandra stores data in partitions, representing a set of rows in a table across a cluster. Each row contains a partition key — one or more columns that are hashed to determine how data is distributed across the nodes in the cluster.

Why partitioning? Because this makes scaling so much easier! Big Data doesn’t fit in a single server. Instead, it’s split into chunks that are easily spread over dozens, hundreds or even thousands of servers, adding more if needed.

Once you set a partition key for your table, a partitioner transforms the value in the partition key to tokens (also called hashing) and assigns every node with a range of data called a token range.

Cassandra then distributes each row of data across the cluster by the token value automatically. If you need to scale up, just add a new node, and your data gets redistributed according to the new token range assignments. On the flip side, you can also scale down hassle-free.

Data architects need to know how to create a partition that returns queries accurately and quickly before they create a data model. Once you’ve set a primary key for your table, it cannot be changed. Instead, you’ll need to create a new table and migrate all the new data.

### The CAP theorem: is Cassandra AP or CP?

Any database system, including Cassandra, has to guarantee partition tolerance: It must continue to function during data losses or system failures. To achieve partition tolerance, databases have to either prioritize consistency over availability “CP,” or availability over consistency or “AP”.

Cassandra is usually described as an “AP” system, meaning it errs on the side of ensuring data availability even if this means sacrificing consistency. But that’s not the whole picture. Cassandra is configurably consistent: You can set the Consistency Level you need and tune it to be more AP or CP according to your use case.

### CQL vs. SQL

If you are familiar with SQL, CQL may look quite similar. Indeed, there are many syntactic similarities between the two languages, but there are also many important differences. Here are just a few facts about CQL that highlight some of the differences:

- CQL supports tables with single-row and multi-row partitions
- CQL table primary key consists of a mandatory partition key and an optional clustering key
- CQL does not support referential integrity constraints
- CQL updates or inserts may result in upserts
- CQL queries cannot retrieve data based on an arbitrary table column
- CQL supports no joins or other binary operations
- CQL CRUD operations are executed with a tunable consistency level
- CQL supports lightweight transactions but not ACID transactions

### Amazon Keyspaces

Watch this video: https://www.youtube.com/watch?v=PYdLIvBHe2E

## References

1. [Introduction to Apache Cassandra - the “Lamborghini” of the NoSQL World](https://bit.ly/3fsVUAR)
2. [Apache Cassandra Database – Full Course for Beginners](https://youtu.be/J-cSy5MeMOA)
3. [Overview of Amazon Keyspaces](https://youtu.be/PYdLIvBHe2E) [[Long](https://youtu.be/KPh_8DeRgxQ)]
4. [Cassandra Case Studies](https://cassandra.apache.org/_/case-studies.html)
5. [Cassandra Case Studies](https://cassandra.apache.org/_/case-studies.html)
6. [AWS re:Invent 2020: Running Apache Cassandra workloads with Amazon Keyspaces](https://youtu.be/KPh_8DeRgxQ)

# NoSQL Databases

## Cassandra

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

### Makefile

```makefile
connect:
	import os
	from cassandra.cqlengine.models import Model
	from cassandra.cqlengine import columns
	from datetime import datetime
	import pandas as pd
	from datetime import datetime

	from cassandra.cqlengine.management import sync_table
	from cassandra.policies import TokenAwarePolicy
	from cassandra.auth import PlainTextAuthProvider
	from cassandra.cluster import (
		Cluster,
		DCAwareRoundRobinPolicy
	)
	from cassandra.cqlengine.connection import (
		register_connection,
		set_default_connection
	)

	CASSANDRA_USERNAME='cassandra'
	CASSANDRA_PASSWORD='cassandra'
	CASSANDRA_HOST='127.0.0.1'
	CASSANDRA_PORT=9042
	session = None
	cluster = None

	auth_provider = PlainTextAuthProvider(username=CASSANDRA_USERNAME, password=CASSANDRA_PASSWORD)
	cluster = Cluster([CASSANDRA_HOST],
	load_balancing_policy=TokenAwarePolicy(DCAwareRoundRobinPolicy()),
	port=CASSANDRA_PORT,
	auth_provider=auth_provider,
	executor_threads=2,
	protocol_version=4,
	)   

	session = cluster.connect()
	register_connection(str(session), session=session)
	set_default_connection(str(session))
	rows = session.execute('select * from demo.click_stream;')
	df = pd.DataFrame(list(rows))
	df.head()
```

### Install Cassandra

```sh
wget https://dlcdn.apache.org/cassandra/4.0.6/apache-cassandra-4.0.6-bin.tar.gz

tar -xvf apache-cassandra-4.0.6-bin.tar.gz

mv apache-cassandra-4.0.6 ~/cassandra
```

Add `export PATH="$HOME/cassandra/bin:$PATH"` in your bash profile. Validate by running `cassandra --version`. It will show `4.0.6`.

Congratulations! Now your Cassandra server should be up and running with a new single-node cluster called “Test Cluster,” ready to interact with other nodes and clients.

- Run server: `cassandra -f`

### Install DataStax Bulk Loader

```sh
wget https://downloads.datastax.com/dsbulk/dsbulk-1.10.0.tar.gz

tar -xvf dsbulk-1.10.0.tar.gz

mv dsbulk-1.10.0 ~/dsbulk

rm dsbulk-1.10.0.tar.gz
```

Add `export PATH="$HOME/dsbulk/bin:$PATH"` in your bash profile.

### To download and install JVM

1. Go to https://www.oracle.com/java/technologies/downloads/#java8-mac or https://download.oracle.com/otn/java/jdk/8u341-b10/424b9da4b48848379167015dcc250d8d/jdk-8u341-macosx-x64.dmg (for mac users)
2. Install the downloaded package
3. Run these commands to set java path

```sh
/usr/libexec/java_home
export JAVA_HOME=$(/usr/libexec/java_home)
source .bash_profile
```

### Explore Further

1. [Introduction to Apache Cassandra - the “Lamborghini” of the NoSQL World](https://bit.ly/3fsVUAR)
2. [Apache Cassandra Database – Full Course for Beginners](https://youtu.be/J-cSy5MeMOA)
3. [Overview of Amazon Keyspaces](https://youtu.be/PYdLIvBHe2E) [[Long](https://youtu.be/KPh_8DeRgxQ)]
4. [Cassandra Case Studies](https://cassandra.apache.org/_/case-studies.html)
5. [Cassandra Case Studies](https://cassandra.apache.org/_/case-studies.html)
6. [AWS re:Invent 2020: Running Apache Cassandra workloads with Amazon Keyspaces](https://youtu.be/KPh_8DeRgxQ)

## Amazon Keyspaces

Watch this video: https://www.youtube.com/watch?v=PYdLIvBHe2E

## BigTable

### High-throughput streaming with Cloud Bigtable

Watch this video: https://www.youtube.com/watch?v=EsOREMES9N0

### Optimizing Cloud Bigtable performance

Watch this video: https://www.youtube.com/watch?v=1EQJNWcjMQ8

## DynamoDB

### Getting Started with DynamoDB

1. [DynamoDB Explained](https://www.dynamodbguide.com/)
2. [Best practices for designing and architecting with DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/best-practices.html)
3. [Various Examples and AWS SDK code examples for Amazon DynamoDB](https://github.com/aws-samples/aws-dynamodb-examples)
4. [The DynamoDB Book](https://knowledgetree.notion.site/The-DynamoDB-Book-Shared-8e9346036a704e0da2765f4c8cfe1153)

### Data Modeling with DynamoDB

1. [AWS DynamoDB Tutorial for Beginners](https://youtu.be/2k2GINpO308)
2. [AWS DynamoDB Tutorial](https://youtu.be/k0fcbRj_pZE)
3. [Deep-dive into the NoSQL, serverless scaling of Amazon DynamoDB](https://bit.ly/3flUatm)
4. [DynamoDB Office Hours: Modeling an online banking service](https://youtu.be/sBpgH5RFAlQ)

## Apache CouchDB

Apache CouchDB is an open source [NoSQL](https://www.ibm.com/in-en/topics/cloud-database "cloud-database") document database that collects and stores data in JSON-based document formats. Unlike relational databases, CouchDB uses a schema-free data model, which simplifies record management across various computing devices, mobile phones, and web browsers.

CouchDB was introduced in 2005 and later became an Apache Software Foundation project in 2008. As an open source project, CouchDB is supported by an active community of developers who continuously improve the software with a focus on ease of use and embracing the web.

## MongoDB

```makefile
install:
	wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
	tar -xf mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
	export PATH=$PATH:/home/project/mongodb-database-tools-ubuntu1804-x86_64-100.3.1/bin

start_server:
	start_mongo

connect:
	mongo -u <username> -p <password> --authenticationDatabase admin local
	mongosh "mongodb+srv://cluster0.mongodb.net/myFirstDatabase" --apiVersion 1 --username admin

version:
	db.version()
	mongoimport --version
	mongoexport --version

list_databases:
	show dbs

create_database:
	use training

create_collection:
	db.createCollection("mycollection")

list_collections:
	show collections

insert_record:
	db.mycollection.insert({"color":"white","example":"milk"})

import_data:
	mongoimport -u <username> --authenticationDatabase admin --db catalog --collection <collection_name> --file <filename>

	mongoimport --uri "mongodb+srv://admin:@cluster0.mongodb.net/catalog?retryWrites=true&w=majority" --collection electronics --drop --file data/catalog.json

export_data:
	mongoexport -u <username> --authenticationDatabase admin --db=catalog --collection=<collection_name> --type=csv --fields=_id,type,model --out=<filename.csv>
```

## Labs

1. Fundamentals of Apache Cassandra
2. [Getting started with Cassandra](02-storage/nosql-databases/lab-getting-started-with-cassandra/)
3. [Streaming Data Processing - Streaming Data Pipelines into GCP Bigtable](02-storage/nosql-databases/bigtable/lab-gcp-streaming-bigtable/)
4. [Cassandra on Cloud with Amazon Keyspaces](02-storage/nosql-databases/lab-amazon-keyspaces/)
5. [Fundamentals of DynamoDB](02-storage/nosql-databases/lab-intro-to-dynamodb/)
6. [Getting started with MongoDB](02-storage/nosql-databases/lab-mongodb-basics/)
7. [Ingest Movies data into CouchDB database](02-storage/nosql-databases/lab-couchdb-movies-data-migration/)

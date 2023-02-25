# Data Lakehouses

![lakehouse-architecture](https://user-images.githubusercontent.com/62965911/216760249-832980a9-2e58-4c7f-8dcf-a482cadc2415.png)

Table formats are instrumental for getting the scalability benefits of the data lake and the underlying object store, while at the same time getting the data quality and governance associated with data warehouses. Previously, users had to pick one or the other, or replicate data from a lake to the warehouse and hope (or pray) that it stays up-to-date. But by using a table format, lakehouse users don’t have to accept tradeoffs and get the benefits of both.

Three table formats have emerged over the past few years to power data lakehouses. Apache Iceberg was created by engineers at Netflix and Apple who were tired of trying to use Apache Hive’s metastore to track data updates and manage transactions. [Databricks](https://www.databricks.com/) created its own table format to live at the heart of its Delta Lake offering, and then open sourced it. Apache Hudi, meanwhile, was created by engineers at Uber to provide support for transactions for a massive data lake running on Hadoop.

The whole elevator pitch for lakehouse is ACID transactions. Not to turn it into an OLTP database, but is the data that we’re doing these analytics on or building these machine learning models on–is this valid data? Is it consistent? Or are we basically chasing our tail? That was the real driver of this. From that, you then get all the other goodies, like now with a table structure, we can do much more granular governance. Arguably there are ways to basically accelerate processing Parquet. But basically with tables, you can get much better performance that you can through file scans than you can with something like Impala.

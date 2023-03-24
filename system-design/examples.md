# System Design Examples

## BookMyShow

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2022/11/25/BMS_Arch.png)

> Reference - [How BookMyShow saved 80% in costs by migrating to an AWS modern data architecture](https://aws.amazon.com/blogs/big-data/how-bookmyshow-saved-80-in-costs-by-migrating-to-an-aws-modern-data-architecture/)

## Jeevansathi

![jeevansathi_datalake](https://user-images.githubusercontent.com/62965911/215028720-51313643-9cdb-435b-9b2c-f187411ea47e.jpeg)

The data is mainly collected via three sources, i.e., RDBMS, MongoDB, and through websites and apps. This data is loaded into the data lake in batches or in real-time with the help of various tools like Maxwell-Daemon, Apache Sqoop, MongoExport, Change Stream, etc.

### Ingestion Tier

#### RDBMS

There are mainly two types of data that need to be ingested from RDBMS, i.e., historical data that is already present in the DB and transactional data which comes in real-time.

1. Historical Data: The historical data is imported from DB via Apache Sqoop and stored in the HDFS file system. This data is then stored into AWS S3 with the help of Spark Jobs in parquet format after pre-processing.
2. Real-Time Data: The real-time data is imported using Maxwell’s Daemon, which reads the MySql BinLogs and writes to Kafka topics in JSON format. With the help of Apache Spark (Structured Streaming and Batch Write), this data is also stored in AWS S3 in parquet format. We have a generic binlog collection pipeline with the help of Maxwell, Kafka, and Spark.

#### MongoDB

Similar to RDBMS, both historical and real-time data need to be ingested from MongoDB as well.

1. Historical Data: The historical data is imported from MongoDB into the file system with the help of the mongo export tool. This data is then stored into AWS S3 using Spark Jobs in parquet format after pre-processing it.
2. Real-Time Data: The real-time data is imported using MongoDB Change Stream Connector which reads the change events and writes to Kafka topics. With the help of Apache Spark (Structured Streaming and Batch Write), this data is also stored in AWS S3 in parquet format.

#### Website/Apps

We have a Java service that collects data from our application and website. This data is collected based on the name of the event. We have one end-point for the data collection. On the basis of event-name, this data is segregated into different Kafka topics. As per the requirement, the data is persisted in AWS S3, MongoDB, and Clickhouse DB.

### Preparation Tier

- Data collected from multiple sources is aggregated, cleansed, and manipulated in order to make it available for further analysis.
- Using different spark jobs, we read data from AWS S3, transform it and then persist it into AWS S3, Clickhouse DB, MongoDB, and RDBMS as per the use cases.
- This includes persisting data into different file formats, compressing it, and partitioning it for faster access. The tools and file formats that we use provide a very high compression ratio as the data is saved in columnar format.
- We use AWS S3 as cold storage as well for the data persisted in Clickhouse for a longer period of time but not used frequently.
- We use delta lakes for taking transaction(ACID) support in Data Lake for real-time processing of some algorithms.

### Consumption Tier

- When Data is in Data Lake, it is ready to use for operations, decision-making systems, and live applications.
- We have a java service that serves this data to the live application as per the use cases to make a personalized experience for the user on the application.
- We have integrated Apache Superset, with the Clickhouse DB. This tool helps the teams in reporting, data analysis, and extracting information and hence make data-driven decisions.
- We have multiple algorithms that consume this data to run multiple logic and serve the results to applications for different use cases like match-making, spammers identifications, inactivity notifications, etc.
- With the help of our ingestion pipelines and Apache Spark, we have implemented match-making algorithms which is the backbone of Jeevansathi as the slogan of Jeevansathi says that “WE MATCH BETTER”.
- Similarly, with the help of Delta Lakes and Apache Spark, we have been able to block the spammers in real-time. With the support of ACID transactions and schema enforcement, Delta Lake provides the reliability that traditional Data Lake lack.
- We have an algorithm for increasing verified profiles on the platform with the help of mass push notifications based on user activity.

### Conclusion

Data Lake empowers us to make our user experience more personalized on our application. It helps us to identify the user’s needs and work on them quickly.

It has removed the use of transactional systems for data analysis. Resulting in 95% less storage, use of the cloud as cold storage for less frequently used data, high querying speed, and run-time data transformations.

It has empowered us to identify spam users in real-time, allowing them no time to cause chaos on the system or create a bad experience for genuine users.

It has helped us to eliminate the load from the database and reduce the computation time manifold to generate recommendations for our users.

It has empowered us to send notifications to the mass population of users based on the analysis of activity that requires a big amount of data to be analyzed.

### Future Scope

We have a user-driven approach in our business. Our vision is to provide a smooth, clean and personalized experience to our users. We have the vision to leverage our data lake system to personalize user experience, AI-driven approach for matchmaking and other user cases, and create user funneling so that we can find bottlenecks that create problems for our users as quickly as possible.

We want to move toward an intelligent notification system, a data-driven decision-making system that will help us to take business decisions quickly.

The use of Data Lake for Jeevansathi has helped us to create an intelligent, data-driven, faster, and more accessible system. Foundation is ready and we are ready to fly high by leveraging our data lake to create a user-centric system.
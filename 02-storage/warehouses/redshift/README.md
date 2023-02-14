# Amazon Redshift

## Steps

1. [Lab: Connect to Amazon Redshift Cluster using Python](./lab-redshift-python/)
1. [Lab: Copy Data from S3 into Amazon Redshift](./lab-copy-from-s3/)
1. [Lab: Implement a slowly changing dimension in Amazon Redshift](./lab-redshift-scd/)
1. [Lab: Credit Card Fraud detection in Amazon Redshift](./lab-redshift-ml/)
1. [Lab: Taxi Data Process and Save to Redshift using AWS Wrangler](./lab-redshift-taxi/)
1. [Project: Sales Order Analytics with Amazon Redshift](./project-redshift-sales/)

## Note

Amazon Redshift is a data warehousing service optimized for **online analytical processing** (**OLAP**) applications. You can start with just a few hundred **gigabytes** (**GB**) of data and scale to a **petabyte** (**PB**) or more. Designing your database for analytical processing lets you take full advantage of Amazon Redshift's columnar architecture.

An analytical schema forms the foundation of your data model. You can choose a star or snowflake schema by using Normalized, Denormalized, or Data Vault data modeling techniques. Redshift is a relational database management system (RDBMS) that supports a number of data model structures, including dimensional, denormalized, and aggregate (rollup) structures. This makes it optimal for analytics.

Watch this video: https://www.youtube.com/watch?v=lWwFJV_9PoE

### Data Ingestion in Amazon Redshift

Data ingestion is the process of getting data from the source system to Amazon Redshift. This can be done by using one of many AWS cloud-based ETL tools like AWS Glue, Amazon EMR, or AWS Step Functions, or you can simply load data from Amazon Simple Storage Service (Amazon S3) to Amazon Redshift using the COPY command. A COPY command is the most efficient way to load a table because it uses the Amazon Redshift massively parallel processing (MPP) architecture to read and load data in parallel from a file or multiple files in an S3 bucket.

Now SQL users can easily automate data ingestion from Amazon S3 to Amazon Redshift with a simple SQL command using the Amazon Redshift auto-copy feature. COPY statements are triggered and start loading data when Amazon Redshift auto-copy detects new files in the specified Amazon S3 paths. This also ensures end-users have the latest data available in Amazon Redshift shortly after the source data is available.

Copy jobs have the following benefits:

- SQL users such as data analysts can now load data from Amazon S3 automatically without having to build a pipeline or using an external framework
- Copy jobs offer continuous and incremental data ingestion from an Amazon S3 location without the need to implement a custom solution
- This functionality comes at no additional cost
- Existing COPY statements can be converted into copy jobs by appending the JOB CREATE <job_name> parameter
- It keeps track of all loaded files and prevents data duplication
- It can be easily set up using a simple SQL statement and any JDBC or ODBC client

### References

4. [Accelerate Application Development with Real Time Streams in Amazon Redshift](https://bit.ly/3Se99Ur)
5. [Data Engineering at Udemy](https://www.slideshare.net/ankarabigdata/data-engineering-at-udemy?qid=d835f0e3-f290-4445-bd19-d6ac6824e24c&v=&b=&from_search=5)
6. [Implement a slowly changing dimension in Amazon Redshift](https://aws.amazon.com/blogs/big-data/implement-a-slowly-changing-dimension-in-amazon-redshift/)
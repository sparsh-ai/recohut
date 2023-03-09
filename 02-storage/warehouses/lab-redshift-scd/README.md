# Implement a slowly changing dimension in Amazon Redshift

Follow [this](https://aws.amazon.com/blogs/big-data/implement-a-slowly-changing-dimension-in-amazon-redshift/) tutorial.

This tutoiral walks you through the process of implementing SCDs on an Amazon Redshift cluster. It goes through the best practices and anti-patterns. To demonstrate this, it uses the customer table from the TPC-DS benchmark dataset. It shows how to create a type 2 dimension table by adding slowly changing tracking columns, and go over the extract, transform, and load (ETL) merge technique, demonstrating the SCD process.

The following figure is the process flow diagram:

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2021/09/27/BDB-1563-image001.png)

The following diagram shows how a regular dimensional table is converted to a type 2 dimension table:

![](https://d2908q01vomqb2.cloudfront.net/b6692ea5df920cad691c20319a6fffd7a4a766b8/2021/09/27/BDB-1563-image003.png)


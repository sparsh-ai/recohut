# Lab: Implementing the Serving Layer Star Schema

In this lab, we will learn about implementing the serving layer, which involves implementing star schemas, techniques to read and write different data formats, sharing data between services such as SQL and Spark, and more. Once you complete this lab, you should be able to understand the differences between a Synapse dedicated SQL pool versus traditional SQL systems for implementing the Star schema, the various ways of accessing Parquet data using technologies such as Spark and SQL, and the details involved in storing metadata across services. All this knowledge should help you build a practical and maintainable serving layer in a data lake.

We will cover the following topics in this lab:

- Delivering data in a relational star schema
- Implementing a dimensional hierarchy
- Delivering data in Parquet files
- Maintaining metadata

## Technical requirements

For this lab, you will need the following:

- An Azure account (free or paid)
- An active Synapse workspace

Let's get started.

## Delivering data in a relational star schema

In this recipe, we will learn how to implement a star schema in Synapse SQL and deliver data from it.

Star schemas have two types of tables, **fact tables** and **dimensional tables**. Fact tables are usually much higher in volume than the dimension tables and hence would benefit from using a **hash distribution** with **clustered columnstore indexing**. On the other hand, dimension tables are smaller and can benefit from using **replicated tables**.

IMPORTANT NOTE

Synapse dedicated SQL pools didn't support **foreign key** constraints at the time of development of this lab. Hence, the responsibility of maintaining data integrity falls on the applications.

Let's consider the **Imaginary Airport Cabs** (**IAC**) cab rides example for our star schema. We have the following tables in this design:

- **FactTrips**
- **DimDriver**
- **DimCustomer**
- **DimCab**
- **DimDate**

Let's see how to implement these tables.

- In the Synapse screen, create a new SQL pool from the **Manage** tab, as shown in the following screenshot. Click on the **+New** symbol and fill in the details to create a new dedicated SQL pool.

![B17525_07_01](https://user-images.githubusercontent.com/62965911/218294867-6f115513-ea35-4c12-bf96-90644d5e3a7b.jpg)

- Next, create a new SQL script from the **Editor** tab by clicking on the **+** sign, as shown in the next screenshot:

![B17525_07_02](https://user-images.githubusercontent.com/62965911/218294869-4bacd6c1-3987-49b9-90cc-5597c8214cb0.jpg)

- In the SQL editor, you can enter SQL commands to create tables representing the star schema. You can use the **COPY INTO** statement to populate the tables. The fact and dimension tables will have the same syntax for loading information. And, finally, query from the star schema tables. Here is a sample query to get the list of all customers whose end location was **'San Jose'**:

```sql
-- Example for creating a Star schema 

-- Create the Fact Table. In our case it would be the TripTable
DROP TABLE dbo.FactTrips;

CREATE TABLE dbo.FactTrips
(
    [tripId] INT NOT NULL,
    [driverId] INT NOT NULL,
    [customerId] INT NOT NULL,
    [tripdate] INT,
    [startLocation] VARCHAR (40),
    [endLocation] VARCHAR (40)
 )
 WITH
 (
    CLUSTERED COLUMNSTORE INDEX,
    DISTRIBUTION = HASH ([tripId])
 )
GO

-- Insert some sample values. In reality the Fact tables will have Millions of rows.

 INSERT INTO dbo.FactTrips VALUES (101, 201, 301, 20220101, 'New York', 'New Jersey');
 INSERT INTO dbo.FactTrips VALUES (102, 202, 302, 20220101, 'Miami', 'Dallas');
 INSERT INTO dbo.FactTrips VALUES (103, 203, 303, 20220102, 'Phoenix', 'Tempe');
 INSERT INTO dbo.FactTrips VALUES (104, 204, 304, 20220204, 'LA', 'San Jose');
 INSERT INTO dbo.FactTrips VALUES (105, 205, 305, 20220205, 'Seattle', 'Redmond');
 INSERT INTO dbo.FactTrips VALUES (106, 206, 306, 20220301, 'Atlanta', 'Chicago');


-- Create the Customer Dimension table
DROP TABLE dbo.DimCustomer;

CREATE TABLE dbo.DimCustomer
(
    [customerId] INT NOT NULL,
    [name] VARCHAR(40) NOT NULL,
    [emailId] VARCHAR(40),
    [phoneNum] VARCHAR(40),
    [city] VARCHAR(40)
)
WITH
(
    CLUSTERED COLUMNSTORE INDEX,
    DISTRIBUTION = REPLICATE
)
GO

-- Another way of inserting data using COPY INTO
-- You will have to use the https format here instead of the abfss format
-- Copy the customer.csv file in this directory to the ADLS Gen2 location and use that path here.

COPY INTO dbo.DimCustomer
FROM 'https://sparshstorage1.blob.core.windows.net/dataloading/customer.csv'
WITH (
    FILE_TYPE='CSV',
    FIELDTERMINATOR=',',
    FIELDQUOTE='',
    ROWTERMINATOR='\n',
    ENCODING = 'UTF8',
    FIRSTROW = 2
);

SELECT * from dbo.DimCustomer;

-- Create a Driver Dimension table
CREATE TABLE dbo.DimDriver
(
    [driverId] INT NOT NULL,
    [firstName] VARCHAR(40),
    [middleName] VARCHAR(40),
    [lastName] VARCHAR(40),
    [city] VARCHAR(40),
    [gender] VARCHAR(40),
    [salary] INT
)
WITH
(
    CLUSTERED COLUMNSTORE INDEX,
    DISTRIBUTION = REPLICATE
)
GO

-- Insert some sample values

INSERT INTO dbo.DimDriver VALUES (210, 'Alicia','','Yang','New York', 'Female', 2000);
INSERT INTO dbo.DimDriver VALUES (211, 'Brandon','','Rhodes','New York','Male', 3000);
INSERT INTO dbo.DimDriver VALUES (212, 'Cathy','','Mayor','California','Female', 3000);
INSERT INTO dbo.DimDriver VALUES (213, 'Dennis','','Brown','Florida','Male', 2500);
INSERT INTO dbo.DimDriver VALUES (214, 'Jeremey','','Stilton','Arizona','Male', 2500);
INSERT INTO dbo.DimDriver VALUES (215, 'Maile','','Green','Florida','Female', 4000);

SELECT * from dbo.DimDriver;

DROP TABLE dbo.DimDate
-- Create the date dimension table
CREATE TABLE dbo.DimDate
(
    [dateId] INT NOT NULL,
    [date] DATETIME NOT NULL,
    [dayOfWeek] VARCHAR(40),
    [fiscalQuarter] VARCHAR(40)
)
WITH
(
    CLUSTERED COLUMNSTORE INDEX,
    DISTRIBUTION = REPLICATE
)
GO

INSERT INTO dbo.DimDate VALUES (20210101, '20210101','Saturday','Q3');
INSERT INTO dbo.DimDate VALUES (20210102, '20210102','Sunday','Q3');
INSERT INTO dbo.DimDate VALUES (20210103, '20210103','Monday','Q3');
INSERT INTO dbo.DimDate VALUES (20210104, '20210104','Tuesday','Q3');
INSERT INTO dbo.DimDate VALUES (20210105, '20210105','Wednesday','Q3');
```

Now run some sample queries

```sql
SELECT trip.[tripId], customer.[name] from 
dbo.FactTrips AS trip
JOIN dbo.DimCustomer AS customer
ON trip.[customerId] = customer.[customerId] 
WHERE trip.[endLocation] = 'San Jose';
```

As you can see, once we understand the concept of star schemas, creating them is as simple as creating tables in Synapse SQL.

You can learn more about Synapse SQL and schemas here: [https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-tables-overview](https://docs.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-tables-overview).

## Implementing a dimensional hierarchy

Let's look at the techniques available for reading and writing data in Parquet files.

![](https://user-images.githubusercontent.com/62965911/218298780-34ee67c4-ec50-42d8-a000-edbecc62c4e1.png)

The code is in the `./assets` folder.

## Maintaining metadata

Metastores are like data catalogs that contain information about all the tables you have, the table schemas, the relationships among them, where they are stored, and so on.

### Metadata using Synapse SQL and Spark pools

Synapse supports a shared metadata model. The databases and tables that use Parquet or CSV storage formats are automatically shared between the compute pools, such as SQL and Spark.

IMPORTANT NOTE

Data created from Spark can only be read and queried by SQL pools but cannot be modified as of now.

Let's look at an example of creating a database and a table using Spark and accessing it via SQL:

1. In the Synapse Spark notebook, create a sample table, as shown in the following screenshot:

![B17525_07_08](https://user-images.githubusercontent.com/62965911/218294882-b336953a-0691-4d66-99ff-73484bcaacd6.jpg)

Now, let's query the contents of the table from the SQL serverless pool.

IMPORTANT NOTE

This database will be synced asynchronously, so there might be a slight delay before you see the databases and tables in the SQL pool.

SQL serverless pool is an on-demand service, so all you need to do is just click on the **+** sign in the Synapse workspace page and select **SQL script** to create a new SQL editor, as shown in the following screenshot:

![B17525_07_09](https://user-images.githubusercontent.com/62965911/218294885-22c12346-1733-4fa9-91ad-d1da6e7d30c8.jpg)

Then, in the **Connect to** field, select the **Built-in** pool, as shown in the following screenshot:

![B17525_07_10](https://user-images.githubusercontent.com/62965911/218294886-fe417706-deea-4e58-868e-291285c6f8fd.jpg)

Now, just run a simple script to query the shared table; in the example, the shared table would be the **tripID** table:

![B17525_07_11](https://user-images.githubusercontent.com/62965911/218294888-51c67fb8-5470-4896-b5ee-11bcfa310178.jpg)

As you just noticed, the shared data model of Synapse makes it very easy to share data between SQL and Spark pools. Everything is already taken care of by Synapse and the data is readily made available to us.

You can learn more about maintaining metadata in Synapse here: [https://docs.microsoft.com/en-us/azure/synapse-analytics/metadata/overview](https://docs.microsoft.com/en-us/azure/synapse-analytics/metadata/overview).

Let's next explore how to work with metastores in Azure Databricks.

### Metadata using Azure Databricks

In order to share data between Spark and other services outside of Synapse, we have to make use of the Hive metastore. Spark uses the Hive metastore to share information with other services. Let's look at an example of sharing data between Azure Databricks Spark and Azure HDInsight Hive. The logic and steps for using an external Hive metastore would be similar for Synapse Spark too. Here are the steps:

We will need a standalone database that can be used by Spark to store the metadata. Let's use Azure SQL for this purpose. Create an Azure SQL database from the Azure portal. Search for **Azure SQL** from the portal search box and select it. Click on the **+ Create** option. You will see a screen, as shown in the following screenshot:

![B17525_07_12](https://user-images.githubusercontent.com/62965911/218294890-029b290a-3962-4a18-a6df-647eb83a6185.jpg)

- Select the **SQL databases** box and click the **Single database** option from the dropdown.
- You can create the database with pre-populated sample data so that we have ready-made data for experimentation. Select the **Sample** option for the **Use existing data** field, as shown in the following screenshot:

![B17525_07_13](https://user-images.githubusercontent.com/62965911/218294893-69e754ee-2282-4bb9-a6cf-4f9b57094e8f.jpg)

- Fill up the rest of the tabs and click on **Review + create** to create the Azure SQL database.
- Retrieve the JDBC connection string from the **Connection Strings** tab, as shown in the following screenshot, and save it in Notepad. We will need this information later:

![B17525_07_14](https://user-images.githubusercontent.com/62965911/218294895-759c3a11-d86b-41b9-a008-a14da27a14a7.jpg)

- Next, we have to create an **HDInsight** Hive cluster. By now, you might already know the process to instantiate any Azure service. Just search for **HDInsight** in the portal search bar and click on it. On the HDInsight portal home page, click on the **+ Create** link to open the create form and fill in the details.
- On the **Create HDInsight cluster** screen, you can choose either the **Hadoop** option or the **Interactive Query** option for **cluster type**, as both will install Hive. Refer to the next screenshot for the options available:

![B17525_07_15](https://user-images.githubusercontent.com/62965911/218294896-d6591494-c745-4055-bc1b-56e9fd27d06f.jpg)

- Once you have selected the type of cluster, fill up the rest of the fields on the **Basics** screen.
- In the **Storage** tab, under the **External metadata stores** section, provide the Azure SQL database that we created in the earlier steps as **SQL database for Hive**. The following screenshot shows the location:

![B17525_07_16](https://user-images.githubusercontent.com/62965911/218294897-e4c67860-47d2-4b03-98f1-b5bec500cb90.jpg)

- Complete the rest of the fields and then click on **Review + Create** to create the HDInsight cluster.
- Once the cluster is created, go to the Ambari home page from the HDInsight portal by clicking on the **Ambari home** link, as shown in the following screenshot:

![B17525_07_17](https://user-images.githubusercontent.com/62965911/218294899-ceebc268-a35e-45bf-ac84-43e572caf4c4.jpg)

- From the Ambari dashboard, click on **Hive view 2.0**, as shown in the following screenshot:

![B17525_07_18](https://user-images.githubusercontent.com/62965911/218294900-121dabcb-d1e5-4954-b237-6854e578dba8.jpg)

- Now, you should be able to see the **Hivesampletable** database in the Hive dashboard, as shown in the following screenshot:

![B17525_07_19](https://user-images.githubusercontent.com/62965911/218294902-ba49163d-1400-439f-869a-28724c7823bf.jpg)

- Now that we have the HDInsight cluster, we have to next create an Azure Databricks cluster. We have to create a new cluster with the following configurations. Let's see how to enter these configurations in the Spark create screen in the next step:

```
spark.sql.hive.metastore.version 2.1.1 // For HDInsight Interactive 2.1 version

spark.hadoop.javax.jdo.option.ConnectionUserName **`<Your Azure SQL Database Username>`**

spark.hadoop.javax.jdo.option.ConnectionURL **`<Your Azure SQL Database JDBC connection string>`**

spark.hadoop.javax.jdo.option.ConnectionPassword **`<Your Azure SQL Database Password>`**

spark.hadoop.javax.jdo.option.ConnectionDriverName com.microsoft.sqlserver.jdbc.SQLServerDriver

spark.sql.hive.metastore.jars **`<Location where you have copied the Hive Metastore Jars>`**

datanucleus.autoCreateSchema true

datanucleus.fixedDatastore false
```

Note that you will have to use the JDBC link that you had saved earlier, for the config that says **spark.hadoop.javax.jdo.option.ConnectionURL**.

- You will have to enter the configs in the **Spark Config** field on the **Create Cluster** page, as shown in the following screenshot:

![B17525_07_20](https://user-images.githubusercontent.com/62965911/218294905-15ab62ea-514e-4b40-9f89-657078c2059d.jpg)

IMPORTANT NOTE

Apart from the config fields, you will also have to download the Hive metastore JAR files and provide them a location where the Azure Databricks clusters can access them. Azure provides step-by-step instructions along with readymade scripts to easily download the JAR files here: [https://docs.microsoft.com/en-us/azure/databricks/_static/notebooks/setup-metastore-jars.html](https://docs.microsoft.com/en-us/azure/databricks/_static/notebooks/setup-metastore-jars.html).

- Once you have created the Spark cluster, you will be able to access the Hive Metastore tables directly from a Spark notebook. In the following screenshot, you can see how the Databricks Spark cluster is able to access the **HiveSampletable** table that we saw earlier using the Hive query view:

![B17525_07_21](https://user-images.githubusercontent.com/62965911/218294907-c79685ae-f97c-4663-b37a-e673f92accba.jpg)

Hurray! Now you know how to access metadata between Spark and Hive clusters using an external Hive metastore.

You can learn more about Azure Databricks metastores here: [https://docs.microsoft.com/en-us/azure/databricks/data/metastores/external-hive-metastore](https://docs.microsoft.com/en-us/azure/databricks/data/metastores/external-hive-metastore). With that, we have come to the end of this section and the lab. You should now be familiar with the different ways in which metadata can be shared across the SQL, Spark, and Hive services in Azure.

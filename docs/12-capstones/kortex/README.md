# Kortex

## Objectives

1. Demonstrate the skills required for an entry-level data engineering role.
1. Implement various concepts in the data engineering lifecycle.
1. Showcase working knowledge with Python, Relational Databases, NoSQL Data Stores, Big Data Engines, Data Warehouses, and Data Pipelines.

## Introduction

As part of the capstone project, you will assume the role of an Associate Data Engineer who has recently joined an e-commerce organization. You will be presented with a business challenge that requires building a data platform for retailer data analytics.

In this Capstone project, you will:

1. Design a data platform that uses MySQL as an OLTP database and MongoDB as a NoSQL database.
1. Design and implement a data warehouse and generate reports from the data.
1. Design a reporting dashboard that reflects the key metrics of the business.
1. Extract data from OLTP, and NoSQL databases, transform it and load it into the data warehouse, and then create an ETL pipeline.
1. And finally, create a Spark connection to the data warehouse, and then deploy a machine learning model.

In Module 1, you will design the OLTP database for an E-Commerce website, populate the OLTP Database with the data provided and automate  the export of the daily incremental data into the data warehouse.

In Module 2, you will set up a NoSQL database to store the catalog data for an E-Commerce website, load the E-Commerce catalog data into the NoSQL database, and query the E-Commerce catalog data in the NoSQL database.

In Module 3, you will design the schema for a data warehouse based on the schema of the OLTP and NoSQL databases. You’ll then create the schema and load the data into fact and dimension tables, automate the daily incremental data insertion into the data warehouse, and create Cubes and Rollups to make the reporting easier.

In Module 4, you will create a Cognos data source that points to a data warehouse table, create a bar chart of Quarterly sales of cell phones, create a pie chart of sales of electronic goods by category, and create a line chart of total sales per month for the year 2020.

In Module 5, you will extract data from OLTP, NoSQL, and MongoDB databases into CSV format. You will then transform the OLTP data to suit the data warehouse schema, and then load the transformed data into the data warehouse.

Finally, you will verify that the data is loaded properly.

In the sixth and final module, you will use your skills in Big Data Analytics to create a Spark connection to the data warehouse, and then deploy a machine learning model on SparkML for making sales projections.

## Module 1 - Data Platform Architecture and OLTP Database

In this assignment, you will perform three exercises with multiple tasks:

1. The first exercise requires you to design the schema for the OLTP database by storing data like row ID, product ID, customer ID, price, quantity, and time stamp of sale.
1. In the second exercise, you will load this data into the OLTP database by importing the data and then listing the tables in the database. You will also write a query to find out the count of records in the tables.
1. In the final exercise, you will automate admin tasks by creating an index on the timestamp field and listing all the indexes of salesdata table. You will also write a bash script that exports records created in the table into another file.

### Scenario

You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MySQL as an OLTP database. You will be using MySQL to store the OLTP data.

### Objectives

In this assignment you will:

- design the schema for OLTP database.
- load data into OLTP database.
- automate admin tasks.

### Assignment

1. Create a database named sales.
1. Design a table named `sales_data` based on the sample data given.
1. Create the sales_data table in `sales` database.
1. Import the data from sales_data.csv into `sales_data` table.
1. List the tables in the database `sales`.
1. Write a query to find out the count of records in the tables sales_data.
1. Create an index named `ts` on the timestamp field.
1. List indexes on the table sales_data.
1. Exports all the rows in the sales_data table to a file named `sales_data.sql`.
1. End of assignment.

## Module 2 - Querying Data in NoSQL Databases

In this assignment, you will

1. first import the JSON file to the MongoDB server into a database and a collection (electronics) then list out all the databases and the collections in the database catalog.
1. Next, you will list the first five documents in the collection, and then you will write a query to find the count of laptops, the number of mobile phones with a screen size of 6 inches, and the average screen size of smartphones.
1. Finally, you will export the ID, type, and model fields from the collection into a Comma Separated Values (CSV) file.

### Scenario

You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MongoDB as a NoSQL database. You will be using MongoDB to store the e-commerce catalog data.

### Objectives

In this assignment you will:

- Import data into a MongoDB database
- Query data in a MongoDB database
- Export data from MongoDB

### Assignment

1. Import `catalog.json` into mongodb server into a database named 'catalog' and a collection named 'electronics'.
1. List out all the databases.
1. List out all the collections in the database `catalog`.
1. Create an index on the field "type".
1. Write a query to find the count of laptops.
1. Write a query to find the number of `smart phones` with screen size of 6 inches.
1. Write a query to find out the average screen size of `smart phones`.
1. Export the fields `_id`, "type", "model", from the 'electronics' collection into a file named `electronics.csv`.
1. End of assignment.

## Module 3a - Data Warehousing

The e-commerce company has provided you with sample data. You will start your project by designing a Star Schema for the warehouse by identifying the columns for the various dimension and fact tables in the schema. You will name your database as softcart and then use the ERD design tool to design the table softcartDimDate using fields such as DateID, Month, Monthname, and so on. The company would like to have the ability to generate the report on a yearly, monthly, daily, and weekday basis.

The following tasks require you to design the dimension tables softcartDimCategory, softcartDimCountry, and softcartFactSales using the ERD design tool. Finally, you will use the ERD design tool to design the required relationships (one-to-one, one-to-many, and so on) amongst the tables.

In the second exercise, you will load the data into the data warehouse. Your senior Data Engineer has reviewed your design and made a few improvements to your schema design.

### Scenario

You are a data engineer hired by an ecommerce company named SoftCart.com. The company retails download only items like E-Books, Movies, Songs etc. The company has international presence and customers from all over the world. The company would like to create a data warehouse so that it can create reports like

-   total sales per year per country
-   total sales per month per category
-   total sales per quarter per country
-   total sales per category per country

You will use your data warehousing skills to design and implement a data warehouse for the company.

### Objectives

In this assignment you will:

- Design a Data Warehouse
- Create the schema in the Data Warehouse

### Assignment

1. Design the table `softcartDimDate`. The company is looking at a granularity of a day. Which means they would like to have the ability to generate the report on yearly, monthly, daily, and weekday basis.
1. Design tool design the table `softcartDimCategory`.
1. Design the table `softcartDimItem`.
1. Design the table `softcartDimCountry`.
1. Design the table `softcartFactSales`.
1. Design the required relationships(one-to-one, one-to-many etc) amongst the tables.
1. Download the schema sql from ERD tool and create the schema in a database named `staging`.
1. End of the assignment.

## Module 3b - Data Warehousing Reporting

The first exercise requires you to load the data provided by the company into the tables in CSV format by performing a series of tasks. You will load that data into the DimDate table, DimCategory table, DimCountry table, and fact table FactSales.

In the second exercise, you will query the loaded data by creating a grouping sets query, rollup query, and cube query using the columns Orderid*, Category, and Price collected. Finally, you will create an MQT named Total_sales_per_country using the country and total sales columns.

### Scenario

You are a data engineer hired by an ecommerce company named SoftCart.com . The company retails download only items like E-Books, Movies, Songs etc. The company has international presence and customers from all over the world. You have designed the schema for the data warehouse in the previous assignment. Data engineering is a team game. Your senior data engineer reviewed your design. Your schema design was improvised to suit the production needs of the company. In this assignment you will generate reports out of the data in the data warehouse.

### Objectives

In this assignment you will:

-   Load data into Data Warehouse
-   Write aggregation queries
-   Create MQTs

### Assignment

1. Load `DimDate.csv` into the dimension table `DimDate`.
1. Load `DimCategory.csv` into the dimension table `DimCategory`.
1. Load `DimCountry.csv` into the dimension table `DimCountry`.
1. Load `FactSales.csv` into the fact table `FactSales`.
1. Create a grouping sets query using the columns country, category, totalsales.
1. Create a rollup query using the columns year, country, and totalsales.
1. Create a cube query using the columns year, country, and average sales.
1. Create an MQT named total_sales_per_country that has the columns country and total_sales.
1. End of the assignment.

## Module 4 - Data Analytics

In this assignment, you will perform a couple of exercises with multiple tasks.

The first exercise requires you to load data into the data warehouse. You will first import data from the downloaded CSV file into a table and then list the first ten rows in the table.

In the second exercise, you will create a data source that points to the table in your database. In the final exercise, you will create a dashboard by performing tasks such as creating a bar chart of Quarterly sales of mobile phones, a pie chart of category-wise sales of electronic goods, and a line chart of month-wise total sales for the year 2020.

### Scenario

You are a data engineer at an e-commerce company. Your company has finished setting up a datawarehouse. Now you are assigned the responsibility to design a reporting dashboard that reflects the key metrics of the business.

### Objectives

In this assignment you will:

- Create a dashboard using Cognos Analytics

### Assignment

1. Load the `ecommerce.csv` data into a table named `sales_history`.
1. List the first 10 rows in the table `sales_history`.
1. Create a data source in Cognos that points to the table `sales_history`.
1. Create a line chart of month wise total sales for the year 2020.
1. Create a pie chart of category wise total sales.
1. Create a bar chart of Quarterly sales of mobile phones.
1. End of assignment.

## Module 5a - ETL using Python

The Data Warehouse gets information from several sources including the transactional (OLTP) database. Transactional data from the OLTP database (in this case MySQL) needs to be propagated to the Warehouse on frequent basis. This data movement can be updated using ETL processes.

In this first part of the assignment, you will setup an ETL process using Python to extract new transactional data for each day from the MySQL database, transform it and then load it into the data warehouse in Redshift.

You will begin by preparing the lab environment by starting the MySQL server. You will then create a sales database in MySQL and import the sales.sql into the sales database. You will then be uploading the sales.csv to a table in Redshift.

The final task requires you to automate the extraction of daily incremental data and load yesterday's data into the data warehouse. You will write a python script that automatically loads yesterday's data from the production database into the data warehouse.

### Scenario

You are a data engineer at an e-commerce company. You need to keep data synchronized between different databases/data warehouses as a part of your daily routine. One task that is routinely performed is the sync up of staging data warehouse and production data warehouse. Automating this sync up will save you a lot of time and standardize your process. You will be given a set of python scripts to start with. You will use/modify them to perform the incremental data load from MySQL server which acts as a staging warehouse to the Redshift which is a production data warehouse. This script will be scheduled by the data engineers to sync up the data between the staging and production data warehouse.

### Objectives

In this assignment you will write a python program that will:

-   Connect to Redshift data warehouse and identify the last row on it.
-   Connect to MySQL staging data warehouse and find all rows later than the last row on the datawarehouse.
-   Insert the new data in the MySQL staging data warehouse into the Redshift production data warehouse.

### Assignment

1. Create a database named `sales`.
1. Import the data in the file `sales.sql` into the `sales` database.
1. Modify `mysqlconnect.py` suitably and make sure you are able to connect to the MySQL server instance.
1. Modify `redshiftconnect.py` suitably and make sure you are able to connect to your Redshift warehouse.
1. Load `sales.csv` into a table named `sales_data` on your Redshift warehouse.
1. You will be using `automation.py` as a scafolding program to execute the tasks in this assignment.

**Automate loading of incremental data into the data warehouse**

One of the routine tasks that is carried out around a data warehouse is the extraction of daily new data from the operational database and loading it into the data warehouse. In this exercise you will automate the extraction of incremental data, and loading it into the data warehouse.

1. In the program `automation.py` implement the function get_last_rowid(). This function must connect to the Redshift data warehouse and return the last rowid.
1. In the program `automation.py` implement the function get_latest_records(). This function must connect to the MySQL database and return all records later than the given last_rowid.
1. In the program `automation.py` implement the function insert_records(). This function must connect to the Redshift data warehouse and insert all the given records.
1. Run the program `automation.py` and test if the synchronization is happening as expected.
1. End of the assignment.

## Module 5b - Data Pipelines using Apache AirFlow

Our data platform includes a Big Data repository that is used for analytics using Machine Learning with Apache Spark. This Big Data repository gets data from several sources including the Data Warehouse and the Web Server log. As data from the web server log is logged, it needs to be added to the Big Data system on a frequent basis - making it an ideal process to automate using a data pipeline.

In this second part of the assignment, you will create and run a DAG using Apache Airflow to extract daily data from the web server log, process it, and store it in a format to prepare it for loading into the Big Data platform.

To complete this part of the assignment, you will perform a couple of exercises. In the first exercise, you will perform a series of tasks to create a DAG that runs daily. You will create a task that extracts the IP address field from the webserver log file and then saves it into a text file. The next task should filter out all the occurrences of ipaddress "198.46.149.143" from text file and save the output to a new text file. In the final task creation, you will load the data by archiving the transformed text file into a TAR file. Before moving on to the next exercise, you will define the task pipeline as per the given details.

In the second exercise, you will get the DAG operational by saving the defined DAG into a PY file. Further, you will submit, unpause and then monitor the DAG runs for the Airflow console.

### Scenario

Write a pipeline that analyzes the web server log file, extracts the required lines(ending with html) and fields(time stamp, size ) and transforms (bytes to mb) and load (append to an existing file.)

### Objectives

In this assignment you will author an Apache Airflow DAG that will:

-   Extract data from a web server log file
-   Transform the data
-   Load the transformed data into a tar file

### Assignment

1. Start Apache Airflow.
1. Create a DAG named `process_web_log` that runs daily.
1. Create a task named `extract_data`. This task should extract the ipaddress field from the web server log file and save it into a file named extracted_data.txt.
1. Create a task named `transform_data`. This task should filter out all the occurrences of ipaddress "198.46.149.143" from extracted_data.txt and save the output to a file named `transformed_data.txt`.
1. Create a task named `load_data`. This task should archive the file `transformed_data.txt` into a tar file named `weblog.tar`.
1. Define the task pipeline as per the details given below:
    | Task | Functionality |
    | --- | --- |
    | First task | `extract_data` |
    | Second task | `transform_data` |
    | Third task | `load_data` |
1. Save the DAG you defined into a file named `process_web_log.py`.
1. Run the DAG.
1. End of the assignment.

## Module 6 - Big Data Analytics with Spark

In this assignment, you will perform a number of tasks to analyse search terms on the e-commerce webserver. You will run your analysis against a CSV file containing the webserver data. You will load this file into a Spark dataframe and print the results of your queries against this dataset. You will then load a pretrained sales forecasting model and use this to predict the sales for 2023.
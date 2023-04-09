# Realtime Streaming analytics with Apache Kafka and Spark Streaming

## Activity 1

Basketista is a retail company and they want to build a real-time analytics solution to get insights about their business orders and take decisions in near real-time environment.

![](https://user-images.githubusercontent.com/62965911/211325959-dec2aa5c-93c5-403d-9dbe-bb5fe0b8d45f.svg)

In this activity, you will:

1. Setup the Environment - Postgres, Kafka, Spark Streaming applications
2. Create Kafka Producer and send data to Kafka topic
3. Build ETL logic in PySpark and integrate in Spark Stream
4. Create Kafka Consumer and Store the procesed data in Postgres
5. Connect to Postgres and validate the data load

## Activity 2

The objective is to analyze the “retail_db” dataset, provide reports on the total completed orders, and perform customer and product analytics. This activity is designed to help understand the retail database and generate reports on the completed orders. You should be able to analyze the dataset for this activity to create a report. You will be able to use PySpark, do analyses, and obtain the desired results.

Problem Statement: Customers can purchase products or services from Amazon for consumption and usage. Amazon usually sells products and services in-store. However, some may be sold online or over the phone and shipped to the customer. Clothing, medicine, supermarkets, and convenience stores are examples of their retail operations.
 
Perform the following tasks on the dataset provided using PySpark:

1. Explore the customer records saved in the "customers-tab-delimited“ directory on HDFS
    - Show the client information for those who live in California
    - Save the results in the result/scenario1/solution folder
    - Include the customer's entire name in the output
2. Explore the order records saved in the “orders parquet” directory on HDFS
    - Show all orders with the order status value "COMPLETE“
    - Save the data in the "result/scenario2/solution" directory on HDFS
    - Include order number, order date, and current situation in the output
3. Explore the customer records saved in the "customers-tab- delimited“ directory on HDFS
    - Produce a list of all consumers who live in the city of "Caguas"
    - Save the results in the result/scenario3/solutionfolder
    - The result should only contain records with the value "Caguas" for the customer city
4. Explore the order records saved in the “categories” directory on HDFS
    - Save the result files in CSV format
    - Save the data in the result/scenario4/solution directory on HDFS
    - Use lz4 compression to compress the output
5. Explore the customer records saved in the “products_avro" directory on HDFS
    - Include the products with a price of more than 1000.0 in the output
    - Remove data from the table if the product price is greater than 1000.0
    - Save the results in the result/scenario5/solution folder
6. Explore the order records saved in the “products_avro” directory on HDFS
    - Only products with a price of more than 1000.0 should be in the output
    - The pattern "Treadmill" appears in the product name
    - Save the data in the result/scenario6/solution directory on HDFS
7. Explore the customer records saved in the “orders parquet" directory on HDFS
    - Output all PENDING orders in July 2013
    - Only entries with the order status value of "PENDING" should be included in the result
    - Order date should be in the YYY-MM-DD format
    - Save the results in the result/scenario7/solution folder
# Logsense

## Lab 1: Apache Server Log Analysis

This lab is designed to help gain an understanding of working with the error log of a website and user interaction on different modules of a website. You should be able to analyze the dataset for this project to create a report. You will be able to use PySpark, do analyses, and obtain the desired results.

**Objectives**

- Perform server log analysis to assist businesses in identifying and analyzing critical business errors
- Identify potential customers and their domains

**Problem Statement**

The Apache services such as Hadoop, Spark, Tomcat, and Hive run on most data engineering servers throughout the world. All the services follow the same pattern because they are all open source. You are a data engineer who works for a start-up named "Logsense", which serves major clientele.

You have been assigned to one of their prestigious clients to resolve a production issue. As you are dealing with Hadoop, you are familiar with the working of logs. The server's information is stored in the logs along with the information listed below:

1. Resource details
2. Identification of the person who accessed the logs
3. Date and time the logs were accessed
4. Specifications on any problems that emerge
5. Information about the final product
 
Perform the following tasks on the dataset provided using PySpark:

1. Status code analysis
   1. Read the log file as an RDD in PySpark
   1. Consider the sixth element as it is a “request type”
   1. Replace the “single quote" with a blank
   1. Convert each word into a tuple of (word,1)
   1. Apply the “reduceByKey“ transformation to count the values
   1. Display the data
2. Arrange the result in descending order and display
3. Identify the top 10 frequent visitors of the website
4. Identify the top 10 missing (does not exist) URLs using these steps:
   1. Read the log file as an RDD in PySpark
   1. Identify the URLs for which the server is returning the 404-request code and display the data
5. Identify the traffic (total number of HTTP requests received per day)
   1. Read the log file as an RDD in PySpark
   2. Fetch the DateTime string and replace "[" with blank
   3. Get the date string from the DateTime
   4. Identify HTTP requests using the map function
6. Identify the top 10 endpoints that transfer maximum content in megabytes and display the data
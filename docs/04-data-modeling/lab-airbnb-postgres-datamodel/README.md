# Lab: AirBnB Postgres Datamodel

## Objective

Build a Star Schema based Data Model in Postgres on the AirBnB dataset

## Dataset

Dataset consist of 6 different data files in CSV format, listed below:

- calendar.csv
- listings.csv
- listings_details.csv
- neighbourhoods.csv
- reviews.csv
- reviews_details.csv

## Data Ingestion

Steps for uploading one csv into a table inside a database

1. Create the Database if not created
1. Connect to the Database
1. Create the Table using the below sql command inside the database server
    ```
    CREATE TABLE tableName (var1 varType, var2, varType...);
    ```
1. Insert the data into the Table row by row using the following SQL command
    ```
    INSERT INTO tableName (var1, var2 ...) values (val1, val2...);
    ```

Repeat the above steps for all the 6 files that I have. Below are the row and column counts of two major CSV file

- listings_details.csv ==> 20,000 ROWS and 90 Column
- reviews_details.csv ==> 413,000 ROWS and 8 Columns
    
## Data Model

![](https://user-images.githubusercontent.com/62965911/214234180-d970394c-91bf-4012-b59f-47b09fd8b14e.png)

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/04-data-modeling/lab-airbnb-postgres-datamodel/)
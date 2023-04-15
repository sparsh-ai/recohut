# Lab: Postgres Crime Reports

> Building a Database for Crime Reports

Using PostgreSQL for storing data related to crimes that occurred in Boston. Dataquest provided the dataset `boston.csv` for input. We will:

* Create the table `boston_crimes`
* Create the table with the appropriate data types for storing the information from `boston.csv`
* Store the table inside the schema `crimes`
* Create the user groups `readonly` and `readwrite` with appropriate privileges
* Create the users `data_analyst` and `data_scientist` and assign to `readonly` and `readwrite` groups, respectively
* Verify if the privileges of user groups are set accordingly

![](https://user-images.githubusercontent.com/62965911/211729249-e14ed252-03c0-4989-b1fa-606bfb2873f5.jpg)

To accomplish these goals in this lab, you would have to perform the following:

* Create the required database and schema after installing PostgreSQL and `psycopg2` module
* Explore the column headings and content of `boston.csv` to determine the appropriate data types
* Create the required table using the appropriate data types
* Load the data from `boston.csv` into the table
* Create the user group `readonly` which has the following privileges: database connection, schema usage, and data selection from all tables in the schema
* Create the user group `readwrite` which has similar privileges with `readonly` and capable of inserting, deleting, and updating the data in all tables in the schema
* Create the requested users and assign them to their respective user groups
* Test the database if correct objects is created and users/groups have the right privileges

## Building a Database for Crime Reports

Using PostgreSQL for storing data related to crimes that occurred in Boston.  Dataquest provided the dataset `boston.csv` for input. Your goal is to:

* Create the table `boston_crimes`
* Create the table with the appropriate data types for storing the information from `boston.csv`
* Store the table inside the schema `crimes`
* Create the user groups `readonly` and `readwrite` with appropriate privileges
* Create the users `data_analyst` and `data_scientist` and assign to `readonly` and `readwrite` groups, respectively
* Verify if the privileges of user groups are set accordingly

To accomplish your goals in this project, you would have to  perform the following:

* Create the required database and schema after installing PostgreSQL and `psycopg2` module
* Explore the column headings and content of `boston.csv` to determine the appropriate data types
* Create the required table using the appropriate data types
* Load the data from `boston.csv` into the table
* Create the user group `readonly` which has the following privileges: database connection, schema usage, and data selection from all tables in the schema
* Create the user group `readwrite` which has similar privileges with `readonly` and capable of inserting, deleting, and updating the data in all tables in the schema
* Create the requested users and assign them to their respective user groups
* Test the database if correct objects is created and users/groups have the right privileges

## Notebook

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/02-storage/lab-postgres-crime-reports/main.ipynb)

## References

1. https://github.com/bbpajarito/database-crime-reports
2. https://github.com/dataquestio/solutions/blob/master/Mission251Solution.ipynb

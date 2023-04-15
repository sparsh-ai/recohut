# Lab: ETL with bash script

## Objective

In this lab, you will use bash shell commands to extract, transform and load data

## Activity

After completing this lab you will be able to:

1. Extract data from a delimited file.
2. Transform text data.
3. Load data into a database using shell commands.

## Assignment

### Problem

Copy the data in the file `web-server-access-log.txt.gz` to the table 'access_log' in the PostgreSQL database 'postgres'.

The following are the columns and their data types in the file:

1. `timestamp` - TIMESTAMP
2. `latitude` - float
3. `longitude` - float
4. `visitorid` - char(37)

and two more columns: `accessed_from_mobile` (boolean) and `browser_code` (int)

The columns which we need to copy to the table are the first four coumns.

NOTE: The file comes with a header. So use the 'HEADER' option in the 'COPY' command.

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/02-storage/lab-postgres-bash-etl/)
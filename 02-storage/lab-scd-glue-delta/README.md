# Lab: Implement slowly changing dimensions in a data lake using AWS Glue and Delta

[![](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/02-storage/lab-scd-glue-delta)

![process-flow drawio](https://user-images.githubusercontent.com/62965911/228874138-525c0572-d3f3-4cdc-a122-4f09997d3f8d.svg)

1. Upload initial JSON data into S3 Raw layer
1. Process the data from raw JSON to Delta format using Glue ETL Job
1. Load the processed data locally and read in pandas dataframe
1. Change the raw json by deleting, updating and creating some records
1. Process the data again from changed raw JSON to Delta format using Glue ETL Job
1. Load the processed data locally and read in pandas dataframe, compare changes and run SQL queries
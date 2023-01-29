# Covid-19 Data Pipeline

## Objective

Created an ETL pipeline using python in AWS on Covid-19 data. 

The raw data was initially uploaded to an S3 bucket. Then using crawler, the raw data was crawled and uploaded to Athena and then queried. The queried data was then uploaded back to s3 bucket. Then a cluster was created in redshift to copy the data from s3 using aws glue. The technologies used in this project are: 

- Python
- AWS S3
- AWS Athena
- AWS Glue
- AWS EC2
- AWS Redshift

The raw data are in csv, json format. Few of the datasets were corrupt so it required little bit of tweaking.

## Datasets

Datasets used in Project: https://aws.amazon.com/blogs/big-data/exploring-the-public-aws-covid-19-data-lake/

## Architecture

![](https://user-images.githubusercontent.com/62965911/211188266-16b2721b-f036-433a-8643-96c7f819d3c4.png)
# US Immigration analysis and data pipeline

## Problem Statement

Combining US Immigration Data, World Temperature Data and US City Demographic Data, and some simple joins and aggregations, to identify the average age and sex of arrivals to US Cities. This data was then combined with temperature data for each city so one can correlate arrivals with weather trends. The demographics data could also illustrate whether there are relationships between the average age of the attendee and city. Alternatively, the data could be repurposed to see what relationships exist between the race of the arrivee and city/state demographics.

A business consulting firm specialized in data warehouse services through assisting the enterprises with navigating their data needs and creating strategic operational solutions that deliver tangible business results is contacted by U.S Customs & Border Protection Department. Specifically, they want help with the modernization of department's data warehousing infrastructure by improving performance and ease of use for end users, enhancing functionality, decreasing total cost of ownership while making it possible for real-time decision making. In total, the department is asking for a full suite of services includes helping department with data profiling, data standardization, data acquisition, data transformation and integration.

The U.S. Customs and Border Protection needs help to see what is hidden behind the data flood. The consulting firm aim to model and create a brand new analytics solution on top of the state-of-the-art technolgies available to enable department to unleash insights from data then making better decisions on immigration policies for those who came and will be coming in near future to the US.

## What you'll build

1. Data Load into S3
2. Data Preprocessing with PySpark
3. Data Modeling and Warehousing with Amazon Redshift
4. Advanced analytics using Python and Matplotlib
5. Assignment: Airflow Pipeline

## Solution

```
├── [ 41K]  01-sa-preprocessing.ipynb
├── [5.4K]  02-sa-create-tables.ipynb
├── [ 11K]  03-sa-etl.ipynb
├── [2.0M]  04-sa-analytics.ipynb.zip
├── [ 21K]  assets
│   └── [ 21K]  data-dictionary.md
├── [ 177]  data
│   └── [  49]  download.sh
├── [2.3K]  expatriate.mdx
├── [ 155]  img
│   └── [  59]  download.sh
└── [ 47K]  src
    └── [ 26K]  sql_queries.py

 2.1M used in 5 directories, 10 files
```
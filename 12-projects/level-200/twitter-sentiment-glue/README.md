# Twitter data Topic Analysis and Realtime Sentiment Analysis

## Problem Statement

Twitter is one of the most popular social networking website in the world. Every second, on average, around 8,000 tweets are tweeted on Twitter, which corresponds to over 450,000 tweets sent per minute, 650 million tweets per day and around 250 billion tweets per year. As claimed by the official site, Twitter data is the most comprehensive source of live, public conversation worldwide. Furthermore, Twitter allows developers to access their tweet data through their APIs that enable programmatic analysis of data in real-time or back to the first Tweet in 2006. This project aims to utilize the tweet data and combine the data with world happiness index data and earth surface temperature data and warehouse them on AWS. The Twitter data extraction could be limited to specific topics/hash-tags as per requirements which allows us to explore various domains.

In this project, we combine [Twitter](https://www.twitter.com) data, [World happiness index](https://www.kaggle.com/unsdsn/world-happiness) data and [Earth surface temperature data](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data) data to explore whether there is any correlation between the above. The Twitter data is dynamic and the other two dataset are static in nature. The general idea of this project is to extract Twitter data, analyze its sentiment and use the resulting data to gain insights with the other datasets. For instance, we could answer interesting questions like whether positive or negative tweets are correlated with the happiness index of the country a person is residing in, or, is there a relationship between the sentiment of a tweet and the temperature change in a country a user is living in?

#:draft
Build an ETL pipeline that sources data from Twitter, apply transformation, and stores it in a Data Warehouse

We will use Twitter API to get the data on a particular topic (dark-net for now) and put a filter on request to get data starting from 7 days ago. Then we will schedule our pipeline to run on 7 day interval. Thus avoiding conflicts of fetching and storing same data again. We will fetch the data and put it in a NoSQL database, CouchDB for our case. The reason to put it in a intermediary database and not straight up in the DW is to perform transformation operations. This allows us with more flexibility to run operations such as filtering, data cleaning, or building summaries for the data being inserted in Data Warehouse.
#:

## Query

- Create an Amazon S3 bucket for customer data
- Copy data into Amazon S3 bucket
- Create a database in the AWS Glue Data Catalog
- Create a table in the AWS Glue Data Catalog with proper schema, format, and Amazon S3 location
- Use Amazon Athena to query using SQL

## Visualization

- Create QuickSight data source for Amazon Athena
- Create QuickSight data set for our data
- Create QuickSight analysis

## Streaming Data

- Create an Amazon Kinesis Data Stream for Twitter data
- Create an Amazon S3 bucket/folder to persist the Twitter data
- Create Amazon Kinesis Data Firehose to
  - Read from Amazon Kinesis Data Stream
  - Write to Amazon S3

## Enrichment

- Create an Amazon S3 bucket/folder for the enriched data
- Create an AWS IAM role for the AWS Lambda function with proper permissions
- Create an AWS Lambda function that
  - Reads from Amazon S3
  - Calls Amazon Comprehend to determine customer sentiment and extract key phrases
  - Writes output to enriched Amazon S3 location
- Create an Amazon S3 event to trigger the Lambda function on new data arrival

## Insight

- Create tables and views in the AWS Glue Data Catalog with proper schema, format, and Amazon S3 location
  - Sentiment and phrases data
  - Sentiment and phrases joined with customer status data
- Create QuickSight data sets for our data
- Create visualizations in Amazon QuickSight
  - Word cloud for all Tweets
  - Word cloud for Tweets with negative sentiment
  - Word cloud for Tweets with negative sentiment for users who canceled
  - Histogram of key terms in Tweets with negative sentiment for users who canceled

## Data Model

![](https://user-images.githubusercontent.com/62965911/215313668-5e02ea96-a6c1-4fc0-9424-57c4d624cafe.png)

## Project Structure

```
├── [ 61K]  01-sa-main.ipynb
├── [ 34K]  02-sa-preprocessing.ipynb
├── [ 37K]  03-sa-twitter-couchdb.ipynb
├── [4.1K]  README.md
├── [ 17K]  airflow
│   ├── [ 11K]  dags
│   │   └── [7.2K]  dag.py
│   ├── [ 326]  run.sh
│   └── [6.0K]  sql
│       ├── [2.6K]  create_tables.sql
│       ├── [ 347]  happiness_insert.sql
│       ├── [ 369]  sources_insert.sql
│       ├── [ 748]  temperature_insert.sql
│       ├── [ 882]  time_insert.sql
│       ├── [ 808]  tweets_insert.sql
│       └── [  70]  users_insert.sql
├── [6.5K]  assets
│   └── [6.4K]  _DATADICT.md
├── [ 471]  config.cfg
├── [ 141]  data
│   └── [  45]  download.sh
├── [ 250]  download.sh
└── [1.7K]  requirements.txt

 332K used in 7 directories, 22 files
```
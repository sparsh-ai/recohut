# Reddit Submissions, Authors and Subreddits analysis

## Problem Statement

Reddit is "the frontpage of the internet" and has a broad range of discussions about nearly every topic one can think of. This makes it a perfect candidate for analytics. This project will use a sample of publicly available dump of Reddit and load it into a AWS Redshift warehouse so that Data Scientists can make use of the content and for example develop a recommender system that finds the most suitable subreddit for your purposes.

The goal of this project is to create a Data Warehouse to analyze trending and new subreddits using Airflow.

The project uses the Reddit API to get subreddits and stores them on AWS S3 in JSON format. Data processing happens on an EMR cluster on AWS using PySpark and processed data gets stored on AWS S3 in parquet format. Finally, the data gets inserted into AWS Redshift, gets denormalized to create fact and dimension tables.

## Data Sources

1. [Authors](http://files.pushshift.io/reddit/authors/)
2. [Submissions](http://files.pushshift.io/reddit/submissions/)
3. [Subreddits](http://files.pushshift.io/reddit/subreddits/)

## Airflow

### Pipeline 1

![](https://user-images.githubusercontent.com/62965911/215309302-da77564a-f1cc-44c4-ab49-5313f0845063.png)

**Setting up the airflow environment**

![](https://user-images.githubusercontent.com/62965911/215309290-0b99e64f-20bb-47eb-9fbf-4e9e00ce70d7.png)

![](https://user-images.githubusercontent.com/62965911/215309292-d2eab5b0-0d25-4ab0-8579-6748d6f5b788.png)

**Output**

![](https://user-images.githubusercontent.com/62965911/215309315-2cef7bf0-ab34-4281-a191-867c762b666a.png)

### Pipeline 2

#TODO: This pipeline is yet to be tested.

![](https://user-images.githubusercontent.com/62965911/215309305-15c2d3d0-5add-4fc2-bf15-ad0a0f02f206.png)

### Pipeline 3

Architecture:

![](https://recohut-images.s3.amazonaws.com/labs/lab-117-reddit/datawarehouse_architecture.png)

## Project Structure

```
├── [ 18K]  01-sa.ipynb
├── [4.6K]  README.md
├── [ 16K]  REPORT.md
├── [ 768]  airflow
│   ├── [ 288]  dags
│   ├── [ 160]  plugins
│   └── [ 160]  plugins_2
├── [ 148]  data
│   └── [  52]  download.sh
├── [134K]  nbs
│   ├── [ 55K]  create_dates_and_holiday_dataset.ipynb
│   └── [ 79K]  data-model-explained.ipynb
└── [ 14K]  src
    ├── [1.8K]  data_quality_queries.py
    ├── [1.4K]  download_datasets.sh
    ├── [1.5K]  make_chunks.py
    ├── [1.4K]  preprocess_authors.py
    ├── [ 922]  sample_dataset.sh
    ├── [ 192]  sql
    └── [6.4K]  sql_queries.py

 187K used in 8 directories, 12 files
```
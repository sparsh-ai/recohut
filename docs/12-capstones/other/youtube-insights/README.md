# YouTube Trend Analysis Workshop

![youtube_trending](https://user-images.githubusercontent.com/62965911/215285044-800a4b41-3226-4fc2-bbed-f1d95f562f60.png)

YTinsights would like to launch a data-driven ad-campaign on YouTube.

You as a data engineer will help their analytics team answering the following questions:

1. How do we categorize videos based on the comments and statistics?
1. What factors affect how popular a YouTube video will be?

## What we'll do

1. Joining semi-structured and structured data in AWS
1. Perform ETL in AWS Glue using Spark jobs

## Architecture

![pipeline](https://user-images.githubusercontent.com/62965911/215285037-d865e0ff-33aa-4bf0-8e98-175db5e6562e.png)

## Data Cleansing - Semi-structured to Structured data

![datacleansing_pipeline](https://user-images.githubusercontent.com/62965911/215285026-e7ff3e14-ec74-4f04-871c-c98bb9a18d7c.png)

## Data 

- Top trending videos on YouTube
- Source: https://www.kaggle.com/datasets/datasnaek/youtube-new
- Data collected using Trending YouTube Scraper
- Uploaded in S3 here - `s3://wysde-datasets/ytinsights`

:::tip What is "Trending"?
YouTube uses factors, including users interactions (e.g., number of views, shares, comments and likes). Not the most-viewed videos overall per calendar year.
:::

![athena_final_query](https://user-images.githubusercontent.com/62965911/215285019-d7fd4ddb-2f28-498e-bafb-40c15c700495.png)

![glue_crawlers](https://user-images.githubusercontent.com/62965911/215285033-aa7c8057-4990-4f35-b08b-d047703a5d1e.png)

![glue_tables](https://user-images.githubusercontent.com/62965911/215285034-eb9ee157-4f26-439d-b7f3-bafb00672071.png)

![iam_roles](https://user-images.githubusercontent.com/62965911/215285035-ff224bf6-77b4-47e4-894c-ea53c5322e1a.png)

![s3_buckets](https://user-images.githubusercontent.com/62965911/215285040-f24b4da2-65e0-4cc5-8fd9-3592caf552a5.png)
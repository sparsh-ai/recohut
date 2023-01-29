# Movie Review Sentiment Analysis Pipeline

Build a pipeline that expresses the fact artist review sentiment and film review sentiment, based on the data provided by IMDb and TMDb.

The goal of our Data Pipeline is to publish a PDF report to S3 with the following summarised information:

- Top 10 Films
- Worst 10 Films
- Review Sentiment Distibution
- Top 10 Actors/Actresses in Best Reviewed Films
- IMDb Average Voting vs TMDb Sentiment Reviews through Years

Process steps:

1. Modify the variables in DAG
2. Export the Variables before starting airflow
3. Run the DAG

The project follows the follow steps:

* Step 1: Scope the Project and Gather Data
* Step 2: Explore and Assess the Data
* Step 3: Define the Data Model
* Step 4: Run ETL to Model the Data
* Step 5: Complete Project Write Up

## Problem Statement

The project expresses the fact artist review sentiment and film review sentiment, based on the data provided by [IMDb](https://www.imdb.com/) and [TMDb](https://www.themoviedb.org/)

## Data Sources

* [IMDB Large Movie Reviews Sentiment Dataset](https://www.kaggle.com/jcblaise/imdb-sentiments)
* [TMDB Movies (2000-2020) with imdb_id](https://www.kaggle.com/hudsonmendes/tmdb-movies-20002020-with-imdb-id)
* [TMDB Reviews, movies released from 2000 and 2020](https://www.kaggle.com/hudsonmendes/tmdb-reviews-movies-released-from-2000-and-2020)
* [IMDB Cast (Links)](https://datasets.imdbws.com/title.principals.tsv.gz)
* [IMDB Cast (Names)](https://datasets.imdbws.com/name.basics.tsv.gz)

## Choice of Technology

The present solution allows Data Analysts to perform roll-ups and drill-downs into film review sentiment facts linked to both films and actors.

Since the raw data provided into S3 and reported on demand to the Data Analysis Team who can then perform further analysis on the database, a single write step is required, whereas many reads and aggregations will be performer.

Given those requirements, the choice of technology was the following:

1. AWS S3 to store the raw files from IMDb and TMDb films, reviews and casting.
2. AWS Redshift to produce a Data Warehouse with the required dimension and fact tables.
3. Tensorflow to allow us training a model and running the classification
4. Apache Airflow to automate our Data Piepeline.

## Pipeline

![](https://user-images.githubusercontent.com/62965911/215307460-cb3ace57-b09a-4e25-a909-2360083dfe39.png)
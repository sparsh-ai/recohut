# dbt Olist

## Objective

In this lab, we will use Brazilian Olist dataset. We will load this data into the database and build data models for it using dbt.

## Steps

1. Download the data from https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce and store into `data` directory.
2. Use ingest.ipynb to ingest the data to `postgres.postgres.olist` database.
3. Run `dbt debug --profiles-dir .` and then `dbt run --profiles-dir .` to run the pipeline.
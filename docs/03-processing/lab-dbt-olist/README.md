# Lab: dbt Postgres on Olist Retail data

## Objective

In this lab, we will use Brazilian Olist dataset. We will load this data into the database and build data models for it using dbt.

## Steps

1. Download the data from https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce and store into `data` directory.
2. Use ingest.ipynb to ingest the data to `postgres.postgres.olist` database.
3. Run `dbt debug --profiles-dir .` and then `dbt run --profiles-dir .` to run the pipeline.

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/03-processing/lab-dbt-olist)

```
├── [ 886]  README.md
├── [ 466]  dbt_project.yml
├── [5.8K]  ingest.ipynb
├── [ 235]  macros
│   └── [ 139]  cents_to_dollars.sql
├── [6.0K]  models
│   ├── [1.0K]  marts
│   │   └── [ 943]  ecommerce
│   │       └── [ 847]  fct_orders.sql
│   └── [4.8K]  staging
│       └── [4.8K]  olist
│           ├── [ 515]  stg_ecommerce.md
│           ├── [1.3K]  stg_ecommerce.yml
│           ├── [ 858]  tables
│           │   ├── [  75]  stg_category_translation.sql
│           │   ├── [  53]  stg_customers.sql
│           │   ├── [  55]  stg_geolocation.sql
│           │   ├── [  55]  stg_order_items.sql
│           │   ├── [  57]  stg_order_reviews.sql
│           │   ├── [  50]  stg_orders.sql
│           │   ├── [  58]  stg_payments.sql
│           │   ├── [  52]  stg_products.sql
│           │   └── [  51]  stg_sellers.sql
│           └── [2.0K]  views
│               └── [1.9K]  stg_rfm.sql
├── [ 239]  profiles.yml
├── [ 764]  requirements.txt
└── [ 277]  tests
    └── [ 181]  assert_fct_orders_payment_value_greater_than_zero.sql

  15K used in 9 directories, 20 files
```

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/03-processing/lab-dbt-olist)
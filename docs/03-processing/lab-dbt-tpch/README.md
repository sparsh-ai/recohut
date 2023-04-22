# Lab: dbt Snowflake on TPCH data

> Accelerating Data Teams with Snowflake and dbt Cloud Hands On Lab

In this lab we'll be transforming raw retail data into a consumable orders model that's ready for visualization. We'll be utilizing the TPC-H dataset that comes out of the box with your Snowflake account and transform it using some of dbt's most powerful features. By the time we're done you'll have a fully functional dbt project with testing and documentation, dedicated development and production environments, and experience with the dbt git workflow.

![dbtcloud](https://user-images.githubusercontent.com/62965911/214353071-f6a011dd-db9f-42f9-b04d-f48883956c15.png)

![dbtconnect](https://user-images.githubusercontent.com/62965911/214353091-0fbf7972-1e89-43f0-9b8d-d73cfac82d3e.png)

![flow](https://user-images.githubusercontent.com/62965911/214353101-a381a803-67f7-42fd-a47e-8f8eee3db637.png)

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/03-processing/lab-dbt-tpch)

```
├── [1.3K]  README.md
├── [ 406]  dbt_project.yml
├── [389K]  img
│   ├── [141K]  dbtcloud.png
│   ├── [210K]  dbtconnect.png
│   └── [ 38K]  flow.png
├── [ 12K]  main.ipynb
├── [7.3K]  models
│   ├── [4.5K]  marts
│   │   └── [4.4K]  core
│   │       ├── [ 117]  _core.md
│   │       ├── [1.3K]  core.yml
│   │       ├── [1.1K]  fct_orders.sql
│   │       └── [1.6K]  int_order_items.sql
│   └── [2.7K]  staging
│       └── [2.7K]  tpch
│           ├── [ 848]  stg_tpch_line_items.sql
│           ├── [ 529]  stg_tpch_nations.sql
│           ├── [ 461]  stg_tpch_orders.sql
│           └── [ 684]  tpch_sources.yml
├── [  61]  packages.yml
├── [ 421]  profiles.yml
├── [ 983]  seeds
│   └── [ 887]  nations.csv
└── [ 256]  tests
    └── [ 160]  fct_orders_negative_discount_amount.sql

 413K used in 8 directories, 18 files
```

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/03-processing/lab-dbt-tpch)
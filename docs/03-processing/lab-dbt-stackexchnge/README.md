# Lab: dbt BigQuery on Stack Exchange data

Extract, Load and Transform the Stack Exchange data using dbt and google bigquery warehouse.

The data is the publicly available [Stack Exchange Data Dump](https://archive.org/details/stackexchange). `Users.xml` and `Posts.xml` were converted to `users.csv.gz` and `posts.csv.gz` and used as the source files for this project.

For the ISO 3166-1 country codes, the CSV used from [DataHub](https://datahub.io/core/country-list) was used (as `country_codes.csv`).

## Pre-requisites

For Google Cloud:

- Create a project
- Create a Cloud Storage Bucket and upload `posts.csv.gz`, `users.csv.gz` and `country_codes.csv` files 

For dbt:

- Python 3.x installed
- Install packages from `requirements.txt`
- Copy the ISO 3166-1 country codes CSV into `./seeds/country_codes.csv`
- Setup a dbt profile in `~/.dbt/profiles.yml` called `bigquery_dbt` for BigQuery ([Example](https://docs.getdbt.com/reference/warehouse-profiles/bigquery-profile))
  
## Running

1. Make BigQuery dataset
`bq mk --dataset ${PROJECT_ID}:${DATASET}`

2. Load files into BigQuery as tables (can be done concurrently)
```
bq load \
    --autodetect \
    --source_format=CSV \
    ${DATASET}.posts \
    gs://${BUCKET_NAME}/posts.csv.gz

bq load \
    --autodetect \
    --source_format=CSV \
    ${DATASET}.users \
    gs://${BUCKET_NAME}/users.csv.gz
```

3. Ensure Google project id is specified in `database` field in [`schema.yml`](models/schema.yml)

4. Run dbt
```
dbt build # Load CSV as reference table (via seeds), run tests etc.
dbt run
```

5. Load created table into GCS
```
bq extract \
--destination_format CSV \
--compression GZIP \
--field_delimiter ',' \
${PROJECT_ID}:${DATASET}.aggregated_users \
gs://${BUCKET_NAME}/dbt_bigquery/agg_users.csv.gz
```

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/03-processing/lab-dbt-stackexchnge)

```
├── [2.1K]  README.md
├── [1.1K]  dbt_project.yml
└── [1.8K]  models
    ├── [1.2K]  aggregated_users.sql
    └── [ 525]  schema.yml

 5.2K used in 1 directory, 4 files
```

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/03-processing/lab-dbt-stackexchnge)
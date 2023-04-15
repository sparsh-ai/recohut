# Lab: Redshift Slowly Changing Dimension

[![](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/02-storage/lab-redshift-scd-2/main.ipynb)

Data loading into a SCD table involves a first-time bulk data loading, referred to as the _initial data load_. This is followed by continuous or regular data loading, referred to as an _incremental data load_, to keep the records up to date with changes in the source tables.

To demonstrate the solution, we walk through the following steps for initial data load (1–7) and incremental data load (8–12):

1. Land the source data files in an Amazon S3 location, using one subfolder per source table.
2. Use an [AWS Glue](https://aws.amazon.com/glue) crawler to parse the data files and register tables in the AWS Glue Data Catalog.
3. Create an external schema in Amazon Redshift to point to the AWS Glue database containing these tables.
4. In Amazon Redshift, create one view per source table to fetch the latest version of the record for each primary key (`customer_id`) value.
5. Create the `dim_customer` table in Amazon Redshift, which contains attributes from all relevant source tables.
6. Create a view in Amazon Redshift joining the source table views from Step 4 to project the attributes modeled in the dimension table.
7. Populate the initial data from the view created in Step 6 into the `dim_customer` table, generating `customer_sk`.
8. Land the incremental data files for each source table in their respective Amazon S3 location.
9. In Amazon Redshift, create a temporary table to accommodate the change-only records.
10. Join the view from Step 6 and `dim_customer` and identify change records comparing the combined hash value of attributes. Populate the change records into the temporary table with an `I`, `U`, or `D` indicator.
11. Update `rec_exp_dt` in `dim_customer` for all `U` and `D` records from the temporary table.
12. Insert records into `dim_customer`, querying all `I` and `U` records from the temporary table.
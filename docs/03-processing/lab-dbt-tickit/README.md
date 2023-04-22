# Lab: Building an ELT Pipeline with dbt and Amazon Redshift on TICKIT data

## Objective

Building an ELT Pipeline with dbt and Amazon Redshift on TICKIT data

## Business Problem

A fictional company 'Recohut' is looking to leverage dbt on their existing data warehouse in Amazon Redshift. They need your help in establishing the dbt models and pipelines in their warehouse.

## Solution Architecture

In this project, you will:

1. Install dbt CLI
2. Use dbt dbt-labs/codegen package and Python script to automate creation of a base layer
3. Use dbt models to maintain data transformations with referencing capabilities
4. Use dbt macros to maintain common logic as functions and to administer user creation and grants
5. Use dbt hooks to automate continuous execution of grants
6. Use dbt seeds to manage manual files
7. Use dbt docs to generate documentation with visualization
8. Use dbt experimental package explore materialization of materialize views

## Activity 1: Amazon Redshift Serverless

In this activity, we are going to:

1. Create Amazon Redshift Serverless Cluster on AWS
2. Connect to the Cluster from our local computer using Python
3. Use AWS Secret Manager to store and retrieve our Warehouse credentials

## Activity 2: Data Ingestion

In this activity, we are going to ingest the TICKIT dataset into the Redshift warehouse

## Activity 3: Setup dbt

In this activity, we will install dbt in our system. We will then setup the dbt project.

## Activity 4: Setup base layer

In this activity, you will setup a base layer for your models to reference. What is a base layer and what are models? Models are SQL Select statements that represents your data transformation logic including usage of case statements and joins. Base layer falls under the category of models and represents existing objects (tables and views) in your Amazon Redshift cluster.

In addition, depending on the nature of your dbt project, a base layer can be made up of different objects. For instance, a data engineer's base layer likely relates to tables containing raw data while a data analyst's base layer likely relates to tables containing cleaned data.

## Activity 5: Create models

To explore dbt's ability for objects to be referenced by other objects, in this activity, you will simulate a Finance deparment that maintains two models where the second model references the first model. To reference means to reuse and not have to duplicate code.

- Model 1 - Quarterly Total Sales By Event
- Model 2 - Quarterly Top Events By Sales (references Model 1 to rank and filter for top 3 events by sales for each quarter)

## Activity 6: Create macros

In this activity, you will use macros to create a piece of reusable data transformation logic and also to manage users and grants. Macros are a great way in dbt to create reusable pieces of SQL codes like a function in Python.

## Activity 7: Data Masking

In this activity, you will simulate a Technology department with one model that contains data masking logic.

## Activity 8: Access Control Management with dbt macros

Macros can be used to send queries to Amazon Redshift. In this activity, you will use macros to manage users and grants. Similar to the Python script earlier, you can modify the macros created in this activity to better suit your needs beyond the scope of this workshop. For example, you might want to include a new macro to manage Role-based access control (RBAC) in Amazon Redshift.

## Activity 9: dbt hooks

As models are added or updated, you will constantly need to grant access to new views and regrant access to existing views. Regranting access to an existing view is required as dbt updates by dropping existing view and creating a new view.

This introduces the operational challenge of you having to remember to run macro macro_manage_users_grants. However the process of running macro macro_manage_users_grants can be automated by hooks in dbt.

## Activity 10: Create seeds

Seeds are a convenient way in dbt for you to manage manual files. A common use case for manual files is to introduce data mappings. Manual files allows data mappings to be easily maintained and reused as compared to the usage of case statements in SQL which requires code changes when data mappings are changed.

In this activity, you will simulate a Marketing department that maintains a custom data mapping csv that a model uses.

## Activity 11: Create documentations

The ability for objects to reference other objects improves code reusability but can result in widespread negative impact when an erroneous change is introduced to an object that is referenced by a large number of objects. dbt provides you with an interface to visualize all models and its dependencies on other models which is useful for impact analysis.

## Activity 12: Materialized View

Materialized view stores precomputed results to reduce processing time for complex queries involving multi-table joins and aggregations.

In this activity, you will simulate an Experimental department that is exploring a dbt experimental feature.

## Project outputs

### Docs

![](https://user-images.githubusercontent.com/62965911/214304361-8dd06672-faad-43cd-b844-3a1b38dcc876.png)

### Dag

![](https://user-images.githubusercontent.com/62965911/214304345-b5a29b42-2d57-48bd-8a2e-2ce886d33de0.png)

### Database

![](https://user-images.githubusercontent.com/62965911/214304319-ffe03556-37d7-49c2-8111-01a8380707ee.png)

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/03-processing/lab-dbt-tickit)

```
├── [ 40K]  01-sa-main.ipynb
├── [5.7K]  README.md
├── [ 41K]  cfn
│   └── [ 40K]  dbt-redshift.json
├── [1.9K]  dbt_project.yml
├── [4.0K]  generate_base_tables.py
├── [8.4K]  macros
│   ├── [3.1K]  macro_hello_world.sql
│   ├── [3.9K]  macro_manage_access.sql
│   ├── [ 803]  macro_overwrite_for_mv.sql
│   └── [ 421]  macro_pii_masking.sql
├── [4.9K]  models
│   ├── [2.5K]  base_public
│   │   ├── [ 211]  base_public_category.sql
│   │   ├── [ 257]  base_public_date.sql
│   │   ├── [ 242]  base_public_event.sql
│   │   ├── [ 290]  base_public_listing.sql
│   │   ├── [ 314]  base_public_sales.sql
│   │   ├── [ 473]  base_public_users.sql
│   │   ├── [ 234]  base_public_venue.sql
│   │   └── [ 201]  schema.yml
│   ├── [ 536]  dept_experimental
│   │   └── [ 440]  rpt_experimental_qtr_total_sales_by_event.sql
│   ├── [ 822]  dept_finance
│   │   ├── [ 205]  rpt_finance_qtr_top_events_by_sales.sql
│   │   └── [ 489]  rpt_finance_qtr_total_sales_by_event.sql
│   ├── [ 291]  dept_marketing
│   │   └── [ 195]  rpt_marketing_category_full_desc.sql
│   └── [ 617]  dept_tech
│       └── [ 521]  rpt_tech_all_users.sql
├── [ 157]  packages.yml
├── [ 635]  seeds
│   └── [ 539]  dept_marketing
│       └── [ 443]  mnl_category_desc.csv
└── [2.6K]  src
    └── [2.6K]  data_load.sql

 110K used in 11 directories, 25 files
```

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/03-processing/lab-dbt-tickit)
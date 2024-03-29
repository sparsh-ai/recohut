# Lab: Create a star schema from 3NF schema on DVD rental Pagila dataset

## Objective

Create a star schema from 3NF schema on DVD rental Pagila dataset

Build a Postgres data model of Pagila dataset

## Introduction

Pagila is a dataset representing a DVD rental store (remember those?!), containing information about films (like title, category, actresses), rental stores (like address, staff members, customers) and rentals, where a customer rents a film from a store through its staff.

With all these relational information, Pagila is a perfect fit to play around with PostgreSQL and the SQL language.

In this lab, we will use this Pagila dataset to build a data model in Postgres.

## 3NF Schema

![](https://user-images.githubusercontent.com/62965911/211511428-e9fb7f88-aabb-4e8a-810c-5e6b69f301b4.png)

## Star Schema

![](https://user-images.githubusercontent.com/62965911/211511442-3a579b9f-3cf9-453d-be80-c44a1349d69d.png)

## Files

```
├── [ 41K]  01-sa-relational-datamodel.ipynb
├── [ 44K]  02-sa-relational-to-star-schema.ipynb
├── [ 51K]  03-sa-olap-cubes.ipynb
├── [1.3K]  README.md
├── [ 171]  data
│   └── [  75]  download.sh
└── [ 51K]  src
    ├── [5.7K]  data\ warehouse.sql
    └── [ 45K]  restore.sql

 189K used in 2 directories, 7 files
```

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/04-data-modeling/lab-dvd-rental-datamodel)

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/04-data-modeling/lab-dvd-rental-datamodel)
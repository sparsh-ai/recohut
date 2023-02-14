# dbt Jaffle Shop

## Objective

`jaffle_shop` is a fictional ecommerce store. This dbt project transforms raw data from an app database into a customers and orders model ready for analytics.

In this lab, we will use Jaffle Shop dataset. We will load this data into the database and build data models for it.

## Data Model

![](https://user-images.githubusercontent.com/62965911/214291813-a0816724-c1a3-42da-928f-5b9f15f126c9.png)

## Running this project

- Set up a profile called `jaffle_shop` to connect to a data warehouse by following [these instructions](https://docs.getdbt.com/docs/configure-your-profile). If you have access to a data warehouse, you can use those credentials – we recommend setting your [target schema](https://docs.getdbt.com/docs/configure-your-profile#section-populating-your-profile) to be a new schema (dbt will create the schema for you, as long as you have the right privileges). If you don't have access to an existing data warehouse, you can also setup a local postgres database and connect to it in your profile.

- Ensure your profile is setup correctly from the command line:
```bash
$ dbt debug
```

- Load the CSVs with the demo data set. This materializes the CSVs as tables in your target schema. Note that a typical dbt project **does not require this step** since dbt assumes your raw data is already in your warehouse.
```bash
$ dbt seed
```

- Run the models:

```bash
$ dbt run
```

> **NOTE:** If this steps fails, it might mean that you need to make small changes to the SQL in the models folder to adjust for the flavor of SQL of your target database. Definitely consider this if you are using a community-contributed adapter.

- Test the output of the models:

```bash
$ dbt test
```

- Generate documentation for the project:

```bash
$ dbt docs generate
```

- View the documentation for the project:

```bash
$ dbt docs serve
```

## What is a jaffle?

A jaffle is a toasted sandwich with crimped, sealed edges. Invented in Bondi in 1949, the humble jaffle is an Australian classic. The sealed edges allow jaffle-eaters to enjoy liquid fillings inside the sandwich, which reach temperatures close to the core of the earth during cooking. Often consumed at home after a night out, the most classic filling is tinned spaghetti, while my personal favourite is leftover beef stew with melted cheese.
# dbt

> Transform your data in warehouse

dbt (data build tool) is an open source Python package that enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications. dbt allows you to build your data transformation pipeline using SQL queries.

dbt fits nicely into the modern BI stack, coupling with products like Stitch, Fivetran, Redshift, Snowflake, BigQuery, Looker, and Mode. Here’s how the pieces fit together:

![](https://www.getdbt.com/ui/img/blog/what-exactly-is-dbt/1-BogoeTTK1OXFU1hPfUyCFw.png)

dbt is the T in ELT. It doesn’t extract or load data, but it’s extremely good at transforming data that’s already loaded into your warehouse. This “transform after load” architecture is becoming known as ELT (extract, load, transform).

ELT has become commonplace because of the power of modern analytic databases. Data warehouses like Redshift, Snowflake, and BigQuery are extremely performant and very scalable such that at this point most data transformation use cases can be much more effectively handled in-database rather than in some external processing layer. Add to this the separation of compute and storage and there are decreasingly few reasons to want to execute your data transformation jobs elsewhere.

dbt is a tool to help you write and execute the data transformation jobs that run inside your warehouse. dbt’s only function is to take code, compile it to SQL, and then run against your database.

Watch this video: https://www.youtube.com/watch?v=8FZZivIfJVo

Watch this video: https://www.youtube.com/watch?v=efsqqD_Gak0

<details>
<summary>Want to deep-dive?</summary>
This is the playlist if you get into deep-dive :

https://www.youtube.com/playlist?list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT

</details>

## Data modeling techniques for more modularity

https://www.getdbt.com/analytics-engineering/modular-data-modeling-technique/

![](https://user-images.githubusercontent.com/62965911/214275837-a9c09ea9-81a0-4e8d-aed0-42abb31e1c5f.png)

dbt (data build tool) is an open source Python package that enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications. dbt allows you to build your data transformation pipeline using SQL queries.

## Watch this

- [What Is DBT and Why Is It So Popular - Intro To Data Infrastructure Part 3](https://youtu.be/8FZZivIfJVo)
- [What is dbt Data Build Tool? | What problem does it solve? | Real-world use cases](https://youtu.be/efsqqD_Gak0)
- [What is dbt(Data Build Tool)?](https://youtu.be/lHjLAdbPiuc)
- [DBT Tutorial (data built tool)](https://youtu.be/3gfRw9qBmF8)
- This is the playlist if you get into deep-dive : [Data Build Tool (dbt)](https://www.youtube.com/playlist?list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT)

## Read this

- [What, exactly, is dbt?](https://www.getdbt.com/blog/what-exactly-is-dbt/)
- [dbt vs Delta Live Tables](https://medium.com/@rahulxsharma/dbt-vs-delta-live-tables-ef629b627e0)
- [Four Reasons that make DBT a great time saver for Data Engineers](https://medium.com/@montadhar/four-reasons-that-make-dbt-a-great-time-saver-for-data-engineers-4c4ceb721522)

## **What Do Airflow and dbt Solve?**

Airflow and dbt share the same high-level purpose: to help teams deliver reliable data to the people they work with, using a common interface to collaborate on that work.

But the two tools handle different parts of that workflow:

- Airflow helps **orchestrate** jobs that extract data, load it into a warehouse, and handle machine-learning processes.
- dbt hones in on a subset of those jobs – enabling team members who use SQL to **transform** data that has already landed in the warehouse.

With a combination of dbt **and** Airflow, each member of a data team can focus on what they do best, with clarity across [analysts](https://docs.getdbt.com/blog/dbt-airflow-spiritual-alignment#pipeline-observability-for-analysts) and [engineers](https://docs.getdbt.com/blog/dbt-airflow-spiritual-alignment#transformation-observability-for-engineers) on who needs to dig in (and where to start) when data pipeline issues come up.

## Trainings

[Learn the Fundamentals of Analytics Engineering with dbt](https://courses.getdbt.com/courses/fundamentals)

## Commands

![](https://user-images.githubusercontent.com/62965911/214275903-c30fbcbc-febb-4c4a-a3ab-499ef4688e7c.png)

## Data Transformation with Snowpark Python and dbt

dbt is one of the most popular data transformation tools today. And until now dbt has been entirely a SQL-based transformation tool. But with the announcement of dbt Python models, things have changed. It's now possible to create both SQL and Python based models in dbt! Here's how dbt explains it:

dbt Python ("dbt-py") models will help you solve use cases that can't be solved with SQL. You can perform analyses using tools available in the open source Python ecosystem, including state-of-the-art packages for data science and statistics. Before, you would have needed separate infrastructure and orchestration to run Python transformations in production. By defining your Python transformations in dbt, they're just models in your project, with all the same capabilities around testing, documentation, and lineage. ([dbt Python models](https://docs.getdbt.com/docs/building-a-dbt-project/building-models/python-models)). Python based dbt models are made possible by Snowflake's new native Python support and Snowpark API for Python. With Snowflake's native Python support and DataFrame API, you no longer need to maintain and pay for separate infrastructure/services to run Python code, it can be run directly within Snowflake's Enterprise grade data platform!

## More Resources

3. [Transform your data with dbt and Serverless architecture](https://platform.deloitte.com.au/articles/transform-your-data-with-dbt-and-serverless-architecture)
4. [How JetBlue is eliminating the data engineering bottlenecks with dbt](https://www.getdbt.com/success-stories/jetblue/)
5. [dbt development at Vimeo](https://medium.com/vimeo-engineering-blog/dbt-development-at-vimeo-fe1ad9eb212)
6. [Best practices for data modeling with SQL and dbt](https://airbyte.com/blog/sql-data-modeling-with-dbt)
7. https://www.getdbt.com/analytics-engineering/start-here
8. https://www.getdbt.com/blog/what-exactly-is-dbt/
9. [Four Reasons that make DBT a great time saver for Data Engineers](https://medium.com/@montadhar/four-reasons-that-make-dbt-a-great-time-saver-for-data-engineers-4c4ceb721522)
10. https://courses.getdbt.com/courses/fundamentals

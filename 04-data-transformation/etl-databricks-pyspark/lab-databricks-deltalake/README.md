# Databricks Deltalake

Objective: Creation of an elementary Data Lakehouse using Databricks and the Delta lake technology

This lab is the creation of an elementary [Data Lakehouse](https://www.databricks.com/glossary/data-lakehouse) - using [Databricks](https://www.databricks.com) and the [Delta lake](https://delta.io) technology - for a database containing sales data of a fictitious company called “**Northwind** Traders”, which imports and exports specialty foods around the world. 

With the Data Lakehouse created, a **business analysis** is conducted to answer the following questions:

- What are the 5 least sold products?
- What are the top 5 Customers with the highest number of purchases?
- What are the top 5 Customers with the highest purchases value?
- Who was the employee who made more sales last year?

Northwind Database:

![erd](https://user-images.githubusercontent.com/62965911/214517643-7793aab8-f8b4-4e72-805e-c0ab9d52caea.jpg)

## Architecture

![arch](https://user-images.githubusercontent.com/62965911/214517619-ea319823-7f68-4080-8ce6-6a470f052202.png)

**Bronze** layer:

- Python.
- COPY INTO (SQL).

**Silver** layer:

- MERGE INTO (SQL).
- Data types wrangling (SQL).
- Null values wrangling (SQL).

**Gold** layer and **Analysis**:

- PySpark.
- Koalas.
- Spark Pandas.
- Spark/Hive SQL.

## 🗄 Reproducibility

To reproduce the project, follow the steps below:

1. Log into your community version of Databricks.
2. Import the notebook into your workspace
3. Import the ```.csv``` files from ```/data``` folder into your Databricks DBFS.
4. Start a Cluster following the ```requirements.txt``` file guidance.
5. Customize the DBFS root path of ```01-sa-main.ipynb``` in the utilities section according to your specifics.
6. Run all cells in their sequence.

## Cluster

![cluster_config](https://user-images.githubusercontent.com/62965911/214517632-b9955484-9990-4ac8-88c0-919d9d5645c3.png)

![cluster_libs](https://user-images.githubusercontent.com/62965911/214517637-67dc1546-3cfc-4270-87a9-888409dcd53c.png)

## 📚 Learnings

- The project uses the community version of Databricks, which imposes **restrictions**, such as the use of Delta Live Streams, Cloud Partners Integration, Github Integration and Job Scheduling - the usage of this tools would enrich the project by a lot.
- Only structured data was used in the project, but the workspace and project structure - a Data Lakehouse - remains scalable for using semi-structured and unstructured data - just requires the use-case wrangling.

## 🛣 Roadmap

- Transform the Database schema to a Star Schema in the Gold layer.
- Add semi-structured and unstructured data into the Data Lakehouse.
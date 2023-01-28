# Data Pipeline with dbt, Airflow and Great Expectations

In this project, we will learn how to combine the functions of three open source tools - Airflow, dbt and Great expectations - to build, test, validate, document, and orchestrate an entire pipeline, end to end, from scratch. We are going to load the NYC Taxi data into Redshift warehouse and then transform + validate the data using dbt and great expectations.

Data quality has become a much discussed topic in the fields of data engineering and data science, and it’s become clear that data validation is crucial to ensuring the reliability of data products and insights produced by an organization’s data pipelines. Apache Airflow and dbt (data build tool) are among the prominent open source tools in the data engineering ecosystem, and while dbt offers some data testing capabilities, another open source data tool, Great Expectations, enhances the pipeline with data validation and can add layers of robustness.

**By the end of this project, you’ll understand:**

- The basics of dbt, Airflow, and Great Expectations
- How to effectively combine these components to build a robust data pipeline
- When and how to implement data validation using these tools
- How to start developing a data quality strategy for your organization that goes beyond implementing data validation

**And you’ll be able to:**

- Write and run Airflow, dbt, and Great Expectations code
- Design and implement a robust data pipeline
- Implement data validation and alerting across a data pipeline

**This project is for you because…**

- You’re a data engineer or analytics engineer who works with components of the dAG stack and wants to understand how to combine these tools.
- You want to port existing data pipelines over to a modern data stack.
- You’re starting out in data engineering and want to better understand the types of tools used in the field.

**Prerequisites**

- Familiarity with Python and SQL (useful but not required)

**Little bit of theory**

While there is a large number of data engineering frameworks have established themselves as leaders in the modern open-source data stack:

- dbt (data build tool) is a framework that allows data teams to quickly iterate on building data transformation pipelines using templated SQL.
- Apache Airflow is a workflow orchestration tool that enables users to define complex workflows as “DAGs” (directed acyclic graphs) made up of various tasks, as well as schedule and monitor execution.
- Great Expectations is a python-based open-source data validation and documentation framework.

## Project Structure

```
├── [6.6K]  01-sa-main.ipynb
├── [2.5K]  README.md
├── [ 48K]  airflow.cfg
├── [4.5K]  dags
│   ├── [1.5K]  dag1.py
│   ├── [1.3K]  dag2.py
│   └── [1.5K]  dag3.py
├── [ 58K]  data.zip
├── [ 15K]  dbt
│   ├── [  96]  analysis
│   ├── [ 367]  dbt_project.yml
│   ├── [  96]  macros
│   ├── [2.7K]  models
│   │   └── [2.6K]  taxi
│   │       ├── [ 362]  schema.yml
│   │       ├── [1.7K]  staging
│   │       │   ├── [1.1K]  schema.yml
│   │       │   ├── [ 292]  taxi_trips_stage.sql
│   │       │   └── [ 173]  taxi_zone_lookup_stage.sql
│   │       └── [ 396]  trips_with_borough_name.sql
│   ├── [ 233]  profiles.yml
│   ├── [ 497]  requirements.txt
│   ├── [ 10K]  seeds
│   │   └── [ 10K]  taxi_zone_lookup.csv
│   ├── [  96]  snapshots
│   └── [  96]  tests
├── [   0]  download.sh
├── [ 18K]  great_expectations
│   ├── [1.9K]  checkpoints
│   │   ├── [ 910]  yellow_tripdata_sample_2019_01.yml
│   │   └── [ 910]  yellow_tripdata_sample_2019_02.yml
│   ├── [2.2K]  expectations
│   │   └── [2.0K]  my_suite.json
│   ├── [4.2K]  great_expectations.yml
│   ├── [ 987]  plugins
│   │   └── [ 891]  custom_data_docs
│   │       └── [ 795]  styles
│   │           └── [ 699]  data_docs_custom_styles.css
│   └── [8.8K]  scripts
│       ├── [ 581]  checkpoint_taxi_data_load_2019_3.py
│       ├── [ 919]  checkpoint_taxi_data_load_2019_3.yml
│       ├── [ 556]  create_checkpoint.py
│       ├── [ 556]  create_checkpoint_taxi_data_load_2019_1.py
│       ├── [ 765]  create_datasource.py
│       ├── [ 893]  my_checkpoint.yml
│       ├── [ 915]  my_checkpoint_taxi_data_load_2019_2.yml
│       ├── [ 915]  my_checkpoint_taxi_data_load_2019_3.yml
│       ├── [ 929]  sparsh_my_checkpoint_taxi_data_load_2019_3.yml
│       ├── [ 556]  taxi_data_load_2019_1.py
│       └── [1.0K]  yellow_tripdata_taxi_checkpoints.py
├── [ 34K]  main.ipynb
├── [246K]  nbs
│   ├── [ 72K]  Data_Engineering_Lab___Airflow,_dbt_and_Great_Expectations.ipynb
│   ├── [ 54K]  Data_Engineering_Lab___Great_Expectations.ipynb
│   ├── [116K]  Data_Engineering_Lab___Transforming_Data_with_dbt.ipynb
│   └── [4.8K]  session1.ipynb
├── [ 153]  requirements.txt
└── [ 545]  setup-simple.sh

 435K used in 18 directories, 40 files
```
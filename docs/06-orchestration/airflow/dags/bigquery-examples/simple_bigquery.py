import json

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.sensors.bigquery import BigQueryTableExistenceSensor
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
    BigQueryCreateEmptyTableOperator,
    BigQueryInsertJobOperator,
    BigQueryCheckOperator,
    BigQueryValueCheckOperator,
    BigQueryDeleteDatasetOperator,
)
from airflow.utils.dates import datetime
from airflow.utils.task_group import TaskGroup


DATASET = "simple_bigquery_example_dag"
TABLE = "forestfires"

with DAG(
    "simple_bigquery",
    start_date=datetime(2021, 1, 1),
    description="Example DAG showcasing loading and data quality checking with BigQuery.",
    schedule_interval=None,
    template_searchpath="/usr/local/airflow/include/sql/bigquery_examples/",
    catchup=False,
) as dag:
    """
    ### Simple Extract/Load Pipeline with Data Quality Checks Using BigQuery

    Before running the DAG, set the following in an Airflow or Environment Variable:
    - key: gcp_project_id
      value: [gcp_project_id]
    Fully replacing [gcp_project_id] with the actual ID.

    Ensure you have a connection to GCP, using a role with access to BigQuery
    and the ability to create, modify, and delete datasets and tables.

    What makes this a simple data quality case is:
    1. Absolute ground truth: the local CSV file is considered perfect and immutable.
    2. No transformations or business logic.
    3. Exact values of data to quality check are known.
    """

    """
    #### BigQuery dataset creation
    Create the dataset to store the sample data tables.
    """
    create_dataset = BigQueryCreateEmptyDatasetOperator(
        task_id="create_dataset", dataset_id=DATASET
    )

    """
    #### BigQuery table creation
    Create the table to store sample forest fire data.
    """
    create_table = BigQueryCreateEmptyTableOperator(
        task_id="create_table",
        dataset_id=DATASET,
        table_id=TABLE,
        schema_fields=[
            {"name": "id", "type": "INTEGER", "mode": "REQUIRED"},
            {"name": "y", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "month", "type": "STRING", "mode": "NULLABLE"},
            {"name": "day", "type": "STRING", "mode": "NULLABLE"},
            {"name": "ffmc", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "dmc", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "dc", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "isi", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "temp", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "rh", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "wind", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "rain", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "area", "type": "FLOAT", "mode": "NULLABLE"},
        ],
    )

    """
    #### BigQuery table check
    Ensure that the table was created in BigQuery before inserting data.
    """
    check_table_exists = BigQueryTableExistenceSensor(
        task_id="check_for_table",
        project_id="{{ var.value.gcp_project_id }}",
        dataset_id=DATASET,
        table_id=TABLE,
    )

    """
    #### Insert data
    Insert data into the BigQuery table using an existing SQL query (stored in
    a file under dags/sql).
    """
    load_data = BigQueryInsertJobOperator(
        task_id="insert_query",
        configuration={
            "query": {
                "query": "{% include 'load_bigquery_forestfire_data.sql' %}",
                "useLegacySql": False,
            }
        },
    )

    """
    #### Row-level data quality check
    Run data quality checks on a few rows, ensuring that the data in BigQuery
    matches the ground truth in the correspoding JSON file.
    """
    with open("include/validation/forestfire_validation.json") as ffv:
        with TaskGroup(group_id="row_quality_checks") as quality_check_group:
            ffv_json = json.load(ffv)
            for id, values in ffv_json.items():
                values["id"] = id
                values["dataset"] = DATASET
                values["table"] = TABLE
                BigQueryCheckOperator(
                    task_id=f"check_row_data_{id}",
                    sql="row_quality_bigquery_forestfire_check.sql",
                    use_legacy_sql=False,
                    params=values,
                )

    """
    #### Table-level data quality check
    Run a row count check to ensure all data was uploaded to BigQuery properly.
    """
    check_bq_row_count = BigQueryValueCheckOperator(
        task_id="check_row_count",
        sql=f"SELECT COUNT(*) FROM {DATASET}.{TABLE}",
        pass_value=9,
        use_legacy_sql=False,
    )

    """
    #### Delete test dataset and table
    Clean up the dataset and table created for the example.
    """
    delete_dataset = BigQueryDeleteDatasetOperator(
        task_id="delete_dataset", dataset_id=DATASET, delete_contents=True
    )

    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")

    chain(
        begin,
        create_dataset,
        create_table,
        check_table_exists,
        load_data,
        [quality_check_group, check_bq_row_count],
        delete_dataset,
        end,
    )

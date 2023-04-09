import json

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.empty import EmptyOperator
from airflow.providers.snowflake.operators.snowflake import (
    SnowflakeOperator,
    SnowflakeCheckOperator,
    SnowflakeValueCheckOperator,
)
from airflow.utils.dates import datetime
from airflow.utils.task_group import TaskGroup


SNOWFLAKE_FORESTFIRE_TABLE = 'forestfires'

with DAG('simple_snowflake',
         description='Example DAG showcasing loading and data quality checking with Snowflake.',
         start_date=datetime(2021, 1, 1),
         schedule_interval=None,
         template_searchpath="/usr/local/airflow/include/sql/snowflake_examples/",
         catchup=False) as dag:
    """
    ### Simple EL Pipeline with Data Quality Checks Using Snowflake

    Before running the DAG, set the following in an Airflow or Environment Variable:
    - key:

    Ensure a Snowflake Warehouse, Database, Schema, and Role exist for the Snowflake
    connection provided to the Operator. The names of these data should replace the
    dummy values at the top of the file.

    A Snowflake Connection is also needed, named `snowflake_default`.

    What makes this a simple data quality case is:
    1. Absolute ground truth: the local CSV file is considered perfect and immutable.
    2. No transformations or business logic.
    3. Exact values of data to quality check are known.
    """

    """
    #### Snowflake table creation
    Create the table to store sample forest fire data.
    """
    create_table = SnowflakeOperator(
        task_id="create_table",
        sql="{% include 'create_forestfire_table.sql' %}",
        params={"table_name": SNOWFLAKE_FORESTFIRE_TABLE}
    )

    """
    #### Insert data
    Insert data into the Snowflake table using an existing SQL query (stored in
    the include/sql/snowflake_examples/ directory).
    """
    load_data = SnowflakeOperator(
        task_id="insert_query",
        sql="{% include 'load_snowflake_forestfire_data.sql' %}",
        params={"table_name": SNOWFLAKE_FORESTFIRE_TABLE}
    )

    """
    #### Row-level data quality check
    Run data quality checks on a few rows, ensuring that the data in Snowflake
    matches the ground truth in the correspoding JSON file.
    """
    with open("/usr/local/airflow/include/validation/forestfire_validation.json") as ffv:
        with TaskGroup(group_id="row_quality_checks") as quality_check_group:
            ffv_json = json.load(ffv)
            for id, values in ffv_json.items():
                values["id"] = id
                values["table_name"] = SNOWFLAKE_FORESTFIRE_TABLE
                SnowflakeCheckOperator(
                    task_id=f"check_row_data_{id}",
                    sql="row_quality_snowflake_forestfire_check.sql",
                    params=values
                )

    """
    #### Table-level data quality check
    Run a row count check to ensure all data was uploaded to Snowflake properly.
    """
    check_bq_row_count = SnowflakeValueCheckOperator(
        task_id="check_row_count",
        sql=f"SELECT COUNT(*) FROM {SNOWFLAKE_FORESTFIRE_TABLE}",
        pass_value=9
    )

    """
    #### Delete table
    Clean up the table created for the example.
    """
    delete_table = SnowflakeOperator(
        task_id="delete_table",
        sql="{% include 'delete_snowflake_table.sql' %}",
        params={"table_name": SNOWFLAKE_FORESTFIRE_TABLE}
    )

    begin = EmptyOperator(task_id='begin')
    end = EmptyOperator(task_id='end')

    chain(
        begin,
        create_table,
        load_data,
        [quality_check_group, check_bq_row_count],
        delete_table,
        end
    )

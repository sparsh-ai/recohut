import os

from pathlib import Path
from datetime import datetime

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.amazon.aws.transfers.local_to_s3 import (
    LocalFilesystemToS3Operator,
)
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.snowflake.transfers.s3_to_snowflake import S3ToSnowflakeOperator
from great_expectations_provider.operators.great_expectations import (
    GreatExpectationsOperator,
)
from include.great_expectations.configs.snowflake_configs import (
    snowflake_checkpoint_config,
)

# This table variable is a placeholder, in a live environment, it is better
# to pull the table info from a Variable in a template
table = "YELLOW_TRIPDATA"
base_path = Path(__file__).parents[2]
data_file = os.path.join(
    base_path,
    "include",
    "sample_data/yellow_trip_data/yellow_tripdata_sample_2019-01.csv",
)
ge_root_dir = os.path.join(base_path, "include", "great_expectations")
checkpoint_config = snowflake_checkpoint_config

with DAG(
    "great_expectations.snowflake",
    start_date=datetime(2021, 1, 1),
    description="Example DAG showcasing loading and data quality checking with Snowflake and Great Expectations.",
    schedule_interval=None,
    template_searchpath=f"{base_path}/include/sql/great_expectations_examples/",
    catchup=False,
) as dag:
    """
    ### Simple EL Pipeline with Data Quality Checks Using Snowflake and Great Expectations

    Ensure a Snowflake Warehouse, Database, Schema, Role, and S3 Key and Secret
    exist for the Snowflake connection, named `snowflake_default`. Access to S3
    is needed for this example. An 'aws_configs' variable is needed in Variables,
    see the Redshift Examples in the README section for more information.

    What makes this a simple data quality case is:
    1. Absolute ground truth: the local CSV file is considered perfect and immutable.
    2. No transformations or business logic.
    3. Exact values of data to quality check are known.
    """

    """
    #### Upload task
    Simply loads the file to a specified location in S3.
    """
    upload_to_s3 = LocalFilesystemToS3Operator(
        task_id="upload_to_s3",
        filename=data_file,
        dest_key="{{ var.json.aws_configs.s3_key_prefix }}/tripdata/yellow_tripdata_sample_2019-01.csv",
        dest_bucket="{{ var.json.aws_configs.s3_bucket }}",
        aws_conn_id="aws_default",
        replace=True,
    )

    """
    #### Snowflake table creation
    Create the table to store sample data.
    """
    create_snowflake_table = SnowflakeOperator(
        task_id="create_snowflake_table",
        sql="{% include 'create_yellow_tripdata_snowflake_table.sql' %}",
        params={
            "table_name": table,
        },
    )

    """
    #### Snowflake stage creation
    Create the stage to load data into from S3
    """
    create_snowflake_stage = SnowflakeOperator(
        task_id="create_snowflake_stage",
        sql="{% include 'create_snowflake_yellow_tripdata_stage.sql' %}",
        params={"stage_name": f"{table}_STAGE"},
    )

    """
    #### Delete table
    Clean up the table created for the example.
    """
    delete_snowflake_table = SnowflakeOperator(
        task_id="delete_snowflake_table",
        sql="{% include 'delete_yellow_tripdata_table.sql' %}",
        params={"table_name": table},
        trigger_rule="all_done",
    )

    """
    #### Snowflake load task
    Loads the S3 data from the previous load to a Redshift table (specified
    in the Airflow Variables backend).
    """
    load_to_snowflake = S3ToSnowflakeOperator(
        task_id="load_to_snowflake",
        prefix="test/tripdata",
        stage=f"{table}_STAGE",
        table=table,
        file_format="(type = 'CSV', skip_header = 1, time_format = 'YYYY-MM-DD HH24:MI:SS')",
    )

    """
    #### Great Expectations suite
    Run the Great Expectations suite on the table.
    """
    ge_snowflake_validation = GreatExpectationsOperator(
        task_id="ge_snowflake_validation",
        data_context_root_dir=ge_root_dir,
        checkpoint_config=checkpoint_config,
    )

    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")

    chain(
        begin,
        upload_to_s3,
        create_snowflake_table,
        create_snowflake_stage,
        load_to_snowflake,
        ge_snowflake_validation,
        delete_snowflake_table,
        end,
    )

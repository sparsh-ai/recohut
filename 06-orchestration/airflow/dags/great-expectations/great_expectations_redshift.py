import os

from pathlib import Path
from datetime import datetime

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.amazon.aws.transfers.local_to_s3 import (
    LocalFilesystemToS3Operator,
)
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from great_expectations_provider.operators.great_expectations import (
    GreatExpectationsOperator,
)
from include.great_expectations.configs.redshift_configs import (
    redshift_checkpoint_config,
)

table = "yellow_tripdata"
base_path = Path(__file__).parents[2]
data_file = os.path.join(
    base_path,
    "include",
    "sample_data/yellow_trip_data/yellow_tripdata_sample_2019-01.csv",
)
ge_root_dir = os.path.join(base_path, "include", "great_expectations")
checkpoint_config = redshift_checkpoint_config

with DAG(
    "great_expectations.redshift",
    start_date=datetime(2021, 1, 1),
    description="Example DAG showcasing loading and data quality checking with Redshift and Great Expectations.",
    schedule_interval=None,
    template_searchpath=f"{base_path}/include/sql/great_expectations_examples/",
    catchup=False,
) as dag:
    """
    ### Simple EL Pipeline with Data Quality Checks Using Redshift and Great Expectations

    Before running the DAG, set the following in an Airflow or Environment Variable:
    - key: aws_configs
    - value: { "s3_bucket": [bucket_name], "s3_key_prefix": [key_prefix], "redshift_table": [table_name]}
    Fully replacing [bucket_name], [key_prefix], and [table_name].

    What makes this a simple data quality case is:
    1. Absolute ground truth: the local CSV file is considered perfect and immutable.
    2. No transformations or business logic.
    3. Exact values of data to quality check are known.
    """

    upload_to_s3 = LocalFilesystemToS3Operator(
        task_id="upload_to_s3",
        filename=data_file,
        dest_key="{{ var.json.aws_configs.s3_key_prefix }}/yellow_tripdata_sample_2019-01.csv",
        dest_bucket="{{ var.json.aws_configs.s3_bucket }}",
        aws_conn_id="aws_default",
        replace=True,
    )

    """
    #### Create Redshift Table
    For demo purposes, create a Redshift table to store the forest fire data to.
    The database is not automatically destroyed at the end of the example; ensure
    this is done manually to avoid unnecessary costs. Additionally, set-up may
    need to be done in Airflow connections to allow access to Redshift.
    """
    create_redshift_table = PostgresOperator(
        task_id="create_redshift_table",
        sql="{% include 'create_yellow_tripdata_redshift_table.sql' %}",
        params={"table_name": "yellow_tripdata"},
        postgres_conn_id="redshift_default",
    )

    """
    #### Second load task
    Loads the S3 data from the previous load to a Redshift table (specified
    in the Airflow Variables backend).
    """
    load_to_redshift = S3ToRedshiftOperator(
        task_id="load_to_redshift",
        s3_bucket="{{ var.json.aws_configs.s3_bucket }}",
        s3_key="{{ var.json.aws_configs.s3_key_prefix }}/yellow_tripdata_sample_2019-01.csv",
        schema="PUBLIC",
        table=table,
        copy_options=["csv", "ignoreheader 1"],
    )

    """
    #### Great Expectations suite
    Run the Great Expectations suite on the table.
    """
    ge_redshift_validation = GreatExpectationsOperator(
        task_id="ge_redshift_validation",
        data_context_root_dir=ge_root_dir,
        checkpoint_config=checkpoint_config,
    )

    """
    #### Drop Redshift table
    Drops the Redshift table if it exists already. This is to make sure that the
    data in the success and failure cases do not interfere with each other during
    the data quality check.
    """
    drop_redshift_table = PostgresOperator(
        task_id="drop_table",
        sql="delete_yellow_tripdata_table.sql",
        postgres_conn_id="redshift_default",
        params={"table_name": table},
    )

    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")

    chain(
        begin,
        upload_to_s3,
        create_redshift_table,
        load_to_redshift,
        ge_redshift_validation,
        drop_redshift_table,
        end,
    )

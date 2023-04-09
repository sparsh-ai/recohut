import os

from pathlib import Path
from datetime import datetime

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateEmptyDatasetOperator,
    BigQueryDeleteDatasetOperator,
    BigQueryCreateEmptyTableOperator,
)
from airflow.providers.google.cloud.transfers.local_to_gcs import (
    LocalFilesystemToGCSOperator,
)
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import (
    GCSToBigQueryOperator,
)
from great_expectations_provider.operators.great_expectations import (
    GreatExpectationsOperator,
)
from include.great_expectations.configs.bigquery_configs import (
    bigquery_checkpoint_config,
)

base_path = Path(__file__).parents[2]
data_file = os.path.join(
    base_path,
    "include",
    "sample_data/yellow_trip_data/yellow_tripdata_sample_2019-01.csv",
)
ge_root_dir = os.path.join(base_path, "include", "great_expectations")
checkpoint_config = bigquery_checkpoint_config

# In a production DAG, the global variables below should be stored as Airflow
# or Environment variables.
bq_dataset = "great_expectations_bigquery_example"
bq_table = "taxi"
gcp_bucket = "great-expectations-demo"
gcp_data_dest = "data/yellow_tripdata_sample_2019-01.csv"

with DAG(
    "great_expectations.bigquery",
    description="Example DAG showcasing loading and data quality checking with BigQuery and Great Expectations.",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:
    """
    ### Simple EL Pipeline with Data Quality Checks Using BigQuery and Great Expectations

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
        task_id="create_dataset", dataset_id=bq_dataset
    )

    """
    #### Upload taxi data to GCS
    Upload the test data to GCS so it can be transferred to BigQuery.
    """
    upload_taxi_data = LocalFilesystemToGCSOperator(
        task_id="upload_taxi_data",
        src=data_file,
        dst=gcp_data_dest,
        bucket=gcp_bucket,
    )

    """
    #### Create Temp Table for GE in BigQuery
    """
    create_temp_table = BigQueryCreateEmptyTableOperator(
        task_id="create_temp_table",
        dataset_id=bq_dataset,
        table_id=f"{bq_table}_temp",
        schema_fields=[
            {"name": "vendor_id", "type": "INTEGER", "mode": "REQUIRED"},
            {"name": "pickup_datetime", "type": "DATETIME", "mode": "NULLABLE"},
            {"name": "dropoff_datetime", "type": "DATETIME", "mode": "NULLABLE"},
            {"name": "passenger_count", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "trip_distance", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "rate_code_id", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "store_and_fwd_flag", "type": "STRING", "mode": "NULLABLE"},
            {"name": "pickup_location_id", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "dropoff_location_id", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "payment_type", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "fare_amount", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "extra", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "mta_tax", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "tip_amount", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "tolls_amount", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "improvement_surcharge", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "total_amount", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "congestion_surcharge", "type": "FLOAT", "mode": "NULLABLE"},
        ],
    )

    """
    #### Transfer data from GCS to BigQuery
    Moves the data uploaded to GCS in the previous step to BigQuery, where
    Great Expectations can run a test suite against it.
    """
    transfer_taxi_data = GCSToBigQueryOperator(
        task_id="taxi_data_gcs_to_bigquery",
        bucket=gcp_bucket,
        source_objects=[gcp_data_dest],
        skip_leading_rows=1,
        destination_project_dataset_table="{}.{}".format(bq_dataset, bq_table),
        schema_fields=[
            {"name": "vendor_id", "type": "INTEGER", "mode": "REQUIRED"},
            {"name": "pickup_datetime", "type": "DATETIME", "mode": "NULLABLE"},
            {"name": "dropoff_datetime", "type": "DATETIME", "mode": "NULLABLE"},
            {"name": "passenger_count", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "trip_distance", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "rate_code_id", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "store_and_fwd_flag", "type": "STRING", "mode": "NULLABLE"},
            {"name": "pickup_location_id", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "dropoff_location_id", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "payment_type", "type": "INTEGER", "mode": "NULLABLE"},
            {"name": "fare_amount", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "extra", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "mta_tax", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "tip_amount", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "tolls_amount", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "improvement_surcharge", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "total_amount", "type": "FLOAT", "mode": "NULLABLE"},
            {"name": "congestion_surcharge", "type": "FLOAT", "mode": "NULLABLE"},
        ],
        source_format="CSV",
        create_disposition="CREATE_IF_NEEDED",
        write_disposition="WRITE_TRUNCATE",
        allow_jagged_rows=True,
    )

    """
    #### Great Expectations suite
    Run the Great Expectations suite on the table.
    """
    ge_bigquery_validation = GreatExpectationsOperator(
        task_id="ge_bigquery_validation",
        data_context_root_dir=ge_root_dir,
        checkpoint_config=checkpoint_config,
    )

    """
    #### Delete test dataset and table
    Clean up the dataset and table created for the example.
    """
    delete_dataset = BigQueryDeleteDatasetOperator(
        task_id="delete_dataset",
        project_id="{{ var.value.gcp_project_id }}",
        dataset_id=bq_dataset,
        delete_contents=True,
    )

    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")

    chain(
        begin,
        create_dataset,
        create_temp_table,
        upload_taxi_data,
        transfer_taxi_data,
        ge_bigquery_validation,
        delete_dataset,
        end,
    )

import os

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.google.cloud.operators.bigquery import (
    BigQueryCreateExternalTableOperator,
    BigQueryInsertJobOperator
)


PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
BIGQUERY_DATASET = os.environ.get("BIGQUERY_DATASET", 'trips_data')

DATASET = "citibike_tripdata"
PARTITION_COL = 'starttime'
CLUSTER_COL = 'bikeid'
INPUT_PART = "raw"
INPUT_FILETYPE = "parquet"

default_args = {
    "owner": "airflow",
    "start_date": days_ago(1),
    "depends_on_past": False,
    "retries": 1,
}

# NOTE: DAG declaration - using a Context Manager (an implicit way)
with DAG(
    dag_id="gcs_to_bq_dag",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False,
    max_active_runs=1,
    tags=['city-bikes'],
) as dag:

    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id=f"bq_{DATASET}_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": f"{DATASET}_external_table",
            },
            "externalDataConfiguration": {
                "autodetect": "True",
                "sourceFormat": f"{INPUT_FILETYPE.upper()}",
                "sourceUris": [
                    f"gs://{BUCKET}/city_bikes_trips/2018/*.{INPUT_FILETYPE}",
                    f"gs://{BUCKET}/city_bikes_trips/2019/*.{INPUT_FILETYPE}",
                    f"gs://{BUCKET}/city_bikes_trips/2020/*.{INPUT_FILETYPE}",
                ],
            },
        },
    )

    CREATE_BQ_TBL_QUERY = (
        f"CREATE OR REPLACE TABLE {BIGQUERY_DATASET}.{DATASET} \
        PARTITION BY DATE({PARTITION_COL}) \
        CLUSTER BY {CLUSTER_COL} AS \
        SELECT * FROM {BIGQUERY_DATASET}.{DATASET}_external_table;"
    )

    # Create a partitioned and clustered table from external table
    bq_create_partitioned_table_job = BigQueryInsertJobOperator(
        task_id=f"bq_create_{DATASET}_optimized_table_task",
        configuration={
            "query": {
                "query": CREATE_BQ_TBL_QUERY,
                "useLegacySql": False,
            }
        }
    )

    bigquery_external_table_task >> bq_create_partitioned_table_job

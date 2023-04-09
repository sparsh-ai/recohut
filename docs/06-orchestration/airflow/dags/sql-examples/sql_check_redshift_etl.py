from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import datetime
from airflow.operators.sql import (
    SQLCheckOperator,
    SQLValueCheckOperator,
    SQLIntervalCheckOperator,
    SQLThresholdCheckOperator
)
from airflow.utils.task_group import TaskGroup
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.decorators import task

import pandas as pd


DATES = ["2019-01", "2019-02"]
TASK_DICT = {}

with DAG("sql_data_quality_redshift_etl",
         start_date=datetime(2021, 7, 7),
         description="A sample Airflow DAG to perform data quality checks using SQL Operators.",
         schedule_interval=None,
         default_args={"conn_id": "redshift_default"},
         template_searchpath="/usr/local/airflow/include/sql/sql_examples/",
         catchup=False) as dag:
    """
    ### SQL Check Operators Data Quality ETL Example

    Before running the DAG, set the following in an Airflow or Environment Variable:
    - key: aws_configs
    - value: { "s3_bucket": [bucket_name], "s3_key_prefix": [key_prefix], "redshift_table": [table_name]}
    Fully replacing [bucket_name], [key_prefix], and [table_name].

    See the README for information on how to set up your Redshift connection.
    This DAG can be used with other databases as long as the Redshift (and possibly
    transfer operators) are changed.
    """

    """
    #### Dummy operators
    Help label start and end of dag. Converges exist because lists of tasks
    cannot set another list as downstream.
    """
    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")
    converge_1 = DummyOperator(task_id="converge_1")
    converge_2 = DummyOperator(task_id="converge_2")

    """
    #### Create Redshift Table
    For demo purposes, create a Redshift table to store the forest fire data to.
    The database is not automatically destroyed at the end of the example; ensure
    this is done manually to avoid unnecessary costs. Additionally, set-up may
    need to be done in Airflow connections to allow access to Redshift.
    """
    create_redshift_table = PostgresOperator(
        task_id="create_table",
        sql="create_redshift_yellow_tripdata_table.sql",
        postgres_conn_id="redshift_default"
    )

    with TaskGroup(group_id="row_quality_checks") as quality_check_group:
        # Create 10 tasks, to spot-check 10 random rows
        for i in range(0, 10):
            """
            #### Run Row-Level Quality Checks
            Runs a series of checks on different columns of data for a single,
            randomly chosen row. This acts as a spot-check on data. Note: When
            using the sample data, row level checks may fail. Which column(s) of
            the row that failed may be checked in the logs. To further diagnose
            the issue, run a modified query directly in Redshift's query editor
            to check individual values against calculations and expectations.
            """
            SQLCheckOperator(
                task_id=f"yellow_tripdata_row_quality_check_{i}",
                sql="row_quality_yellow_tripdata_check.sql"
            )

    """
    #### Run Table-Level Quality Check
    Ensure that the correct number of rows are present in the table.
    """
    value_check = SQLValueCheckOperator(
        task_id="check_row_count",
        sql="SELECT COUNT(*) FROM {{ var.json.aws_configs.redshift_table }};",
        pass_value=20000
    )

    """
    #### Run Interval Check
    Check that the average trip distance today is within a desirable threshold
    compared to the average trip distance yesterday.
    """
    interval_check = SQLIntervalCheckOperator(
        task_id="check_interval_data",
        table="{{ var.json.aws_configs.redshift_table }}",
        days_back=-1,
        date_filter_column="upload_date",
        metrics_thresholds={"AVG(trip_distance)": 1.5}
    )

    """
    #### Threshold Check
    Similar to the threshold cases in the Row-Level Check above, ensures that
    certain row(s) values meet the desired threshold(s).
    """
    threshold_check = SQLThresholdCheckOperator(
        task_id="check_threshold",
        sql="SELECT MAX(passenger_count) FROM {{ var.json.aws_configs.redshift_table }};",
        min_threshold=1,
        max_threshold=8
    )

    """
    #### Drop Redshift table
    Drops the Redshift table if it exists already. This is to make sure that the
    data in the success and failure cases do not interfere with each other during
    the data quality check.
    """
    drop_redshift_table = PostgresOperator(
        task_id="drop_table",
        sql="drop_redshift_yellow_tripdata_table.sql",
        postgres_conn_id="redshift_default"
    )

    @task
    def add_upload_date(file_path, upload_date):
        """
        #### Transform Task
        In general, it is not recommended to perform transform operations in
        Airflow Tasks, as Airflow is designed to be an orchestrator, not a
        computation engine. However, the transform is done here as it is a
        relatively small operation, simply adding an upload_date column to the
        dataframe for use in the SQL data quality checks later. Doing the
        transform here also makes this example more easily extensible to the
        use of other backend datastores.
        """
        trip_dict = pd.read_csv(
            file_path,
            header=0,
            parse_dates=["pickup_datetime"],
            infer_datetime_format=True
        )
        trip_dict["upload_date"] = upload_date
        trip_dict.to_csv(
            file_path,
            header=True,
            index=False
        )

    @task
    def delete_upload_date(file_path):
        """
        #### Drop added column
        Drops the upload_date column used for this example, as this data is used
        by other example DAGs in this repository, so it should not interfere
        with those.
        """
        trip_dict = pd.read_csv(
            file_path,
            header=0,
            parse_dates=["pickup_datetime"],
            infer_datetime_format=True
        )
        trip_dict.drop(columns="upload_date", inplace=True)
        trip_dict.to_csv(
            file_path,
            header=True,
            index=False
        )

    for i, date in enumerate(DATES):
        file_path = f"/usr/local/airflow/include/sample_data/yellow_trip_data/yellow_tripdata_sample_{date}.csv"

        TASK_DICT[f"add_upload_date_{date}"] = add_upload_date(
            file_path,
            "{{ macros.ds_add(ds, " + str(-i) + ") }}"
        )

        """
        #### Upload task
        Simply loads the file to a specified location in S3.
        """
        TASK_DICT[f"upload_to_s3_{date}"] = LocalFilesystemToS3Operator(
            task_id=f"upload_to_s3_{date}",
            filename=file_path,
            dest_key="{{ var.json.aws_configs.s3_key_prefix }}/" + file_path,
            dest_bucket="{{ var.json.aws_configs.s3_bucket }}",
            aws_conn_id="aws_default",
            replace=True
        )

        """
        #### Redshift load task
        Loads the S3 data from the previous load to a Redshift table (specified
        in the Airflow Variables backend).
        """
        TASK_DICT[f"load_to_redshift_{date}"] = S3ToRedshiftOperator(
            task_id=f"load_to_redshift_{date}",
            s3_bucket="{{ var.json.aws_configs.s3_bucket }}",
            s3_key="{{ var.json.aws_configs.s3_key_prefix }}/" + file_path,
            schema="PUBLIC",
            table="{{ var.json.aws_configs.redshift_table }}",
            copy_options=["csv",
                          "ignoreheader 1",
                          "TIMEFORMAT AS 'YYYY-MM-DD HH24:MI:SS'"]
        )

        TASK_DICT[f"delete_upload_date_{date}"] = delete_upload_date(file_path)

        chain(
            begin,
            [TASK_DICT[f"add_upload_date_{date}"]],
            converge_1,
            [TASK_DICT[f"upload_to_s3_{date}"]],
            create_redshift_table,
            [TASK_DICT[f"load_to_redshift_{date}"]],
            converge_2,
            [quality_check_group, value_check, interval_check, threshold_check],
            drop_redshift_table,
            [TASK_DICT[f"delete_upload_date_{date}"]],
            end
        )

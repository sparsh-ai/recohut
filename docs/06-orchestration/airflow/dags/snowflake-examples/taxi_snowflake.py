import pandas as pd

from airflow import DAG
from airflow.decorators import task
from airflow.models.baseoperator import chain
from airflow.operators.empty import EmptyOperator
from airflow.utils.dates import datetime
from airflow.utils.task_group import TaskGroup
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.providers.snowflake.transfers.s3_to_snowflake import S3ToSnowflakeOperator
from plugins.snowflake_check_operators import (
    SnowflakeCheckOperator,
    SnowflakeValueCheckOperator,
    SnowflakeIntervalCheckOperator,
    SnowflakeThresholdCheckOperator,
)

# This table variable is a placeholder, in a live environment, it is better
# to pull the table info from a Variable in a template
TABLE = "YELLOW_TRIPDATA_WITH_UPLOAD_DATE"
DATES = ["2019-01", "2019-02"]
TASK_DICT = {}
SNOWFLAKE_CONN_ID = "snowflake_default"

with DAG(
    "taxi_snowflake",
    start_date=datetime(2021, 7, 7),
    description="A sample Airflow DAG to perform data quality checks using SQL Operators.",
    schedule_interval=None,
    template_searchpath="/usr/local/airflow/include/sql/snowflake_examples/",
    catchup=False,
) as dag:
    """
    ### SQL Check Operators Data Quality Example with Snowflake

    Ensure a Snowflake Warehouse, Database, Schema, Role, and S3 Key and Secret
    exist for the Snowflake connection, named `snowflake_default`. Access to S3
    is needed for this example. A staging table may need to be created in
    Snowflake manually.

    Note: The data files for this example do **not** include an `upload_date`
    column. This column is needed for the interval check, and is added as a
    Task.
    """

    begin = EmptyOperator(task_id="begin")
    end = EmptyOperator(task_id="end")
    converge_1 = EmptyOperator(task_id="converge_1")

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

    """
    #### Snowflake table creation
    Create the table to store sample data.
    """
    create_snowflake_table = SnowflakeOperator(
        task_id="create_snowflake_table",
        sql="{% include 'create_snowflake_yellow_tripdata_table.sql' %}",
        params={"table_name": TABLE}
    )

    """
    #### Snowflake stage creation
    Create the stage to load data into from S3
    """
    create_snowflake_stage = SnowflakeOperator(
        task_id="create_snowflake_stage",
        sql="{% include 'create_snowflake_yellow_tripdata_stage.sql' %}",
        params={"stage_name": f"{TABLE}_STAGE"}
    )

    """
    #### Delete table
    Clean up the table created for the example.
    """
    delete_snowflake_table = SnowflakeOperator(
        task_id="delete_snowflake_table",
        sql="{% include 'delete_snowflake_table.sql' %}",
        params={"table_name": TABLE},
        trigger_rule="all_done"
    )

    """
    #### Run Table-Level Quality Check
    Ensure that the correct number of rows are present in the table.
    """
    value_check = SnowflakeValueCheckOperator(
        task_id="check_row_count",
        sql=f"SELECT COUNT(*) FROM {TABLE};",
        pass_value=20000,
    )

    """
    #### Run Interval Check
    Check that the average trip distance today is within a desirable threshold
    compared to the average trip distance yesterday.
    """
    interval_check = SnowflakeIntervalCheckOperator(
        task_id="check_interval_data",
        table=TABLE,
        days_back=-1,
        date_filter_column="upload_date",
        metrics_thresholds={"AVG(trip_distance)": 1.5},
    )

    """
    #### Threshold Check
    Similar to the threshold cases in the Row-Level Check above, ensures that
    certain row(s) values meet the desired threshold(s).
    """
    threshold_check = SnowflakeThresholdCheckOperator(
        task_id="check_threshold",
        sql=f"SELECT MAX(passenger_count) FROM {TABLE};",
        min_threshold=1,
        max_threshold=8,
    )

    """
    #### Run Row-Level Quality Checks
    Runs a series of checks on different columns of data. Due to SQLCheckOperator's
    current implementation, only one row is returned, so an aggregate value of
    the data is actually checked. A failure then indicates that **at least one**
    row failed, but a success that all rows succeeded.
    """
    with TaskGroup(group_id="row_quality_checks") as quality_check_group:
        """
        #### Row Quality Check
        Run the check across all columns in one query. This method works when
        queries are small and unlikely to ever change. When too many columns
        are being returned, it can become difficult to diagnose what failed.
        """
        row_quality_check = SnowflakeCheckOperator(
            task_id="row_quality_check",
            sql="row_quality_yellow_tripdata_check.sql",
            params={"table": TABLE}
        )

        """
        #### Row Quality Check Template
        Break the above query out into each quality check using a sql template
        file. This more modular approach is more flexible, and easily allows
        more tests to be added. Although it does increase the amount of tasks
        linearly with the number of tests, it is the recommended appraoch due to
        its greater observability, flexibility, and modularity.
        """
        date_check = SnowflakeCheckOperator(
            task_id="date_check",
            sql="row_quality_yellow_tripdata_template.sql",
            params={
                "check_name": "date_check",
                "check_statement": "dropoff_datetime > pickup_datetime",
                "table": TABLE
            },
        )

        passenger_count_check = SnowflakeCheckOperator(
            task_id="passenger_count_check",
            sql="row_quality_yellow_tripdata_template.sql",
            params={
                "check_name": "passenger_count_check",
                "check_statement": "passenger_count >= 0",
                "table": TABLE
            },
        )

        trip_distance_check = SnowflakeCheckOperator(
            task_id="trip_distance_check",
            sql="row_quality_yellow_tripdata_template.sql",
            params={
                "check_name": "trip_distance_check",
                "check_statement": "trip_distance >= 0 AND trip_distance <= 100",
                "table": TABLE
            },
        )

        fare_check = SnowflakeCheckOperator(
            task_id="fare_check",
            sql="row_quality_yellow_tripdata_template.sql",
            params={
                "check_name": "fare_check",
                "check_statement": "ROUND((fare_amount + extra + mta_tax + tip_amount + improvement_surcharge + COALESCE(congestion_surcharge, 0)), 1) = ROUND(total_amount, 1) THEN 1 WHEN ROUND(fare_amount + extra + mta_tax + tip_amount + improvement_surcharge, 1) = ROUND(total_amount, 1)",
                "table": TABLE
            },
        )

    """
    #### Snowflake load task
    Loads the S3 data from the previous load to a Redshift table (specified
    in the Airflow Variables backend).
    """
    load_to_snowflake = S3ToSnowflakeOperator(
        task_id="load_to_snowflake",
        prefix="test/tripdata_to_snowflake",
        stage=f"{TABLE}_STAGE",
        table=TABLE,
        file_format="(type = 'CSV', skip_header = 1, time_format = 'YYYY-MM-DD HH24:MI:SS')"
    )

    for i, date in enumerate(DATES):
        file_name = f"yellow_tripdata_sample_{date}.csv"
        file_path = f"/usr/local/airflow/include/sample_data/yellow_trip_data/{file_name}"

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
            dest_key="{{ var.json.aws_configs.s3_key_prefix }}/tripdata_to_snowflake/" + file_name,
            dest_bucket="{{ var.json.aws_configs.s3_bucket }}",
            aws_conn_id="aws_default",
            replace=True
        )

        TASK_DICT[f"delete_upload_date_{date}"] = delete_upload_date(
            file_path)

        chain(
            begin,
            [TASK_DICT[f"add_upload_date_{date}"]],
            converge_1,
            [TASK_DICT[f"upload_to_s3_{date}"]],
            create_snowflake_table,
            create_snowflake_stage,
            load_to_snowflake,
            [quality_check_group, value_check,
                interval_check, threshold_check],
            delete_snowflake_table,
            [TASK_DICT[f"delete_upload_date_{date}"]],
            end
        )

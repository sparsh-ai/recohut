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

# This table variable is a placeholder, in a live environment, it is better
# to pull the table info from a Variable in a template
TABLE = "yellow_tripdata"
DATES = ["2019-01", "2019-02"]

# By putting conn_id as a default_arg, the arg is passed to every task,
# reducing boilerplate
with DAG("sql_data_quality",
         start_date=datetime(2021, 7, 7),
         description="A sample Airflow DAG to perform data quality checks using SQL Operators.",
         schedule_interval=None,
         default_args={"conn_id": "postgres_default"},
         template_searchpath="/usr/local/airflow/include/sql/sql_examples/",
         catchup=False) as dag:
    """
    ### SQL Check Operators Data Quality Example

    Before running the DAG, ensure you have an active and reachable SQL database
    running, with a connection to that database in an Airflow Connection, and
    the data loaded. This DAG **will not** run successfully as-is. For an
    out-of-the-box working demo, see the sql_data_quality_redshift_etl DAG.

    Note: The data files for this example do **not** include an `upload_date`
    column. This column is needed for the interval check, and is added as a
    Task in sql_check_redshift_etl.py.
    """

    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")

    """
    #### Run Table-Level Quality Check
    Ensure that the correct number of rows are present in the table.
    """
    value_check = SQLValueCheckOperator(
        task_id="check_row_count",
        sql=f"SELECT COUNT(*) FROM {TABLE};",
        pass_value=20000
    )

    """
    #### Run Interval Check
    Check that the average trip distance today is within a desirable threshold
    compared to the average trip distance yesterday.
    """
    interval_check = SQLIntervalCheckOperator(
        task_id="check_interval_data",
        table=TABLE,
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
        sql=f"SELECT MAX(passenger_count) FROM {TABLE};",
        min_threshold=1,
        max_threshold=8
    )

    """
    #### Run Row-Level Quality Checks
    For each date of data, run checks on 10 rows to ensure basic data quality
    cases (found in the .sql file) pass.
    """
    with TaskGroup(group_id="row_quality_checks") as quality_check_group:
        # Create 10 tasks, to spot-check 10 random rows
        for i in range(0, 10):
            """
            #### Run Row-Level Quality Checks
            Runs a series of checks on different columns of data for a single,
            randomly chosen row. This acts as a spot-check on data.
            """
            SQLCheckOperator(
                task_id=f"yellow_tripdata_row_quality_check_{i}",
                sql="row_quality_yellow_tripdata_check.sql"
            )

        chain(
            begin,
            [quality_check_group, value_check, interval_check, threshold_check],
            end
        )

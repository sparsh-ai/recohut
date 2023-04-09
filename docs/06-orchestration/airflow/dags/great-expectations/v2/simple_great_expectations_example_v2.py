"""
NOTE: This DAG uses the Great Expectations V2 API which is deprecated in favor of
the V3 API. This DAG will not work with the requirements file in the repository.
"""

import os

from datetime import datetime

from airflow import DAG
from airflow.models.baseoperator import chain
from great_expectations_provider.operators.great_expectations import (
    GreatExpectationsOperator,
)


base_path = "/usr/local/airflow/"
data_file = os.path.join(
    base_path, "include", "data/yellow_tripdata_sample_2019-01.csv"
)
ge_root_dir = os.getenv("GE_DATA_CONTEXT_ROOT_DIR")

with DAG(
    dag_id="example_great_expectations_dag",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    default_args={"data_context_root_dir": ge_root_dir},
) as dag:

    """
    ### Simple Great Expectations Example
    This runs an expectation suite against a sample data asset. Before running the DAG,
    you may need to change these paths if you do not have your `data` directory
    living in a top-level `include` directory. Ensure the checkpoint yml files
    have the correct path to the data file.
    What makes this a simple data quality case is:
    1. Absolute ground truth: the local data file is considered perfect and immutable.
    2. No transformations or business logic.
    3. Exact values of data to quality check are known.
    """

    """
    #### This runs an expectation suite against a data asset that passes the tests
    """
    ge_batch_kwargs_list_pass = GreatExpectationsOperator(
        task_id="ge_batch_kwargs_list_pass",
        assets_to_validate=[
            {
                "batch_kwargs": {"path": data_file, "datasource": "data__dir"},
                "expectation_suite_name": "taxi.demo",
            }
        ],
    )

    """
    #### This runs a checkpoint and passes in a root dir
    """
    ge_checkpoint_pass_root_dir = GreatExpectationsOperator(
        task_id="ge_checkpoint_pass_root_dir",
        run_name="ge_airflow_run",
        checkpoint_name="taxi.pass.chk",
    )

    """
    #### This runs an expectation suite using the batch_kwargs parameter
    """
    ge_batch_kwargs_pass = GreatExpectationsOperator(
        task_id="ge_batch_kwargs_pass",
        expectation_suite_name="taxi.demo",
        batch_kwargs={"path": data_file, "datasource": "data__dir"},
    )

    """
    #### This runs a checkpoint that will fail, but we set a flag to exit the
         task successfully.
    """
    ge_checkpoint_fail_but_continue = GreatExpectationsOperator(
        task_id="ge_checkpoint_fail_but_continue",
        run_name="ge_airflow_run",
        checkpoint_name="taxi.fail.chk",
        fail_task_on_validation_failure=False,
    )

    """
    #### This runs a checkpoint that will pass. Make sure the checkpoint yml file
         has the correct path to the data file
    """
    ge_checkpoint_pass = GreatExpectationsOperator(
        task_id="ge_checkpoint_pass",
        run_name="ge_airflow_run",
        checkpoint_name="taxi.pass.chk",
    )

    """
    #### This runs a checkpoint that will fail. Make sure the checkpoint yml file
         has the correct path to the data file
    """
    ge_checkpoint_fail = GreatExpectationsOperator(
        task_id="ge_checkpoint_fail",
        run_name="ge_airflow_run",
        checkpoint_name="taxi.fail.chk",
    )

    chain(
        ge_batch_kwargs_list_pass,
        ge_checkpoint_pass_root_dir,
        ge_batch_kwargs_pass,
        ge_checkpoint_fail_but_continue,
        ge_checkpoint_pass,
        ge_checkpoint_fail,
    )

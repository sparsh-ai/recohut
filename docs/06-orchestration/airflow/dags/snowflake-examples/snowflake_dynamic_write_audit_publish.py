import json

from pathlib import Path

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.empty import EmptyOperator
from airflow.providers.common.sql.operators import SQLColumnCheckOperator, SQLTableCheckOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from airflow.utils.dates import datetime
from airflow.utils.task_group import TaskGroup

from include.forestfire_checks.checks import TABLE_CHECKS, COL_CHECKS
from include.libs.schema_reg.base_schema_transforms import snowflake_load_column_string


SNOWFLAKE_FORESTFIRE_TABLE = "forestfires"
SNOWFLAKE_AUDIT_TABLE = f"{SNOWFLAKE_FORESTFIRE_TABLE}_AUDIT"

base_path = Path(__file__).parents[2]
table_schema_path = (
    f"{base_path}/include/sql/snowflake_examples/table_schemas/"
)

with DAG(
    "snowflake_dynamic_write_audit_publish",
    description="Example DAG showcasing loading and data quality checking with Snowflake and dynamic task mapping.",
    start_date=datetime(2021, 1, 1),
    schedule_interval=None,
    template_searchpath="/usr/local/airflow/include/sql/snowflake_examples/",
    default_args={"conn_id": "snowflake_default"},
    catchup=False,
) as dag:
    """
    ### Simple ELT Pipeline with Data Quality Checks Using Snowflake and Dynamic Task Mapping
    """

    """
    #### Snowflake audit table creation
    Creates the tables to store sample data for testing
    """
    create_forestfire_audit_table = SnowflakeOperator(
        task_id="create_forestfire_audit_table",
        sql="create_forestfire_table.sql",
        params={"table_name": SNOWFLAKE_AUDIT_TABLE},
    )

    """
    #### Snowflake table creation
    Create the table to store verified sample data.
    """
    create_forestfire_production_table = SnowflakeOperator(
        task_id="create_forestfire_production_table",
        sql="create_forestfire_table.sql",
        params={"table_name": SNOWFLAKE_FORESTFIRE_TABLE}
    )

    """
    #### Insert data
    Insert data into the Snowflake audit table using an existing SQL query (stored in
    the include/sql/snowflake_examples/ directory).
    """
    load_data = SnowflakeOperator(
        task_id="insert_query",
        sql="load_snowflake_forestfire_data.sql",
        params={"table_name": SNOWFLAKE_AUDIT_TABLE}
    )

    with TaskGroup(group_id="quality_checks") as quality_check_group:
        """
        #### Column-level data quality check
        Run data quality checks on columns of the audit table
        """
        column_checks = SQLColumnCheckOperator.partial(
            task_id="column_checks",
            table=SNOWFLAKE_AUDIT_TABLE,
        ).expand(
            column_mapping=COL_CHECKS
        )

        """
        #### Table-level data quality check
        Run data quality checks on the audit table
        """
        table_checks = SQLTableCheckOperator.partial(
            task_id="table_checks",
            table=SNOWFLAKE_AUDIT_TABLE,
        ).expand(
            checks=TABLE_CHECKS
        )

    with open(
        f"{table_schema_path}/forestfire_schema.json",
        "r",
    ) as f:
        table_schema = json.load(f).get("forestfire")
        table_props = table_schema.get("properties")
        table_dimensions = table_schema.get("dimensions")
        table_metrics = table_schema.get("metrics")

        col_string = snowflake_load_column_string(table_props)

        """
        #### Snowflake audit to production task
        Loads the data from the audit table to the production table
        """
        copy_snowflake_audit_to_production_table = SnowflakeOperator(
            task_id="copy_snowflake_audit_to_production_table",
            sql="copy_forestfire_snowflake_audit.sql",
            params={
                "table_name": SNOWFLAKE_FORESTFIRE_TABLE,
                "audit_table_name": f"{SNOWFLAKE_FORESTFIRE_TABLE}_AUDIT",
                "table_schema": table_props,
                "col_string": col_string,
            },
            trigger_rule="all_success"
        )

    """
    #### Delete audit table
    Clean up the table created for the example.
    """
    delete_audit_table = SnowflakeOperator(
        task_id="delete_audit_table",
        sql="delete_forestfire_table.sql",
        params={"table_name": f"{SNOWFLAKE_FORESTFIRE_TABLE}_AUDIT"},
        trigger_rule="all_success"
    )

    begin = EmptyOperator(task_id="begin")
    end = EmptyOperator(task_id="end")

    chain(
        begin,
        [create_forestfire_production_table, create_forestfire_audit_table],
        load_data,
        quality_check_group,
        copy_snowflake_audit_to_production_table,
        delete_audit_table,
        end
    )

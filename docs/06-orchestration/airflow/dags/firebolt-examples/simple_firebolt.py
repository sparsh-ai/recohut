#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example use of Firebolt operators.
"""
from datetime import datetime

from airflow import DAG
from airflow.models.baseoperator import chain
from airflow.operators.sql import SQLCheckOperator
from airflow.utils.task_group import TaskGroup
from firebolt_provider.operators.firebolt import (
    FireboltOperator, FireboltStartEngineOperator, FireboltStopEngineOperator
)

FIREBOLT_CONN_ID = "firebolt_default"
FIREBOLT_SAMPLE_TABLE = "forest_fire"
FIREBOLT_DATABASE = "firebolt_test"
FIREBOLT_ENGINE = "firebolt_test_general_purpose"

CHECKS = {
    "id": "'column' IS NOT NULL",
    "ffmc": "MAX(ffmc) < 100"
}

with DAG(
    "simple_firebolt",
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    default_args={
        "conn_id": FIREBOLT_CONN_ID,
        "firebolt_conn_id": FIREBOLT_CONN_ID,
        "database": FIREBOLT_DATABASE,
        "engine_name": FIREBOLT_ENGINE
    },
    template_searchpath="/usr/local/airflow/include/sql/firebolt_examples/",
    catchup=False,
) as dag:
    """Example Firebolt Data Quality DAG

    DAG starts the Firebolt engine specificed, creates sample table, loads sample data into table,
    runs quality checks in CHECKS dictionary, then deletes the table and stops the engine.

    Checks work by running a MIN() function over the specific aggregate check, where the aggregate
    check is contained in a CASE statement. The CASE statement checks the result of the condition;
    if true, the CASE statement returns 1, else 0. Then MIN() will return 0 if any row returns a
    false result, and true otherwise.

    Note: the Firebolt operator currently does not support templated SQL queries.
    """

    start_engine = FireboltStartEngineOperator(
        task_id="start_engine"
    )

    create_table = FireboltOperator(
        task_id="create_table",
        sql="create_table.sql",
        params={"table": FIREBOLT_SAMPLE_TABLE},
    )

    load_data = FireboltOperator(
        task_id="load_data",
        sql="load_forestfire_data.sql",
        params={"table": FIREBOLT_SAMPLE_TABLE},
    )

    with TaskGroup(group_id="aggregate_quality_checks") as check_group:
        for name, statement in CHECKS.items():
            check = SQLCheckOperator(
                task_id=f"check_{name}",
                sql="quality_check_template.sql",
                params={"col": name, "check_statement": statement, "table": FIREBOLT_SAMPLE_TABLE},
            )

    drop_table = FireboltOperator(
        task_id="drop_table",
        sql="drop_table.sql",
        params={"table": FIREBOLT_SAMPLE_TABLE},
    )

    stop_engine = FireboltStopEngineOperator(
        task_id="stop_engine"
    )

    chain(
        start_engine,
        create_table,
        load_data,
        check_group,
        drop_table,
        stop_engine,
    )

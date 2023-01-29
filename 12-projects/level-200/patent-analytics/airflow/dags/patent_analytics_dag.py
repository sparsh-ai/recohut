import os

from pathlib import Path
from urllib.parse import urlparse
from datetime import datetime
from airflow import DAG
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.providers.common.sql.operators.sql import (
    SQLColumnCheckOperator,
    SQLTableCheckOperator,
)
from airflow.utils.task_group import TaskGroup

from task_builder.build_emr_task import build_emr_task, upload_file_to_s3
from task_builder.job_flow_overrides import (
    JOB_FLOW_OVERRIDES,
    JOB_FLOW_OVERRIDES_NLP_SPARK,
)

from operators.check_s3_key_exist_operator import CheckS3KeyExistOperator
from operators.download_data_and_put_in_s3_operator import (
    DownloadZipDataAndPutInS3Operator,
)


CUR_DIR = Path(os.path.abspath(os.path.dirname(__file__)))

# Connection Configuration
AWS_CONNECTION_ID = "aws_credentials"
EMR_CONNECTION_ID = "emr_credentials"
REDSHIFT_CONNECTION_ID = "redshift"

# S3 path for storing the pyspark scripts
S3_BUCKET_NAME = "patents-analytics"

# S3 key for spark scripts
SPARK_SCRIPTS_S3_KEY = "spark-scripts"

# pyspark dependencies
LOCAL_DEPENDENCIES_PATH = CUR_DIR / "scripts/dependencies/packages.zip"
DEPENDENCIES_S3_KEY = f"{SPARK_SCRIPTS_S3_KEY}/dependencies/packages.zip"

# pyspark config
LOCAL_CONFIGS_PATH = CUR_DIR / "scripts/configs/etl_config.json"
CONFIGS_S3_KEY = f"{SPARK_SCRIPTS_S3_KEY}/configs/etl_config.json"

# Cleaning scripts
LOCAL_CLEANING_SCRIPTS_PATH = CUR_DIR / "scripts/jobs/Data_Cleaning/"
CLEANING_SCRIPTS_S3_KEY = f"{SPARK_SCRIPTS_S3_KEY}/Data_Cleaning/"

# ETL scripts
LOCAL_ETL_SCRIPTS_PATH = CUR_DIR / "scripts/jobs/ETL/"
ETL_SCRIPTS_S3_KEY = f"{SPARK_SCRIPTS_S3_KEY}/ETL/"

# Keyword Extraction scripts
LOCAL_KEYWORD_EXTRACTION_SCRIPTS_PATH = CUR_DIR / "scripts/jobs/Keyword_Extraction/"
KEYWORD_EXTRACTION_SCRIPTS_S3_KEY = f"{SPARK_SCRIPTS_S3_KEY}/Keyword_Extraction/"

# raw file S3 key
RAW_FILE_S3_KEY = "raw/"

# cleaned file S3 key
CLEANED_FILE_S3_KEY = "cleaned/"


PATENT_DATA_URLS = [
    "https://s3.amazonaws.com/data.patentsview.org/download/patent.tsv.zip",
    "https://s3.amazonaws.com/data.patentsview.org/download/patent_assignee.tsv.zip",
    "https://s3.amazonaws.com/data.patentsview.org/download/assignee.tsv.zip",
    "https://s3.amazonaws.com/data.patentsview.org/download/location.tsv.zip",
    "https://s3.amazonaws.com/data.patentsview.org/download/wipo.tsv.zip",
    "https://s3.amazonaws.com/data.patentsview.org/download/wipo_field.tsv.zip",
    "https://s3.amazonaws.com/data.patentsview.org/download/inventor.tsv.zip",
    "https://s3.amazonaws.com/data.patentsview.org/download/patent_inventor.tsv.zip",
]

LOCAL_DATA_PATH = CUR_DIR / "data"

LOCAL_RAW_DATA = ["countryInfo.txt", "shapes_simplified_low.json"]

# list of raw files required before cleaning job
RAW_FILES = [
    "assignee.tsv",
    "countryInfo.txt",
    "inventor.tsv",
    "location.tsv",
    "patent_assignee.tsv",
    "patent_inventor.tsv",
    "patent.tsv",
    "shapes_simplified_low.json",
    "wipo_field.tsv",
    "wipo.tsv",
]

# list of files generated after cleaning job
CLEANED_FILES = [
    "assignee.parquet",
    "inventor.parquet",
    "location.parquet",
    "patent_assignee.parquet",
    "patent_inventor.parquet",
    "patent.parquet",
    "wipo_field.parquet",
    "wipo.parquet",
]

# list of files generated after keyword extraction job
KEYWORD_FILES = ["patent_keyword_raw.parquet", "patent_keyword.parquet"]

CLEANING_SCRIPTS_BY_ORDER = [
    "cleaning_country_shapes_job.py",
    "cleaning_location_job.py",
    "cleaning_patent_job.py",
    "cleaning_wipo_job.py",
    "cleaning_wipo_field_job.py",
    "cleaning_assignee_job.py",
    "cleaning_inventor_job.py",
    "cleaning_patent_assignee_job.py",
    "cleaning_patent_inventor_job.py",
]

KEYWORD_EXTRACTION_SCRIPTS_BY_ORDER = [
    "yake_keyword_extraction_job.py",
    "rank_keyword_job.py",
]

ETL_SCRIPTS_BY_ORDER = [
    "dates_etl_job.py",
    "details_etl_job.py",
    "wipo_classifications_etl_job.py",
    "intermediary_patent_etl_job.py",
    "locations_etl_job.py",
    "owners_etl_job.py",
    "patents_etl_job.py",
    "patent_keywords_etl_job.py",
]

ANALYTICS_TABLES = [
    "patents",
    "dates",
    "details",
    "wipo_classifications",
    "owners",
    "locations",
    "patent_keywords",
]

DEFAULT_ARGS = {
    "owner": "Karlina",
    "start_date": datetime(2022, 9, 1),
    "depends_on_past": False,
}


with DAG(
    "patent_analytics_dag",
    default_args=DEFAULT_ARGS,
    description="ETL for Patent data",
    schedule_interval=None,
) as dag:

    start_operator = EmptyOperator(task_id="Begin_execution")

    with TaskGroup(
        group_id="upload_local_raw_data_to_S3"
    ) as upload_local_raw_data_to_S3:
        for filename in LOCAL_RAW_DATA:
            PythonOperator(
                task_id=f"upload_{filename}_to_s3",
                python_callable=upload_file_to_s3,
                op_kwargs=dict(
                    filename=f"{LOCAL_DATA_PATH}/{filename}",
                    key=RAW_FILE_S3_KEY,
                    bucket_name=S3_BUCKET_NAME,
                    aws_connection_id=AWS_CONNECTION_ID,
                ),
            )

    with TaskGroup(
        group_id="download_raw_patent_data_to_s3"
    ) as download_raw_patent_data_to_s3:
        for data_url in PATENT_DATA_URLS:
            filename = os.path.basename(urlparse(data_url).path)
            DownloadZipDataAndPutInS3Operator(
                task_id=f"download_raw_{filename}_to_s3",
                aws_connection_id=AWS_CONNECTION_ID,
                s3_bucket_name=S3_BUCKET_NAME,
                s3_key=RAW_FILE_S3_KEY,
                data_url=data_url,
            )

    with TaskGroup(group_id="check_raw_data_exists") as check_raw_data_exist:
        for file in RAW_FILES:
            CheckS3KeyExistOperator(
                task_id=f"check_raw_{file}_exist",
                aws_connection_id=AWS_CONNECTION_ID,
                s3_bucket_name=S3_BUCKET_NAME,
                s3_key=f"{RAW_FILE_S3_KEY}{file}",
            )

    cleaning_emr_job = build_emr_task(
        dag=dag,
        task_group_id="cleaning_emr_task",
        aws_connection_id=AWS_CONNECTION_ID,
        s3_bucket_name=S3_BUCKET_NAME,
        local_dependencies_path=LOCAL_DEPENDENCIES_PATH,
        dependencies_s3_key=DEPENDENCIES_S3_KEY,
        local_configs_path=LOCAL_CONFIGS_PATH,
        configs_s3_key=CONFIGS_S3_KEY,
        scripts_by_order=CLEANING_SCRIPTS_BY_ORDER,
        local_scripts_path=LOCAL_CLEANING_SCRIPTS_PATH,
        scripts_s3_key=CLEANING_SCRIPTS_S3_KEY,
        spark_job_flow_overrides=JOB_FLOW_OVERRIDES,
        emr_connection_id=EMR_CONNECTION_ID,
    )

    with TaskGroup(group_id="check_cleaned_data_exists") as check_cleaned_data_exist:
        for file in CLEANED_FILES:
            CheckS3KeyExistOperator(
                task_id=f"check_cleaned_{file}_exist",
                aws_connection_id=AWS_CONNECTION_ID,
                s3_bucket_name=S3_BUCKET_NAME,
                s3_key=f"{CLEANED_FILE_S3_KEY}{file}",
            )

    keyword_extraction_emr_job = build_emr_task(
        dag=dag,
        task_group_id="keyword_extraction_emr_task",
        aws_connection_id=AWS_CONNECTION_ID,
        s3_bucket_name=S3_BUCKET_NAME,
        local_dependencies_path=LOCAL_DEPENDENCIES_PATH,
        dependencies_s3_key=DEPENDENCIES_S3_KEY,
        local_configs_path=LOCAL_CONFIGS_PATH,
        configs_s3_key=CONFIGS_S3_KEY,
        scripts_by_order=KEYWORD_EXTRACTION_SCRIPTS_BY_ORDER,
        local_scripts_path=LOCAL_KEYWORD_EXTRACTION_SCRIPTS_PATH,
        scripts_s3_key=KEYWORD_EXTRACTION_SCRIPTS_S3_KEY,
        spark_job_flow_overrides=JOB_FLOW_OVERRIDES_NLP_SPARK,
        emr_connection_id=EMR_CONNECTION_ID,
    )

    with TaskGroup(group_id="check_keyword_data_exists") as check_keyword_data_exist:
        for file in KEYWORD_FILES:
            CheckS3KeyExistOperator(
                task_id=f"check_keyword_{file}_exist",
                aws_connection_id=AWS_CONNECTION_ID,
                s3_bucket_name=S3_BUCKET_NAME,
                s3_key=f"{CLEANED_FILE_S3_KEY}{file}",
            )

    etl_emr_job = build_emr_task(
        dag=dag,
        task_group_id="etl_emr_task",
        aws_connection_id=AWS_CONNECTION_ID,
        s3_bucket_name=S3_BUCKET_NAME,
        local_dependencies_path=LOCAL_DEPENDENCIES_PATH,
        dependencies_s3_key=DEPENDENCIES_S3_KEY,
        local_configs_path=LOCAL_CONFIGS_PATH,
        configs_s3_key=CONFIGS_S3_KEY,
        scripts_by_order=ETL_SCRIPTS_BY_ORDER,
        local_scripts_path=LOCAL_ETL_SCRIPTS_PATH,
        scripts_s3_key=ETL_SCRIPTS_S3_KEY,
        spark_job_flow_overrides=JOB_FLOW_OVERRIDES,
        emr_connection_id=EMR_CONNECTION_ID,
    )

    with TaskGroup(group_id="check_tables_count") as check_tables_count_group:
        for table in ANALYTICS_TABLES:
            SQLTableCheckOperator(
                task_id=f"check_{table}_table_count",
                conn_id=REDSHIFT_CONNECTION_ID,
                table=table,
                checks={"row_count_check": {"check_statement": "COUNT(*) >10"}},
            )

    with TaskGroup(
        group_id="check_tables_data_quality"
    ) as check_tables_data_quality_group:
        check_patents_table_quality = SQLColumnCheckOperator(
            task_id="check_patents_table_quality",
            conn_id=REDSHIFT_CONNECTION_ID,
            table="patents",
            column_mapping={
                "id": {
                    "null_check": {"equal_to": 0},
                    "unique_check": {"equal_to": 0},
                },
                "granted_date": {
                    "null_check": {"equal_to": 0},
                    "min": {"greater_than": datetime(1999, 12, 31)},
                },
                "detail_id": {
                    "null_check": {"equal_to": 0},
                    "unique_check": {"equal_to": 0},
                },
                "wipo_classification_id": {
                    "null_check": {"equal_to": 0},
                    "unique_check": {"equal_to": 0},
                },
                "num_claims": {"min": {"geq_to": 1}},
            },
        )

        check_dates_table_quality = SQLColumnCheckOperator(
            task_id="check_dates_table_quality",
            conn_id=REDSHIFT_CONNECTION_ID,
            table="dates",
            column_mapping={
                "date": {
                    "null_check": {"equal_to": 0},
                    "min": {"greater_than": datetime(1999, 12, 31)},
                },
                "year": {
                    "min": {"greater_than": 1999},
                },
            },
        )

        check_details_table_quality = SQLColumnCheckOperator(
            task_id="check_details_table_quality",
            conn_id=REDSHIFT_CONNECTION_ID,
            table="details",
            column_mapping={
                "detail_id": {
                    "null_check": {"equal_to": 0},
                    "unique_check": {"equal_to": 0},
                },
                "title": {
                    "null_check": {"equal_to": 0},
                },
            },
        )

        check_wipo_classifications_table_quality = SQLColumnCheckOperator(
            task_id="check_wipo_classifications_table_quality",
            conn_id=REDSHIFT_CONNECTION_ID,
            table="wipo_classifications",
            column_mapping={
                "wipo_classification_id": {
                    "null_check": {"equal_to": 0},
                    "unique_check": {"equal_to": 0},
                },
                "sector": {
                    "null_check": {"equal_to": 0},
                },
                "field": {
                    "null_check": {"equal_to": 0},
                },
            },
        )

        check_owners_table_quality = SQLColumnCheckOperator(
            task_id="check_owners_table_quality",
            conn_id=REDSHIFT_CONNECTION_ID,
            table="owners",
            column_mapping={
                "owner_id": {
                    "null_check": {"equal_to": 0},
                    "unique_check": {"equal_to": 0},
                },
                "type": {
                    "null_check": {"equal_to": 0},
                    "distinct_check": {"equal_to": 3},
                },
                "name": {
                    "null_check": {"equal_to": 0},
                },
            },
        )

        check_locations_table_quality = SQLColumnCheckOperator(
            task_id="check_locations_table_quality",
            conn_id=REDSHIFT_CONNECTION_ID,
            table="locations",
            column_mapping={
                "location_id": {
                    "null_check": {"equal_to": 0},
                    "unique_check": {"equal_to": 0},
                },
                "country": {
                    "null_check": {"equal_to": 0},
                    "unique_check": {"equal_to": 0},
                },
                "continent": {
                    "null_check": {"equal_to": 0},
                },
            },
        )

        check_patent_keywords_table_quality = SQLColumnCheckOperator(
            task_id="check_patent_keywords_table_quality",
            conn_id=REDSHIFT_CONNECTION_ID,
            table="patent_keywords",
            column_mapping={
                "patent_keyword_id": {
                    "null_check": {"equal_to": 0},
                    "unique_check": {"equal_to": 0},
                },
                "patent_id": {
                    "null_check": {"equal_to": 0},
                },
                "keyword": {
                    "null_check": {"equal_to": 0},
                },
            },
        )

    end_operator = EmptyOperator(task_id="End_execution")

    (
        start_operator
        >> [upload_local_raw_data_to_S3, download_raw_patent_data_to_s3]
        >> check_raw_data_exist
        >> cleaning_emr_job
        >> check_cleaned_data_exist
        >> keyword_extraction_emr_job
        >> check_keyword_data_exist
        >> etl_emr_job
        >> [check_tables_count_group, check_tables_data_quality_group]
        >> end_operator
    )

import hashlib

from airflow import DAG, AirflowException
from airflow.decorators import task
from airflow.models import Variable
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.transfers.local_to_s3 import (
    LocalFilesystemToS3Operator,
)
from airflow.utils.dates import datetime


# The file(s) to upload shouldn't be hardcoded in a production setting, this is just for demo purposes.
CSV_FILE_NAME = "forestfires.csv"
CSV_FILE_PATH = f"include/sample_data/forestfire_data/{CSV_FILE_NAME}"
CSV_CORRUPT_FILE_NAME = "forestfires_corrupt.csv"
CSV_CORRUPT_FILE_PATH = f"include/sample_data/forestfire_data/{CSV_CORRUPT_FILE_NAME}"

with DAG(
    "simple_redshift_1",
    start_date=datetime(2021, 7, 7),
    description="A sample Airflow DAG to load data from csv files to S3, then check that all data was uploaded properly.",
    schedule_interval=None,
    catchup=False,
) as dag:
    """
    ### Simple EL Pipeline with Data Integrity Check 1
    This is a very simple DAG showing a minimal EL data pipeline with a data
    integrity check. A single file is uploaded to S3, then its ETag is verified
    against the MD5 hash of the local file. The two should match, which will
    allow the DAG to flow along the "happy path". To see the "sad path", change
    `CSV_FILE_PATH` to `CSV_CORRUPT_FILE_PATH` in the `validate_etag` task.

    Before running the DAG, set the following in an Airflow or Environment Variable:
    - key: aws_configs
    - value: { "s3_bucket": [bucket_name], "s3_key_prefix": [key_prefix]}
    Fully replacing [bucket_name] and [key_prefix].

    What makes this a simple data quality case is:
    1. Absolute ground truth: the local CSV file is considered perfect and immutable.
    2. Single-step data pipeline: no business logic to complicate things.
    3. Single metric to validate.

    This demo works well in the case of validating data that is read from S3, such
    as other data pipelines that will read from S3, or Athena. It would not be
    helpful for data that is read from Redshift, as there is another load step
    that should be validated separately.
    """

    upload_file = LocalFilesystemToS3Operator(
        task_id="upload_to_s3",
        filename=CSV_FILE_PATH,
        dest_key="{{ var.json.aws_configs.s3_key_prefix }}/" + CSV_FILE_PATH,
        dest_bucket="{{ var.json.aws_configs.s3_bucket }}",
        aws_conn_id="aws_default",
        replace=True,
    )

    @task
    def validate_etag():
        """
        #### Validation task
        Check the destination ETag against the local MD5 hash to ensure the file
        was uploaded without errors.
        """
        s3 = S3Hook()
        aws_configs = Variable.get("aws_configs", deserialize_json=True)
        obj = s3.get_key(
            key=f"{aws_configs.get('s3_key_prefix')}/{CSV_FILE_PATH}",
            bucket_name=aws_configs.get("s3_bucket"),
        )
        obj_etag = obj.e_tag.strip('"')
        # Change `CSV_FILE_PATH` to `CSV_CORRUPT_FILE_PATH` for the "sad path".
        file_hash = hashlib.md5(
            open(CSV_FILE_PATH).read().encode("utf-8")).hexdigest()
        if obj_etag != file_hash:
            raise AirflowException(
                f"Upload Error: Object ETag in S3 did not match hash of local file."
            )

    validate_file = validate_etag()

    begin = DummyOperator(task_id="begin")
    end = DummyOperator(task_id="end")

    begin >> upload_file >> validate_file >> end

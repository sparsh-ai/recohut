from airflow.exceptions import AirflowException
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.models.baseoperator import BaseOperator


class CheckS3KeyExistOperator(BaseOperator):
    def __init__(self, aws_connection_id, s3_bucket_name, s3_key, *args, **kwargs):
        super(CheckS3KeyExistOperator, self).__init__(*args, **kwargs)
        self.aws_connection_id = aws_connection_id
        self.s3_bucket_name = s3_bucket_name
        self.s3_key = s3_key

    def execute(self, context):
        self.log.info(
            f"Running CheckS3KeyExistOperator for {self.s3_bucket_name}/{self.s3_key}"
        )

        s3 = S3Hook(self.aws_connection_id)
        prefix_exist = s3.check_for_prefix(
            bucket_name=self.s3_bucket_name, prefix=self.s3_key, delimiter="/"
        )
        key_exist = s3.check_for_key(self.s3_key, bucket_name=self.s3_bucket_name)
        if not (prefix_exist or key_exist):
            raise AirflowException(
                f"S3 Key {self.s3_bucket_name}/{self.s3_key} not found"
            )

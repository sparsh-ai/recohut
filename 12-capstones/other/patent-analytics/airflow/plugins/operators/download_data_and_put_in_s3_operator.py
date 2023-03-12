import requests
from io import BytesIO
from zipfile import ZipFile
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.models.baseoperator import BaseOperator


class DownloadZipDataAndPutInS3Operator(BaseOperator):
    def __init__(
        self, aws_connection_id, s3_bucket_name, s3_key, data_url, *args, **kwargs
    ):
        super(DownloadZipDataAndPutInS3Operator, self).__init__(*args, **kwargs)
        self.aws_connection_id = aws_connection_id
        self.s3_bucket_name = s3_bucket_name
        self.s3_key = s3_key
        self.data_url = data_url

    def execute(self, context):
        self.log.info(f"DownloadZipDataAndPutInS3Operator for {self.data_url}")
        response = requests.get(self.data_url)
        zipfile = ZipFile(BytesIO(response.content))
        filename = zipfile.namelist()[0]
        s3 = S3Hook(self.aws_connection_id)
        s3.load_file_obj(
            zipfile.open(filename),
            key=f"{self.s3_key}/{filename}",
            bucket_name=self.s3_bucket_name,
            replace=True,
        )

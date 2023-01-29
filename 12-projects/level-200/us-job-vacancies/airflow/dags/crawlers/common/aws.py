import boto3
import uuid
from airflow.contrib.hooks.aws_hook import AwsHook
from io import BytesIO


def get_credentials():
    aws_hook = AwsHook("aws_credentials")
    return aws_hook.get_credentials()


def upload_file_to_s3(file_path, destiny_path, credentials, content_type="image/png", acl="public-read"):
    img_data = open(file_path, "rb")
    s3 = boto3.resource('s3', aws_access_key_id=credentials.access_key, aws_secret_access_key=credentials.secret_key, region_name='us-east-2')
    bucket = s3.Bucket('social-wiki-datalake')
    bucket.put_object(
        Key=destiny_path,
        Body=img_data,
        ContentType=content_type,
        ACL=acl
    )


def create_file_on_s3_from_string(content, destiny_path, credentials, content_type="text/html", acl="public-read"):
    s3 = boto3.resource('s3', aws_access_key_id=credentials.access_key, aws_secret_access_key=credentials.secret_key, region_name='us-east-2')
    bucket = s3.Bucket('social-wiki-datalake')
    bucket.put_object(
        Key=destiny_path,
        Body=BytesIO(content.encode('utf-8')),
        ContentType=content_type,
        ACL=acl
    )


def list_all_files(prefix, credentials, callback_func):
    s3 = boto3.client('s3', aws_access_key_id=credentials.access_key, aws_secret_access_key=credentials.secret_key, region_name='us-east-2')
    paginator = s3.get_paginator('list_objects')
    pages = paginator.paginate(Bucket='social-wiki-datalake', Prefix=prefix)
    for page in pages:
        for obj in page['Contents']:
            callback_func(obj)


def read_text_file(key, credentials, callback_func):
    s3 = boto3.client('s3', aws_access_key_id=credentials.access_key, aws_secret_access_key=credentials.secret_key, region_name='us-east-2')
    tmp_file_path = '/tmp/' + str(uuid.uuid4())
    s3.download_file('social-wiki-datalake', key, tmp_file_path)
    callback_func(
        open(tmp_file_path).read()
    )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Manage AWS Kinesis Firehose Streams."""

from typing import Dict

import boto3

# pylint: disable=too-many-arguments


def create_kinesis_firehose_stream(
    firehose_stream_name: str,
    iam_role_arn: str,
    s3_bucket_name: str,
    stream_s3_destination_prefix: str,
    cw_log_group_name: str,
    iam_role_name: str,
    iam_role_path: str,
    aws_region: str,
    buffer_size_mbs: int = 5,
    buffer_interval_sec: int = 300,
) -> Dict:
    """Create AWS Kinesis Firehose Stream."""
    client = boto3.client("iam", region_name=aws_region)
    response = client.list_roles(PathPrefix=iam_role_path)
    # print(response)
    if iam_role_name in [
        role_dict["RoleName"] for role_dict in response["Roles"]
    ]:
        firehost_client = boto3.client("firehose", region_name=aws_region)
        try:
            kfs_create_response = firehost_client.create_delivery_stream(
                DeliveryStreamName=firehose_stream_name,
                DeliveryStreamType="DirectPut",
                S3DestinationConfiguration={
                    # ARN for existing iam role
                    "RoleARN": iam_role_arn,
                    # ARN for existing s3 bucket
                    "BucketARN": f"arn:aws:s3:::{s3_bucket_name}",
                    "Prefix": stream_s3_destination_prefix,
                    "BufferingHints": {
                        "SizeInMBs": buffer_size_mbs,
                        "IntervalInSeconds": buffer_interval_sec,
                    },
                    "CompressionFormat": "UNCOMPRESSED",
                    "EncryptionConfiguration": {
                        "NoEncryptionConfig": "NoEncryption",
                    },
                    "CloudWatchLoggingOptions": {
                        "Enabled": True,
                        "LogGroupName": cw_log_group_name,
                        "LogStreamName": firehose_stream_name,
                    },
                },
            )
            return kfs_create_response
        except firehost_client.exceptions.InvalidArgumentException:
            print(
                f"Kinesis Firehose cannot assume {iam_role_name}. Check "
                "Role. Did nothing"
            )
            return {}
    return {}


def describe_kinesis_firehose_stream(
    firehose_stream_name: str, aws_region: str
) -> Dict:
    """Describe an AWS Kinesis Firehose Stream."""
    firehost_client = boto3.client("firehose", region_name=aws_region)
    firehose_stream_description = firehost_client.describe_delivery_stream(
        DeliveryStreamName=firehose_stream_name
    )
    return firehose_stream_description


def delete_kinesis_firehose_stream(
    firehose_stream_name: str, aws_region: str
) -> Dict:
    """Delete AWS Kinesis Firehose Stream."""
    firehost_client = boto3.client("firehose", region_name=aws_region)
    stream_deletion_response = firehost_client.delete_delivery_stream(
        DeliveryStreamName=firehose_stream_name,
        # should not be necessary to delete this by force
        AllowForceDelete=False,
    )
    return stream_deletion_response


def check_kinesis_firehose_stream_seletion(
    firehose_stream_name: str, aws_region: str
):
    """Verify Deletion of AWS Kinesis Firehose Stream."""
    firehost_client = boto3.client("firehose", region_name=aws_region)
    delivery_stream_names = firehost_client.list_delivery_streams(
        DeliveryStreamType="DirectPut",
        ExclusiveStartDeliveryStreamName=firehose_stream_name,
    )["DeliveryStreamNames"]
    assert firehose_stream_name not in delivery_stream_names

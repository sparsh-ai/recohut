#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Manage AWS S3 Buckets."""

# pylint: disable=invalid-name,dangerous-default-value

from typing import Dict

import boto3


def create_s3_bucket(
    s3_bucket_name: str, aws_region: str, acl: str = "public-read"
) -> Dict:
    """Create S3 bucket."""
    s3_client = boto3.client("s3", region_name=aws_region)
    bucket_creation_response = s3_client.create_bucket(
        # ACL=acl,
        Bucket=s3_bucket_name,
        CreateBucketConfiguration={"LocationConstraint": aws_region},
    )
    return bucket_creation_response


def delete_bucket_objects(s3_bucket_name: str, region: str) -> None:
    """Delete objects in bucket."""
    s3_resource = boto3.resource("s3", region_name=region)
    s3_bucket = s3_resource.Bucket(s3_bucket_name)
    # Deleting objects
    for s3_object in s3_bucket.objects.all():
        s3_object.delete()
    # Deleting objects versions if S3 versioning enabled
    for s3_object_ver in s3_bucket.object_versions.all():
        s3_object_ver.delete()
    print(f"Bucket {s3_bucket_name} has been cleaned up")


def delete_s3_bucket(s3_bucket_name: str, aws_region: str) -> Dict:
    """Delete S3 bucket."""
    s3_client = boto3.client("s3", region_name=aws_region)
    delete_bucket_objects(s3_bucket_name, aws_region)
    bucket_delete_response = s3_client.delete_bucket(Bucket=s3_bucket_name)
    print(f"Bucket {s3_bucket_name} has been deleted")
    return bucket_delete_response


def check_s3_bucket_deletion(s3_bucket_name: str, aws_region: str):
    """Verify that S3 bucket is deleted."""
    s3_client = boto3.client("s3", region_name=aws_region)
    buckets_list_response = s3_client.list_buckets()
    # print(buckets_list_response["Buckets"])
    if buckets_list_response:
        assert s3_bucket_name not in buckets_list_response["Buckets"]
    else:
        assert not buckets_list_response

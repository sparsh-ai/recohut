#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Extract details about S3 buckets."""


from typing import List

import boto3


def get_existing_csv_files_list(
    s3_bucket_name: str, objects_filter_prefix: str
) -> List[str]:
    """Get list of files in subfolder in S3 bucket."""
    s3_resource = boto3.resource("s3")
    bucket = s3_resource.Bucket(s3_bucket_name)
    files_found_objects_list = list(
        bucket.objects.filter(Prefix=objects_filter_prefix)
    )
    files_found_names_list = [w.key for w in files_found_objects_list]
    return files_found_names_list

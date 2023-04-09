#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Manage AWS CloudWatch Log Groups and Streams."""

# pylint: disable=invalid-name,dangerous-default-value

from typing import Dict

import boto3


def create_cw_logs_group_stream(
    cw_logs_group_name: str, firehose_stream_name: str, aws_region: str
) -> Dict:
    """Create CloudWatch Logging Group."""
    cw_logs_client = boto3.client("logs", region_name=aws_region)
    cw_log_creation_response = cw_logs_client.create_log_group(
        logGroupName=cw_logs_group_name
    )
    cw_stream_creation_response = cw_logs_client.create_log_stream(
        logGroupName=cw_logs_group_name, logStreamName=firehose_stream_name
    )
    return [cw_log_creation_response, cw_stream_creation_response]


def delete_cw_log_group_stream(
    cw_log_group_name: str, firehose_stream_name: str, aws_region: str
) -> Dict:
    """Delete CloudWatch Logging Group and Stream."""
    cw_logs_client = boto3.client("logs", region_name=aws_region)
    cw_log_deletion_response = cw_logs_client.delete_log_group(
        logGroupName=cw_log_group_name
    )
    # cw_stream_deletion_response = cw_logs_client.delete_log_stream(
    #     logGroupName=cw_log_group_name,
    #     logStreamName=firehose_stream_name,
    # )
    # print(cw_log_deletion_response)
    # print(cw_stream_deletion_response)
    return {
        "log_group": cw_log_deletion_response,
        # "log_stream": cw_stream_deletion_response,
    }


def check_cw_log_group_deletion(cw_logs_group_name: str, aws_region: str):
    """Verify Deletion of CloudWatch Logging Group."""
    cw_logs_client = boto3.client("logs", region_name=aws_region)
    # Get CW Log Groups
    cw_log_group_response = cw_logs_client.describe_log_groups(
        logGroupNamePrefix=cw_logs_group_name,
    )
    # Get CW Log Group Names
    cw_log_group_names = [
        cw_log_group_response_name["logGroupName"]
        for cw_log_group_response_name in cw_log_group_response["logGroups"]
    ]
    # Verify that deleted CW Log Group name is not in list of Log Group Names
    assert cw_logs_group_name not in cw_log_group_names


def check_cw_log_stream_deletion(
    cw_logs_group_name: str, firehose_stream_name: str, aws_region: str
):
    """Verify Deletion of CloudWatch Logging Stream."""
    cw_logs_client = boto3.client("logs", region_name=aws_region)
    # Get names of CW Log Streams in CW Log Group
    try:
        cw_log_stream_response = cw_logs_client.describe_log_streams(
            logGroupName=cw_logs_group_name,
        )
        # Get CW Log Stream Names
        cw_log_stream_names = [
            cwlog_stream_response_name["logStreamName"]
            for cwlog_stream_response_name in cw_log_stream_response[
                "logStreams"
            ]
        ]
        msg_check = firehose_stream_name in cw_log_stream_names
        msg = (
            f"Found streams [{', '.join(cw_log_stream_names)}] in CW log "
            f"group {cw_logs_group_name}. Specified stream "
            f"{firehose_stream_name} in Log Group = {msg_check}"
        )
    except cw_logs_client.exceptions.ResourceNotFoundException:
        msg = f"Did not find CloudWatch Log Group {cw_logs_group_name}"
    # If CW Log Group is deleted, then CW Log Streams should not exist
    # and describing streams within the CW Log Group should raise an exception
    assert msg == f"Did not find CloudWatch Log Group {cw_logs_group_name}"

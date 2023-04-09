#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Manage AWS IAM."""

# pylint: disable=invalid-name,dangerous-default-value

import json
from typing import Dict, List

import boto3


def create_iam_role(
    iam_role_path: str,
    iam_role_name: str,
    iam_role_description: str,
    iam_role_trust_policy: Dict,
    aws_region: str,
) -> Dict:
    """Create IAM Role."""
    iam_client = boto3.client("iam", region_name=aws_region)
    iam_role_creation_response = iam_client.create_role(
        Path=iam_role_path,
        RoleName=iam_role_name,
        AssumeRolePolicyDocument=json.dumps(iam_role_trust_policy),
        Description=iam_role_description,
        MaxSessionDuration=3600,
    )
    return iam_role_creation_response


def delete_iam_role(iam_role_name: str, aws_region: str) -> Dict:
    """Delete IAM Role."""
    iam_client = boto3.client("iam", region_name=aws_region)
    role_delete_response = iam_client.delete_role(RoleName=iam_role_name)
    return role_delete_response


def check_iam_role_deletion(iam_role_name: str, aws_region: str):
    """Verify Deletion of IAM Role."""
    iam_client = boto3.client("iam", region_name=aws_region)
    iam_roles_list = iam_client.list_roles()["Roles"]
    role_names_list = [role_dict["RoleName"] for role_dict in iam_roles_list]
    assert iam_role_name not in role_names_list


def create_iam_policy(
    region: str,
    iam_firehose_s3_policy_name: str,
    iam_firehose_s3_policy_document: Dict,
    iam_policy_description: str,
    iam_policy_tags: List[Dict],
) -> Dict:
    """Create an IAM policy."""
    iam_client = boto3.client("iam", region_name=region)
    policy_creation_response = iam_client.create_policy(
        PolicyName=iam_firehose_s3_policy_name,
        PolicyDocument=json.dumps(iam_firehose_s3_policy_document),
        Description=iam_policy_description,
        Tags=iam_policy_tags,
    )
    return policy_creation_response


def get_iam_policies(region: str, attached: bool = True) -> List:
    """Get a list of all attached IAM policies."""
    iam_client = boto3.client("iam", region_name=region)
    iam_policy_list = iam_client.list_policies(OnlyAttached=attached)[
        "Policies"
    ]
    return iam_policy_list


def attach_iam_policy_to_role(
    iam_role_name, region: str, iam_policy_arn: str
) -> Dict:
    """Attach an IAM policy to an IAM role."""
    iam_client = boto3.client("iam", region_name=region)
    policy_attachment_response = iam_client.attach_role_policy(
        RoleName=iam_role_name, PolicyArn=iam_policy_arn
    )
    return policy_attachment_response


def delete_iam_policy(
    iam_policy_arn: str, iam_role_name: str, region: str, delete: bool = True
) -> Dict:
    """Delete IAM Policy."""
    iam_client = boto3.client("iam", region_name=region)
    policy_detachment_response = iam_client.detach_role_policy(
        RoleName=iam_role_name, PolicyArn=iam_policy_arn
    )
    print(f"Detached IAM policy {iam_policy_arn} from role {iam_role_name}")
    if delete:
        policy_deletion_response = iam_client.delete_policy(
            PolicyArn=iam_policy_arn
        )
        print(f"Deleted IAM policy {iam_policy_arn}")
        policy_deletion_response = None
    return [policy_detachment_response, policy_deletion_response]

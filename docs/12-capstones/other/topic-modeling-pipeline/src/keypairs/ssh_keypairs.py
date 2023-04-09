#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Manage SSH Access Keys for AWS EC2 Instances."""

import os
from glob import glob
from typing import Dict, List

import boto3


def create_key_pair(
    keypair_name: str = "ec2-key-pair",
    region: str = "us-west-2",
    key_dir: str = "tmp",
    key_fname: str = "aws_ec2_key",
    tags: str = [{"Key": "Name", "Value": "ec2-key-pair"}],
) -> Dict:
    """Create a key pair."""
    ec2_client = boto3.client("ec2", region_name=region)
    key_pair = ec2_client.create_key_pair(
        KeyName=keypair_name,
        TagSpecifications=[{"ResourceType": "key-pair", "Tags": tags}],
    )

    keys_wanted = ["KeyFingerprint", "KeyMaterial", "KeyName", "KeyPairId"]
    private_key = key_pair["KeyMaterial"]

    # write private key to file with 400 permissions
    fname = f"{key_dir}/{key_fname}.pem"
    with os.fdopen(
        os.open(fname, os.O_WRONLY | os.O_CREAT, 0o400),
        "w+",
    ) as handle:
        handle.write(private_key)
    return {k: key_pair[k] for k in keys_wanted}


def delete_key_pair(
    keypair_name: str = "ec2-key-pair", region: str = "us-west-2"
) -> Dict:
    """Delete a key pair."""
    ec2_client = boto3.client("ec2", region_name=region)
    ssh_key_pair_deletion_response = ec2_client.delete_key_pair(
        KeyName=keypair_name
    )
    local_key_files = glob("/tmp/aws_*.pem")
    if local_key_files:
        for local_key_filepath in local_key_files:
            os.remove(local_key_filepath)
            print(f"Found local key file at {local_key_filepath}. Deleted.")
    else:
        print("Did not find local key files in /tmp. Did nothing.")
    return ssh_key_pair_deletion_response


def check_deletion_key_pair(key_filter: List[Dict], aws_region: str) -> None:
    """Verify Deletion of a key pair by filter."""
    ec2_resource = boto3.resource("ec2", region_name=aws_region)
    key_pairs_list = ec2_resource.key_pairs.filter(**key_filter)
    assert not list(key_pairs_list)

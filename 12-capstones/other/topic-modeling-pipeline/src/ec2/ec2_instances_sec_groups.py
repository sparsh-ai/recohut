#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Manage AWS EC2 Security Groups and Instances."""

# pylint: disable=invalid-name,dangerous-default-value

from typing import Dict, List

import boto3
from botocore.exceptions import ClientError


def list_vpcs(region: str) -> Dict:
    """Describe all VPCs."""
    client = boto3.client("ec2", region_name=region)
    response = client.describe_vpcs()
    resp = response["Vpcs"]
    return resp


def create_security_group(
    sg_group_name: str, sg_desc: str, region: str, tags: List[Dict]
) -> None:
    """Create EC2 Security group."""
    resp = list_vpcs(region)
    vpc_id = resp[0]["VpcId"]
    if resp:
        ec2_resource = boto3.resource("ec2", region_name=region)
        security_group = ec2_resource.create_security_group(
            Description=sg_desc,
            GroupName=sg_group_name,
            VpcId=vpc_id,
            TagSpecifications=[
                {"ResourceType": "security-group", "Tags": tags}
            ],
        )
        security_group.authorize_ingress(
            CidrIp="0.0.0.0/0",
            FromPort=22,
            ToPort=22,
            IpProtocol="tcp",
        )
        print(f"Found VPC: {vpc_id}. Created Security Group {sg_group_name}")
    else:
        print("Did not find VPC. Did not create Security Group.")


def get_security_group_ids(region: str, sg_filter: List[Dict]) -> List:
    """Get EC2 Security group IDs."""
    ec2_resource = boto3.resource("ec2", region_name=region)
    if not sg_filter:
        security_groups = ec2_resource.security_groups.all()
    else:
        security_groups = ec2_resource.security_groups.filter(**sg_filter)
    sg_group_list = []
    for security_group in security_groups:
        sg_group_list.append(security_group.id)
    return sg_group_list


def list_ec2_instances_by_filter(
    region: str, instance_filter: Dict
) -> List[Dict]:
    """List all EC2 instances by filter."""
    ec2_resource = boto3.resource("ec2", region_name=region)
    instances_list_by_tag = ec2_resource.instances.filter(**instance_filter)
    instances_attrs = [
        {
            "id": instance.id,
            "key_name": instance.key_name,
            "instance_type": instance.instance_type,
            "state": instance.state["Name"],
            "ami": instance.image.id,
            "platform": instance.platform,
            "security_groups": instance.security_groups,
            "public_dns_name": instance.public_dns_name,
            "public_ip_address": instance.public_ip_address,
            "private_ip_address": instance.private_ip_address,
        }
        for instance in instances_list_by_tag
    ]
    return instances_attrs


def create_instance(
    image_id: str = "ami-0b0154d3d8011b0cd",
    instance_type: str = "t4g.nano",
    keypair_name: str = "ec2-key-pair",
    region: str = "us-west-2",
    tags_list: List[Dict] = [],
) -> Dict:
    """Create an EC2 instance."""
    ec2_client = boto3.client("ec2", region_name=region)
    instances = ec2_client.run_instances(
        ImageId=image_id,
        MinCount=1,
        MaxCount=1,
        InstanceType=instance_type,
        KeyName=keypair_name,
        BlockDeviceMappings=[
            {
                "DeviceName": "/dev/xvda",
                "Ebs": {
                    "DeleteOnTermination": True,
                    "VolumeSize": 8,
                    "VolumeType": "gp2",
                },
            }
        ],
        TagSpecifications=[{"ResourceType": "instance", "Tags": tags_list}],
    )
    return instances["Instances"][0]


def attach_sg_id_to_ec2_instance(instance_id: str, sg_id: str, region: str):
    """Attach an EC2 Security group to an EC2 instance by ID."""
    ec2_client = boto3.client("ec2", region_name=region)
    instance_state = get_instance_state(ec2_client, instance_id)
    ec2_resource = boto3.resource("ec2", region_name=region)
    if instance_state in ["running", "pending", "stopping", "stopped"]:
        instance = ec2_resource.Instance(instance_id)
        instance.modify_attribute(Groups=[sg_id])
        print(f"Attached Security Group {sg_id} to Instance {instance_id}")
    else:
        print(
            f"EC2 Instance in state {instance_state}. Cannot attach Security "
            "Group. Did nothing"
        )


def attach_sg_to_ec2_instance(
    sg_filter: Dict,
    ec2_instance_filter: Dict,
    sg_idx: int = 0,
    ins_idx: int = 0,
    region: str = "us-west-2",
) -> None:
    """Get EC2 SG and Instance by ID and attach SG to instance."""
    # Filter security groups by tag
    sg_id_list = get_security_group_ids(region, sg_filter)
    # Filter instances group by tag
    filtered_instances_list = list_ec2_instances_by_filter(
        region, ec2_instance_filter
    )
    # print(filtered_instances_list)
    # Slice filtered security groups by index, to get a single matching
    # security group
    first_sg_id = sg_id_list[sg_idx]
    # Slice filtered instances by index, to get a single matching instance_id
    first_filtered_instance_id = filtered_instances_list[ins_idx]["id"]
    # Attach sliced SG to EC2 instance
    attach_sg_id_to_ec2_instance(
        first_filtered_instance_id, first_sg_id, region
    )


def get_instance_state(client, instance_id) -> List:
    """Get the state of an EC2 instance."""
    reservations = client.describe_instances(Filters=[]).get("Reservations")
    instance_info = [
        {ins["InstanceId"]: ins["State"]["Name"]}
        for res in reservations
        for ins in res["Instances"]
        if instance_id == ins["InstanceId"]
    ]
    instance_state = [
        list(ins_state.values())[0] for ins_state in instance_info
    ][0]
    return instance_state


def stop_instance(instance_id: str, region: str):
    """Stop an EC2 instance."""
    ec2_client = boto3.client("ec2", region_name=region)
    instance_state = get_instance_state(ec2_client, instance_id)
    cant_stop_states = ["shutting-down", "terminated", "stopping", "stopped"]
    if instance_state not in cant_stop_states:
        response = ec2_client.stop_instances(InstanceIds=[instance_id])
        print("Stopped instance")
    else:
        print(
            f"Instance is in state {instance_state}. Cannot be stopped. "
            "Did nothing."
        )
        return {}
    return response


def terminate_instance(instance_id: str, region: str):
    """Terminate an EC2 instance."""
    ec2_client = boto3.client("ec2", region_name=region)
    instance_state = get_instance_state(ec2_client, instance_id)
    cant_terminate_states = ["terminated"]
    if instance_state not in cant_terminate_states:
        response = ec2_client.terminate_instances(InstanceIds=[instance_id])
        print("Terminated instance")
    else:
        print(
            f"Instance is in state {instance_state}. Cannot be terminated. "
            "Did nothing."
        )
        return {}
    return response


def check_ec2_instance_termination(
    ec2_instance_filter: Dict, aws_region: str
) -> None:
    """Verify termination of EC2 instance by filter."""
    # Filter instances group by tag
    filtered_instances_list = list_ec2_instances_by_filter(
        aws_region, ec2_instance_filter
    )
    for instance in filtered_instances_list:
        assert instance["state"] in ["shutting-down", "terminated"]


def delete_sg(sg_id: str, region: str) -> None:
    """Delete an EC2 Security group."""
    ec2_resource = boto3.resource("ec2", region_name=region)
    security_group = ec2_resource.SecurityGroup(sg_id)
    try:
        security_group.delete()
    except ClientError as e:
        if "dependent object" in str(e):
            print(
                f"Found object depending on Security Group {sg_id}: {str(e)}."
                " Cannot delete the Security Group. Did nothing."
            )
    print(f"Deleted Security Group {sg_id}")


def check_ec2_security_group_deletion(
    sg_filter_dict: Dict, aws_region: str
) -> None:
    """Verify deletion of EC2 Security Group by filter."""
    sg_id_list = get_security_group_ids(aws_region, sg_filter_dict)
    assert not sg_id_list

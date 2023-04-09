#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Programmatic execution of notebooks."""

# pylint: disable=invalid-name

import argparse
import os
from datetime import datetime
from typing import Dict, List

import papermill as pm

PROJ_ROOT_DIR = os.getcwd()
data_dir = os.path.join(PROJ_ROOT_DIR, "data")
output_notebook_dir = os.path.join(PROJ_ROOT_DIR, "executed_notebooks")

raw_data_path = os.path.join(data_dir, "raw")

one_dict_nb_name = "1_create_aws_resources.ipynb"
two_dict_nb_name = "2_create_sagemaker_resources.ipynb"
three_dict_nb_name = "3_combine_raw_data.ipynb"
four_dict_nb_name = "4_data_processing.ipynb"
five_dict_nb_name = "5_delete_sagemaker_resources.ipynb"
six_dict_nb_name = "6_delete_aws_resources.ipynb"

s3_bucket_name = os.getenv("AWS_S3_BUCKET_NAME")
firehose_stream_name = "twitter_delivery_stream"
sg_group_name = "mysgname"
nb_instance_name = "mydemo"
ansible_host_vars_filepath = "inventories/production/host_vars/ec2host"

one_dict = dict(
    s3_bucket_name=s3_bucket_name,
    iam_role_path="/",
    iam_role_name="kinesis-firehose-role",
    iam_role_description="IAM Role to be assumed by Kinesis Firehose",
    iam_role_trust_policy={
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "",
                "Effect": "Allow",
                "Principal": {"Service": "firehose.amazonaws.com"},
                "Action": "sts:AssumeRole",
            }
        ],
    },
    iam_firehose_s3_policy_name="mypolicy",
    iam_firehose_s3_policy_description=(
        "IAM Policy Granting Firehose Access to S3"
    ),
    iam_firehose_s3_policy_tags=[
        {"Key": "Name", "Value": "firehose_access_s3"}
    ],
    stream_s3_destination_prefix="datasets/twitter/kinesis-demo/",
    firehose_stream_name="twitter_delivery_stream",
    cw_logs_group_name=f"kinesisfirehose_{firehose_stream_name}",
    sg_group_tags=[{"Key": "Name", "Value": "allow-inbound-ssh"}],
    key_fname="aws_ec2_key",
    keypair_name="ec2-key-pair",
    ec2_instance_image_id="ami-0cc00ed857256d2b4",
    ec2_instance_type="t2.micro",
    ec2_instance_tags_list=[{"Key": "Name", "Value": "my-ec2-instance"}],
    ansible_inventory_host_vars_fpath=ansible_host_vars_filepath,
)
two_dict = dict(
    s3_bucket_name="",
    iam_role_name="AmazonSageMaker-ExecutionRole-20211228T122046",
    sg_group_name="mysgname",
    sg_group_desc="My security group",
    sg_group_tags=[{"Key": "Name", "Value": sg_group_name}],
    nb_lifecycle_name="mynbconfig",
    nb_instance_name=nb_instance_name,
    nb_instance_type="ml.t3.xlarge",
    nb_instance_tags=[{"Key": "Name", "Value": nb_instance_name}],
    cw_log_group_name="/aws/sagemaker/NotebookInstances",
)
three_dict = dict(
    path_to_folder="/datasets/twitter/kinesis-demo/",
    sub_folders_list=[
        "csvs",
        "predictions",
        "athena-queries-outputs",
        "models",
    ],
    headers=[
        "id",
        "geo",
        "coordinates",
        "place",
        "contributors",
        "is_quote_status",
        "quote_count",
        "reply_count",
        "retweet_count",
        "favorite_count",
        "favorited",
        "retweeted",
        "created_at",
        "source",
        "in_reply_to_user_id",
        "in_reply_to_screen_name",
        "source_text",
        "place_id",
        "place_url",
        "place_place_type",
        "place_name",
        "place_full_name",
        "place_country_code",
        "place_country",
        "place_bounding_box_type",
        "place_bounding_box_coordinates",
        "place_attributes",
        "coords_type",
        "coords_lon",
        "coords_lat",
        "geo_type",
        "geo_lon",
        "geo_lat",
        "user_name",
        "user_screen_name",
        "user_followers",
        "user_friends",
        "user_listed",
        "user_favourites",
        "user_statuses",
        "user_protected",
        "user_verified",
        "user_contributors_enabled",
        "user_joined",
        "user_location",
        "retweeted_tweet",
        "tweet_text_urls",
        "tweet_text_hashtags",
        "tweet_text_usernames",
        "num_urls_in_tweet_text",
        "num_users_in_tweet_text",
        "num_hashtags_in_tweet_text",
        "text",
    ],
    cols_to_use=[
        "id",
        "contributors",
        "created_at",
        "source",
        "in_reply_to_screen_name",
        "source_text",
        "place_id",
        "place_url",
        "place_place_type",
        "place_country_code",
        "place_country",
        "user_name",
        "user_screen_name",
        "user_followers",
        "user_friends",
        "user_listed",
        "user_favourites",
        "user_statuses",
        "user_protected",
        "user_verified",
        "user_joined",
        "user_location",
        "retweeted_tweet",
        "text",
    ],
    unwanted_partial_strings_list=[
        "crypto",
        "token",
        "koistarter",
        "daostarter",
        "decentralized",
        "services",
        "pancakeswap",
        "eraxnft",
        "browsing",
        "kommunitas",
        "hosting",
        "internet",
        "exipofficial",
        "servers",
        "wallet",
        "liquidity",
        "rewards",
        "floki",
        "10000000000000linkstelegram",
        "dogecoin",
        "czbinance",
        "watch",
        "binance",
        "dogelonmars",
        "cryptocurrency",
        "hbomax",
        "money",
        "danheld",
        "cybersecurity",
        "prostitution",
        "nairobi",
        "musembe",
        "volcano detected",
        "block-2",
        "mo-greene",
        "running scared2012",
        "running scared 2012",
        "massacres",
        "eric ephriam chavez",
        "drugs",
        "tanzanite",
        "vvsorigin",
        "gemstonecarat",
        "bin laden",
        "saddam",
        "webuye",
        "bungoma",
        "perished",
        "popescu",
        "whore",
        "nasty",
        "ethereum",
        "pay someone",
        "gamejoin",
        "nft",
        "breeding",
        "seungkwan",
        "woozi",
        "hoshi",
        "bitcrush",
        "arcade",
        "homeworkpay",
        "homework",
        "photocards",
        "deta",
        "marketing",
        "dreamcast",
        "sega",
        "xbox",
        "wii",
        "ps4",
        "kasama",
        "nung",
        "lahat",
        "jinsoul",
        "brunisoul",
        "loona",
        "taas",
        "nung",
        "essay",
        "scriptures",
        "methusealah",
        "testament",
        "yahweh",
        "god",
        "mullah",
        "allah",
        "clergy",
        "mercy",
        "morality",
        "muslims,",
        "hindus",
        "buddhist",
        "catholics",
        "christians",
        "atheist",
        "nazist",
        "antifa",
        "proud boys",
    ],
)
four_dict = dict(
    path_to_folder="/datasets/twitter/kinesis-demo/",
    num_files_to_use=25,
    nrows=800_000,
    all_cols_to_process=[
        "document",
        "created_at",
        "user_joined",
        "in_reply_to_screen_name",
        "source_text",
        "place_country",
        "user_followers",
        "user_friends",
        "user_listed",
        "user_favourites",
        "user_statuses",
        "user_protected",
        "user_verified",
        "user_location",
        "reviewText",
    ],
    count_vectorizer_filename="count_vec_model",
    save_count_vectorizer=False,
    s3_models_subfolder="models",
    num_topics=4,
    num_top_terms_per_topic=15,
    num_top_docs_to_read=8,
    output_file_name="processed_with_predictions",
)
five_dict = dict(
    s3_bucket_name="",
    iam_role_name="AmazonSageMaker-ExecutionRole-20211228T122046",
    iam_policy_name="AmazonSageMaker-ExecutionPolicy-20211228T122046",
    delete_iam_resources="no",
    sg_group_name="mysgname",
    nb_lifecycle_name="mynbconfig",
    nb_instance_name="mydemo",
    nb_instance_tags=[{"Key": "Name", "Value": nb_instance_name}],
    cw_log_group_name="/aws/sagemaker/NotebookInstances",
)
six_dict = dict(
    s3_bucket_name=s3_bucket_name,
    iam_role_name="kinesis-firehose-role",
    iam_policy_name="mypolicy",
    firehose_stream_name=firehose_stream_name,
    cw_logs_group_name=f"kinesisfirehose_{firehose_stream_name}",
    sg_group_tags=[{"Key": "Name", "Value": "allow-inbound-ssh"}],
    key_fname="aws_ec2_key",
    keypair_name="ec2-key-pair",
    ec2_instance_tags_list=[{"Key": "Name", "Value": "my-ec2-instance"}],
    ansible_inventory_host_vars_fpath=ansible_host_vars_filepath,
)


def papermill_run_notebook(
    nb_dict: Dict, output_notebook_directory: str = "executed_notebooks"
) -> None:
    """Execute notebook with papermill"""
    for notebook, nb_params in nb_dict.items():
        now = datetime.now().strftime("%Y%m%d-%H%M%S")
        output_nb = os.path.basename(notebook).replace(
            ".ipynb", f"-{now}.ipynb"
        )
        print(
            f"\nInput notebook path: {notebook}",
            f"Output notebook path: {output_notebook_directory}/{output_nb} ",
            sep="\n",
        )
        for key, val in nb_params.items():
            print(key, val, sep=": ")
        pm.execute_notebook(
            input_path=notebook,
            output_path=f"{output_notebook_directory}/{output_nb}",
            parameters=nb_params,
        )


def run_notebooks(
    notebooks_list: List, output_notebook_directory: str = "executed_notebooks"
) -> None:
    """Execute notebooks from CLI.
    Parameters
    ----------
    nb_dict : List
        list of notebooks to be executed
    Usage
    -----
    > import os
    > PROJ_ROOT_DIR = os.path.abspath(os.getcwd())
    > one_dict_nb_name = "a.ipynb
    > one_dict = {"a": 1}
    > run_notebook(
          notebook_list=[
              {os.path.join(PROJ_ROOT_DIR, one_dict_nb_name): one_dict}
          ]
      )
    """
    for nb in notebooks_list:
        papermill_run_notebook(
            nb_dict=nb, output_notebook_directory=output_notebook_directory
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--action",
        type=str,
        dest="action",
        default="create",
        help="whether to create or destroy AWS resources",
    )
    args = parser.parse_args()

    if args.action == "create":
        nb_dict_list, nb_name_list = [one_dict, one_dict_nb_name]
    elif args.action == "sagemaker-create":
        nb_dict_list, nb_name_list = [two_dict, two_dict_nb_name]
    elif args.action == "sagemaker-delete":
        nb_dict_list, nb_name_list = [five_dict, five_dict_nb_name]
    elif args.action == "delete":
        nb_dict_list, nb_name_list = [six_dict, six_dict_nb_name]

    notebook_list = [
        {os.path.join(PROJ_ROOT_DIR, nb_name): nb_dict}
        for nb_dict, nb_name in zip(nb_dict_list, nb_name_list)
    ]
    run_notebooks(
        notebooks_list=notebook_list,
        output_notebook_directory=output_notebook_dir,
    )

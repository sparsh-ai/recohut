#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Combine raw tweets data, per hour, into single CSV file."""

# pylint: disable=invalid-name,too-many-locals,too-many-arguments

import os
from datetime import datetime
from io import StringIO
from typing import Dict, List, Union

import boto3
import pandas as pd


def get_objects_in_one_s3_level(
    s3b_name: str, content: Union[Dict, str], region: str
) -> Dict:
    """Get list of all storage objects in single S3 level."""
    s3_client = boto3.client("s3", region_name=region)
    # Get path to hourly sub-folders within each daily folder on S3 bucket
    prefix = content if isinstance(content, str) else content.get("Prefix")
    # Get list of all objects in all hourly sub-folders
    # - each list of is a list of dictionaries, where each dict contains keys:
    #   - Key, LastModified, ETag, Size, StorageClass
    response_new = s3_client.list_objects_v2(
        Bucket=s3b_name, Prefix=prefix, Delimiter="/"
    )
    return response_new


def get_data_metadata(file: str, s3_bucket_name: str, region: str) -> Dict:
    """Extract data and file metadata from raw tweets data."""
    s3_client = boto3.client("s3", region_name=region)
    # Get File body (decoded contents) from file dictionary
    file_body = s3_client.get_object(
        Bucket=s3_bucket_name, Key=file.get("Key")
    )["Body"].read()
    # Get File name from file dictionary
    file_name = os.path.basename(file["Key"])
    return {"file_body": file_body, "file_name": file_name}


def get_attrs_extracted_from_tweet_text(
    row: pd.Series, attr_type: str = "hashtags"
) -> str:
    """Get attrs (hashtags or usernames) extracted from tweet text."""
    # Get extracted attribute (tweet_text_hashtags or tweet_text_usernames)
    # from each tweet (row of a pandas DataFrame)
    # - attributes will be the '|' separated string
    extracted = str(row[f"tweet_text_{attr_type}"])
    # Split the string by the pipe operator ('|') to give a single string of
    # space-separated attributes
    extracted_separated = (
        " " + extracted.replace("|", " ") if str(extracted) != "nan" else ""
    )
    # print(
    #     row.name,
    #     type(extracted_separated),
    #     extracted_separated,
    #     f"extracted_{attr_type}={extracted_separated}",
    # )
    return extracted_separated


def get_datetime_string() -> str:
    """Generate current timestamp as string."""
    return datetime.now().strftime("%Y%m%d%H%M%S")


def get_hourly_data_metadata(
    data_list: List,
    headers: List,
    fpath: str,
    cols_to_use: List[str],
    unwanted_partial_strings_list: List[str],
    combine_hashtags_usernames: bool = False,
    get_metadata_agg: bool = False,
) -> List[pd.DataFrame]:
    """Load raw tweets data and file metadata into DataFrames."""
    year, month, day, hour = fpath.split("/", 3)[-1].split("/", 3)
    dfs = []
    dfs_metadata = []
    # Loop over list of dictionaries, where each dict corresponds to a
    # separate file and contains keys: file_name, file_body (file contents)
    for k, raw_data_contents in enumerate(data_list):
        # Decode file contents and split by \n giving nested list
        # - each sub-list is a single tweet and its metadata
        single_buffer_data_strings = (
            raw_data_contents["file_body"].decode("utf-8").split("\n")
        )
        # Iterate over nested list
        all_buffer_contents = []
        for q, data_string in enumerate(single_buffer_data_strings):
            if data_string:
                # split each sub-list by \t in order to get values for each
                # field
                values = data_string.strip().split("\t")
                # print(
                #     k+1,
                #     q+1,
                #     len(raw_data_contents["file_body"]),
                #     len(values),
                #     len(values) != len(headers),
                #     data_string,
                # )
                # Append tweet metadata to dict
                dfs_metadata.append(
                    {
                        "file": k + 1,
                        "file_name": raw_data_contents["file_name"],
                        "encoded_length": len(raw_data_contents["file_body"]),
                        "values_index": q + 1,
                        "len_values": len(values),
                        "malformed_values": len(values) != len(headers),
                        "file_year": year,
                        "file_month": month,
                        "file_day": day,
                        "file_hour": hour[:-1],
                    }
                )
                # Append tweet data to dict (if data is not malformed with
                # more fields than expected)
                if len(values) == len(headers):
                    all_buffer_contents.append(values)
        # Convert nested list of tweet data into DataFrame and append raw data
        # filename as separate column
        df_row = pd.DataFrame(all_buffer_contents, columns=headers).assign(
            file_name=raw_data_contents["file_name"]
        )
        # Append DataFrame of data to empty list
        dfs.append(df_row)
    # Vertically concatenate list of DFs of data in order to get single DF of
    # tweets retrieved per hour
    df = pd.concat(dfs, ignore_index=True)
    # Remove tweets with sensitive partial text that are clearly unrelated to
    # the specified search terms (this list was built up retrospectively)
    unwanted_partial_strings = "|".join(unwanted_partial_strings_list)
    df = df[~df["text"].str.lower().str.contains(unwanted_partial_strings)]
    # (Optional) Combine hashtags and usernames with tweet text (if not done,
    # then these will be completely excluded from tweet text
    if combine_hashtags_usernames:
        # Combine tweet text with space-separated hashtags and usernames that
        # were extracted from the text of the tweet
        # - eg. tweet text ('tweet text goes here') will be combined with
        #       hashtags string ('hashtag1 hashtag2 hashtag3') and
        #       user names string ('username1 username2 username3')
        for attribute_type in ["hashtags", "usernames"]:
            df[f"{attribute_type}_str"] = df.apply(
                get_attrs_extracted_from_tweet_text,
                axis=1,
                attr_type=attribute_type,
            )
        df["text"] = df["text"] + df["hashtags_str"] + df["usernames_str"]
    # Slice vertically concatenated data to select required columns
    all_cols_to_use = cols_to_use + ["file_name"]
    df = df[all_cols_to_use].dropna()
    # Vertically concatenate list of DFs of metadata in order to get single DF
    # of tweets metadata per hour
    # - metadata will not be filtered so that we have access to statistics
    #   about the raw data that was streamed
    df_metadata = pd.DataFrame.from_records(dfs_metadata)
    # (optional) Aggregate metadata by raw data file name
    if get_metadata_agg:
        df_metadata_agg = (
            df_metadata.groupby(["file_name"], as_index=False)
            .agg(
                {
                    "encoded_length": "min",
                    "values_index": "max",
                    "len_values": "min",
                    "malformed_values": "sum",
                }
            )
            .assign(num_valid_records=len(df))
        )
    else:
        # if no aggregation wanted, return empty DataFrame
        df_metadata_agg = pd.DataFrame()
    return [df, df_metadata, df_metadata_agg]


def create_folder_in_s3_bucket(
    region: str, s3_bucket_name: str, folder_name: str = "csvs"
) -> None:
    """Create folder in S3 bucket, if it does not exist."""
    s3_client = boto3.client("s3", region_name=region)
    # List all objects in S3 bucket that are inside the CSVs/ sub-folder
    folders_response_result = s3_client.list_objects_v2(
        Bucket=s3_bucket_name,
        Prefix=f"datasets/twitter/kinesis-demo/{folder_name}",
        Delimiter="/",
    )
    # Create object (with no body), which will result in an empty folder
    # (if a folder of the same name is not already present in the CSVs/
    # sub-folder)
    if "CommonPrefixes" in folders_response_result:
        print(
            f"Found existing folder {folder_name} in specified S3 bucket. "
            "Did nothing."
        )
    else:
        proc_data_folder_creation_response = s3_client.put_object(
            Bucket=s3_bucket_name,
            Body="",
            Key=f"datasets/twitter/kinesis-demo/{folder_name}/",
        )
        print(f"Created folder {folder_name} in bucket.")


def get_existing_csv_files_list(
    s3_bucket_name: str, region: str, prefix: str
) -> List[str]:
    """Get list of files in subfolder in S3 bucket, by filename prefix."""
    s3_resource = boto3.resource("s3", region_name=region)
    bucket = s3_resource.Bucket(s3_bucket_name)
    # Get list of objects containing user-specified prefix in filename
    files_found_objects_list = list(bucket.objects.filter(Prefix=prefix))
    # For each object, get dictionary of file attributes under .key attribute
    # and store these dictionaries in a list
    files_found_names_list = [w.key for w in files_found_objects_list]
    return files_found_names_list


def save_df_to_csv_on_s3(
    df: pd.DataFrame,
    bucket_name: str,
    filepath: str,
    region: str,
    df_type: str = "metadata",
) -> None:
    """Export DataFrame as CSV to folder in S3 bucket."""
    s3_client = boto3.client("s3", region_name=region)
    # Prepare DataFrame for export to an S3 bucket
    # - https://stackoverflow.com/a/58636316/4057186
    csv_buf = StringIO()
    df.to_csv(csv_buf, header=True, index=False)
    csv_buf.seek(0)
    # Add CSV to bucket under the specified filepath (in this case, under
    # the CSVs/ sub-folder)
    s3_client.put_object(
        Bucket=bucket_name, Body=csv_buf.getvalue(), Key=filepath
    )
    print(f"- Copied {len(df):,} rows of {df_type} to bucket at {filepath}.")


def save_data_and_metadata_to_s3_csv(
    subfolder_path: str,
    existing_csv_files: List[str],
    s3_bucket_name: str,
    headers: List[str],
    content: Dict,
    path_to_csvs_folder: str,
    region: str,
    cols_to_use: List[str],
    unwanted_partial_strings_list: List[str],
    combine_hashtags_usernames: bool = False,
    aggregate_metadata: bool = False,
) -> None:
    """Extract tweets data and metadata and export to csvs/ in S3 bucket."""
    # Concatenate year, month, day and hour specified by subfolder_path
    # - 'datasets/twitter/kinesis-demo/2021/12/30/17/' becomes 'hc2021123017'
    ctime_str = "hc" + subfolder_path.split("/", 3)[-1].rstrip("/").replace(
        "/", ""
    )
    # Get list of hourly CSVs of data and metadata that already exist in
    # csvs/ sub-folder in S3 bucket
    existing_matching_csv_files = [
        f for f in existing_csv_files if ctime_str in f
    ]
    # Get string with current datetime
    ftime_str = "s" + get_datetime_string()
    # For the given subfolder path, if no hourly CSVs of data and metadata
    # exists in S3 bucket under the CSVs/ sub-folder, then extract these as
    # pandas DFs and export each
    # - i.e. if the above list (existing_matching_csv_files) is not empty,
    #   then export data and metadata, else do nothing
    if not existing_matching_csv_files:
        # Get list of dictionaries (with file name and file body) in S3 bucket
        data_list = [
            get_data_metadata(file_name, s3_bucket_name, region)
            for file_name in get_objects_in_one_s3_level(
                s3_bucket_name,
                content,
                region,
            )["Contents"]
        ]
        # Get DFs of tweets data and metadata from file attributes in list of
        # dicts
        df, df_metadata, _ = get_hourly_data_metadata(
            data_list,
            headers,
            content.get("Prefix"),
            cols_to_use,
            unwanted_partial_strings_list,
            combine_hashtags_usernames,
            aggregate_metadata,
        )
        # Change datetime format in DF of data
        for c in ["created_at", "user_joined"]:
            df[c] = pd.to_datetime(df[c])
        # Save DFs of data and metadata as CSVs to S3 bucket under the CSVs/
        # sub-folder, if a CSV does not already exist for that hour
        for df_obj, suffix, file_type in zip(
            [df, df_metadata],
            ["tweets_", "tweets_metadata_"],
            ["data", "metadata"],
        ):
            fpath = (
                f"{path_to_csvs_folder}csvs/{suffix}"
                f"{len(data_list)}_{ctime_str}_{ftime_str}.csv"
            )
            print(f"Did not find {file_type} CSV file in {fpath}. ")
            save_df_to_csv_on_s3(
                df_obj, s3_bucket_name, fpath, region, file_type
            )
    else:
        # Since hourly CSV exists in CSVs/ sub-folder in S3 bucket, do nothing
        fpath = existing_matching_csv_files[0]
        print(f"Found existing matching CSV file in {fpath}. Did nothing.")

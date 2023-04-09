#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Read streamed and locally saved twitter data."""

import pandas as pd

if __name__ == "__main__":
    local_csv_fpath = "CSV_FILE_TWEETS_LOCAL.csv"
    cols_to_show = [
        # "id",
        # "user",
        "screen_name",
        "location",
        "created_at"
        # "geo",
        # "text",
    ]
    dtypes_dict = {
        "id": str,
        "user": str,
        "screen_name": str,
        "location": str,
        "text": str,
        "followers": int,
    }

    # Read data
    df = pd.read_csv(
        local_csv_fpath,
        dtype=dtypes_dict,
        lineterminator="\n",
        parse_dates=["created_at"],
    )
    # Convert datetime col to EST
    df["created_at"] = pd.to_datetime(df["created_at"]).dt.tz_convert(
        "US/Eastern"
    )
    # Show subset of columns
    with pd.option_context("display.max_columns", 100):
        with pd.option_context("display.max_rows", 500):
            with pd.option_context("display.width", 1000):
                print(df[cols_to_show])

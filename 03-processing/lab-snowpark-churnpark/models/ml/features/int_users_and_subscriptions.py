import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col, when, lit
import numpy as np
import pandas as pd

def build_user_df(dbt ,session):
    df_cf = dbt.ref("int_user_encoded")
    df_af = dbt.ref("int_user_subscription_agg")

    df_spdf = (
        df_cf.join(df_af, df_cf["user_id"] ==  df_af["user_id"])
            .drop(df_af["user_id"])
            .with_column("user_id",df_cf["user_id"])
            .drop(df_cf["user_id"])
    )

    # We need to rename the joined column
    # hence we are doing this rouandabouts
    for c in df_spdf.columns:
        if c.upper().endswith('_USER_ID"'):
            df_spdf = df_spdf.with_column_renamed(col(c), "USER_ID")

    return df_spdf

def model(dbt, session):
    dbt.config(
        packages = ["numpy",  "pandas"],
        materialized = "table"
    )

    df_user = build_user_df(dbt ,session)
    
    return df_user
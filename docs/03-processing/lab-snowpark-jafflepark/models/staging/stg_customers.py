import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col

def model(dbt, session):
    dbt.config(materialized = "table")
    df = dbt.ref("raw_customers")
    df_new= df.select(df["id"].alias("customer_id"), df.first_name, df.last_name)
    return df_new
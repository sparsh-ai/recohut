import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col

def model(dbt, session):
    dbt.config(materialized = "table")
    df = dbt.ref("raw_orders")
    df_new = df.select(df["id"].alias("order_id"),df["user_id"].alias("customer_id"), col("order_date"), col("status"))
    return df_new
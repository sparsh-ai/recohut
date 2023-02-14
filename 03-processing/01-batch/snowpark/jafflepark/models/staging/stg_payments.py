import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col

def model(dbt, session):
    dbt.config(materialized = "table")
    df = dbt.ref("raw_payments")
    df_new= df.select(df["id"].alias("payment_id"), col("order_id"), col("payment_method"), col("amount")).with_column("amount", df["amount"] / 100)
    return df_new
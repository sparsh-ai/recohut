import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col

def model(dbt, session):
    dbt.config(materialized = "table")
    
    df_cust = dbt.ref("stg_customers")
    df_ord = dbt.ref("stg_orders")
    df_pay = dbt.ref("stg_payments")

    df_customer_orders = df_ord.group_by(col("customer_id")).agg([f.min(col("order_date")).alias("first_order"), f.max("order_date").alias("most_recent_order"), f.count("order_id").alias("number_of_orders")]) 
    df_customer_payments = df_pay.join(df_ord, df_ord.order_id == df_pay.order_id, join_type="left").select(df_ord.customer_id, df_pay.amount).group_by(df_ord.customer_id).agg([f.sum(df_pay.amount).alias("total_amount")]) 
    df_final = df_cust.join(df_customer_orders, df_customer_orders.customer_id == df_cust.customer_id, join_type="left").drop(df_customer_orders.customer_id).with_column_renamed(df_cust.customer_id, "customer_id").join(df_customer_payments, df_cust.customer_id == df_customer_payments.customer_id, join_type="left").drop(df_customer_payments.customer_id).with_column_renamed(df_cust.customer_id, "customer_id").with_column_renamed(df_customer_payments.total_amount,"customer_lifetime_value") 
    return df_final

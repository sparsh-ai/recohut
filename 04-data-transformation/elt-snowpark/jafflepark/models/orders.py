import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col, iff, lit
from functools import reduce
from decimal import *

payment_methods = ['credit_card', 'coupon', 'bank_transfer', 'gift_card']

def model(dbt, session):
    dbt.config(materialized = "table")

    df_ord = dbt.ref("stg_orders")
    df_pay = dbt.ref("stg_payments")
    
    df_payment_types= df_pay.drop("payment_id").pivot('PAYMENT_METHOD',payment_methods).sum('AMOUNT').na.fill(Decimal(0))
    df_renamed=renameColumns(df_payment_types)

    df_order_payments = df_pay.group_by(col("order_id")).agg([f.sum(col("amount")).alias("total_amount")])
    df_new = df_order_payments.join(df_renamed, df_renamed.order_id == df_order_payments.order_id).drop(df_order_payments.order_id).with_column_renamed(df_renamed.order_id, "order_id")
    df_final = df_ord.join(df_new, df_ord.order_id == df_new.order_id, join_type="left").drop(df_new.order_id).with_column_renamed(df_ord.order_id, "order_id").with_column_renamed(df_new.total_amount, "amount")
    return df_final

def renameColumns(df):
    colscleaned = [col[2:-2] if col.startswith('"') and col.endswith('"') else col for col in df.columns ]
    df_cleaned = reduce(lambda df, 
            idx: df.with_column_renamed(df.columns[idx], colscleaned[idx]), 
            range(len(df.columns)), df)

    colsrenamed = [col+"_AMOUNT" if col.lower() in payment_methods else col for col in df_cleaned.columns ]
    df_renamed = reduce(lambda df_cleaned, 
            idx: df_cleaned.with_column_renamed(df_cleaned.columns[idx], colsrenamed[idx]), 
            range(len(df_cleaned.columns)), df_cleaned)
    return df_renamed


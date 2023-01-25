'''
 We want to build out an aggregated view of the user and thier various subscription. This will get us to know
 - the number of months subscription has been active
  - the amount so far billed
  - the number of subscriptions assosciated with the user.
'''
import snowflake.snowpark.functions as f
from snowflake.snowpark.functions import col, udf
from ftfy import fix_text
import snowflake.snowpark.types as T
import logging
import sys

logger = logging.getLogger("mylog")
def model(dbt, session):
    dbt.config(
        packages = ["ftfy"],
        materialized = "table"
    )
   
    df = dbt.source('ott','subscription_billing_cycles')   
    
    logger.info('Anonymous UDF getting created')
    
    #Create anonymous udf
    fix_chars = udf(lambda x: fix_text(str(x)), return_type=T.StringType(), input_types=[T.StringType()], max_batch_size=2000)

    #drop null subcription types
    df.na.drop(subset=["subscription_type"])
   
    #fix characters that are not Unicode
    df_f = df.withColumn("subscription_type", fix_chars("subscription_type"))
    
    # aggregate to find the duration range of subscription
    df_aggregated = df_f.filter(col("subscription_type") == "ACTIVE").group_by(col("user_id"), col("subscription_id")).agg([
        f.min(f.to_date(col("billing_cycle_start_ts"))).alias("subscripton_start_date")
        ,f.max(f.to_date(col("billing_cycle_expire_ts"))).alias("last_billing_cycle_end_date")
        ,f.sum(col("amount_paid")).alias("total_amount_paid_for_subscription")
    ]) 

    df_calc = df_aggregated \
        .with_column("subscription_months", 
            f.datediff("month" ,col("subscripton_start_date") ,col("last_billing_cycle_end_date"))
        )
    
    # Build aggregation view regardless of subscription
    df_user_level_agg = (
        df_calc
            .group_by(col("user_id"))
            .agg([
                f.sum(col("total_amount_paid_for_subscription")).alias("total_amount_paid")
                ,f.count_distinct("subscription_id").alias("number_of_subscriptions")
                ,f.sum(col("subscription_months")).alias("total_subscribed_month")
            ])
    ) 
   
    return df_user_level_agg

from pyspark.sql import SparkSession, DataFrame, Row
from pyspark.sql import functions as F

from pyspark.sql.types import DoubleType, FloatType, LongType, StructType, StructField, StringType

from pyspark.sql.functions import col, lit
#from datetime import datetime


spark = SparkSession \
        .builder \
        .config("hive.metastore.client.factory.class", "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory") \
        .enableHiveSupport() \
        .getOrCreate()    


#Variables 
DB_NAME = "datalake"
TABLE_NAME_CUSTOMER = "customer_iceberg"
TABLE_NAME_WEBSALES = "web_sales_iceberg"
TABLE_NAME_CADRESS = "customer_address_iceberg"
TABLE_NAME_DATEDIM = "date_dim_iceberg"
TABLE_NAME_HOUSEHOLD = "household_demographics_iceberg"
TABLE_NAME_INCOMEBAND = "income_band_iceberg"
TABLE_NAME_ITEM = "item_iceberg"
TABLE_NAME_PROMOTION = "promotion_iceberg"
TABLE_NAME_TIMEDIM = "time_dim_iceberg"
TABLE_NAME_WEBPAGE = "web_page_iceberg"
TABLE_NAME_WEBRETURNS =  "web_returns_iceberg"
TPC_DS_DATABASE = "tpc-source"


#Create the customer table in Iceberg 
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_CUSTOMER}`(
        c_customer_sk             int,
        c_customer_id             string,
        c_current_cdemo_sk        int,
        c_current_hdemo_sk        int,
        c_current_addr_sk         int,
        c_first_shipto_date_sk    int,
        c_first_sales_date_sk     int,
        c_salutation              string,
        c_first_name              string,
        c_last_name               string,
        c_preferred_cust_flag     string,
        c_birth_day               int,
        c_birth_month             int,
        c_birth_year              int,
        c_birth_country           string,
        c_login                   string,
        c_email_address           string,
        c_last_review_date        string
    )
    USING iceberg
    PARTITIONED BY (c_birth_country)
    OPTIONS ('format-version'='2')
    """)

#Insert data into customer table
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_CUSTOMER}` 
    SELECT *
    FROM `{TPC_DS_DATABASE}`.customer
    """)


#Create the websales table in Iceberg  
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_WEBSALES}`(
        ws_sold_date_sk           int,
        ws_sold_time_sk           int,
        ws_ship_date_sk           int,
        ws_item_sk                int,
        ws_bill_customer_sk       int,
        ws_bill_cdemo_sk          int,
        ws_bill_hdemo_sk          int,
        ws_bill_addr_sk           int,
        ws_ship_customer_sk       int,
        ws_ship_cdemo_sk          int,
        ws_ship_hdemo_sk          int,
        ws_ship_addr_sk           int,
        ws_web_page_sk            int,
        ws_web_site_sk            int,
        ws_ship_mode_sk           int,
        ws_warehouse_sk           int,
        ws_promo_sk               int,
        ws_order_number           int,
        ws_quantity               int,
        ws_wholesale_cost         double,
        ws_list_price             double,
        ws_sales_price            double,
        ws_ext_discount_amt       double,
        ws_ext_sales_price        double,
        ws_ext_wholesale_cost     double,
        ws_ext_list_price         double,
        ws_ext_tax                double,
        ws_coupon_amt             double,
        ws_ext_ship_cost          double,
        ws_net_paid               double,
        ws_net_paid_inc_tax       double,
        ws_net_paid_inc_ship      double,
        ws_net_paid_inc_ship_tax  double,
        ws_net_profit             double
    )
    USING iceberg
    PARTITIONED BY (ws_warehouse_sk)
    OPTIONS ('format-version'='2')
    """)

#Insert data into websales table
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_WEBSALES}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.web_sales
    """)


#Create the customer adresse table customer_address
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_CADRESS}`(
        ca_address_sk          int,
        ca_address_id          string,
        ca_street_number       string,
        ca_street_name         string,
        ca_street_type         string,
        ca_suite_number        string,
        ca_city                string,
        ca_county              string,
        ca_state               string,
        ca_zip                 string,
        ca_country             string,
        ca_gmt_offset          float,
        ca_location_type       string
    )
    USING iceberg
    PARTITIONED BY (ca_country, ca_city)
    OPTIONS ('format-version'='2')
    """)

#Insert data into customer address table
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_CADRESS}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.customer_address
    """)


#Create the customer adresse table date_dim
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_DATEDIM}`(
        d_date_sk              int,
        d_date_id              string,
        d_date                 date,
        d_month_seq            int,
        d_week_seq             int,
        d_quarter_seq          int,
        d_year                 int,
        d_dow                  int,
        d_moy                  int,
        d_dom                  int,
        d_qoy                  int,
        d_fy_year              int,
        d_fy_quarter_seq       int,
        d_fy_week_seq          int,
        d_day_name             string,
        d_quarter_name         string,
        d_holiday              string,
        d_weekend              string,
        d_following_holiday    string,
        d_first_dom            int,
        d_last_dom             int,
        d_same_day_ly          int,
        d_same_day_lq          int,
        d_current_day          string,
        d_current_week         string,
        d_current_month        string,
        d_current_quarter      string,
        d_current_year         string
    )
    USING iceberg
    PARTITIONED BY (d_year)
    OPTIONS ('format-version'='2')
    """)

#insert date_dim data
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_DATEDIM}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.date_dim
    """)

#Create the table household_demographics
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_HOUSEHOLD}`(
        hd_demo_sk             int,
        hd_income_band_sk      int,
        hd_buy_potential       string,
        hd_dep_count           int,
        hd_vehicle_count       int
    )
    USING iceberg
    PARTITIONED BY (hd_buy_potential)
    OPTIONS ('format-version'='2')
    """)

#insert household_demographic data
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_HOUSEHOLD}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.household_demographics
    """)    


#Create the table income_band
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_INCOMEBAND}`(   
        ib_income_band_sk      int,
        ib_lower_bound         int,
        ib_upper_bound         int
    )
    USING iceberg
    OPTIONS ('format-version'='2')
    """)

#insert household_demographic data
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_INCOMEBAND}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.income_band
    """)    



#Create table item
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_ITEM}`(   
        i_item_sk              int,
        i_item_id              string,
        i_rec_start_date       string,
        i_rec_end_date         string,
        i_item_desc            string,
        i_current_price        double,
        i_wholesale_cost       double,
        i_brand_id             int,
        i_brand                string,
        i_class_id             int,
        i_class                string,
        i_category_id          int,
        i_category             string,
        i_manufact_id          int,
        i_manufact             string,
        i_size                 string,
        i_formulation          string,
        i_color                string,
        i_units                string,
        i_container            string,
        i_manager_id           string,
        i_product_name         string
    )
    USING iceberg
    PARTITIONED BY (i_category)
    OPTIONS ('format-version'='2')
    """)

#insert item data
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_ITEM}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.item
    """)   

#Create the promotion table promotion
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_PROMOTION}`(   
        p_promo_sk             int,
        p_promo_id             string,
        p_start_date_sk        int,
        p_end_date_sk          int,
        p_item_sk              int,
        p_cost                 double,
        p_response_target      int,
        p_promo_name           string,
        p_channel_dmail        string,
        p_channel_email        string,
        p_channel_catalog      string,
        p_channel_tv           string,
        p_channel_radio        string,
        p_channel_press        string,
        p_channel_event        string,
        p_channel_demo         string,
        p_channel_details      string,
        p_purpose              string,
        p_discount_active      string
    )
    USING iceberg
    PARTITIONED BY (p_purpose)
    OPTIONS ('format-version'='2')
    """)

#insert promotion data
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_PROMOTION}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.promotion
    """)   


#Create the promotion table time_dim
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_TIMEDIM}`(   
        t_time_sk              int,
        t_time_id              string,
        t_time                 int,
        t_hour                 int,
        t_minute               int,
        t_second               int,
        t_am_pm                string,
        t_shift                string,
        t_sub_shift            string,
        t_meal_time            string
    )
    USING iceberg
    PARTITIONED BY (t_hour)
    OPTIONS ('format-version'='2')
    """)


#insert time_dim data
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_TIMEDIM}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.time_dim
    """)   


#Create the promotion table web_page
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_WEBPAGE}`(   
        wp_web_page_sk         int,
        wp_web_page_id         string,
        wp_rec_start_date      string,
        wp_rec_end_date        string,
        wp_creation_date_sk    int,
        wp_access_date_sk      int,
        wp_autogen_flag        string,
        wp_customer_sk         int,
        wp_url                 string,
        wp_type                string,
        wp_char_count          int,
        wp_link_count          int,
        wp_image_count         int,
        wp_max_ad_count        int
    )
    USING iceberg
    PARTITIONED BY (wp_rec_start_date )
    OPTIONS ('format-version'='2')
    """)

#insert web_page data
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_WEBPAGE}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.web_page
    """)   


#Create the promotion table web_page
spark.sql(f"""
    CREATE OR REPLACE TABLE  dev.`{DB_NAME}`.`{TABLE_NAME_WEBRETURNS}`( 
        ws_sold_date_sk             int,
        ws_sold_time_sk             int,
        wr_returned_date_sk         int,   
        wr_returned_time_sk         int, 
        wr_item_sk                  int, 
        wr_refunded_customer_sk     int,
        wr_refunded_cdemo_sk        int,   
        wr_refunded_hdemo_sk        int,   
        wr_refunded_addr_sk         int,    
        wr_returning_customer_sk    int,
        wr_returning_cdemo_sk       int,   
        wr_returning_hdemo_sk       int,  
        wr_returning_addr_sk        int,   
        wr_web_page_sk              int,         
        wr_reason_sk                int,           
        wr_order_number             int,
        wr_return_quantity          int,     
        wr_return_amt               double,  
        wr_return_tax               double,     
        wr_return_amt_inc_tax       double,
        wr_fee                      double,         
        wr_return_ship_cost         double,
        wr_refunded_cash            double,   
        wr_reversed_charge          double, 
        wr_account_credit           double,  
        wr_net_loss                 double 
    )
    USING iceberg
    PARTITIONED BY (wr_reason_sk)
    OPTIONS ('format-version'='2')
    """)
       
#insert web_returns data
spark.sql(f"""
    INSERT INTO dev.`{DB_NAME}`.`{TABLE_NAME_WEBRETURNS}`
    SELECT *
    FROM `{TPC_DS_DATABASE}`.web_returns
    """) 

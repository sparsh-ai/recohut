from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from sqlalchemy import create_engine
import psycopg2

spark = SparkSession \
    .builder \
    .config("spark.jars", "/home/athoillah/venv/ML-1/lib/python3.10/site-packages/pyspark/jars/postgresql-42.5.1.jar") \
    .master("local[*]") \
    .appName("Csv_to_Postgresql") \
    .getOrCreate()

application_train = spark.read \
                .format("csv") \
                .option("inferSchema", "true") \
                .option("header", "true") \
                .load('/home/athoillah/Final/Local/Extract_Spark/Data/application_train.csv')

url = 'postgresql+psycopg2://airflow_user:airflow_pass@localhost:5432/airflow_db'
engine = create_engine(url)
conn = psycopg2.connect(database="airflow_db", user='airflow_user', password='airflow_pass', host='localhost', port= '5432')

cursor = conn.cursor()

sql ='''CREATE TABLE IF NOT EXISTS dwh_final.home_credit_default_risk_application_train(
    SK_ID_CURR integer,
    NAME_CONTRACT_TYPE text, 
    CODE_GENDER text ,
    FLAG_OWN_CAR text ,
    FLAG_OWN_REALTY text, 
    CNT_CHILDREN integer ,
    AMT_INCOME_TOTAL bigint, 
    AMT_CREDIT bigint ,
    AMT_ANNUITY bigint ,
    AMT_GOODS_PRICE bigint, 
    NAME_TYPE_SUITE text ,
    NAME_INCOME_TYPE text ,
    NAME_EDUCATION_TYPE text, 
    NAME_FAMILY_STATUS text ,
    NAME_HOUSING_TYPE text ,
    REGION_POPULATION_RELATIVE bigint ,
    DAYS_BIRTH integer ,
    DAYS_EMPLOYED integer, 
    DAYS_REGISTRATION bigint, 
    DAYS_ID_PUBLISH integer ,
    OWN_CAR_AGE bigint ,
    FLAG_MOBIL integer ,
    FLAG_EMP_PHONE integer, 
    FLAG_WORK_PHONE integer ,
    FLAG_CONT_MOBILE integer ,
    FLAG_PHONE integer ,
    FLAG_EMAIL integer ,
    OCCUPATION_TYPE text, 
    CNT_FAM_MEMBERS bigint, 
    REGION_RATING_CLIENT integer, 
    REGION_RATING_CLIENT_W_CITY integer, 
    WEEKDAY_APPR_PROCESS_START text ,
    HOUR_APPR_PROCESS_START integer ,
    REG_REGION_NOT_LIVE_REGION integer, 
    REG_REGION_NOT_WORK_REGION integer ,
    LIVE_REGION_NOT_WORK_REGION integer ,
    REG_CITY_NOT_LIVE_CITY integer ,
    REG_CITY_NOT_WORK_CITY integer ,
    LIVE_CITY_NOT_WORK_CITY integer ,
    ORGANIZATION_TYPE text ,
    EXT_SOURCE_1 bigint ,
    EXT_SOURCE_2 bigint ,
    EXT_SOURCE_3 bigint ,
    APARTMENTS_AVG bigint, 
    BASEMENTAREA_AVG bigint, 
    YEARS_BEGINEXPLUATATION_AVG bigint, 
    YEARS_BUILD_AVG bigint ,
    COMMONAREA_AVG bigint ,
    ELEVATORS_AVG bigint ,
    ENTRANCES_AVG bigint ,
    FLOORSMAX_AVG bigint ,
    FLOORSMIN_AVG bigint ,
    LANDAREA_AVG bigint ,
    LIVINGAPARTMENTS_AVG bigint ,
    LIVINGAREA_AVG bigint ,
    NONLIVINGAPARTMENTS_AVG bigint ,
    NONLIVINGAREA_AVG bigint ,
    APARTMENTS_MODE bigint ,
    BASEMENTAREA_MODE bigint, 
    YEARS_BEGINEXPLUATATION_MODE bigint, 
    YEARS_BUILD_MODE bigint ,
    COMMONAREA_MODE bigint ,
    ELEVATORS_MODE bigint ,
    ENTRANCES_MODE bigint ,
    FLOORSMAX_MODE bigint ,
    FLOORSMIN_MODE bigint ,
    LANDAREA_MODE bigint ,
    LIVINGAPARTMENTS_MODE bigint, 
    LIVINGAREA_MODE bigint ,
    NONLIVINGAPARTMENTS_MODE bigint, 
    NONLIVINGAREA_MODE bigint ,
    APARTMENTS_MEDI bigint ,
    BASEMENTAREA_MEDI bigint, 
    YEARS_BEGINEXPLUATATION_MEDI bigint, 
    YEARS_BUILD_MEDI bigint ,
    COMMONAREA_MEDI bigint ,
    ELEVATORS_MEDI bigint ,
    ENTRANCES_MEDI bigint ,
    FLOORSMAX_MEDI bigint ,
    FLOORSMIN_MEDI bigint ,
    LANDAREA_MEDI bigint ,
    LIVINGAPARTMENTS_MEDI bigint, 
    LIVINGAREA_MEDI bigint ,
    NONLIVINGAPARTMENTS_MEDI bigint ,
    NONLIVINGAREA_MEDI bigint ,
    FONDKAPREMONT_MODE text ,
    HOUSETYPE_MODE text ,
    TOTALAREA_MODE bigint ,
    WALLSMATERIAL_MODE text ,
    EMERGENCYSTATE_MODE text ,
    OBS_30_CNT_SOCIAL_CIRCLE bigint ,
    DEF_30_CNT_SOCIAL_CIRCLE bigint ,
    OBS_60_CNT_SOCIAL_CIRCLE bigint ,
    DEF_60_CNT_SOCIAL_CIRCLE bigint ,
    DAYS_LAST_PHONE_CHANGE bigint ,
    FLAG_DOCUMENT_2 integer ,
    FLAG_DOCUMENT_3 integer ,
    FLAG_DOCUMENT_4 integer ,
    FLAG_DOCUMENT_5 integer ,
    FLAG_DOCUMENT_6 integer ,
    FLAG_DOCUMENT_7 integer ,
    FLAG_DOCUMENT_8 integer ,
    FLAG_DOCUMENT_9 integer ,
    FLAG_DOCUMENT_10 integer ,
    FLAG_DOCUMENT_11 integer ,
    FLAG_DOCUMENT_12 integer ,
    FLAG_DOCUMENT_13 integer ,
    FLAG_DOCUMENT_14 integer ,
    FLAG_DOCUMENT_15 integer ,
    FLAG_DOCUMENT_16 integer ,
    FLAG_DOCUMENT_17 integer ,
    FLAG_DOCUMENT_18 integer ,
    FLAG_DOCUMENT_19 integer ,
    FLAG_DOCUMENT_20 integer ,
    FLAG_DOCUMENT_21 integer ,
    AMT_REQ_CREDIT_BUREAU_HOUR bigint ,
    AMT_REQ_CREDIT_BUREAU_DAY bigint ,
    AMT_REQ_CREDIT_BUREAU_WEEK bigint ,
    AMT_REQ_CREDIT_BUREAU_MON bigint ,
    AMT_REQ_CREDIT_BUREAU_QRT bigint ,
    AMT_REQ_CREDIT_BUREAU_YEAR bigint
)'''

cursor.execute(sql)
print("Table created successfully........")
conn.commit()
conn.close()

application_train.write.format('jdbc').options(
    url='jdbc:postgresql://localhost:5432/airflow_db',
    driver='org.postgresql.Driver',
    dbtable='dwh_final.home_credit_default_risk_application_train',
    user='airflow_user',
    password='airflow_pass').mode('overwrite').save()
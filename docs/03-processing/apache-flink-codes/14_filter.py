from pyflink.table import (
  EnvironmentSettings, TableEnvironment
)
from pyflink.table.expressions import col

t_env = TableEnvironment.create(
  EnvironmentSettings.in_streaming_mode())
t_env.get_config().get_configuration().set_string("parallelism.default", "1")

input_path = "tripsdata/sample_trips.csv"
source_ddl = f"""
  create table sample_trips (
    VendorID INT,
    tpep_pickup_datetime STRING,
    tpep_dropoff_datetime STRING,
    passenger_count INT,
    trip_distance DOUBLE,
    RatecodeID INT,
    store_and_fwd_flag STRING,
    PULocationID INT,
    DOLocationID INT,
    payment_type INT,
    fare_amount DOUBLE,
    extra DOUBLE,
    mta_tax DOUBLE,
    tip_amount DOUBLE,
    tolls_amount DOUBLE,
    improvement_surcharge DOUBLE,
    total_amount DOUBLE,
    congestion_surcharge DOUBLE
  ) with (
    'connector' = 'filesystem',
    'format' = 'csv',
    'path' = '{input_path}',
    'csv.ignore-parse-errors' = 'true'
  )
"""

t_env.execute_sql(source_ddl)
tbl = t_env.from_path("sample_trips")


# print("===============WHERE=================")
r1 = tbl.select(
  tbl.total_amount
).where(col('total_amount') >= 10)
print(r1.to_pandas())

r1_sql = t_env.sql_query("""
  SELECT total_amount FROM sample_trips WHERE total_amount >= 10
""")
print(r2.to_pandas())


print("===============WHERE ON CALCUATION=================")
r2 = tbl.select(
  (tbl.total_amount / tbl.passenger_count).alias("ppp")
).where(col("ppp") >= 10)
print(r2.to_pandas())

r2_sql = t_env.sql_query("""
  SELECT * FROM (
    SELECT total_amount / passenger_count AS ppp
    FROM sample_trips
  ) WHERE ppp >= 10 
""")
print(r2_sql.to_pandas())
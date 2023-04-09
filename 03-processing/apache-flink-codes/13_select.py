from pyflink.table import (
  EnvironmentSettings, TableEnvironment
)

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

# 기본적인 select
print("===========BASIC SELECT============")
r1 = tbl.select(
  tbl.PULocationID.alias("pickup_location_id"),
  tbl.total_amount
)
print(r1.to_pandas())

r1_sql = t_env.sql_query("""
  SELECT 
    PULocationID AS pickup_location_id, 
    total_amount
  FROM sample_trips
""")
print(r1.to_pandas())

# distinct 
print("===========DISTINCT============")
distinct_pu_loc = tbl.select(
  tbl.PULocationID.alias("pickup_location_id")
).distinct()
print(distinct_pu_loc.to_pandas())

distinct_pu_loc_sql = t_env.sql_query("""
  SELECT DISTINCT PULocationID AS pickup_location_id FROM sample_trips
""")
print(distinct_pu_loc_sql.to_pandas())


# 간단한 계산
print("===========CALCULATION============")
ppp = tbl.select(tbl.total_amount / tbl.passenger_count)
print(ppp.to_pandas())

ppp_sql = t_env.sql_query("""
  SELECT total_amount / passenger_count AS price_per_person
  FROM sample_trips
""")
print(ppp_sql.to_pandas())
from pyflink.table import (
  EnvironmentSettings, TableEnvironment
)
from pyflink.table.expressions import col

t_env = TableEnvironment.create(
  EnvironmentSettings.in_streaming_mode())
t_env.get_config().get_configuration().set_string("parallelism.default", "1")

trips_path = "tripsdata/sample_trips.csv"
sample_trips_ddl = f"""
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
    'path' = '{trips_path}',
    'csv.ignore-parse-errors' = 'true'
  )
"""

zone_path = "./tripsdata/taxi+_zone_lookup.csv"
zone_ddl = f"""
  create table zones (
    LocationID INT,
    Borough STRING,
    Zone STRING,
    service_zone STRING
  ) with (
    'connector' = 'filesystem',
    'format' = 'csv',
    'path' = '{zone_path}',
    'csv.ignore-parse-errors' = 'true'
  )
"""

t_env.execute_sql(sample_trips_ddl)
t_env.execute_sql(zone_ddl)
trips = t_env.from_path("sample_trips")
zones = t_env.from_path("zones")

# join 
r1 = trips.join(zones, trips.PULocationID == zones.LocationID)\
          .select(zones.Zone, trips.total_amount)
print(r1.to_pandas())


r1_sql = t_env.sql_query("""
  SELECT zones.Zone, sample_trips.total_amount
  FROM sample_trips JOIN zones ON sample_trips.PULocationID = zones.LocationID
""")
print(r1_sql.to_pandas())


# left outer join
r2 = trips.left_outer_join(zones, trips.PULocationID == zones.LocationID)\
          .select(zones.Zone, trips.total_amount)
print(r2.to_pandas())


r2_sql = t_env.sql_query("""
  SELECT zones.Zone, sample_trips.total_amount
  FROM sample_trips LEFT OUTER JOIN zones ON sample_trips.PULocationID = zones.LocationID
""")
print(r2_sql.to_pandas())
from pyflink.table import (
  EnvironmentSettings, TableEnvironment
)
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

t_env.execute_sql(sample_trips_ddl)
trips = t_env.from_path("sample_trips")

# group by
r1 = trips.select(trips.PULocationID, trips.total_amount)\
          .group_by(trips.PULocationID)\
          .select(trips.PULocationID, trips.total_amount.sum.alias("total"))
print(r1.to_pandas())


r1_sql = t_env.sql_query("""
  SELECT PULocationID, SUM(total_amount) AS total
  FROM sample_trips GROUP BY PULocationID
""")
print(r1_sql.to_pandas())
import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import (
  StreamTableEnvironment,
  EnvironmentSettings,
  DataTypes
)
from pyflink.table.udf import udf 
from pyflink.common import Row

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)
settings = EnvironmentSettings.new_instance().in_streaming_mode().use_blink_planner().build()
t_env = StreamTableEnvironment.create(env, environment_settings=settings)

kafka_jar_path = os.path.join(
  os.path.abspath(os.path.dirname(__file__)), "../",
  "flink-sql-connector-kafka_2.11-1.14.0.jar"
)
t_env.get_config().get_configuration().set_string(
  "pipeline.jars", f"file://{kafka_jar_path}"
)

source_query = """
  CREATE TABLE trips (
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
    congestion_surcharge DOUBLE,
    pickup_ts AS TO_TIMESTAMP(tpep_pickup_datetime)
  ) WITH (
    'connector' = 'kafka',
    'topic' = 'taxi-trips',
    'properties.bootstrap.servers' = 'localhost:9092',
    'properties.group.id' = 'taxi-group',
    'format' = 'csv',
    'scan.startup.mode' = 'latest-offset'
  )
"""

sink_query = """
  CREATE TABLE sink (
    pickup_ts TIMESTAMP(3),
    trip_distance DOUBLE,
    trip_hour INT,
    expected_price DOUBLE
  ) WITH (
    'connector' = 'print'
  )
"""

t_env.execute_sql(source_query)
t_env.execute_sql(sink_query)

@udf(result_type=DataTypes.ROW([
  DataTypes.FIELD("pickup_ts", DataTypes.TIMESTAMP(3)),
  DataTypes.FIELD("trip_distance", DataTypes.DOUBLE()),
  DataTypes.FIELD("trip_hour", DataTypes.INT()),
  DataTypes.FIELD("expected_price", DataTypes.DOUBLE()),
]))
def calc_price(row):
  import pickle 
  import pandas as pd 
  with open("./model.pkl", "rb") as f:
    lr = pickle.load(f)
    pickup_ts, trip_distance = row
    trip_hour = pickup_ts.hour
    df = pd.DataFrame([[trip_hour, trip_distance]], columns=['trip_hour', "trip_distance"])
    prediction = lr.predict(df)
    return Row(pickup_ts, trip_distance, trip_hour, prediction[0])

trips = t_env.from_path("trips")
trips = trips.select(trips.pickup_ts, trips.trip_distance)
trips = trips.map(calc_price).alias("prickup_ts", "trip_distance", "trip_hour", "expected_price")
trips.execute_insert("sink").wait()
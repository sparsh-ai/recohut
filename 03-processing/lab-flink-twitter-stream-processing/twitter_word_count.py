import os
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings, DataTypes
from pyflink.table.udf import udf 

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
  CREATE TABLE tweets (
    text STRING,
    timestamp_ms BIGINT,
    ts AS TO_TIMESTAMP_LTZ(timestamp_ms, 3),
    WATERMARK FOR ts AS ts - INTERVAL '5' SECOND
  ) WITH (
    'connector' = 'kafka',
    'topic' = 'korean-tweets',
    'properties.bootstrap.servers' = 'localhost:9092',
    'properties.group.id' = 'tweet-group',
    'format' = 'json',
    'scan.startup.mode' = 'latest-offset'
  )
"""

sink_query = """
  CREATE TABLE sink (
    word_count STRING,
    w_start TIMESTAMP(3),
    w_end TIMESTAMP(3)
  ) WITH (
    'connector' = 'print'
  )
"""

t_env.execute_sql(source_query)
t_env.execute_sql(sink_query)

# t_env.from_path("tweets").execute_insert("sink").wait()

windowed = t_env.sql_query("""
  SELECT 
    text,
    HOP_START(ts, INTERVAL '2' SECONDS, INTERVAL '10' SECONDS) AS w_start,
    HOP_END(ts, INTERVAL '2' SECONDS, INTERVAL '10' SECONDS) AS w_end
  FROM tweets
  GROUP BY
    HOP(ts, INTERVAL '2' SECONDS, INTERVAL '10' SECONDS),
    text
""")

@udf(result_type=DataTypes.STRING())
def word_count(data):
  word_list = data.split()
  counter = {}
  for word in word_list:
    if word not in counter:
      counter[word] = 1
    else:
      counter[word] += 1
  return str(counter)

res = windowed.select(word_count(windowed.text).alias("word_count"), windowed.w_start, windowed.w_end)
res.execute_insert("sink").wait()
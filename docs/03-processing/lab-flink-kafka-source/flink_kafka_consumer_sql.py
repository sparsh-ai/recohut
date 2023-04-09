import os 
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, EnvironmentSettings

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

souce_query = f"""
  create table source (
    framework STRING,
    chapter INT
  ) with (
    'connector' = 'kafka',
    'topic' = 'flink-test',
    'properties.bootstrap.servers' = 'localhost:9092',
    'properties.group.id' = 'test-group',
    'format' = 'csv',
    'scan.startup.mode' = 'earliest-offset'
  )
"""

t_env.execute_sql(souce_query)

sink_query = """
  CREATE TABLE blackhole (
    framework STRING,
    chapter INT
  ) WITH (
    'connector' = 'blackhole'
  )
"""

t_env.execute_sql(sink_query)
t_env.from_path("source").insert_into("blackhole")
t_env.execute("flink_kafka_consumer_sql")
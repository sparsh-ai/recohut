import os
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer
from pyflink.datastream.execution_mode import RuntimeExecutionMode 
from pyflink.table import StreamTableEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
env.set_runtime_mode(execution_mode=RuntimeExecutionMode.STREAMING)
env.enable_checkpointing(1000)
env.get_checkpoint_config().set_max_concurrent_checkpoints(1)
t_env = StreamTableEnvironment.create(env)

kafka_jar_path = os.path.join(
  os.path.abspath(os.path.dirname(__file__)), "../",
  "flink-sql-connector-kafka_2.11-1.14.0.jar"
)
t_env.get_config().get_configuration().set_string(
  "pipeline.jars", f"file://{kafka_jar_path}"
)


schema = SimpleStringSchema()
kafka_consumer = FlinkKafkaConsumer(
  topics="flink-test",
  deserialization_schema=schema,
  properties={
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'test_group'
  })

ds = env.add_source(kafka_consumer)
t_env.execute_sql("""
  CREATE TABLE blackhole (
    data STRING
  ) WITH (
    'connector' = 'blackhole'
  )
""")

table = t_env.from_data_stream(ds)
table.insert_into("blackhole")
t_env.execute("flink_kafka_consumer")
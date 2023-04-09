import os
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer, FlinkKafkaProducer
from pyflink.datastream.execution_mode import RuntimeExecutionMode 

env = StreamExecutionEnvironment.get_execution_environment()
env.set_runtime_mode(execution_mode=RuntimeExecutionMode.STREAMING)
env.enable_checkpointing(1000)
env.get_checkpoint_config().set_max_concurrent_checkpoints(1)

kafka_jar_path = os.path.join(
  os.path.abspath(os.path.dirname(__file__)), "../",
  "flink-sql-connector-kafka_2.11-1.14.0.jar"
)
env.add_jars(f"file://{kafka_jar_path}")

in_schema = SimpleStringSchema()
kafka_consumer = FlinkKafkaConsumer(
  topics="example-source",
  deserialization_schema=in_schema,
  properties={
    "bootstrap.servers": "localhost:9092",
    "group.id": "test_group"
  })

out_schema = SimpleStringSchema()
kafka_producer = FlinkKafkaProducer(
  topic="example-destination",
  serialization_schema=out_schema,
  producer_config={
    "bootstrap.servers": "localhost:9092"
  })

ds = env.add_source(kafka_consumer)
ds.add_sink(kafka_producer)

env.execute("kafka_to_kafa")
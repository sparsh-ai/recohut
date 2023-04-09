import json 

from pyflink.table import (
  EnvironmentSettings,
  TableEnvironment,
  DataTypes,
  TableDescriptor,
  Schema
)
from pyflink.table.udf import udf 


t_env = TableEnvironment.create(EnvironmentSettings.in_streaming_mode())

table = t_env.from_elements(
  elements = [
    (1, '{"name": "Spark", "score": 5}'),
    (2, '{"name": "Airflow", "score": 7}'),
    (3, '{"name": "Kafka", "score": 9}'),
    (4, '{"name": "Flink", "score": 8}'),
  ],
  schema = ['id', 'data'])

t_env.create_temporary_table(
  "sink",
  TableDescriptor.for_connector("print")
                 .schema(Schema.new_builder()
                    .column("id", DataTypes.BIGINT())
                    .column("data", DataTypes.STRING())
                    .build())
                 .build())

@udf(result_type=DataTypes.STRING())
def update_score(data):
  json_data = json.loads(data)
  json_data["score"] += 1
  return json.dumps(json_data)

table = table.select(table.id, update_score(table.data))
table.execute_insert("sink").wait()


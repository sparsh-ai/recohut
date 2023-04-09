from pyflink.table import (
  EnvironmentSettings, TableEnvironment
)

t_env = TableEnvironment.create(
  EnvironmentSettings.in_streaming_mode())
t_env.get_config().get_configuration().set_string("parallelism.default", "1")

input_path = "./sample.csv"
source_ddl = f"""
  create table source (
    framework STRING,
    chapter INT
  ) with (
    'connector' = 'filesystem',
    'format' = 'csv',
    'path' = '{input_path}'
  )
"""

t_env.execute_sql(source_ddl)
src = t_env.from_path("source")

print(src.to_pandas())
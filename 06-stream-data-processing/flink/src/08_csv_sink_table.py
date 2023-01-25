from pyflink.table import (
  EnvironmentSettings, TableEnvironment, DataTypes,
  CsvTableSource, CsvTableSink, WriteMode
)

settings = EnvironmentSettings.new_instance()\
  .in_batch_mode().use_blink_planner().build()
t_env = TableEnvironment.create(settings)

in_field_names = ["framework", "chapter"]
in_field_types = [DataTypes.STRING(), DataTypes.BIGINT()]

source = CsvTableSource(
  "./sample.csv",
  in_field_names,
  in_field_types,
  ignore_first_line=False
)

t_env.register_table_source("chapters", source)
table = t_env.from_path("chapters")

print("--- print schema ---")
table.print_schema()

out_field_names = ["framework", "chapter"]
out_field_types = [DataTypes.STRING(), DataTypes.BIGINT()]
sink = CsvTableSink(
  out_field_names,
  out_field_types,
  './sample_copy.csv',
  num_files=1,
  write_mode=WriteMode.OVERWRITE
)
t_env.register_table_sink('out', sink)

table.insert_into('out')
t_env.execute("sample_copy")
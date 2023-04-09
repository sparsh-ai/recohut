from pyflink.table import (
  EnvironmentSettings, TableEnvironment,
  Schema, DataTypes, TableDescriptor
)

t_env = TableEnvironment.create(
  EnvironmentSettings.in_streaming_mode())
t_env.get_config().get_configuration().set_string("parallelism.default", "1")

input_path = "./sample.csv"

t_env.create_temporary_table(
  "source",
  TableDescriptor.for_connector("filesystem")
    .schema(Schema.new_builder()
                  .column("framework", DataTypes.STRING())
                  .column("chapter", DataTypes.INT())
                  .build())
    .option("path", input_path)
    .format("csv")
    .build())

src = t_env.from_path("source")
print(src.to_pandas())
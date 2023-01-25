from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

datastream_env = StreamExecutionEnvironment.get_execution_environment()
table_env = StreamTableEnvironment.create(datastream_env)


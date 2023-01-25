from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment
from pyflink.common.typeinfo import Types 

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

ds = env.from_collection(["c", "python", "php", "java"], Types.STRING())
t = t_env.from_data_stream(ds)

t_env.create_temporary_view("lang", t)
res_table = t_env.sql_query("SELECT * FROM lang WHERE f0 like 'p%'")

res_ds = t_env.to_data_stream(res_table)

res_ds.print()
env.execute()
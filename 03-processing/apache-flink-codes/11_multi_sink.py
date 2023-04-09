from pyflink.table import EnvironmentSettings, TableEnvironment 

env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

col_names = ["id", "lang"]
data = [
  (1, "php"),
  (2, "python"),
  (3, "c++"),
  (4, "java")
]

t1 = t_env.from_elements(data, col_names)
t2 = t_env.from_elements(data, col_names)
t_env.execute_sql("""
  CREATE TABLE print_sink1 (
    id BIGINT,
    lang VARCHAR
  ) WITH (
    'connector' = 'print'
  )
""")
t_env.execute_sql("""
  CREATE TABLE print_sink2 (
    id BIGINT,
    lang VARCHAR
  ) WITH (
    'connector' = 'print'
  )
""")

statement_set = t_env.create_statement_set()
statement_set.add_insert("print_sink1", t1.where(t1.lang.like("p%")))
statement_set.add_insert("print_sink2", t2)

statement_set.execute().wait()
# print(statement_set.explain())
from pyflink.table import EnvironmentSettings, TableEnvironment 

env_settings = EnvironmentSettings.in_streaming_mode()
t_env = TableEnvironment.create(env_settings)

col_names = ["id", "language"]
data = [
  (1, "php"),
  (2, "python"),
  (3, "c++"),
  (4, "java")
]

t1 = t_env.from_elements(data, col_names)
t2 = t_env.from_elements(data, col_names)

table = t1.where(t1.language.like("p%")).union_all(t2)
print(table.explain())
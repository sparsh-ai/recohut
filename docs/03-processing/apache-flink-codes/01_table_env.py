from pyflink.table import EnvironmentSettings, TableEnvironment 

# batch 환경
batch_settings = EnvironmentSettings.new_instance().in_batch_mode()\
                                    .use_blink_planner().build()
batch_table_env = TableEnvironment.create(batch_settings)

# stream 환경
stream_settings = EnvironmentSettings.new_instace().in_streaming_mode()\
                                     .use_blink_planner().build()
stream_table_env = TableEnvironment.create(stream_settings)
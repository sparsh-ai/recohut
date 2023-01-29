from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 pgsql_conn_id="",
                 tables=[],
                 where_parameters=None,
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.pgsql_conn_id = pgsql_conn_id
        self.tables = tables
        self.where_parameters = where_parameters

    def execute(self, context):
        pgsql_hook = PostgresHook(self.pgsql_conn_id)
        where_params = ''
        if self.where_parameters is not None:
            where_params = f"WHERE {self.where_parameters}"
        for table in self.tables:
            records = pgsql_hook.get_records(f"SELECT COUNT(*) FROM {table} {where_params}")
            if len(records) < 1 or len(records[0]) < 1:
                raise ValueError(f"Data quality check failed. {table} returned no results")
            num_records = records[0][0]
            if num_records < 1:
                raise ValueError(f"Data quality check failed. {table} contained 0 rows")
            self.log.info(f"Data quality on table {table} check passed with {records[0][0]} records")
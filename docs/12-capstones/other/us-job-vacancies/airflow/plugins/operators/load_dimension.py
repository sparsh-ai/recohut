from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    truncate_stmt = """
        TRUNCATE TABLE {table}
    """
    insert_into_stmt = """
        INSERT INTO {table} 
        {select_query}
    """

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 pgsql_conn_id,
                 table,
                 select_query,
                 truncate_table=False,
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)

        self.pgsql_conn_id = pgsql_conn_id
        self.table = table
        self.select_query = select_query
        self.truncate_table = truncate_table

    def execute(self, context):
        pgsql = PostgresHook(postgres_conn_id=self.pgsql_conn_id)

        if self.truncate_table:
            self.log.info("Will truncate table before inserting new data...")
            pgsql.run(LoadDimensionOperator.truncate_stmt.format(
                table=self.table
            ))

        self.log.info("Inserting dimension table data...")
        pgsql.run(LoadDimensionOperator.insert_into_stmt.format(
            table=self.table,
            select_query=self.select_query
        ))
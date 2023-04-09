import pulumi
import pulumi_snowflake as snowflake


# Warehouse: https://docs.snowflake.com/en/user-guide/security-access-control-privileges.html#virtual-warehouse-privileges
RO_WAREHOUSE_PRIVILEGES = ['USAGE']
RW_WAREHOUSE_PRIVILEGES = ['USAGE', 'MONITOR']

# Database: https://docs.snowflake.com/en/user-guide/security-access-control-privileges.html#database-privileges
RO_DATABASE_PRIVILEGES = ['USAGE']
RW_DATABASE_PRIVILEGES = ['USAGE', 'MONITOR', 'CREATE SCHEMA']

# Schema: https://docs.snowflake.com/en/user-guide/security-access-control-privileges.html#schema-privileges
RO_SCHEMA_PRIVILEGES = ['USAGE']
RW_SCHEMA_PRIVILEGES = ['MODIFY', 'MONITOR', 'USAGE', 'CREATE TABLE', 'CREATE EXTERNAL TABLE', 'CREATE VIEW', 'CREATE MATERIALIZED VIEW', 'CREATE MASKING POLICY',
                        'CREATE STAGE', 'CREATE FILE FORMAT', 'CREATE SEQUENCE', 'CREATE FUNCTION', 'CREATE PIPE', 'CREATE STREAM', 'CREATE TASK', 'CREATE PROCEDURE']
# 'CREATE ROW ACCESS POLICY' ?

# Table: https://docs.snowflake.com/en/user-guide/security-access-control-privileges.html#table-privileges
RO_TABLE_PRIVILEGES = ['SELECT']
RW_TABLE_PRIVILEGES = ['SELECT', 'INSERT',
                       'UPDATE', 'TRUNCATE', 'DELETE', 'REFERENCES']

# View: https://docs.snowflake.com/en/user-guide/security-access-control-privileges.html#view-privileges
RO_VIEW_PRIVILEGES = ['SELECT']
RW_VIEW_PRIVILEGES = ['SELECT']

# Function: https://docs.snowflake.com/en/user-guide/security-access-control-privileges.html#user-defined-function-udf-and-external-function-privileges
RO_FUNCTION_PRIVILEGES = ['USAGE']
RW_FUNCTION_PRIVILEGES = ['USAGE']


class MySnowflakeRoles(pulumi.ComponentResource):
    def __init__(self,
                 name,
                 database: snowflake.Database,
                 warehouse: snowflake.Warehouse,
                 opts=None):
        super().__init__('pkg:index:MySnowflakeRoles', name, None, opts)

        # Roles
        self.read_only = snowflake.Role(
            f'{name}_RO',
            name=pulumi.Output.concat(database.name, '_RO'),
            opts=pulumi.ResourceOptions(
                parent=self,
                depends_on=[
                    database,
                    warehouse,
                ],
            ),
        )

        self.read_write = snowflake.Role(
            f'{name}_RW',
            name=pulumi.Output.concat(database.name, '_RW'),
            opts=pulumi.ResourceOptions(
                parent=self,
                depends_on=[
                    database,
                    warehouse,
                ],
            ),
        )

        snowflake.RoleGrants(
            f'{name}_RW_ROLE',
            role_name=self.read_only.name,
            roles=[self.read_write.name],
            opts=pulumi.ResourceOptions(
                parent=self.read_only,
                depends_on=[self.read_only],
            ),
        )

        # Warehouse
        for (suffix, parent, privileges) in [
            ('RO', self.read_only, RO_WAREHOUSE_PRIVILEGES),
            ('RW', self.read_write, RW_WAREHOUSE_PRIVILEGES),
        ]:
            for privilege in privileges:
                snowflake.WarehouseGrant(
                    f'{name}_{suffix}_WAREHOUSE_{privilege}',
                    privilege=privilege,
                    warehouse_name=warehouse.name,
                    roles=[parent.name],
                    opts=pulumi.ResourceOptions(
                        parent=parent,
                        depends_on=[parent],
                    ),
                )

        # Database
        for (suffix, parent, privileges) in [
            ('RO', self.read_only, RO_DATABASE_PRIVILEGES),
            ('RW', self.read_write, RW_DATABASE_PRIVILEGES),
        ]:
            for privilege in privileges:
                snowflake.DatabaseGrant(
                    f'{name}_{suffix}_DATABASE_{privilege}',
                    privilege=privilege,
                    database_name=database.name,
                    roles=[parent.name],
                    opts=pulumi.ResourceOptions(
                        parent=parent,
                        depends_on=[parent],
                    ),
                )

        # Schema
        for (suffix, parent, privileges) in [
            ('RO', self.read_only, RO_SCHEMA_PRIVILEGES),
            ('RW', self.read_write, RW_SCHEMA_PRIVILEGES),
        ]:
            for privilege in privileges:
                snowflake.SchemaGrant(
                    f'{name}_{suffix}_SCHEMA_{privilege}',
                    privilege=privilege,
                    on_future=True,
                    database_name=database.name,
                    roles=[parent.name],
                    opts=pulumi.ResourceOptions(
                        parent=parent,
                        depends_on=[parent],
                    ),
                )

        # Table
        for (suffix, parent, privileges) in [
            ('RO', self.read_only, RO_TABLE_PRIVILEGES),
            ('RW', self.read_write, RW_TABLE_PRIVILEGES),
        ]:
            for privilege in privileges:
                snowflake.TableGrant(
                    f'{name}_{suffix}_TABLE_{privilege}',
                    privilege=privilege,
                    on_future=True,
                    database_name=database.name,
                    roles=[parent.name],
                    opts=pulumi.ResourceOptions(
                        parent=parent,
                        depends_on=[parent],
                    ),
                )

        # View
        for (suffix, parent, privileges) in [
            ('RO', self.read_only, RO_VIEW_PRIVILEGES),
            ('RW', self.read_write, RW_VIEW_PRIVILEGES),
        ]:
            for privilege in privileges:
                snowflake.ViewGrant(
                    f'{name}_{suffix}_VIEW_{privilege}',
                    privilege=privilege,
                    on_future=True,
                    database_name=database.name,
                    roles=[parent.name],
                    opts=pulumi.ResourceOptions(
                        parent=parent,
                        depends_on=[parent],
                    ),
                )

        # Materialized View
        for (suffix, parent, privileges) in [
            ('RO', self.read_only, RO_VIEW_PRIVILEGES),
            ('RW', self.read_write, RW_VIEW_PRIVILEGES),
        ]:
            for privilege in privileges:
                snowflake.MaterializedViewGrant(
                    f'{name}_{suffix}_MATERIALIZED_VIEW_{privilege}',
                    privilege=privilege,
                    on_future=True,
                    database_name=database.name,
                    roles=[parent.name],
                    opts=pulumi.ResourceOptions(
                        parent=parent,
                        depends_on=[parent],
                    ),
                )

        # TODO: Function
        # TODO: Procedures
        # TODO: Sequences
        # TODO: Stages
        # TODO: File Formats
        # TODO: Streams
        # TODO: Tasks

        self.register_outputs({
            'role_name_ro': self.read_only.name,
            'role_name_rw': self.read_write.name,
        })

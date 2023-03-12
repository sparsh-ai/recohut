import pulumi
import pulumi_aws as aws
import pulumi_snowflake as snowflake

from my_snowflake_roles import MySnowflakeRoles
from my_snowflake_snowpipe import MySnowpipe
from my_lambda import MyLambda


PROJECT_NAME = pulumi.get_project()
STACK_NAME = pulumi.get_stack()
PREFIX = f'{PROJECT_NAME}-{STACK_NAME}'.lower().replace('_', '-')


# Constants
SF_DB_NAME = f'{PROJECT_NAME}_{STACK_NAME}'.upper()
SF_STREAM_SCHEMA_NAME = 'RAW'.upper()
SF_STREAM_LOGS_TABLE_NAME = 'LOGS'.upper()

SF_LOGS_STORAGE_INTEGRATION_NAME = f'{SF_DB_NAME}_LOGS_S3'.upper()
SF_LOGS_STAGE_NAME = f'{SF_DB_NAME}_LOGS_STAGE'.upper()
SF_LOGS_PIPE_NAME = f'{SF_DB_NAME}_LOGS_PIPE'.upper()


# S3 Bucket
s3_logs_bucket = aws.s3.Bucket(
    'logs',
    bucket=PREFIX,
    acl='private',
)

# Snowflake
sf_database = snowflake.Database(
    'Database',
    name=SF_DB_NAME,
)

sf_warehouse = snowflake.Warehouse(
    'Warehouse',
    name=pulumi.Output.concat(sf_database.name, '_WH'),
    warehouse_size='x-small',
    auto_suspend=5,
    auto_resume=True,
)

sf_roles = MySnowflakeRoles(
    SF_DB_NAME,
    database=sf_database,
    warehouse=sf_warehouse,
)

sf_stream_schema = snowflake.Schema(
    'Stream',
    name=SF_STREAM_SCHEMA_NAME,
    database=sf_database,
    opts=pulumi.ResourceOptions(
        parent=sf_database,
        depends_on=[
            sf_roles.read_only,
            sf_roles.read_write,
        ],
    ),
)

sf_stream_logs_snowpipe = MySnowpipe(
    'Logs',
    prefix=PREFIX,
    s3_bucket=s3_logs_bucket,
    s3_data_prefix='stream_data',
    s3_error_prefix='stream_errors',
    database=sf_database,
    schema=sf_stream_schema,
    storage_integration_name=SF_LOGS_STORAGE_INTEGRATION_NAME,
    stage_name=SF_LOGS_STAGE_NAME,
    pipe_name=SF_LOGS_PIPE_NAME,
    table_name=SF_STREAM_LOGS_TABLE_NAME,
    table_columns=[
        snowflake.TableColumnArgs(
            name='SERVICE_ID',
            type='VARCHAR(254)',
            nullable=False,
        ),
        snowflake.TableColumnArgs(
            name='REQUEST_ID',
            type='VARCHAR(36)',
            nullable=True,
        ),
        snowflake.TableColumnArgs(
            name='REQUEST_TIMESTAMP',
            type='TIMESTAMP_NTZ(9)',
            nullable=True,
        ),
        snowflake.TableColumnArgs(
            name='RESPONSE_ID',
            type='VARCHAR(36)',
            nullable=True,
        ),
        snowflake.TableColumnArgs(
            name='RESPONSE_TIMESTAMP',
            type='TIMESTAMP_NTZ(9)',
            nullable=True,
        ),
        snowflake.TableColumnArgs(
            name='CLIENT_ID',
            type='VARCHAR(36)',
            nullable=True,
        ),
        snowflake.TableColumnArgs(
            name='DATA',
            type='VARIANT',
            nullable=False,
        ),
        snowflake.TableColumnArgs(
            name='LOG_ID',
            type='VARCHAR(36)',
            nullable=False,
        ),
        snowflake.TableColumnArgs(
            name='LOG_FILENAME',
            type='VARCHAR(16777216)',
            nullable=False,
        ),
        snowflake.TableColumnArgs(
            name='LOG_FILE_ROW_NUMBER',
            type='NUMBER(20,0)',
            nullable=False,
        ),
        snowflake.TableColumnArgs(
            name='LOG_TIMESTAMP',
            type='TIMESTAMP_NTZ(9)',
            nullable=False,
        ),
    ],
    table_cluster_bies=[
        'TO_DATE(REQUEST_TIMESTAMP)',
        'SERVICE_ID',
    ],
    copy_statement=f"""
        COPY INTO {SF_DB_NAME}.{SF_STREAM_SCHEMA_NAME}.{SF_STREAM_LOGS_TABLE_NAME} (
            SERVICE_ID,
            REQUEST_ID,
            REQUEST_TIMESTAMP,
            RESPONSE_ID,
            RESPONSE_TIMESTAMP,
            CLIENT_ID,
            DATA,
            LOG_ID,
            LOG_FILENAME,
            LOG_FILE_ROW_NUMBER,
            LOG_TIMESTAMP
        )
        FROM (
            SELECT
                NULLIF(SUBSTR(LOWER(TRIM($1:service:id::STRING)), 1, 254), ''),
                NULLIF(SUBSTR(LOWER(TRIM($1:request:id::STRING)), 1, 36), ''),
                TO_TIMESTAMP_NTZ($1:request:timestamp::INT, 3),
                NULLIF(SUBSTR(LOWER(TRIM($1:response:id::STRING)), 1, 36), ''),
                TO_TIMESTAMP_NTZ($1:response:timestamp::INT, 3),
                NULLIF(SUBSTR(LOWER(TRIM($1:context:client_id::STRING)), 1, 36), ''),
                $1,
                LOWER(UUID_STRING('da69e958-fee3-428b-9dc3-e7586429fcfc', CONCAT(metadata$filename, ':', metadata$file_row_number))),
                metadata$filename,
                metadata$file_row_number,
                TO_TIMESTAMP_NTZ(CONVERT_TIMEZONE('UTC', CURRENT_TIMESTAMP()))
            FROM @{SF_DB_NAME}.{SF_STREAM_SCHEMA_NAME}.{SF_LOGS_STAGE_NAME}
        )
    """,
    opts=pulumi.ResourceOptions(
        parent=sf_stream_schema,
        depends_on=[
            sf_roles.read_only,
            sf_roles.read_write,
        ],
    ),
)

# API Gateway
api = aws.apigatewayv2.Api(
    'Api',
    name=PREFIX,
    protocol_type='HTTP',
)

api_stage = aws.apigatewayv2.Stage(
    'Rest',
    name='rest',
    api_id=api.id,
    auto_deploy=True,
    opts=pulumi.ResourceOptions(parent=api),
)

# API: Collect
lambda_api_collect = MyLambda(
    'ApiCollect',
    prefix=PREFIX,
    lambda_name='collect',
    clouwatch_logs_retention_in_days=3,
    apigatewayv2_api=api,
    apigatewayv2_route_key='POST /collect',
    code=pulumi.FileArchive('../api/collect'),
    handler='main.handler',
    environment=aws.lambda_.FunctionEnvironmentArgs(
        variables={
            'fh_stream_name': sf_stream_logs_snowpipe.firehose.name,
        },
    ),
    opts=pulumi.ResourceOptions(parent=api_stage),
)

aws.iam.RolePolicy(
    f'ApiLambdaCollect_Firehose',
    name='FirehoseWriteAccess',
    role=lambda_api_collect.iam_role.id,
    policy=aws.iam.get_policy_document(
        statements=[
            aws.iam.GetPolicyDocumentStatementArgs(
                actions=[
                    'firehose:PutRecord',
                    'firehose:PutRecordBatch',
                ],
                resources=[
                    sf_stream_logs_snowpipe.firehose.arn,
                ],
                effect='Allow',
            ),
        ],
    ).json,
    opts=pulumi.ResourceOptions(parent=lambda_api_collect),
)


# Final
pulumi.export('firehose_arn', sf_stream_logs_snowpipe.firehose.arn)
pulumi.export('firehose_name', sf_stream_logs_snowpipe.firehose.name)

pulumi.export('snowflake_database_name', sf_database.name)
pulumi.export('snowflake_stream_schema_name', sf_stream_schema.name)
pulumi.export('snowflake_stream_table_name',
              sf_stream_logs_snowpipe.table.name)

pulumi.export('api_endpoint', api_stage.invoke_url)

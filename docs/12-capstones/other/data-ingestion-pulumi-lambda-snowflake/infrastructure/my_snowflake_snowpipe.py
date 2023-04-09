from typing import Sequence
import time
import asyncio

import pulumi
import pulumi_aws as aws
import pulumi_snowflake as snowflake


BUILD_DATE = str(int(time.time()))
BUILD_DATE_TAG_NAME = '_build'


# Workaround
async def wait_for_iam_eventual_consistency(args: list) -> str:
    resource = args[0]
    tag_name = args[1]
    tag_value = args[2]
    resource_tags = args[3]

    if not pulumi.runtime.is_dry_run():
        if tag_value == resource_tags.get(tag_name):
            pulumi.log.info(
                'Waiting 90 seconds for IAM eventual consistency for IAM Role')
            await asyncio.sleep(90)
    return resource


class MySnowpipe(pulumi.ComponentResource):
    def __init__(self,
                 name,
                 prefix: str,
                 s3_bucket: aws.s3.Bucket,
                 s3_data_prefix: str,
                 s3_error_prefix: str,
                 database: snowflake.Database,
                 schema: snowflake.Schema,
                 storage_integration_name: str,
                 stage_name: str,
                 pipe_name: str,
                 table_name: str,
                 table_columns: Sequence[snowflake.TableColumnArgs],
                 table_cluster_bies: Sequence[str],
                 copy_statement: str,
                 opts=None):
        super().__init__('pkg:index:MySnowpipe', name, None, opts)

        aws_region_id = aws.get_region().id
        aws_account_id = aws.get_caller_identity().account_id

        # Firehose
        fh_iam_role = aws.iam.Role(
            'FirehoseAssumeRole',
            name=f'{prefix}-{aws_region_id}-fh',
            assume_role_policy=aws.iam.get_policy_document(
                statements=[
                    aws.iam.GetPolicyDocumentStatementArgs(
                        actions=[
                            'sts:AssumeRole',
                        ],
                        principals=[
                            aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                                type='Service',
                                identifiers=['firehose.amazonaws.com'],
                            ),
                        ],
                        effect='Allow',
                    ),
                ],
            ).json,
            opts=pulumi.ResourceOptions(parent=self),
        )
        aws.iam.RolePolicy(
            'GrantS3Access',
            role=fh_iam_role.id,
            policy=aws.iam.get_policy_document(
                statements=[
                    aws.iam.GetPolicyDocumentStatementArgs(
                        actions=[
                            's3:AbortMultipartUpload',
                            's3:GetBucketLocation',
                            's3:GetObject',
                            's3:ListBucket',
                            's3:ListBucketMultipartUploads',
                            's3:PutObject',
                        ],
                        resources=[
                            s3_bucket.arn,
                            pulumi.Output.concat(
                                s3_bucket.arn, '/', s3_data_prefix, '/*'),
                            pulumi.Output.concat(
                                s3_bucket.arn, '/', s3_error_prefix, '/*'),
                        ],
                    ),
                ],
            ).json,
            opts=pulumi.ResourceOptions(parent=fh_iam_role),
        )

        self.firehose = aws.kinesis.FirehoseDeliveryStream(
            prefix.lower(),
            destination='extended_s3',
            extended_s3_configuration=aws.kinesis.FirehoseDeliveryStreamExtendedS3ConfigurationArgs(
                bucket_arn=s3_bucket.arn,
                role_arn=fh_iam_role.arn,
                prefix=f'{s3_data_prefix}/',
                error_output_prefix=f'{s3_error_prefix}/',
                buffer_interval=60,
                compression_format='GZIP',
                buffer_size=10,
            ),
            opts=pulumi.ResourceOptions(parent=self),
        )

        self.table = snowflake.Table(
            'StreamLogs',
            name=table_name,
            database=database.name,
            schema=schema.name,
            columns=table_columns,
            cluster_bies=table_cluster_bies,
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Snowpipe
        s3_stage_url = pulumi.Output.concat(
            's3://', s3_bucket.id, '/', self.firehose.extended_s3_configuration.prefix,
        )

        self.storage_integration = snowflake.StorageIntegration(
            'Logs',
            name=storage_integration_name,
            type='EXTERNAL_STAGE',
            storage_provider='S3',
            storage_allowed_locations=[
                s3_stage_url,
            ],
            storage_aws_role_arn=f'arn:aws:iam::{aws_account_id}:role/{prefix}-{aws_region_id}-snowpipe'.lower(
            ).replace('_', '-'),
            enabled=True,
            opts=pulumi.ResourceOptions(parent=self),
        )

        self.stage = snowflake.Stage(
            'LogsStage',
            name=stage_name,
            url=s3_stage_url,
            storage_integration=self.storage_integration.name,
            file_format='TYPE = JSON NULL_IF = [] COMPRESSION = GZIP',
            database=database.name,
            schema=schema.name,
            opts=pulumi.resource.ResourceOptions(
                parent=self,
                depends_on=[
                    self.storage_integration
                ],
            ),
        )

        sf_iam_role = aws.iam.Role(
            'SnowpipeAssumeRole',
            # We're using a static name due to the circual dep between the Storage Integration and the IAM role
            name=f'{prefix}-{aws_region_id}-snowpipe',
            assume_role_policy=aws.iam.get_policy_document(
                statements=[
                    aws.iam.GetPolicyDocumentStatementArgs(
                        actions=[
                            'sts:AssumeRole',
                        ],
                        principals=[
                            aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                                type='AWS',
                                identifiers=[
                                    self.storage_integration.storage_aws_iam_user_arn,
                                ],
                            ),
                        ],
                        conditions=[
                            aws.iam.GetPolicyDocumentStatementConditionArgs(
                                test='StringEquals',
                                variable='sts:ExternalId',
                                values=[
                                    self.storage_integration.storage_aws_external_id,
                                ],
                            ),
                        ],
                    )
                ]
            ).json,
            # Workaround
            tags={
                BUILD_DATE_TAG_NAME: BUILD_DATE,
            },
            opts=pulumi.resource.ResourceOptions(
                parent=self,
                ignore_changes=['tags'],
            ),
        )
        aws.iam.RolePolicy(
            'SnowpipeS3Access',
            role=sf_iam_role.id,
            policy=aws.iam.get_policy_document(
                statements=[
                    aws.iam.GetPolicyDocumentStatementArgs(
                        actions=[
                            's3:GetObject',
                            's3:GetObjectVersion',
                        ],
                        resources=[
                            pulumi.Output.concat(
                                s3_bucket.arn, '/', s3_data_prefix, '/*'),
                        ],
                    ),
                    aws.iam.GetPolicyDocumentStatementArgs(
                        actions=[
                            's3:ListBucket',
                        ],
                        resources=[
                            s3_bucket.arn,
                        ],
                        conditions=[
                            aws.iam.GetPolicyDocumentStatementConditionArgs(
                                test='StringLike',
                                variable='s3:prefix',
                                values=[
                                    f'{s3_data_prefix}/*',
                                ],
                            ),
                        ],
                    ),
                ],
            ).json,
            opts=pulumi.ResourceOptions(parent=sf_iam_role),
        )

        safe_sf_iam_role = pulumi.Output. \
            all(sf_iam_role, BUILD_DATE_TAG_NAME, BUILD_DATE, sf_iam_role.tags). \
            apply(wait_for_iam_eventual_consistency)

        self.pipe = snowflake.Pipe(
            'Logs',
            name=pipe_name,
            auto_ingest=True,
            database=database.name,
            schema=schema.name,
            copy_statement=copy_statement.strip(),
            opts=pulumi.resource.ResourceOptions(
                parent=self.stage,
                depends_on=[
                    # Workaround
                    safe_sf_iam_role,
                    self.table,
                    self.storage_integration,
                ],
            ),
        )

        # S3 to SnowPipe (SNS) notification
        aws.s3.BucketNotification(
            'Snowpipe',
            bucket=s3_bucket.id,
            queues=[
                aws.s3.BucketNotificationQueueArgs(
                    queue_arn=self.pipe.notification_channel,
                    events=[
                        's3:ObjectCreated:*',
                    ],
                    filter_prefix=f'{s3_data_prefix}/',
                ),
            ],
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Final
        self.register_outputs({
            'firehose_arn': self.firehose.arn,
            'firehose_name': self.firehose.name,
            'table_name': self.table.name,
        })

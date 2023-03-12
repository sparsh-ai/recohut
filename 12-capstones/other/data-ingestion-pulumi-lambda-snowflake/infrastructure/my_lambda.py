from typing import List, Optional

import pulumi
import pulumi_aws as aws


class MyLambda(pulumi.ComponentResource):
    def __init__(self,
                 resource_name: str,
                 prefix: str,
                 lambda_name: str,
                 clouwatch_logs_retention_in_days: int = 0,
                 apigatewayv2_api: Optional[aws.apigatewayv2.Api] = None,
                 apigatewayv2_route_key: Optional[str] = None,
                 runtime: str = 'python3.8',
                 architectures: List[str] = ['arm64'],
                 code: Optional[pulumi.Archive] = None,
                 handler: Optional[str] = None,
                 timeout: int = 15,
                 environment: Optional[aws.lambda_.FunctionEnvironmentArgs] = None,
                 opts=None):
        super().__init__('pkg:index:MyLambda', resource_name, None, opts)

        aws_region_id = aws.get_region().id

        self.iam_role = aws.iam.Role(
            resource_name,
            name=f'{prefix}-{aws_region_id}-lambda',
            assume_role_policy=aws.iam.get_policy_document(
                statements=[
                    aws.iam.GetPolicyDocumentStatementArgs(
                        actions=[
                            'sts:AssumeRole',
                        ],
                        principals=[
                            aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                                type='Service',
                                identifiers=['lambda.amazonaws.com'],
                            ),
                        ],
                        effect='Allow',
                    ),
                ],
            ).json,
            opts=pulumi.ResourceOptions(parent=self),
        )

        # Lambda
        self.lambda_function = aws.lambda_.Function(
            resource_name,
            name=f'{prefix}-{lambda_name}',
            role=self.iam_role.arn,
            code=code,
            handler=handler,
            runtime=runtime,
            architectures=architectures,
            timeout=timeout,
            environment=environment,
            opts=pulumi.ResourceOptions(parent=self),
        )

        # CloudWatch
        if clouwatch_logs_retention_in_days > 0:
            self.cloudwatch_log_group = aws.cloudwatch.LogGroup(
                resource_name,
                name=f'/aws/lambda/{prefix}-{lambda_name}',
                retention_in_days=clouwatch_logs_retention_in_days,
                opts=pulumi.ResourceOptions(parent=self.lambda_function),
            )

            aws.iam.RolePolicy(
                f'{resource_name}_CloudWatchWriteAccess',
                name='CloudWatchWriteAccess',
                role=self.iam_role.id,
                policy=aws.iam.get_policy_document(
                    statements=[
                        aws.iam.GetPolicyDocumentStatementArgs(
                            actions=[
                                'logs:CreateLogGroup',
                                'logs:CreateLogStream',
                                'logs:PutLogEvents',
                            ],
                            resources=[
                                pulumi.Output.concat(
                                    self.cloudwatch_log_group.arn,
                                    ':*:*'),
                            ],
                            effect='Allow',
                        ),
                    ],
                ).json,
                opts=pulumi.ResourceOptions(parent=self.iam_role),
            )

        if apigatewayv2_api != None and apigatewayv2_route_key != None:
            self.apigatewayv2_integration = aws.apigatewayv2.Integration(
                resource_name,
                api_id=apigatewayv2_api.id,
                integration_uri=self.lambda_function.invoke_arn,
                integration_type='AWS_PROXY',
                integration_method=apigatewayv2_route_key.split(' ')[0],
                opts=pulumi.ResourceOptions(parent=self.lambda_function),
            )

            self.apigatewayv2_route = aws.apigatewayv2.Route(
                resource_name,
                api_id=apigatewayv2_api.id,
                route_key=apigatewayv2_route_key,
                target=pulumi.Output.concat(
                    'integrations/', self.apigatewayv2_integration.id),
                opts=pulumi.ResourceOptions(
                    parent=self.apigatewayv2_integration),
            )

            aws.lambda_.Permission(
                resource_name,
                statement_id='AllowExecutionFromAPIGateway',
                action='lambda:InvokeFunction',
                function=self.lambda_function.name,
                principal='apigateway.amazonaws.com',
                source_arn=pulumi.Output.concat(
                    apigatewayv2_api.execution_arn,
                    '/*/*',
                ),
                opts=pulumi.ResourceOptions(parent=self.lambda_function),
            )

#!/usr/bin/env python3

from aws_cdk import core

#from flink_cdk.flink_cdk_stack import FlinkCdkStack
from kda_app.kda_app_stack import KdaAppStack
from main_cdk.main_cdk_stack import MainCdkStack

app = core.App()
#FlinkCdkStack(app, "flink-cdk")
#KdaAppStack(app, "kda-app")
#AppInfraStack(app, "infra-stack") 
MainCdkStack(app, "flink-cdk")

app.synth()

#!/usr/bin/env python3

from aws_cdk import core

from producer_cdk.producer_cdk_stack import ProducerCdkStack


app = core.App()
ProducerCdkStack(app, "producer-cdk", env={'region': 'us-east-1'})

app.synth()

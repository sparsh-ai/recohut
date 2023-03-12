import json
import pytest

from aws_cdk import core
from producer-cdk.producer_cdk_stack import ProducerCdkStack


def get_template():
    app = core.App()
    ProducerCdkStack(app, "producer-cdk")
    return json.dumps(app.synth().get_stack("producer-cdk").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())

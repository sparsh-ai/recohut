# Lab: AWS Account Setup

## Create AWS Account

Watch and follow this video: https://www.youtube.com/watch?v=XhW17g73fvY

## Setup AWS Credentials

Watch and follow this video: https://www.youtube.com/watch?v=SON8sY1iOBU

You can also check out the documentation [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

## Process Flow

![](./process-flow.drawio.svg)

## Step 1

```sh
mkdir ~/.aws
touch ~/.aws/credentials
```

## Step 2

```
[default]
aws_access_key_id=
aws_secret_access_key=
region=us-east-1
output=json
```

## Step 3

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## Step 4

```
aws sts get-caller-identity
```
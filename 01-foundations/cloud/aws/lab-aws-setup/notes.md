## Step 1

mkdir ~/.aws
touch ~/.aws/credentials

## Step 2

[default]
aws_access_key_id=
aws_secret_access_key=
region=us-east-1
output=json

## Step 3

https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## Step 4

aws sts get-caller-identity

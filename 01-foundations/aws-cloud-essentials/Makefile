install:
	pip install awscli

setup:
	aws configure

sts-identity:
	aws sts get-caller-identity

secret_manager_get_values:
	aws secretsmanager get-secret-value --secret-id wysde --query SecretString --output text

s3_create_bucket:
	TS=$(date +%s)
	aws s3api create-bucket --bucket <bucket-name>-$TS --region us-east-1

create_policy:
	aws iam create-policy --policy-name <policy-name> --policy-document file://<file-name>.json

create_role:
	aws iam create-role --role-name <role-name> --assume-role-policy-document file://role-trust.json

attach_policy_to_role:
	aws iam attach-role-policy --policy-arn <> --role-name <>
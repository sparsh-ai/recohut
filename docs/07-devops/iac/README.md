# Infra as Code (IaC)

## Amazon Cloudformation

```makefile
create:
	aws cloudformation create-stack \
	--stack-name AthenaSnsWys \
	--template-body file://template.yml \
	--capabilities CAPABILITY_NAMED_IAM \
	--parameters ParameterKey=ProjectSuffix,ParameterValue=wys

update:
	aws cloudformation update-stack \
	--stack-name AthenaSnsWys \
	--template-body file://template.yml \
	--capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
	--parameters ParameterKey=ProjectSuffix,ParameterValue=wys

list:
	aws cloudformation list-stack-resources --stack-name AthenaSnsWys

describe:
	aws cloudformation describe-stacks --stack-name AthenaSnsWys

delete:
	aws cloudformation delete-stack \
	--stack-name AthenaSnsWys
```

## Terraform

### Commands

1. `terraform init`: This command initializes a new or existing Terraform working directory. It downloads and installs any necessary plugins and sets up the backend to store state data.
2. `terraform plan`: This command generates an execution plan, which shows what Terraform will do when you apply the configuration. It also checks the syntax of the configuration files and verifies that the required resources are available.
3. `terraform apply`: This command applies the configuration and provisions the infrastructure resources. It creates, updates, or deletes resources as needed to match the desired state.
4. `terraform destroy`: This command destroys all resources created by the configuration. It removes all traces of the infrastructure and frees up any associated resources.
5. `terraform validate`: This command validates the syntax and structure of the Terraform configuration files, checking for errors and warnings.
6. `terraform state`: This command allows you to view, modify, and manage the Terraform state data, which tracks the current state of your infrastructure.

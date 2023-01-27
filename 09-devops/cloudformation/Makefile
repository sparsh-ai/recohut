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
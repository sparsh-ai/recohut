cf-create:
	aws cloudformation create-stack \
	--stack-name AthenaSnswys \
	--template-body file://template.yml \
	--capabilities CAPABILITY_NAMED_IAM \
	--parameters ParameterKey=ProjectSuffix,ParameterValue=wys

cf-update:
	aws cloudformation update-stack \
	--stack-name AthenaSnswys \
	--template-body file://template.yml \
	--capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND \
	--parameters ParameterKey=ProjectSuffix,ParameterValue=wys

cf-list:
	aws cloudformation list-stack-resources --stack-name AthenaSnswys

cf-describe:
	aws cloudformation describe-stacks --stack-name AthenaSnswys

cf-delete:
	aws cloudformation delete-stack \
    --stack-name AthenaSnswys
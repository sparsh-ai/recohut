Create AWS context:
	docker context create ecs myecscontext
List available contexts:
docker context ls
Install ECS CLI - Linux:
	# ref - https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html
	sudo curl -Lo /usr/local/bin/ecs-cli https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest
	wget -q --show-progress https://github.com/recohut/udacity_dend/raw/main/data_modeling_postgres/ecs_pgp.txt
	gpg --import ecs_pgp.txt
	curl -Lo ecs-cli.asc https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-linux-amd64-latest.asc
	gpg --verify ecs-cli.asc /usr/local/bin/ecs-cli
	sudo chmod +x /usr/local/bin/ecs-cli
	ecs-cli --version
Install ECS CLI - Mac:
	# ref - https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_CLI_installation.html
	curl -Lo /usr/local/bin/ecs-cli https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-darwin-amd64-latest
	brew install gnupg
	brew install bind
	gpg --import ecs_pgp.txt
	curl -Lo ecs-cli.asc https://amazon-ecs-cli.s3.amazonaws.com/ecs-cli-darwin-amd64-latest.asc
	gpg --verify ecs-cli.asc /usr/local/bin/ecs-cli
	chmod +x /usr/local/bin/ecs-cli
	ecs-cli --version
Create and Manage Clusters in ECS:
	ecs-cli configure --cluster asparsh-cluster-1 --default-launch-type EC2 --region us-east-1
	ecs-cli configure --cluster asparsh-cluster-1 --default-launch-type FARGATE --region us-east-1

	aws ec2 create-key-pair --key-name asparsh-cluster-1 --query 'KeyMaterial' --output text > ~/.ssh/asparsh-cluster-1.pem
	chmod 400 ~/.ssh/asparsh-cluster-1.pem

	ecs-cli up --keypair asparsh-cluster-1 --capability-iam --size 1 --instance-type r5a.xlarge --tags project=asparsh-cluster-1,owner=Sparsh
	ecs-cli up --keypair asparsh-cluster-1 --capability-iam --tags project=asparsh-cluster-1,owner=Sparsh

	ecs-cli compose --project-name asparsh-cluster-1 --file docker-compose.yml --debug service up --deployment-max-percent 100 --deployment-min-healthy-percent 0
	ecs-cli ps
	aws ec2 describe-security-groups --filters Name=tag:project,Values=asparsh-cluster-1
	aws ec2 authorize-security-group-ingress --group-id sg-xxxxxxxx --protocol tcp --port 5432 --cidr 0.0.0.0/0
	aws ecs delete-service --cluster asparsh-cluster-1 --service asparsh-cluster-1 --force
	aws ecs delete-cluster --cluster asparsh-cluster-1
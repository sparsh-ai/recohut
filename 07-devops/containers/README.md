# Containers

## Docker

Docker is a tool that enables easy management of the entire container ecosystem. Docker has a command-line tool that makes running containers easy, as well as creating, downloading, and managing container images. Docker also comes with a desktop application, Docker Desktop, that makes container management even easier. Finally, the company that built the Docker tool also runs Docker Hub, which makes it easy to store and access container images in the cloud.

Docker has been at the forefront of container management throughout its technological growth. Many of the modern standards around containers arose from features that originated in Docker, and even those that arose elsewhere were popularized by having an easy-to-use tool to make them accessible to the average developer. Docker is known as a “container runtime,” as it contains the tools to make the containers boot up and execute in their own provisioned space.

Docker was first introduced to the world—with no pre-announcement and little fanfare—by Solomon Hykes, founder and CEO of a company then called dotCloud, in a five-minute lightning talk at the Python Developers Conference in Santa Clara, California on March 15, 2013. At the time of this announcement, only about 40 people outside of dotCloud had been given the opportunity to play with Docker.

Within a few weeks of this announcement, there was a surprising amount of press. The project was quickly open-sourced and made publicly available on GitHub, where anyone could download and contribute to the project. Over the next few months, more and more people in the industry started hearing about Docker and how it was going to revolutionize the way software was built, delivered, and run. And within a year, almost no one in the industry was unaware of Docker, but many were still unsure what it was exactly, and why people were so excited about it.

Docker is a tool that promises to easily encapsulate the process of creating a distributable artifact for any application, deploying it at scale into any environment, and streamlining the workflow and responsiveness of agile software organizations.

### Layers

A *layer* is a modification applied to a Docker image as represented by an instruction in a Dockerfile. Typically, a layer is created when a base image is changed---for example, consider a Dockerfile that looks like this:

```Dockerfile
FROM ubuntu
Run mkdir /tmp/logs
RUN apt-get install vim
RUN apt-get install htop
```

Now in this case, Docker will consider Ubuntu image as the base image and add three layers:

- One layer for creating /tmp/logs
- One other layer that installs vim
- A third layer that installs htop

When Docker builds the image, each layer is stacked on the next and merged into a single layer using the union filesystem. Layers are uniquely identified using sha256 hashes. This makes it easy to reuse and cache them. When Docker scans a base image, it scans for the IDs of all the layers that constitute the image and begins to download the layers. If a layer exists in the local cache, it skips downloading the cached image.

### Docker Image

Docker image is a read-only template that forms the foundation of your application. It is very much similar to, say, a shell script that prepares a system with the desired state. In simpler terms, it's the equivalent of a cooking recipe that has step-by-step instructions for making the final dish.

A Docker image starts with a base image---typically the one selected is that of an operating system are most familiar with, such as Ubuntu. On top of this image, we can add build our application stack adding the packages as and when required.

There are many pre-built images for some of the most common application stacks, such as Ruby on Rails, Django, PHP-FPM with nginx, and so on. On the advanced scale, to keep the image size as low as possible, we can also start with slim packages, such as Alpine or even Scratch, which is Docker's reserved, minimal starting image for building other images.

Docker images are created using a series of commands, known as instructions, in the Dockerfile. The presence of a Dockerfile in the root of a project repository is a good indicator that the program is container-friendly. We can build our own images from the associated Dockerfile and the built image is then published to a registry. We will take a deeper look at Dockerfile in later chapters. For now, consider the Docker image as the final executable package that contains everything to run an application. This includes the source code, the required libraries, and any dependencies.

### Docker Container

A Docker image, when it's run in a host computer, spawns a process with its own namespace, known as a *Docker container*. The main difference between a Docker image and a container is the presence of a thin read/write layer known as the container layer. Any changes to the filesystem of a container, such as writing new files or modifying existing files, are done to this writable container layer than the lower layers.

An important aspect to grasp is that when a container is running, the changes are applied to the container layer and when the container is stopped/killed, the container layer is not saved. Hence, all changes are lost. This aspect of containers is not understood very well and for this reason, stateful applications and those requiring persistent data were initially not recommended as containerized applications. However, with Docker Volumes, there are ways to get around this limitation.

### Bind Mounts and Volumes

We mentioned previously that when a container is running, any changes to the container are present in the container layer of the filesystem. When a container is killed, the changes are lost and the data is no longer accessible. Even when a container is running, getting data out of it is not very straightforward. In addition, writing into the container's writable layer requires a storage driver to manage the filesystem. The storage driver provides an abstraction on the filesystem available to persist the changes and this abstraction often reduces performance.

For these reasons, Docker provides different ways to mount data into a container from the Docker host: volumes, bind mounts, and tmpfs volumes. While tmpfs volumes are stored in the host system's memory only, bind mounts and volumes are stored in the host filesystem.

### Docker Registry

We mentioned earlier that you can leverage existing images of common application stacks---have you ever wondered where these are and how you can use them in building your application? A Docker Registry is a place where you can store Docker images so that they can be used as the basis for an application stack. Some common examples of Docker registries include the following:

- Docker Hub
- Google Container Registry
- Amazon Elastic Container Registry
- JFrog Artifactory

Most of these registries also allow for the visibility level of the images that you have pushed to be set as public/private. Private registries will prevent your Docker images from being accessible to the public, allowing you to set up access control so that only authorized users can use your Docker image.

### Dockerfile

A *Dockerfile* is a set of instructions that tells Docker how to build an image. A typical Dockerfile is made up of the following:

- A FROM instruction that tells Docker what the base image is
- An ENV instruction to pass an environment variable
- A RUN instruction to run some shell commands (for example, install-dependent programs not available in the base image)
- A CMD or an ENTRYPOINT instruction that tells Docker which executable to run when a container is started

As you can see, the Dockerfile instruction set has clear and simple syntax, which makes it easy to understand.

### Docker Engine

Docker Engine is the core part of Docker. Docker Engine is a client-server application that provides the platform, the runtime, and the tooling for building and managing Docker images, Docker containers, and more. Docker Engine provides the following:

- Docker daemon
- Docker CLI
- Docker API

### Makefile

```makefile
random:
	sudo chown -R 1001 /var/run/docker.sock
	docker run -p 80:80 -e 'PGADMIN_DEFAULT_EMAIL=u@dom.l' -e 'PGADMIN_DEFAULT_PASSWORD=1579' --name devgadmin -d dpage/pgadmin4
	docker run -d --name toscript -e 'POSTGRES_PASSWORD=1234' -v /home/postgres-data/:/var/lib/postgresql/data -p 5431:5431 postgres
compose-build:
	~/bin/docker-compose build
compose-up:
	~/bin/docker-compose up -d
compose-down:
	~/bin/docker-compose down
list:
	docker ps
create-container:
	docker run CONTAINER --network NETWORK
	docker run -t -i -p 80:80 hello-world
start-stopped-container:
	docker start CONTAINER NAME
stop-running-container:
	docker stop
list-running-containers:
	docker ps
list-all-containers-including-stopped-ones:
	docker ps -a
inspect-container-config:
	docker inspect CONTAINER
list-all-available-virtual-networks:
	docker network ls
Create a new network:
	docker network create NETWORK --driver bridge
Connect a running container to a network:
	docker network connect NETWORK CONTAINER
Disconnect a running container from a network:
	docker network disconnect NETWORK CONTAINER
Remove a network:
	docker network rm NETWORK
build:
	docker build -t my_first_image .
	docker build .
	docker build <dockerfile_path>
	docker images --filter reference=my_first_image
Install docker on Cloud9 and EC2:
	sudo apt-get update
	sudo apt-get remove docker docker-engine docker.io
	sudo apt install docker.io
	sudo systemctl start docker
	sudo systemctl enable docker
	sudo apt install gnome-keyring
	curl -L https://raw.githubusercontent.com/docker/compose-cli/main/scripts/install/install_linux.sh | sh
	VERSION=$(curl --silent https://api.github.com/repos/docker/compose/releases/latest | grep -Po '"tag_name": "\K.*\d')
	DESTINATION=/usr/bin/docker-compose
	sudo curl -L https://github.com/docker/compose/releases/download/${VERSION}/docker-compose-$(uname -s)-$(uname -m) -o $DESTINATION
	sudo chmod 755 $DESTINATION
Install docker on EC2 in general:
	# #!/bin/bash
	# Linux-only installation script
	# This script installs the two main required packages to install the separate dockers:
	# docker engine to run dockers, and docker compose to run multicontainers together.

	sudo apt-get update

	sudo apt-get -y install \
		apt-transport-https \
		ca-certificates \
		curl \
		gnupg \
		lsb-release

	# Add docker gpg key
	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --yes --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

	# Set up a stable repository for x86_64
	echo \
	"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
	$(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

	sudo apt-get update
	sudo apt-get -y install docker-ce docker-ce-cli containerd.io
	sudo apt-get install vim

	# Install docker compose
	sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

	# Make docker-compose "executable"
	sudo chmod +x /usr/local/bin/docker-compose

	# Test docker engine
	# sudo docker run hello-world

	# Test docker compose installation
	# sudo docker-compose --version
```

### Courses

- https://devopswithdocker.com/

## Amazon ECS (Elastic Container Service)

```makefile
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
```

## Amazon EKS (Elastic Kubernetes Service)

```makefile
Installation-MacOS:
	aws sts get-caller-identity
	brew tap weaveworks/tap
	brew install weaveworks/tap/eksctl
	aws eks update-kubeconfig --region us-east-1 --name kubeflow-poc
# If your current user is different from the user/role used to create EKS, you will get the Unauthorized error. Follow this blog to easily resolve this issue: https://aws.amazon.com/premiumsupport/knowledge-center/eks-api-server-unauthorized-error/
Installation-Linux:
	curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
	sudo mv /tmp/eksctl /usr/local/bin
	eksctl create cluster --name my-cluster --region region-code
	export NODEGROUP_NAME=$(eksctl get nodegroups --cluster kubeflow-poc -o json | jq -r '.[0].Name')
	eksctl scale nodegroup --cluster kubeflow-poc --name $NODEGROUP_NAME --nodes 6 --nodes-max 6
	curl --silent --location "https://github.com/kubeflow/kfctl/releases/download/v1.0.1/kfctl_v1.0.1-0-gf3edb9b_linux.tar.gz" | tar xz -C /tmp
	sudo mv -v /tmp/kfctl /usr/local/bin
kf-install.sh:
	cat << EoF > 
	export AWS_CLUSTER_NAME=kubeflow-poc
	export KF_NAME=\${AWS_CLUSTER_NAME}

	export BASE_DIR=${HOME}/environment
	export KF_DIR=\${BASE_DIR}/\${KF_NAME}

	# export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws_cognito.v1.0.1.yaml"
	export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_aws.v1.0.1.yaml"

	export CONFIG_FILE=\${KF_DIR}/kfctl_aws.yaml
	EoF

	source kf-install.sh

	mkdir -p ${KF_DIR}
	cd ${KF_DIR}

	wget -O kfctl_aws.yaml $CONFIG_URI
# Reference: https://www.eksworkshop.com/advanced/420_kubeflow/install/
Install `kubectl`:
	sed -i '/region: us-east-1/ a \      enablePodIamPolicy: true' ${CONFIG_FILE}
	sed -i -e 's/kubeflow-aws/'"$AWS_CLUSTER_NAME"'/' ${CONFIG_FILE}
	sed -i "s@us-west-2@$AWS_REGION@" ${CONFIG_FILE}
	sed -i "s@roles:@#roles:@" ${CONFIG_FILE}
	sed -i "s@- eksctl-kubeflow-poc-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx@#- eksctl-kubeflow-poc-nodegroup-ng-a2-NodeInstanceRole-xxxxxxx@" ${CONFIG_FILE}
	curl -o aws-iam-authenticator https://amazon-eks.s3.us-west-2.amazonaws.com/1.15.10/2020-02-22/bin/linux/amd64/aws-iam-authenticator
	chmod +x aws-iam-authenticator
	sudo mv aws-iam-authenticator /usr/local/bin
	cd ${KF_DIR}
	kfctl apply -V -f ${CONFIG_FILE}
	kubectl -n kubeflow get all
	kubectl port-forward svc/istio-ingressgateway -n istio-system 8080:80
Deleting EKS:
	kubectl get svc --all-namespaces
	eksctl delete cluster --name kubeflow-poc
```

## Labs

1. Deploy docker in Amazon ECS [[source code](07-devops/containers/lab-deploy-simple-docker-ecs/)]
2. Build and deploy NodeJS Kubia app in Kubernetes [[source code](07-devops/containers/lab-kubernetes-kubia-app/)]
3. Build Address parsing system in python and dockerize it [[source code](07-devops/containers/lab-assignment-etl-docker/)]

# Deploy Simple Docker in ECS

## Create a Docker image

Amazon ECS task definitions use Docker images to launch containers on the container instances in your clusters. In this section, you create a Docker image of a simple web application, and then push the image to the Amazon ECR container registry so you can use it in an Amazon ECS task definition.

### Create Dockerfile

This Dockerfile uses the Ubuntu 18.04 image. The RUN instructions update the package caches, install some software packages for the web server, and then write the "Hello World!" content to the web server's document root. The EXPOSE instruction exposes port 80 on the container, and the CMD instruction starts the web server.

### Build the Docker image

```sh
docker build -t hello-world .
```

### Optional - Verify

Run docker images to verify that the image was created correctly:

```sh
docker images --filter reference=hello-world
```

### Optional - Run

Run the newly built image. The -p 80:80 option maps the exposed port 80 on the container to port 80 on the host system.

```sh
docker run -t -i -p 80:80 hello-world
```

## Push your image to Amazon Elastic Container Registry

Amazon ECR is a managed AWS Docker registry service. You can use the Docker CLI to push, pull, and manage images in your Amazon ECR repositories.

### Create an Amazon ECR repository

Create an Amazon ECR repository to store your hello-world image. Note the repositoryUri in the output.

Substitute region, with your AWS Region, for example, us-east-1.

```
aws ecr create-repository --repository-name hello-repository --region region
```

### Tag the image

Tag the hello-world image with the repositoryUri value from the previous step.

```sh
docker tag hello-world aws_account_id.dkr.ecr.region.amazonaws.com/hello-repo
docker tag hello-world 684199068947.dkr.ecr.region.amazonaws.com/hello-repo
```

### Authenticate

Run the aws ecr get-login-password command. Specify the registry URI you want to authenticate to.

```sh
docker login -u AWS -p $(aws ecr get-login-password --region REGION) aws_account_id.dkr.ecr.REGION.amazonaws.com
```

### Push

Push the image to Amazon ECR with the repositoryUri value from the earlier step.

```sh
docker push aws_account_id.dkr.ecr.region.amazonaws.com/hello-repo
```

## Clean up

```sh
aws ecr delete-repository --repository-name hello-repo --region region --force
```
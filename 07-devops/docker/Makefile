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
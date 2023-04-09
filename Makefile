docsify:
	docsify init
	docsify serve

## INSTALL JDK HADOOP

install:
	curl https://dlcdn.apache.org/hadoop/common/hadoop-3.2.3/hadoop-3.2.3.tar.gz --output hadoop-3.2.3.tar.gz
	tar -xvf hadoop-3.2.3.tar.gz
	cd hadoop-3.2.3
	export JAVA_HOME=/usr/lib/jvm/java-1.11.0-openjdk-amd64
	bin/hadoop
install_dockerized:
	git clone https://github.com/ibm-developer-skills-network/ooxwv-docker_hadoop.git
	cd ooxwv-docker_hadoop
	docker-compose up -d
	docker exec -it namenode /bin/bash

## Java

Java-JVM-install:
# 1. Go to https://www.oracle.com/java/technologies/downloads/#java8-mac or https://download.oracle.com/otn/java/jdk/8u341-b10/424b9da4b48848379167015dcc250d8d/jdk-8u341-macosx-x64.dmg (for mac users)
# 2. Install the downloaded package
# 3. Run these commands to set java path
	/usr/libexec/java_home
	export JAVA_HOME=$(/usr/libexec/java_home)
	source
Java-JDK-install:
	apt-get update
	# apt install default-jdk
	apt-get install openjdk-8-jdk-headless -qq > /dev/null
	export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
	sudo apt update
	sudo apt install build-essential


# ENCRYPTION

encrypt:
# Generate a 256 (or any non-zero value) bit (32 byte) random password
	openssl rand -hex 32 > randompassword
# Encrypt your file with a random key derived from randompassword
	openssl enc -p -aes-256-cbc -salt -in sparsh_solution.sql -out sparsh_solution.enc -pass file:./randompassword
# Encrypt your random password using the shared public key
	openssl rsautl -encrypt -inkey publickey -pubin -in randompassword -out sparsh_randompassword.encrypted
# Git commit the files
	git add sparsh_randompassword.encrypted sparsh_solution.enc
getkey:
	openssl genrsa -out privatekey 1024
	openssl rsa -in privatekey -out publickey -pubout -outform PEM
decrypt:
	openssl rsautl -decrypt -inkey privatekey -in sparsh_randompassword.encrypted -out sparsh_randompassword
	openssl enc -d -p -aes-256-cbc -salt -in sparsh_solution.enc -out sparsh_solution.sql -pass file:./sparsh_randompassword
privatekey:
	-----BEGIN RSA PRIVATE KEY-----
	MIICXQIBAAKBgQDMAecRaju1of3J2gkSLsYA4V6tKvaNLzmXwacfipV74shzgb+S
	XXhcD7yV+4cv37NqRXqr33pgIhABi/8H2arKhQkKDzNhIO+bf/dfvPPXa2L/hleG
	-----END RSA PRIVATE KEY-----
publickey:
	-----BEGIN PUBLIC KEY-----
	MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDMAecRaju1of3J2gkSLsYA4V6t
	KvaNLzmXwacfipV74shzgb+SXXhcD7yV+4cv37NqRXqr33pgIhABi/8H2arKhQkK
	-----END PUBLIC KEY-----


# Load text files into pandas dataframe:
# Let's assume we have a `.txt` file of emails. Each email is seperated by 50 `-` symbols (dashed line). So we can use the below code to load this kind of data into pandas dataframe.
load:
	def load_data(file_path):
		my_file = open(file_path, 'r')
		data = my_file.read()
		data_into_list = data.split("-"*50)
		my_file.close()
		df = pd.DataFrame({'text': data_into_list}).replace('', np.nan).dropna()
		df.reset_index(drop=True, inplace=True)
		return df


# LOGGING

logging:
	import sys
	import logging

	logging.basicConfig(stream=sys.stdout,
						level = logging.DEBUG,
						format='%(asctime)s [%(levelname)s] : %(message)s',
						datefmt='%d-%b-%y %H:%M:%S')

	logger = logging.getLogger('IEEE21 Logger')

init:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest tests

.PHONY: api
api:
	uvicorn app:app --port 5000 --reload
	nohup uvicorn app:app --port 5000 --reload > logs.out 2>&1 &
	kill -9 $(lsof -t -i:5000)

.PHONY: format
format:
	black $$(git ls-files '*.py')

dvc-init:
	dvc init
	dvc remote add -d storage s3://s3bucket/dvcstore
	dvc config core.autostage true

lint:
	pylint --disable=R,C src

test:
	python -m pytest -vv tests
	python -m pytest -vv --cov=src

parallel-test:
	python -m pytest -n auto --dist loadgroup -vv --cov=mylib tests/ 

profile-test-code:
	python -m pytest -vv --durations=1 --durations-min=1.0
	
glossary:
	yarn docusaurus parse --dry-run
	yarn docusaurus parse
	yarn docusaurus glossary

dbt-init:
	dbt init ${PROJECT_NAME}
dbt-debug:
	dbt debug --profiles-dir .
dbt-run:
	dbt run
	dbt run --profiles-dir .
	dbt run --profiles-dir path/to/directory
	export DBT_PROFILES_DIR=path/to/directory
dbt-test:
	dbt test -m model1 [model2]
	dbt test --profiles-dir .
dbt-seed:
	dbt seed

venv:
	pipenv --python 3.9.7
	pipenv install
	pipenv shell
	pipenv --venv
	pipenv --rm

.PHONY: dependencies
pip-install:
	python -m ensurepip --upgrade && pip install -r requirements.txt

.PHONY: docker
start:
	docker-compose up -d
stop:
	docker-compose down --remove-orphans
clean:
	docker system prune -f
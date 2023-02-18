# download amazon 
# https://docs.aws.amazon.com/corretto/latest/corretto-18-ug/macos-install.html

# check java version by cmd `java --version`

# download the binary and unzip here
# https://dlcdn.apache.org/kafka/3.2.0/kafka_2.12-3.2.0.tgz

# place the unzip in HOME or some place else

# add that place bin path to the PATH environment
# e.g. export PATH="$HOME/kafka_2.12-3.2.0/bin:$PATH" in ~/.bash_profile
# source ~/.bash_profile
# verify by typing echo $PATH

kill $(lsof -t -i :2181)
kill -9 $(lsof -ti:2181)

kafka-topics.sh

# start zookeeper
zookeeper-server-start.sh ~/kafka_2.12-3.2.0/config/zookeeper.properties

# start kafka server
kafka-server-start.sh ~/kafka_2.12-3.2.0/config/server.properties

# start kafka connect
# ref - https://kafka.apache.org/quickstart
# copy jars from asset directory to /usr/local/share/java
# optionally download and copy other jars also https://debezium.io/documentation/reference/stable/install.html
# open ~/kafka_2.12-3.2.0/config/connect-standalone.properties
# add plugin.path=/usr/local/share/java/
# echo 'schema.registry.url=http://localhost:8081' >> /etc/kafka/connect-distributed.properties
connect-standalone.sh ~/kafka_2.12-3.2.0/config/connect-standalone.properties ~/kafka_2.12-3.2.0/config/connect-file-source.properties ~/kafka_2.12-3.2.0/config/connect-file-sink.properties

# direct way
brew install kafka

# confluent cli
# https://docs.confluent.io/confluent-cli/current/install.html#cli-install
curl -sL --http1.1 https://cnfl.io/cli | sh -s -- latest
export PATH=$(pwd)/bin:$PATH
# export PATH="$HOME/confluent/bin:$PATH"
source ~/.bash_profile
confluent version

# Connect Confluent CLI to Confluent Cloud Cluster
confluent login --save
confluent environment list
confluent environment use env-q2pmqm
confluent kafka cluster list
confluent kafka cluster use lkc-rrkm50

confluent api-key create --resource lkc-rrkm50

confluent api-key use <api-key> --resource <cluster-id>
confluent api-key store <api-key> <secret> --resource <cluster-id>

"""
# Kafka Setup

In this lab, we will first learn how to setup and work with CLI/Python Kafka in following systems:

1. Local Mac/Unix
1. Google Colab
1. AWS ECS
1. AWS EC2
1. AWS MKS
1. Confluent Kafka

## Task 1: Kafka CLI and Python

We will setup Kafka in our local instance. We will interact with it using CLI command-line and Python API. We will 1) Create/delete/manage Kafka topics, 2) Send messaged with Kafka Producer, 3) Receive messages with Kafka Consumer, and 4) Create Consumer Groups.

## Task 2: Kafka in Google Colab

We will learn how to easily setup a Kafka server in Google Colab. We will also learn how to create kafka topic, producer and consumer.

## Task 3: Kafka on the Cloud with AWS

We will learn how to work with Kafka in AWS. We will setup our Kafka server on Cloud in 3 different ways: 1) EC2 instance, 2) ECS Docker Container, and 3) Amazon MSK - the managed Kafka service.

## Task 4: Kafka on Cloud with Confluent Kafka

We will create a multi-broker cluster and tons of services like Schema registry service, CDC debezium connectors and connect with multiple sources and sinks. We will then build multiple real-time event pipelines.
"""

wget https://downloads.apache.org/kafka/3.3.1/kafka_2.12-3.3.1.tgz
tar -xvf kafka_2.12-3.3.1.tgz


-----------------------
java -version
sudo yum install java-1.8.0-openjdk
java -version
cd kafka_2.12-3.3.1

Start Zoo-keeper:
-------------------------------
bin/zookeeper-server-start.sh config/zookeeper.properties


Start Kafka-server:
----------------------------------------
Duplicate the session & enter in a new console --
export KAFKA_HEAP_OPTS="-Xmx256M -Xms128M"
cd kafka_2.12-3.3.1
bin/kafka-server-start.sh config/server.properties

It is pointing to private server , change server.properties so that it can run in public IP 

To do this , you can follow any of the 2 approaches shared belwo --
Do a "sudo nano config/server.properties" - change ADVERTISED_LISTENERS to public ip of the EC2 instance


Create the topic:
-----------------------------
Duplicate the session & enter in a new console --
cd kafka_2.12-3.3.1
bin/kafka-topics.sh --create --topic demo_testing2 --bootstrap-server {Put the Public IP of your EC2 Instance:9092} --replication-factor 1 --partitions 1

Start Producer:
--------------------------
bin/kafka-console-producer.sh --topic demo_testing2 --bootstrap-server {Put the Public IP of your EC2 Instance:9092} 

Start Consumer:
-------------------------
Duplicate the session & enter in a new console --
cd kafka_2.12-3.3.1
bin/kafka-console-consumer.sh --topic demo_testing2 --bootstrap-server {Put the Public IP of your EC2 Instance:9092}
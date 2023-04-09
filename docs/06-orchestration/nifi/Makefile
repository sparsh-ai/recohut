install_ec2:
	apt-get update
	# apt install default-jdk
	apt-get install openjdk-8-jdk-headless -qq > /dev/null
	export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
	wget https://dlcdn.apache.org/nifi/1.18.0/nifi-1.18.0-bin.zip
	apt-get install unzip
	unzip nifi-1.18.0-bin.zip
	cd nifi-1.18.0
	# we need to add ec2 public ip in the allowed ip list
	# 1. nifi.web.https.host= (i.e. no value, remove 127.0.0.1 if there)
	# 2. nifi.web.proxy.host=<ec2-public-ip>,<ec2-public-ip>:8443
	bin/nifi.sh set-single-user-credentials sparsh <>
	bin/nifi.sh run
	# bin/nifi.sh start
	# bin/nifi.sh stop
	bin/nifi.sh status
	# cat logs/nifi-app.log | grep "http"
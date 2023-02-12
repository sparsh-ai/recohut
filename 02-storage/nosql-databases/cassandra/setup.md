# Setup Cassandra

## Install Cassandra

```sh
wget https://dlcdn.apache.org/cassandra/4.0.6/apache-cassandra-4.0.6-bin.tar.gz

tar -xvf apache-cassandra-4.0.6-bin.tar.gz

mv apache-cassandra-4.0.6 ~/cassandra
```

Add `export PATH="$HOME/cassandra/bin:$PATH"` in your bash profile. Validate by running `cassandra --version`. It will show `4.0.6`.

Congratulations! Now your Cassandra server should be up and running with a new single-node cluster called “Test Cluster,” ready to interact with other nodes and clients.

- Run server: `cassandra -f`

## Install DataStax Bulk Loader

```sh
wget https://downloads.datastax.com/dsbulk/dsbulk-1.10.0.tar.gz

tar -xvf dsbulk-1.10.0.tar.gz

mv dsbulk-1.10.0 ~/dsbulk

rm dsbulk-1.10.0.tar.gz
```

Add `export PATH="$HOME/dsbulk/bin:$PATH"` in your bash profile.

## To download and install JVM

1. Go to https://www.oracle.com/java/technologies/downloads/#java8-mac or https://download.oracle.com/otn/java/jdk/8u341-b10/424b9da4b48848379167015dcc250d8d/jdk-8u341-macosx-x64.dmg (for mac users)
2. Install the downloaded package
3. Run these commands to set java path

```sh
/usr/libexec/java_home
export JAVA_HOME=$(/usr/libexec/java_home)
source .bash_profile
```
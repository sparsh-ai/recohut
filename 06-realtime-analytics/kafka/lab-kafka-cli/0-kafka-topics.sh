# list
kafka-topics.sh --bootstrap-server localhost:9092 --list

# create
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic first-topic

# create with partitions and replication factor
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic second-topic --partitions 3 --replication-factor 1
kafka-topics.sh --bootstrap-server localhost:9092 --create --topic third-topic --partitions 3 --replication-factor 1

# list
kafka-topics.sh --bootstrap-server localhost:9092 --list

# describe
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic first-topic
kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic second-topic

# delete
kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic third-topic
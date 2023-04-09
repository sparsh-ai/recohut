list_topics:
	kafka-topics.sh --bootstrap-server localhost:9092 --list

create_topic:
	kafka-topics.sh --bootstrap-server localhost:9092 --create --topic first-topic

create_topic_with_partitions_and_replication_factor:
	kafka-topics.sh --bootstrap-server localhost:9092 --create --topic second-topic --partitions 3 --replication-factor 1
	kafka-topics.sh --bootstrap-server localhost:9092 --create --topic third-topic --partitions 3 --replication-factor 1

describe_topic:
	kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic first-topic
	kafka-topics.sh --bootstrap-server localhost:9092 --describe --topic second-topic

delete_topic:
	kafka-topics.sh --bootstrap-server localhost:9092 --delete --topic third-topic

produce_messages:
	kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first-topic

produce_messages_with_keys:
	kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first-topic --property "parse.key=true" --property "key.separator=:"

produce_messages_with_ngrok:
	ngrok tcp 9092
	kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first-topic

consume_messages:
	kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic

consume_messages_with_ngrok:
	kafka-console-consumer.sh --bootstrap-server tcp://<>:15178 --topic first-topic

consume_messages_with_beginning_offset:
	kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --from-beginning

consume_messages_with_timestamp:
	kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning

consume_messages_with_consumer_group:
	kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --group first-consumer-group
	kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --from-beginning --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning --group first-consumer-group

list_consumer_groups:
	kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list

describe_consumer_groups:
	kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group first-consumer-group

reset_offsets_of_consumer_groups:
	kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group first-consumer-group --reset-offsets --to-earliest --execute --all-topics
	kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group first-consumer-group --reset-offsets --shift-by 2 --execute --topic first-topic
	kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group first-consumer-group --reset-offsets --shift-by -2 --execute --topic first-topic

confluent-consume:
	python confluent/consumer.py -f confluent/python.config -t test1

# confluent - list topics
confluent kafka topic list

# confluent - create topic
confluent kafka topic create first-topic

# confluent - create topic with partitions
confluent kafka topic create second-topic --partitions 3

# confluent - describe topic
confluent kafka topic describe first-topic

# confluent - delete topic
confluent kafka topic delete first-topic

# confluent - ref: https://docs.confluent.io/confluent-cli/current/command-reference/kafka/topic/confluent_kafka_topic_delete.html

# confluent - product message
confluent kafka topic produce second-topic

# confluent - consume message
confluent kafka topic consume second-topic -b
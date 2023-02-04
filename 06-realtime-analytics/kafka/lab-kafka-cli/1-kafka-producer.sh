# produce messages
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first-topic

# produce messages with keys
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first-topic --property "parse.key=true" --property "key.separator=:"
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic wysde3 --property "parse.key=true" --property "key.separator=:"

# produce messages with ngrok
ngrok tcp 9092
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first-topic

kafka-console-consumer.sh --bootstrap-server tcp://<>:10147 --topic sparsh-study
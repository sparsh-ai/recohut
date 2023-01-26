# consume messages
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic

# consume messages with ngrok
kafka-console-consumer.sh --bootstrap-server tcp://6.tcp.ngrok.io:15178 --topic first-topic

# consume messages with beginning offset
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --from-beginning
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafka-localhost-python --from-beginning

# consume messages with timestamp
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic kafka-localhost-python --formatter kafka.tools.DefaultMessageFormatter --property print.key=true --property print.value=true --from-beginning

# consume messages with consumer group
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --group first-consumer-group
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first-topic --from-beginning --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning --group first-consumer-group
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic wysde3 --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning --group wysde
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic wysde3 --from-beginning --group wysde

Consumer Group - Multiple Consumers - Each consumer connect to a parition. 
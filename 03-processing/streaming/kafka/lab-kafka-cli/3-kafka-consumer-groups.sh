# list consumer groups
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --list

# describe consumer groups
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group first-consumer-group
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group wysde

# reset offsets of consumer groups
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group first-consumer-group --reset-offsets --to-earliest --execute --all-topics
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group first-consumer-group --reset-offsets --shift-by 2 --execute --topic first-topic
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --group first-consumer-group --reset-offsets --shift-by -2 --execute --topic first-topic
from kafka import KafkaConsumer 

brokers = ["localhost:9091", "localhost:9092", "localhost:9093"]
consumer = KafkaConsumer("first-cluster-topic", bootstrap_servers=brokers)

for message in consumer:
  print(message)

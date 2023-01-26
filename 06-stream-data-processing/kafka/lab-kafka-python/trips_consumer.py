from kafka import KafkaConsumer 
import json 

brokers = ["localhost:9091", "localhost:9092", "localhost:9093"]
topicName = "trips"
consumer = KafkaConsumer(topicName, bootstrap_servers=brokers)

for message in consumer:
  row = json.loads(message.value.decode())
  if float(row[10]) > 10:
    print("--over 10--")
    print(f"{row[9]} - {row[10]}")
  
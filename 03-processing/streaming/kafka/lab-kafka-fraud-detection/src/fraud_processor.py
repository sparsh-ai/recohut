from kafka import KafkaConsumer
import json

FRAUD_TOPIC = "fraud_payments"
brokers = ["localhost:9091", "localhost:9092", "localhost:9093"]
consumer = KafkaConsumer(FRAUD_TOPIC, bootstrap_servers=brokers)

for message in consumer:
  msg = json.loads(message.value.decode())
  to = msg["TO"]
  amount = msg["AMOUNT"]
  if msg["TO"] == "stranger":
    print(f"[ALERT] fraud detected payment to: {to} - {amount}")
  else:
    print(f"[PROCESSING BITCOIN] payment to: {to} - {amount}")

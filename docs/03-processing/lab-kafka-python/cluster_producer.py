from kafka import KafkaProducer 

brokers = ["localhost:9091", "localhost:9092", "localhost:9093"]
topicName = "first-cluster-topic"

producer = KafkaProducer(bootstrap_servers = brokers)

producer.send(topicName, b"Hello cluster world")
producer.flush()
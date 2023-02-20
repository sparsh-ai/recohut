import json
import time

from kafka import KafkaConsumer, KafkaProducer

ORDER_CONFIRMED_KAFKA_TOPIC = 'order_confirmed'
ANALYTICS_KAFKA_TOPIC = 'analytics_result'

KAFKA_SERVER_ADDRESS = 'localhost:9092'
# KAFKA_SERVER_ADDRESS = '47.93.191.241:29093`

producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER_ADDRESS], security_protocol="PLAINTEXT",
                            value_serializer=lambda x: json.dumps(x).encode('utf-8'))

consumer = KafkaConsumer(ORDER_CONFIRMED_KAFKA_TOPIC, bootstrap_servers=[KAFKA_SERVER_ADDRESS], security_protocol="PLAINTEXT",
                            value_deserializer=lambda x: json.loads(x.decode('utf-8')))

total_revenue = 0
total_orders_count = 0

while True:
    for message in consumer:
        # read data from consumer and do some analytics on it
        print("Received order details: {}".format(message.value))
        order_details = message.value['order_details']
        total_revenue += int(order_details['price'])
        total_orders_count += 1
        analytics = {}
        analytics['total_revenue'] = total_revenue
        analytics['total_orders_count'] = total_orders_count
        producer.send(ANALYTICS_KAFKA_TOPIC, analytics)
        print("Sent analytics details {} to kafka topic: {}".format(analytics, ANALYTICS_KAFKA_TOPIC))
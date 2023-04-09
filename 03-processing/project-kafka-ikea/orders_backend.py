import json
import time

from kafka import KafkaProducer
from flask import Flask, jsonify, request

ORDER_KAFKA_TOPIC = 'order_details'

KAFKA_SERVER_ADDRESS = 'localhost:9092'
# KAFKA_SERVER_ADDRESS = '47.93.191.241:29093`

app = Flask(__name__)

## from inside docker compose network - when add the service to compose file -> orders_backend:v1
producer = KafkaProducer(bootstrap_servers=[KAFKA_SERVER_ADDRESS], security_protocol="PLAINTEXT",
                              value_serializer=lambda x: json.dumps(x).encode('utf-8'))

# post endpoint to get user id , order id, user email, and order details
@app.route('/order', methods=['POST'])
def order():
    user_id = request.json['user_id']
    order_id = request.json['order_id']
    user_email = request.json['user_email']
    order_details = request.json['order_details']
    order = {}
    order['user_id'] = user_id
    order['order_id'] = order_id
    order['user_email'] = user_email
    order['order_details'] = order_details
    order['time'] = time.time()
    producer.send(ORDER_KAFKA_TOPIC, order)
    print("Sent order details {} to kafka topic: {}".format(order, ORDER_KAFKA_TOPIC))
    return jsonify(order)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
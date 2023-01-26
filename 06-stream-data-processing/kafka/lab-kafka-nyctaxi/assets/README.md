# Kafka with Docker Compose

- zookeeper: a centralized service for maintaining configuration info. Kafka uses it for maintaining metadata knowledge such as topic partitions, etc. Zookeeper is being phased out as a dependency, but for easier deployment we will use it in the lesson.
- broker: the main service. A plethora of environment variables are provided for easier configuration. The image for this service packages both Kafka and Confluent Server, a set of commercial components for Kafka.
- kafka-tools: a set of additional Kafka tools provided by Confluent Community. We will make use of this service later in the lesson.
- schema-registry: provides a serving layer for metadata. We will make use of this service later in the lesson.
- control-center: a web-based Kafka GUI.

Kafka can be entirely used with command-line tools, but the GUI helps us visualize things.

Start the deployment with `docker compose -f kafka-docker-compose.yml up`. It may take several minutes to deploy on the first run. Check the status of the deployment with docker ps. Once the deployment is complete, access the control center GUI by browsing to localhost:9021.

## AVRO Producer and Consumer

```sh
# start avro production
python producer.py
```

```sh
# start avro consumption
python consumer.py
```

## Kafka Streams

```sh
# start json production
python producer_taxi_json.py
```

```sh
# read the stream
python stream.py worker
```

`stream_count_vendor_trips.py` is another Faust app that showcases creating a state from a stream.

```sh
# read the stateful stream
python stream_count_vendor_trips.py worker
```

`branch_price.py` is a Faust app that showcases branching:

```sh
# read the batch stream
python branch_price.py worker
```

`windowing.py` is a very similar app to `stream_count_vendor_trips.py` but defines a tumbling window for the table.

```sh
# read the batch stream
python windowing.py worker
```

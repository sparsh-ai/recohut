# Kafka Streams for NYC Taxi data

## Objective

In this lab, we will use Faust in Kafka Streams to process the taxi data in real-time and consume it via Python consumer instance.

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/03-processing/lab-kafka-nyctaxi)


```
├── [ 199]  README.md
├── [5.1K]  assets
│   ├── [1.9K]  README.md
│   ├── [2.3K]  kafka-docker-compose.yml
│   ├── [ 147]  run.sh
│   ├── [ 165]  taxi_ride_key.avsc
│   └── [ 422]  taxi_ride_value.avsc
├── [ 24K]  data
│   └── [ 24K]  rides.csv
└── [5.6K]  src
    ├── [ 709]  branch_price.py
    ├── [1.1K]  consumer.py
    ├── [1.3K]  producer.py
    ├── [ 730]  producer_taxi_json.py
    ├── [ 352]  stream.py
    ├── [ 445]  stream_count_vendor_trips.py
    ├── [ 175]  taxi_rides.py
    └── [ 556]  windowing.py

  35K used in 3 directories, 15 files
```
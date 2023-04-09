from time import sleep
import requests

CONNECTORS = [
    {
        "name": "source_pg_car_connector",
        "config": {
            "connector.class":
                "io.debezium.connector.postgresql.PostgresConnector",
            "plugin.name": "pgoutput",

            "database.hostname": "postgres",
            "database.port": "5432",
            "database.user": "postgres",
            "database.password": "postgres",
            "database.dbname": "database",

            "database.server.name": "car_database",
            "table.include.list": "public.car_data",
            
            # Defining SMTs
            "transforms": "unwrap",
            # Extacts the new record state from the record
            "transforms.unwrap.type": "io.debezium.transforms.ExtractNewRecordState",
        }
    },
    
    {
        "name": "sink_pg_car_connector",
        "config": {
            "topics": "car_data_predicted",
            
            "connector.class":
                "io.confluent.connect.jdbc.JdbcSinkConnector",
            "tasks.max": "1",
            
            "connection.url": "jdbc:postgresql://postgres:5432/database",
            "connection.user": "postgres",
            "connection.password": "postgres",

            "auto.create": "true",
            "insert.mode": "upsert",
            "pk.fields": "id",
            "pk.mode": "record_value",
        }
    }
]

# Wait for the debezium server to be ready
sleep(50)
    
# Try write the connectors to the debezium server
for connector in CONNECTORS:
    response = requests.post(
        "http://connect:8083/connectors",
        headers={
            "Content-Type": "application/json"
        },
        json=connector
    )
    print(response)
    print(response.json())
    print("")
    print("")
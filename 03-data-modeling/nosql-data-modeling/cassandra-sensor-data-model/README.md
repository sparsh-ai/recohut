# Create a Data Model for Temperature Monitoring Sensor Networks

## Conceptual Data Model

A conceptual data model is designed with the goal of understanding data in a particular domain. In this example, the model is captured using an Entity-Relationship Diagram (ERD) that documents entity types, relationship types, attribute types, and cardinality and key constraints.

![](https://user-images.githubusercontent.com/62965911/214248277-5ad44557-b175-4273-986e-c080650bcc14.png)

The conceptual data model for sensor data features sensor networks, sensors, and temperature measurements. Each network has a unique name, description, region, and number of sensors. A sensor is described by a unique id, location, which is composed of a latitude and longitude, and multiple sensor characteristics. A temperature measurement has a timestamp and value, and is uniquely identified by a sensor id and a measurement timestamp. While a network can have many sensors, each sensor can only belong to one network. Similarly, a sensor can record many temperature measurements at different timestamps and every temperature measurement is reported by exactly one sensor.

## Application workflow

An application workflow is designed with the goal of understanding data access patterns for a data-driven application. Its visual representation consists of application tasks, dependencies among tasks, and data access patterns. Ideally, each data access pattern should specify what attributes to search for, search on, order by, or do aggregation on.

![](https://user-images.githubusercontent.com/62965911/214248269-804877f6-03c5-445c-8b25-2ca7baff20be.png)

The application workflow has an entry-point task that shows all sensor networks. This task requires querying a database to find information about all networks and arrange the results in ascending order of network names, which is documented as Q1 on the diagram. Next, an application can either display a heatmap for a selected network, which requires data access pattern Q2, or display all sensors in a selected network, which requires data access pattern Q3. Finally, the latter can lead to the task of showing raw temperature values for a given sensor based on data access pattern Q4. All in all, there are four data access patterns for a database to support.

## Logical Data model

A logical data model results from a conceptual data model by organizing data into Cassandra-specific data structures based on data access patterns identified by an application workflow. Logical data models can be conveniently captured and visualized using Chebotko Diagrams that can feature tables, materialized views, indexes and so forth.

![](https://user-images.githubusercontent.com/62965911/214248289-7e040329-d61e-480a-9df0-d492fb235230.png)

The logical data model for sensor data is represented by the shown Chebotko Diagram. There are four tables, namely networks, temperatures_by_network, sensors_by_network and temperatures_by_sensor, that are designed to specifically support data access patterns Q1, Q2, Q3 and Q4, respectively. For example, table temperatures_by_network has seven columns, of which network is designated as a partition key column, and date, hour and sensor are clustering key columns with descending or ascending order being represented by a downward or upward arrow. To support Q2, it should be straightforward to see that a query over this table needs to restrict column network to some value and column date to a range of values, while the result ordering based on date and hour is automatically supported by how data is organized in the table.

## Physical Data Model
A physical data model is directly derived from a logical data model by analyzing and optimizing for performance. The most common type of analysis is identifying potentially large partitions. Some common optimization techniques include splitting and merging partitions, data indexing, data aggregation and concurrent data access optimizations.

![](https://user-images.githubusercontent.com/62965911/214248298-61f1c144-249f-48f9-b44b-2813ccb03bfa.png)

The physical data model for sensor data is visualized using the Chebotko Diagram. This time, all table columns have associated data types. In addition, two tables have changes in their primary keys. Table networks used to be partitioned based on column name and is now partitioned based on column bucket. The old design had single-row partitions and required retrieving rows from multiple partitions to satisfy Q1. The new design essentially merges old single-row partitions into one multi-row partition and results in much more efficient Q1. With respect to table temperatures_by_network, there are two optimizations. The minor optimization is to merge columns date and hour into one column date_hour, which is supported by the TIMESTAMP data type. The major optimization is to split potentially large partitions by introducing column week, which represents the first day of a week, as a partition key column. Consider that a network with 100 sensors generates 100 rows per hour in table temperatures_by_network. The old design allows partitions to grow over time: 100 rows in an hour, 2400 rows in a day, 16800 rows in a week, …, 876000 rows in a year, and so forth. The new design restricts each partition to only contain at most 16800 rows that can be generated in one week. Our final blueprint is ready to be instantiated in Cassandra.

## Hands-on

In this lab, you will:

- Create tables for a sensor data use case
- Populate tables with sample sensor data
- Design and execute CQL queries over sensor data

### Create Keyspace

```sql
CREATE KEYSPACE sensor_data
WITH replication = {
  'class': 'SimpleStrategy', 
  'replication_factor': 1 }; 

USE sensor_data;
```

### Create Tables

```sql
CREATE TABLE IF NOT EXISTS networks (
  bucket TEXT,
  name TEXT,
  description TEXT,
  region TEXT,
  num_sensors INT,
  PRIMARY KEY ((bucket),name)
);

CREATE TABLE IF NOT EXISTS temperatures_by_network (
  network TEXT,
  week DATE,
  date_hour TIMESTAMP,
  sensor TEXT,
  avg_temperature FLOAT,
  latitude DECIMAL,
  longitude DECIMAL,
  PRIMARY KEY ((network,week),date_hour,sensor)
) WITH CLUSTERING ORDER BY (date_hour DESC, sensor ASC);

CREATE TABLE IF NOT EXISTS sensors_by_network (
  network TEXT,
  sensor TEXT,
  latitude DECIMAL,
  longitude DECIMAL,
  characteristics MAP<TEXT,TEXT>,
  PRIMARY KEY ((network),sensor)
);

CREATE TABLE IF NOT EXISTS temperatures_by_sensor (
  sensor TEXT,
  date DATE,
  timestamp TIMESTAMP,
  value FLOAT,
  PRIMARY KEY ((sensor,date),timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC);

DESCRIBE TABLES;
```

### Populate tables

```sql
SOURCE 'sensor_data.cql'
```

Retrieve some rows from tables:

```sql
SELECT * FROM networks;        
SELECT network, week, date_hour, 
       sensor, avg_temperature 
FROM temperatures_by_network;
SELECT * FROM sensors_by_network;                    
SELECT * FROM temperatures_by_sensor;
```

### Design query Q1

Find information about all networks; order by name (asc):

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT name, description,
          region, num_sensors
    FROM networks
    WHERE bucket = 'all';  
    ```
</details>
<br/>

### Design query Q2

Find hourly average temperatures for every sensor in network forest-net and date range [2020-07-05,2020-07-06] within the week of 2020-07-05; order by date (desc) and hour (desc):

```sql
SELECT date_hour, avg_temperature, 
      latitude, longitude, sensor 
FROM temperatures_by_network
WHERE network    = 'forest-net'
  AND week       = '2020-07-05'
  AND date_hour >= '2020-07-05'
  AND date_hour  < '2020-07-07';
```

### Design query Q3

Find hourly average temperatures for every sensor in network forest-net and date range [2020-07-04,2020-07-06] within the weeks of 2020-06-28 and 2020-07-05; order by date (desc) and hour (desc):

```sql
SELECT date_hour, avg_temperature, 
      latitude, longitude, sensor 
FROM temperatures_by_network
WHERE network    = 'forest-net'
  AND week       = '2020-07-05'
  AND date_hour >= '2020-07-04'
  AND date_hour  < '2020-07-07';
  
SELECT date_hour, avg_temperature, 
      latitude, longitude, sensor 
FROM temperatures_by_network
WHERE network    = 'forest-net'
  AND week       = '2020-06-28'
  AND date_hour >= '2020-07-04'
  AND date_hour  < '2020-07-07';  
```

```sql
SELECT date_hour, avg_temperature, 
      latitude, longitude, sensor 
FROM temperatures_by_network
WHERE network    = 'forest-net'
  AND week      IN ('2020-07-05','2020-06-28')
  AND date_hour >= '2020-07-04'
  AND date_hour  < '2020-07-07';   
```

### Design query Q4

Find information about all sensors in network forest-net:

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT * 
    FROM sensors_by_network
    WHERE network = 'forest-net';
    ```
</details>
<br/>

### Design query Q5

Find raw measurements for sensor s1003 on 2020-07-06; order by timestamp (desc):

<details>
    <summary>Show me the Answer! </summary>
    ```sql
    SELECT timestamp, value 
    FROM temperatures_by_sensor
    WHERE sensor = 's1003'
      AND date   = '2020-07-06';
    ```
</details>
<br/>
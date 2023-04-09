# Airflow - City Traffic Drone

> City Vehicle Trajactories Data extraction and warehousing for Traffic analysis

A city traffic department wants to collect traffic data using swarm UAVs (drones) from a number of locations in the city and use the data collected for improving traffic flow in the city and for a number of other undisclosed projects. Your startup is responsible for creating a scalable data warehouse that will host the vehicle trajectory data extracted by analysing footage taken by swarm drones and static roadside cameras. The data warehouse should take into account future needs, organise data such that a number of downstream projects query the data efficiently. You should use the Extract Load Transform (ELT) framework using DBT.

![](https://user-images.githubusercontent.com/62965911/224527525-39a2f55f-1c9b-4467-8577-37e2f6fa8dde.png)

Process steps:

1. Download the data from https://open-traffic.epfl.ch/index.php/downloads (optional)
2. Configure the project paths in the DAG
3. Run the DAG

## Dashboard

![](https://user-images.githubusercontent.com/62965911/210303740-f6e3b6ff-c78c-478d-bb7c-d8fbdd6e81e6.png)

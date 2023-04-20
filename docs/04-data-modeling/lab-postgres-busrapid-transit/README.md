# Lab: Creating a Bus Rapid Transit (BRT) Database in Postgres

> Creating a Bus Rapid Transit (BRT) Database

In this lab, our goal is to design the database for Bus Rapid Transit Service.

We will do the following activities:

1. Connect to Postgres Server
1. Create DDL
1. Ingest the data with `psql COPY` commands
1. Run analytics queries
1. Optimize by adding indices

## Schema

![](https://user-images.githubusercontent.com/62965911/211728840-8fbfa70d-61c6-4c60-a408-dca8c49c2493.png)

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/04-data-modeling/lab-postgres-busrapid-transit)

```
├── [ 32K]  01-sa-main.ipynb
├── [ 928]  README.md
└── [172K]  data
    ├── [ 392]  corridor_locations.csv
    ├── [ 389]  corridor_locations.txt
    ├── [1.3K]  driver_additional_details.csv
    ├── [1.7K]  driver_additional_details.txt
    ├── [ 680]  driver_identification_cards.csv
    ├── [ 713]  driver_identification_cards.txt
    ├── [ 434]  driver_vehicle_logs.csv
    ├── [ 464]  driver_vehicle_logs.txt
    ├── [5.2K]  drivers.csv
    ├── [2.1K]  license.csv
    ├── [2.3K]  license.txt
    ├── [ 12K]  passenger_cards.csv
    ├── [ 16K]  passenger_cards.txt
    ├── [ 19K]  passenger_trips.csv
    ├── [ 19K]  passenger_trips.txt
    ├── [ 17K]  passengers.csv
    ├── [ 65K]  trips.csv
    ├── [4.2K]  vehicles.csv
    └── [4.2K]  vehicles.txt

 205K used in 1 directory, 21 files
```

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/04-data-modeling/lab-postgres-busrapid-transit)
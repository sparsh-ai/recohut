# Railway API

## Data Model

When preparing the entity-relationship schema for this project, we sought to design something interesting and at the same time simple and well contained. This application considers four entities: Stations, Trains, Tickets, and Users. A Train is a journey from one station to another one. A Ticket is a connection between a Train and a User. Users can be passengers or administrators, according to what they are supposed to be able to do with the API.

![er-diagram](https://user-images.githubusercontent.com/62965911/215282224-ca7726ef-41b0-42da-aacd-6219c0afd7fc.png)

## Setup

To generate a new database with random data:

```sh
python dummy_data.py
```

## Running the API

```sh
uvicorn main:app --reload
```

Watch this video: https://www.youtube.com/watch?v=XJzDGxcJ06U
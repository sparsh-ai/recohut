# Lufthansa API

## Objective

- Extract the data from Lufthansa API
- Transform it using python
- Store the data into NoSQL database for persistence
- Create a dashboard
- Create a REST API

## Business case

Using the Lufthansa API we want to be able to, given an airport, calculate the delayed flights (how late, how many) over a period of time in order to be able to improve service. We also want to be able to have a way to list which flights are available between airports.
We will look at the airports within the major countries of UK, Spain, Germany, France and Italy.

The Lufthansa API returns request data in JSON format which can be stored within a database (most likely MongoDb) for future querying. 
Because flight information can change regularly we will automate calls to the API daily so that the database contains most recent flights and departures/arrivals information each day.

In this lab, we will:

- Consider 3 major countries - UK, France, Italy (This already gives us a huge load of Airports)
- List flight arrivals for airports
- Display status of flights arriving at airports by country/IATA code
- Count the total statuses of arrivals per country/IATA
- Using MongoDb - update daily but remain within the API limits (5 per second, 1000 per hour)
- Create Dashboard using Plotly dash and connect to MongoDB database

## API

![api](https://user-images.githubusercontent.com/62965911/215280116-4998567e-adcd-406f-80a8-f12baf47a3df.png)

![api_codes](https://user-images.githubusercontent.com/62965911/215280110-7e7a208d-cf52-43da-8bc5-630e0eb99d7e.png)

## Dashboard

![dashboard](https://user-images.githubusercontent.com/62965911/215280118-abf10b81-2059-4fa8-b2c5-ec7134c970f8.png)

## MongoDB Atlas

![mongodb_atlas](https://user-images.githubusercontent.com/62965911/215280124-bc6af95d-86dd-4667-af26-e411cf5d385b.png)
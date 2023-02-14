select 
    vendor_id,
    pickup_datetime, 
    dropoff_datetime, 
    passenger_count, 
    pickup_location_id, 
    dropoff_location_id, 
    fare_amount
from {{ source('source', 'yellow_taxi_trips') }}

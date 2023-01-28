{{ config(materialized='table') }}

with citibike_trips as (
    select * from {{ ref('stg_citibike_tripdata') }}
)
select
    trip_id, 
    bike_id, 
    start_station_name,
    start_station_latitude,
    start_station_longitude,
    end_station_name,
    end_station_latitude,
    end_station_longitude,
    start_time,
    stop_time,
    trip_duration,
    user_type,  
    birth_year, 
    gender
    
from citibike_trips
{{ config(materialized='table') }}

with trips_data as (
    select * from {{ ref('fact_citibike_trips') }}
)
select
    -- Stats grouping 
    start_station_name as station_name,
    date_trunc(start_time, month) as trip_month, 

    -- Stats calculation
    count(trip_id) as total_monthly_trips,
    avg(trip_duration) as avg_montly_trip_duration

from trips_data
group by 1,2
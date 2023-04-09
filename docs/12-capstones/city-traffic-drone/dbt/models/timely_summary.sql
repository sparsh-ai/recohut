{{ config(materialized='view') }}

with vehicles as (
    select * from {{source("source", "endpoints_trafficinfo")}}
),

timely_summary as (
    SELECT 
    time,
    Round(AVG(Cast(speed as numeric)),2) as "speed",
    Round(AVG(Cast(lat_acc as numeric)),2) as "lat_acc",
    Round(AVG(Cast(lon_acc as numeric)),2) as "lon_acc"
    from vehicles
    GROUP BY "time"
)


SELECT * FROM timely_summary
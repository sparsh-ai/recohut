{{ config(materialized='view') }}

with trajectories as (
    select * from {{source("source", "endpoints_trafficinfo")}}
),

fast_vehicles as (
    SELECT *
    from trajectories 
    ORDER BY avg_speed DESC
    LIMIT 100
)


SELECT * FROM fast_vehicles

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null

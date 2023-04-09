{{ config(materialized='table') }}

with fhv_data as (
    select *, 
        'fhv' as service_type 
    from {{ ref('stg_fhv_tripdata') }}
), 

dim_zones as (
    select * from {{ ref('dim_zones') }}
    where borough != 'Unknown'
)
select 
    fhv_data.dispatching_base_num,
    fhv_data.pickup_datetime,
    fhv_data."dropOff_datetime",
    fhv_data."PUlocationID",
    fhv_data."DOlocationID",
    fhv_data."SR_Flag",
    fhv_data."Affiliated_base_number"
from fhv_data
inner join dim_zones as pickup_zone
on fhv_data."PUlocationID" = pickup_zone.locationid

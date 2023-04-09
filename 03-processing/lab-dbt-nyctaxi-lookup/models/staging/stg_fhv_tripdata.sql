{{ config(materialized='view') }}

-- dbt run --select stg_fhv_tripdata
select * from {{ source('staging', 'external_fhv_tripdata') }}
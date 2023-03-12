{{ config(materialized='table') }}
with source_data as (
    select * from {{source("source", "endpoints_trafficinfo")}}
),

final as (
    SELECT distinct
    md5(type) as Id,
    type FROM source_data
)

select * from final
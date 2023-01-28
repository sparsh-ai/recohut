{{ config(materialized='view') }}

select
    -- identifiers
    {{ dbt_utils.surrogate_key(['bikeid', 'starttime']) }} as trip_id,
    cast(bikeid as integer) as bike_id,
    cast(start_station_id as integer) as start_station_id,
    cast(end_station_id as integer) as end_station_id,

    -- timestamps
    cast(starttime as timestamp) as start_time,
    cast(stoptime as timestamp) as stop_time,

    -- trip info
    cast(tripduration as integer) as trip_duration,
    cast(start_station_name as string) as start_station_name,
    cast(start_station_latitude as numeric) as start_station_latitude,
    cast(start_station_longitude as numeric) as start_station_longitude,
    cast(end_station_name as string) as end_station_name,
    cast(end_station_latitude as numeric) as end_station_latitude,
    cast(end_station_longitude as numeric) as end_station_longitude,

    -- customer info
    cast(usertype as string) as user_type,
    cast(birth_year as integer) as birth_year,
    cast(gender as integer) as gender_code,
    {{ get_gender_description('gender') }} as gender

from {{ source('staging','citibike_tripdata') }}
where bikeid is not null

-- dbt build --m <model.sql> --var 'is_test_run: false'
{% if var('is_test_run', default=true) %}

  limit 100

{% endif %}

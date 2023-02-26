{{ 
    config(
        materialized='table',
        partition_by={
            "field": "DATE_TRUNC(date, YEAR)"
        },
        cluster_by=['country_code', 'id']
    )
}}

select
    years.id,
    years.date,
    years.tmax,
    years.tmin,
    years.prcp,
    years.snow,
    years.snwd,
    years.m_flag,
    years.s_flag,
    stations.name as station_name,
    stations.latitude,
    stations.longitude,
    stations.elevation,
    stations.country_code,
    countries.name as country_name
from {{ ref('stg_years_unioned_avg_year') }} as years
inner join {{ ref('stg_stations') }} as stations
on years.id = stations.id
inner join {{ ref('stg_countries') }} as countries
on stations.country_code = countries.code

{% if var('is_test_run', default=true) %}
    limit 500
{% endif %}
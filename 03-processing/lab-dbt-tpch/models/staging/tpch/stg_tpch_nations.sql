{{
    config(
        materialized='incremental',
        unique_key='nation_key'
    )
}}
with source as (
    select * from {{ ref('nations') }}
),
renamed as (
    select
        n_nationkey as nation_key,
        n_name as name,
        n_regionkey as region_key,
        last_updated_date as last_updated_date
    from source
)
select * from renamed
{% if is_incremental() %}
  -- this filter will only be applied on an incremental run
  where last_updated_date > (select max(last_updated_date) from {{ this }})
{% endif %}
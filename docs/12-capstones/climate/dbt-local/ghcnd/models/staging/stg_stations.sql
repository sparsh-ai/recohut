{{ config(materialized='view') }}

select
    *,
    substr(id,1,2) as country_code
from {{ source('staging_other','stations') }}
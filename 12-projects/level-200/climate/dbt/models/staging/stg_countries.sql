{{ config(materialized='view') }}

select * from {{ source('staging_other','countries') }}
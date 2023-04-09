{{
    select_purchases(
        from_table=ref('logs'),
        materialized='incremental'
    )
}}

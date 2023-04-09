{{
    select_events(
        from_table=ref('logs'),
        materialized='incremental'
    )
}}

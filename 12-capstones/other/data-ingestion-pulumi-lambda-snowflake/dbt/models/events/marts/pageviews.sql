{{
    select_pageviews(
        from_table=ref('logs'),
        materialized='incremental'
    )
}}

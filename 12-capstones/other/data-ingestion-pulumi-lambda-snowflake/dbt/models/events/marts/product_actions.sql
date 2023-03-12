{{
    select_product_actions(
        from_table=ref('logs'),
        materialized='incremental'
    )
}}

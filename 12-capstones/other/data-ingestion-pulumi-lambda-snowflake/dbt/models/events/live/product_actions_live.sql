{{
    config(
        alias='product_actions',
        materialized='view'
    )
-}}


{%- set threshold = get_events_threshold(ref('logs')) -%}


SELECT * FROM (
    {{
        select_product_actions(
            from_table=ref('logs_staged')
        )
    }}
)

UNION ALL

SELECT *
FROM {{ ref('product_actions') }}
{% if threshold != False -%}
    WHERE TO_DATE(request_timestamp) < TO_DATE('{{ threshold }}')
{%- endif %}

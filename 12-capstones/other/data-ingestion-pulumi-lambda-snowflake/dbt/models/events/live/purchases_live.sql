{{
    config(
        alias='purchases',
        materialized='view'
    )
-}}


{%- set threshold = get_events_threshold(ref('logs')) -%}


SELECT * FROM (
    {{
        select_purchases(
            from_table=ref('logs_staged')
        )
    }}
)

UNION ALL

SELECT *
FROM {{ ref('purchases') }}
{% if threshold != False -%}
    WHERE TO_DATE(request_timestamp) < TO_DATE('{{ threshold }}')
{%- endif %}

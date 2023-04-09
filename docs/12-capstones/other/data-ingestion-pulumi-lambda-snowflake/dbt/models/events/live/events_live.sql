{{
    config(
        alias='events',
        materialized='view'
    )
-}}


{%- set threshold = get_events_threshold(ref('logs')) -%}


SELECT * FROM (
    {{
        select_events(
            from_table=ref('logs_staged')
        )
    }}
)

UNION

SELECT *
FROM {{ ref('events') }}
{% if threshold != False -%}
    WHERE TO_DATE(request_timestamp) < TO_DATE('{{ threshold }}')
{%- endif %}


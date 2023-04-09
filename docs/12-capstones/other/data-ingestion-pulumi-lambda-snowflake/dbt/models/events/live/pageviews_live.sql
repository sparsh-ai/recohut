{{
    config(
        alias='pageviews',
        materialized='view'
    )
-}}


{%- set threshold = get_events_threshold(ref('logs')) -%}


SELECT * FROM (
    {{
        select_pageviews(
            from_table=ref('logs_staged')
        )
    }}
)

UNION ALL

SELECT *
FROM {{ ref('pageviews') }}
{% if threshold != False -%}
    WHERE TO_DATE(request_timestamp) < TO_DATE('{{ threshold }}')
{%- endif %}

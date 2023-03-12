{{
    config(
        alias='logs',
        materialized='view'
    )
-}}


{%- set threshold = get_events_threshold(ref('logs')) -%}


SELECT *
FROM {{ ref('logs_staged') }}

UNION

SELECT *
FROM {{ ref('logs') }}
{% if threshold != False -%}
    WHERE TO_DATE(request_timestamp) < TO_DATE('{{ threshold }}')
{%- endif %}


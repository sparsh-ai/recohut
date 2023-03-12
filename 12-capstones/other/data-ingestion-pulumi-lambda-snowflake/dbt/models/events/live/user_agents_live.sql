{{
    config(
        alias='user_agents',
        materialized='view'
    )
-}}


{%- set threshold = get_events_threshold(ref('logs')) -%}


SELECT * FROM (
    {{
        select_user_agents(
            from_date=threshold,
            to_date=False,
        )
    }}
)

UNION ALL

SELECT *
FROM {{ ref('user_agents' )}}

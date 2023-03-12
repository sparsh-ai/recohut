{% macro select_events(from_table, materialized='view') -%}

    {{-
        config(
            alias='events',
            cluster_by=['TO_DATE(request_timestamp)', 'event_category', 'event_action'],
            materialized=materialized,
            unique_key='id'
        )
    -}}

    SELECT
          log_id AS id
        , NULLIF(TRIM(req_body:ec::STRING), '') AS event_category
        , NULLIF(TRIM(req_body:ea::STRING), '') AS event_action
        , NULLIF(TRIM(req_body:el::STRING), '') AS event_label
        , NULLIF(TRIM(req_body:ev::STRING), '') AS event_value
        , *
    FROM {{ from_table }}
    WHERE
            hit_type = 'event'
        AND NULLIF(TRIM(req_body:ec::STRING), '') IS NOT NULL

{%- endmacro %}

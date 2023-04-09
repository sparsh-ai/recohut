{% macro select_pageviews(from_table, materialized='view') -%}

    {{-
        config(
            alias='pageviews',
            cluster_by=['TO_DATE(request_timestamp)'],
            materialized=materialized,
            unique_key='id'
        )
    -}}

    SELECT
          log_id AS id
        , *
    FROM {{ from_table }}
    WHERE hit_type = 'pageview'

{%- endmacro %}

{% macro select_purchases(from_table, materialized='view') -%}

    {{-
        config(
            alias='purchases',
            cluster_by=['TO_DATE(request_timestamp)'],
            materialized=materialized,
            unique_key='id'
        )
    -}}

    SELECT
          log_id AS id
        , NULLIF(UPPER(TRIM(req_body:ti::STRING)), '') AS transaction_id
        , TRY_TO_DECIMAL(NULLIF(TRIM(req_body:tr::STRING), ''), 10, 4) AS transaction_revenue
        , TRY_TO_DECIMAL(NULLIF(TRIM(req_body:tr::STRING), ''), 10, 4) AS transaction_tax
        , TRY_TO_DECIMAL(NULLIF(TRIM(req_body:ts::STRING), ''), 10, 4) AS transaction_shipping
        , NULLIF(TRIM(req_body:ta::STRING), '') AS transaction_affiliation
        , NULLIF(TRIM(req_body:tcc::STRING), '') AS transaction_coupon_code
        , *
    FROM {{ from_table }}
    WHERE
            product_action = 'purchase'
        AND NULLIF(TRIM(req_body:ti::STRING), '') IS NOT NULL
    QUALIFY
        ROW_NUMBER() OVER (
            PARTITION BY transaction_id
            ORDER BY request_timestamp ASC
        ) = 1

{%- endmacro %}

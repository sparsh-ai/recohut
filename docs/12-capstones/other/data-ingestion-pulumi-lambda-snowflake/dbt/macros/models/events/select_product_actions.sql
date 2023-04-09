{% macro select_product_actions(from_table, materialized='view') -%}

    {{-
        config(
            alias='product_actions',
            cluster_by=['TO_DATE(request_timestamp)', 'product_action'],
            materialized=materialized,
            unique_key='id'
        )
    -}}

    SELECT
          CONCAT(log_id, '.', p.index) AS id
        , NULLIF(TRIM(UPPER(p.value:id::STRING)), '') AS product_id
        , NULLIF(TRIM(UPPER(p.value:variant::STRING)), '') AS product_variant
        , TRY_TO_NUMBER(p.value:position::STRING, 5, 0) AS product_position
        , TRY_TO_DECIMAL(p.value:quantity::STRING, 10, 4) AS product_quantity
        , TRY_TO_DECIMAL(p.value:price::STRING, 10, 4) AS product_price
        , NULLIF(TRIM(p.value:name::STRING), '') AS product_name
        , NULLIF(TRIM(p.value:brand::STRING), '') AS product_brand
        , NULLIF(TRIM(p.value:category::STRING), '') AS product_category
        , p.value:raw::VARIANT AS product_raw_data
        , NULLIF(LOWER(TRIM(l.req_body:pal::STRING)), '') AS product_action_list
        , NULLIF(UPPER(TRIM(l.req_body:cu::STRING)), '') AS currency_code
        , NULLIF(TRIM(l.req_body:ti::STRING), '') AS transaction_id
        , l.*
    FROM
          {{ from_table }} AS l
        , LATERAL FLATTEN(input => {{ target.schema }}.udf_collect_ec_products_map(l.req_body::variant)) AS p
    WHERE l.product_action IS NOT NULL

{%- endmacro %}

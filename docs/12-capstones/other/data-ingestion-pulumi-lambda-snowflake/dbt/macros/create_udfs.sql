{% macro create_udfs() -%}

    CREATE SCHEMA IF NOT EXISTS {{ target.schema }};

    {{ create_udf_collect_ec_products_map() }}
    {{ create_udf_ua_parser_js() }}

{%- endmacro %}

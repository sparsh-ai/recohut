{% macro select_user_agents(from_date=False, to_date=False, materialized='view') -%}

    {{-
        config(
            alias='user_agents',
            materialized=materialized,
            unique_key='id'
        )
    -}}

    WITH
        user_agents AS (
            SELECT DISTINCT
                COALESCE(
                    NULLIF(TRIM(data:request:body:ua::STRING), '')
                    , NULLIF(TRIM(GET_IGNORE_CASE(data:request:headers, 'user-agent')::STRING), '')
                    , NULLIF(TRIM(data:context:user_agent::STRING), '')
                ) AS user_agent
                , {{ get_user_agent_id('user_agent') }} AS id
            FROM {{ source('RAW', 'LOGS') }}
            WHERE
                    service_id = 'api.collect'
                {% if from_date != False -%}
                    AND TO_DATE(request_timestamp) > TO_DATE('{{ from_date }}')
                {%- endif %}
                {% if to_date != False -%}
                    AND TO_DATE(request_timestamp) <= TO_DATE('{{ to_date }}')
                {%- endif %}
        )

    SELECT
          ua.id
        , ua.user_agent AS user_agent
        , NULLIF(TRIM(data.value:browser:name::STRING), '') AS browser_name
        , NULLIF(TRIM(data.value:browser:version::STRING), '') AS browser_version
        , NULLIF(TRIM(data.value:browser:major::STRING), '') AS browser_major
        , NULLIF(TRIM(data.value:os:name::STRING), '') AS os_name
        , NULLIF(TRIM(data.value:os:version::STRING), '') AS os_version
        , NULLIF(TRIM(data.value:device:type::STRING), '') AS device_type
        , NULLIF(TRIM(data.value:device:model::STRING), '') AS device_model
        , NULLIF(TRIM(data.value:device:vendor::STRING), '') AS device_vendor
        , NULLIF(TRIM(data.value:cpu:architecture::STRING), '') AS cpu_architecture
        , NULLIF(TRIM(data.value:engine:name::STRING), '') AS engine_name
        , NULLIF(TRIM(data.value:engine:version::STRING), '') AS engine_version
    FROM
          user_agents AS ua
        , LATERAL FLATTEN(input => ARRAY_CONSTRUCT({{ target.schema }}.udf_ua_parser_js(ua.user_agent))) AS data
    WHERE
        user_agent IS NOT NULL
        {% if is_incremental() -%}
        AND (
            SELECT COUNT(s.id)
            FROM {{ this }} AS s
            WHERE s.id = ua.id
        ) = 0
        {%- endif %}

{%- endmacro %}

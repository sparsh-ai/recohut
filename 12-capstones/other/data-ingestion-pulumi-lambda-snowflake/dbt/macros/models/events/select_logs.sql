{% macro select_logs(from_date=False, to_date=False, alias='logs', materialized='view') -%}

    {{-
        config(
            alias=alias,
            cluster_by=['TO_DATE(request_timestamp)'],
            materialized=materialized,
            unique_key='log_id'
        )
    -}}

    WITH
          all_events AS (
            -- Using all the most recent "first seen" purchase events
            SELECT n.*
            FROM {{ source('RAW', 'LOGS') }} AS n
            WHERE
                    n.service_id = 'api.collect'
                AND NULLIF(LOWER(n.data:request:body:t::STRING), '') IS NOT NULL
                {% if from_date != False -%}
                    AND n.request_timestamp >= TO_TIMESTAMP_NTZ('{{ from_date }}')
                {%- endif %}
                {% if to_date != False -%}
                    AND n.request_timestamp < TO_TIMESTAMP_NTZ('{{ to_date }}')
                {%- endif %}
                --
                AND NULLIF(TRIM(LOWER(n.data:request:body:pa::STRING)), '') = 'purchase'
                AND NULLIF(TRIM(n.data:request:body:ti::STRING), '') IS NOT NULL
            QUALIFY
                ROW_NUMBER() OVER (
                    PARTITION BY UPPER(TRIM(n.data:request:body:ti::STRING))
                    ORDER BY n.request_timestamp ASC
                ) = 1

            UNION ALL

            -- Using all the other most recent events
            SELECT n.*
            FROM {{ source('RAW', 'LOGS') }} AS n
            WHERE
                    n.service_id = 'api.collect'
                AND NULLIF(LOWER(n.data:request:body:t::STRING), '') IS NOT NULL
                {% if from_date != False -%}
                    AND n.request_timestamp >= TO_TIMESTAMP_NTZ('{{ from_date }}')
                {%- endif %}
                {% if to_date != False -%}
                    AND n.request_timestamp < TO_TIMESTAMP_NTZ('{{ to_date }}')
                {%- endif %}
                --
                AND (
                        NULLIF(TRIM(LOWER(n.data:request:body:pa::STRING)), '') IS NULL
                    OR NULLIF(TRIM(LOWER(n.data:request:body:pa::STRING)), '') != 'purchase'
                )
        )

        , time_lag_sessions AS (
            SELECT
                  *
                , DATE_PART('EPOCH_MILLISECOND', request_timestamp) - LAG(DATE_PART('EPOCH_MILLISECOND', request_timestamp)) OVER (
                    PARTITION BY DATE(request_timestamp), client_id
                    ORDER BY request_timestamp
                ) AS time_lag
            FROM all_events
        )

        , session_history AS (
            SELECT
                  *
                , CASE
                    WHEN (time_lag IS NULL OR time_lag >= 30 * 60 * 1000) THEN
                        UUID_STRING(UUID_STRING('1ff91478-1da1-431f-b1fd-3ec39fff283c', client_id), request_id)
                    ELSE NULL
                END AS new_session_id
            FROM time_lag_sessions
        )

        , partitioned_history AS (
            SELECT
                  *
                , SUM(
                    CASE
                        WHEN new_session_id IS NULL THEN 0
                        ELSE 1
                    END
                ) OVER (
                    PARTITION BY DATE(request_timestamp), client_id
                    ORDER BY request_timestamp
                ) AS value_partition
            FROM session_history
        )

        , sessionized_events AS (
            SELECT
                  *
                , FIRST_VALUE(new_session_id) OVER (
                    PARTITION BY TO_DATE(request_timestamp), client_id, value_partition
                    ORDER BY request_timestamp
                ) AS session_id
            FROM partitioned_history
        )

    SELECT
          request_timestamp
        , request_id

        , session_id

        , LOWER(
            COALESCE(
                  NULLIF(TRIM(data:request:body:cid::STRING), '')
                , NULLIF(TRIM(data:context:client_id::STRING), '')
            )
        ) AS client_id

        , LOWER(
            COALESCE(
                  NULLIF(TRIM(data:request:body:uid::STRING), '')
                , NULLIF(TRIM(data:context:user_id::STRING), '')
            )
        ) AS user_id
        , ARRAY_AGG(DISTINCT user_id) OVER (
            PARTITION BY TO_DATE(request_timestamp), session_id
        ) AS session_based_user_ids

        , LOWER(
            COALESCE(
                  NULLIF(TRIM(data:request:body:uip::STRING), '')
                , NULLIF(TRIM(data:context:user_ip::STRING), '')
            )
        ) AS user_ip
        , ARRAY_AGG(DISTINCT user_ip) OVER (
            PARTITION BY TO_DATE(request_timestamp), session_id
        ) AS session_based_user_ips

        , TRIM(LOWER(data:request:body:t::STRING)) AS hit_type
        , NULLIF(TRIM(LOWER(data:request:body:pa::STRING)), '') AS product_action
        , LOWER(
            COALESCE(
                  NULLIF(TRIM(data:request:body:dl::STRING), '')
                , NULLIF(TRIM(GET_IGNORE_CASE(data:request:headers, 'referer')::STRING), '')
                , NULLIF(TRIM(data:context:document_location::STRING), '')
            )
        ) AS document_location
        , LOWER(
            COALESCE(
                  NULLIF(TRIM(data:request:body:dr::STRING), '')
                , NULLIF(TRIM(data:context:document_referrer::STRING), '')
            )
        ) AS document_referrer

        {% set user_id_query -%}
            COALESCE(
                  NULLIF(TRIM(data:request:body:ua::STRING), '')
                , NULLIF(TRIM(GET_IGNORE_CASE(data:request:headers, 'user-agent')::STRING), '')
                , NULLIF(TRIM(data:context:user_agent::STRING), '')
            )
        {%- endset %}
        , {{ get_user_agent_id(user_id_query) }} AS user_agent_id

        , NULLIF(TRIM(data:request:body:dt::STRING), '') AS document_title
        , NULLIF(TRIM(LOWER(data:request:body:sr::STRING)), '') AS screen_resolution
        , NULLIF(TRIM(UPPER(data:request:body:de::STRING)), '') AS document_encoding
        , NULLIF(TRIM(LOWER(data:request:body:sd::STRING)), '') AS screen_colors
        , NULLIF(TRIM(UPPER(data:request:body:ul::STRING)), '') AS user_language

        , data:request:body::VARIANT AS req_body
        , log_id
        , SYSDATE()::TIMESTAMP_NTZ AS created_at
    FROM sessionized_events AS e

{%- endmacro %}

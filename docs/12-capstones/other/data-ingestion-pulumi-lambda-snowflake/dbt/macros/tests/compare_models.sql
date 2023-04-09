{% test compare_models(model, column, with_model, with_column, date_agg) -%}

    WITH
        source AS (
            SELECT DISTINCT
                {{ date_agg }} AS period
                , SUM({{ column }}) AS value
            FROM {{ model }}
            GROUP BY {{ date_agg }}
        )
        , target AS (
            SELECT DISTINCT
                {{ date_agg }} AS period
                , SUM({{ with_column }}) AS value
            FROM {{ with_model }}
            GROUP BY {{ date_agg }}
        )

    SELECT *
    FROM source AS s
    INNER JOIN target AS t ON
        t.period = s.period
    WHERE
        s.value != t.value

{%- endtest %}

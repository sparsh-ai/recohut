{% macro get_events_threshold(from) -%}
    {%- set threshold_query -%}
        SELECT TO_DATE(MAX(request_timestamp))
        FROM {{ from }}
    {%- endset -%}
    {%- set results = run_query(threshold_query) -%}

    {%- if execute -%}
        {{- return(results[0][0]) -}}
    {%- else -%}
        {{- return(False) -}}
    {%- endif -%}
{%- endmacro %}

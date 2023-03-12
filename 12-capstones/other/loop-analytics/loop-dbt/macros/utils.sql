{% macro floatify(field) %}
replace(replace(NULLIF({{field}}, ''),',', ''), '$', '')::float
{% endmacro %}

{% macro intify(field) %}
SPLIT_PART(replace(replace(NULLIF({{field}}, ''),',', ''), '$', ''), '.', 1)::int as {{field}}
{% endmacro %}

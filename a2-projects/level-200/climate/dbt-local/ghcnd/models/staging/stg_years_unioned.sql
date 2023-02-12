{{ config(materialized='view') }}


{% for year in range( var('start_year'), var('end_year')+1 )     %}
    {{ process_year_table( year ) }}
    {{ 'union all' if not loop.last }}
{% endfor %}

{% if var('is_test_run', default=true) %}
    limit 500
{% endif %}
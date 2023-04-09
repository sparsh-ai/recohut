{# RUN COMMAND: dbt run-operation macro_hello_world_1 #}
{% macro macro_hello_world_1() %}

    {{ log('Congrats on running your 1st macro in dbt', True) }}

{% endmacro %}


{# RUN COMMAND: dbt run-operation macro_hello_world_2 #}
{% macro macro_hello_world_2() %}

    {{ log('Congrats on running your 2nd macro in dbt', True) }}

    {% set external_var = False %}

    {{ log('external_var before loop: ' ~ external_var, True) }}

    {% for i in [1]%}
        {% set external_var = True %}
        {{ log('external_var within loop: ' ~ external_var, True) }}
    {% endfor %}

    {{ log('external_var after  loop: ' ~ external_var, True) }}

{% endmacro %}


{# RUN COMMAND: dbt run-operation macro_hello_world_3 #}
{% macro macro_hello_world_3() %}

    {{ log('Congrats on running your 3rd macro in dbt', True) }}

    {% set ns = namespace() %}

    {% set ns.namespace_var = False %}

    {{ log('namespace_var before loop: ' ~ ns.namespace_var, True) }}

    {% for i in [1]%}
        {% set ns.namespace_var = True %}
        {{ log('namespace_var within loop: ' ~ ns.namespace_var, True) }}
    {% endfor %}

    {{ log('namespace_var after  loop: ' ~ ns.namespace_var, True) }}

{% endmacro %}


{# RUN COMMAND: dbt run-operation macro_hello_world_4 #}
{% macro macro_hello_world_4() %}

    {{ log('Congrats on running your 4th macro in dbt', True) }}

    {% for i in [1, 2, 3]%}
        {% if i == 1 %}
            {{ log('if   i == 1, A', True) }}
        {% elif i == 2 %}
            {{ log('elif i == 2, B', True) }}
        {% else %}
            {{ log('else i == 3, C', True) }}
        {% endif %}
    {% endfor %}

{% endmacro %}


{# RUN COMMAND: dbt run-operation macro_hello_world_5 #}
{% macro macro_hello_world_5() %}

    {{ log('Congrats on running your 5th macro in dbt', True) }}

    {% set test_sql %}
        select 'row_1_col_1' as col_1, 'row_1_col_2' as col_2 union select 'row_2_col_1' as col_1, 'row_2_col_2' as col_2;
    {% endset %}

    {% set results = run_query(test_sql) %}

    {% if execute %}
        {% for row in results.rows %}
            {{ log('Query record: ' ~ row.col_1 ~ ' ' ~ row.col_2, True) }}
        {% endfor %}
    {% endif %}

{% endmacro %}


{# RUN COMMAND: dbt run-operation macro_hello_world_6 --args "{input: 'ABC'}" #}
{% macro macro_hello_world_6(input) %}

    {{ log('Congrats on running your 6th macro in dbt', True) }}

    {{ log('Input parameter value: ' ~ input, True) }}

{% endmacro %}


{# RUN COMMAND: dbt run-operation macro_hello_world_7 #}
{% macro macro_hello_world_7(input) %}

    {{ log('Congrats on running your 7th macro in dbt', True) }}

    {% set dict_var = {'key_1': 'val_1', 'key_2': 'val_2'} %}

    {% for key in dict_var.keys() %}
        {{ log('dict_var key and value: ' ~ key ~ ' ' ~ dict_var[key], True) }}
    {% endfor %}

{% endmacro %}


{# RUN COMMAND: dbt run-operation macro_hello_world_8 #}
{% macro macro_hello_world_8() %}

    {{ log('Congrats on running your 8th macro in dbt', True) }}

    {% set target_dict = target %}

    {% for key in target_dict %}
        {{ log('Key:Value ' ~ key ~ ':' ~ target_dict[key], True) }}
    {% endfor %}

{% endmacro %}

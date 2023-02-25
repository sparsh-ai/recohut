{% macro macro_manage_users() %}

    {% set ns = namespace() %}

    {% set sql_existing_users %}
        select usename from pg_user;
    {% endset %}

    {% set results = run_query(sql_existing_users) %}

    {% set ns.existing_users = [] %}

    {% if execute %}
        {% for row in results.rows %}
            {% set ns.existing_users = ns.existing_users + [row.usename] %}
        {% endfor %}
    {% endif %}

    {% set ns.create_ind = false %}

    {% set sql %}
        {% for user in var('dbt_managed_users') %}
            {% if user in ns.existing_users %}
                {{ log('Existing user: ' ~ user, True) }}
            {% elif user == 'do_not_create_user' %}
                {{ log('Skipping user (for demo purpose): ' ~ user, True) }}
            {% else %}
                {% set ns.create_ind = True %}

                {{ log('Creating user: ' ~ user, True) }}
                create user {{ user }} password '{{ var('new_user_default_pwd') }}';
            {% endif %}
        {% endfor %}
    {% endset %}

    {% if ns.create_ind %}
        {% if execute %}
            {% do run_query(sql) %}
        {% endif %}
    {% endif %}

{% endmacro %}


{% macro macro_manage_users_grants(schema_list) %}

    {% set ns = namespace() %}

    {{ log('##################################################', True) }}
    {{ log('Impacted schema(s)       : ' ~ ', '.join(schema_list), True) }}

    {% set sql_existing_users %}
        select usename from pg_user;
    {% endset %}

    {% set results = run_query(sql_existing_users) %}

    {% set ns.existing_users = [] %}

    {% if execute %}
        {% for row in results.rows %}
            {% set ns.existing_users = ns.existing_users + [row.usename] %}
        {% endfor %}
    {% endif %}

    {% set sql_existing_schemas %}
        select schema_name from svv_all_schemas;
    {% endset %}

    {% set results = run_query(sql_existing_schemas) %}

    {% set ns.existing_schemas = [] %}

    {% if execute %}
        {% for row in results.rows %}
            {% set ns.existing_schemas = ns.existing_schemas + [row.schema_name] %}
        {% endfor %}
    {% endif %}

    {% set ns.create_ind = false %}

    {% set grant_dict = var('dbt_managed_grants') %}

    {% set sql %}
        {% for schema in schema_list %}
            {{ log('##################################################', True) }}

            {% if schema in grant_dict.keys() %}
                {% if schema in ns.existing_schemas %}
                    {% set grant_user_list = grant_dict[schema] %}

                    {% set unmatched_list = grant_user_list | reject('in', ns.existing_users) | list %}
                    {% set matched_list = grant_user_list | reject('in', unmatched_list) | list %}

                    {{ log('Schema                   : ' ~ schema, True) }}
                    {{ log('Grant user(s)            : ' ~ ', '.join(grant_user_list), True) }}
                    {{ log('User missing (skip grant): ' ~ ', '.join(unmatched_list), True) }}
                    {{ log('User found   (exec grant): ' ~ ', '.join(matched_list), True) }}

                    {% if matched_list|length %}
                        {% set ns.create_ind = True %}

                        grant usage on schema {{ schema }} to {{ ', '.join(matched_list) }};
                        grant select on all tables in schema {{ schema }} to {{ ', '.join(matched_list) }};
                    {% endif %}
                {% else %}
                    {{ log('Schema                   : ' ~ schema ~ ' (missing or not visible to ' ~ target.user ~ ')', True) }}  
                {% endif %}
            {% else %}
                {{ log('Schema                   : ' ~ schema ~ ' (grants unconfigured)', True) }}
            {% endif %}
        {% endfor %}
    {% endset %}

    {% if ns.create_ind %}
        {% if execute %}
            {% do run_query(sql) %}
        {% endif %}
    {% endif %}

{% endmacro %}

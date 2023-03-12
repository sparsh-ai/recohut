{% macro get_user_agent_id(query) -%}
    UUID_STRING('2ee51068-335c-4fcf-b58b-313c0d715c07', LOWER({{ query }}))::CHAR(36)
{%- endmacro %}

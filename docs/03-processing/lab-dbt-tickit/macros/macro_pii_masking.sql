{% macro macro_pii_masking_text(field) %}
    case
        when lower(current_user) in ('unmasked_user') then {{ field }}
        when {{ field }} is null then null
        else 'MASKED'
    end
{% endmacro %}


{% macro macro_pii_masking_numeric(field) %}
    case
        when lower(current_user) in ('unmasked_user') then {{ field }}
        when {{ field }} is null then null
        else 9999
    end
{% endmacro %}

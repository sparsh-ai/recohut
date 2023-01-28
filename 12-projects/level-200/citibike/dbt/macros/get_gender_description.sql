{#
    Returns the gender description
#}

{% macro get_gender_description(gender_code) -%}

    case {{ gender_code }}
        when 0 then 'Unknown'
        when 1 then 'Male'
        when 2 then 'Female'
    end

{%- endmacro %}
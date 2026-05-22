{% macro limpiar_codigo_postal(columna) %}
    case
        when trim({{ columna }}::varchar) = '9999999' then null
        when regexp_full_match(lpad(trim({{ columna }}::varchar), 5, '0'), '\d{5}')
            then lpad(trim({{ columna }}::varchar), 5, '0')
        else null
    end
{% endmacro %}

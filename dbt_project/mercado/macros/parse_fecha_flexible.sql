{% macro parse_fecha_flexible(columna) %}
    try_strptime({{ columna }}, ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S', '%Y/%m/%d', '%d-%m-%Y', '%d/%m/%Y', '%d %b %Y'])::date
{% endmacro %}

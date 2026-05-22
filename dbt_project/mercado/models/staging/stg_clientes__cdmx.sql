with fuente as (
    select
        cliente_id,
        nombre,
        apellido_paterno_materno,
        email,
        genero,
        fecha_registro,
        estado,
        telefono,
        codigo_postal,
        activo_flag,
        "alcaldía_municipio"
    from {{ source('raw', 'clientes_cdmx') }}
),

transformado as (
    select
        trim(cliente_id) as cliente_id,
        trim(nombre) || ' ' || trim(apellido_paterno_materno) as nombre_completo,
        nullif(trim(email), '') as email,
        trim(genero) as genero,
        {{ parse_fecha_flexible('fecha_registro') }} as fecha_registro,
        trim(estado) as estado,
        trim(telefono) as telefono,
        {{ limpiar_codigo_postal('codigo_postal') }} as codigo_postal,
        trim(activo_flag) = '1' as activo_flag,
        trim("alcaldía_municipio") as alcaldia_municipio,
        'CDMX' as region
    from fuente
),

final as (
    select
        cliente_id,
        nombre_completo,
        email,
        genero,
        fecha_registro,
        estado,
        telefono,
        codigo_postal,
        activo_flag,
        alcaldia_municipio,
        region
    from transformado
)

select
    cliente_id,
    nombre_completo,
    email,
    genero,
    fecha_registro,
    estado,
    telefono,
    codigo_postal,
    activo_flag,
    alcaldia_municipio,
    region
from final

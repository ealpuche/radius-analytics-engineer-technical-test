with fuente as (
    select
        cliente_id,
        nombre_completo,
        email,
        genero,
        fecha_registro,
        estado,
        telefono,
        codigo_postal,
        activo_flag
    from {{ source('raw', 'clientes_resto') }}
),

transformado as (
    select
        trim(cliente_id) as cliente_id,
        trim(nombre_completo) as nombre_completo,
        nullif(trim(email), '') as email,
        trim(genero) as genero,
        to_timestamp(fecha_registro::bigint)::date as fecha_registro,
        trim(estado) as estado,
        trim(telefono) as telefono,
        {{ limpiar_codigo_postal('codigo_postal') }} as codigo_postal,
        activo_flag::double = 1.0 as activo_flag,
        cast(null as varchar) as alcaldia_municipio,
        'RESTO' as region
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

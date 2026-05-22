with fuente as (
    select
        customer_id,
        first_name,
        last_name,
        email_address,
        gender,
        registration_date,
        state,
        phone,
        zip_code,
        is_active
    from {{ source('raw', 'clientes_gdl_mty') }}
),

transformado as (
    select
        trim(customer_id) as cliente_id,
        trim(first_name) || ' ' || trim(last_name) as nombre_completo,
        nullif(trim(email_address), '') as email,
        trim(gender) as genero,
        {{ parse_fecha_flexible('registration_date') }} as fecha_registro,
        trim(state) as estado,
        trim(phone) as telefono,
        {{ limpiar_codigo_postal('zip_code') }} as codigo_postal,
        lower(trim(is_active)) = 'true' as activo_flag,
        cast(null as varchar) as alcaldia_municipio,
        'GDL_MTY' as region
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

with fuente as (
    select
        devolucion_id,
        order_id,
        fecha_solicitud,
        razon_devolucion,
        dias_para_devolucion,
        monto_reembolso,
        estatus_devolucion,
        motivo_adicional
    from {{ source('raw', 'devoluciones') }}
),

transformado as (
    select
        trim(devolucion_id) as devolucion_id,
        trim(order_id) as order_id,
        {{ parse_fecha_flexible('fecha_solicitud') }} as fecha_solicitud,
        trim(razon_devolucion) as razon_devolucion,
        try_cast(regexp_extract(dias_para_devolucion, '\d+') as integer) as dias_para_devolucion,
        monto_reembolso::decimal(12, 2) as monto_reembolso,
        upper(trim(estatus_devolucion)) as estatus_devolucion,
        nullif(trim(motivo_adicional), '') as motivo_adicional
    from fuente
),

final as (
    select
        devolucion_id,
        order_id,
        fecha_solicitud,
        razon_devolucion,
        dias_para_devolucion,
        monto_reembolso,
        estatus_devolucion,
        motivo_adicional
    from transformado
)

select
    devolucion_id,
    order_id,
    fecha_solicitud,
    razon_devolucion,
    dias_para_devolucion,
    monto_reembolso,
    estatus_devolucion,
    motivo_adicional
from final

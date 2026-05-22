with fuente as (
    select
        order_id,
        id_cliente,
        sku_producto,
        canal_estatus,
        fecha_orden,
        monto_total,
        cantidad,
        direccion_entrega,
        fecha_actualizacion
    from {{ source('raw', 'ordenes_2022_2023') }}
),

transformado as (
    select
        trim(order_id) as orden_id,
        trim(id_cliente) as cliente_id,
        trim(sku_producto) as sku_producto,
        trim(split_part(canal_estatus, '|', 1)) as canal_raw,
        trim(split_part(canal_estatus, '|', 2)) as estatus_pago_raw,
        {{ parse_fecha_flexible('fecha_orden') }} as fecha_orden,
        try_cast(trim(monto_total) as decimal(12, 2)) as monto_total,
        cantidad::integer as cantidad,
        trim(direccion_entrega) as direccion_entrega,
        cast(null as decimal(12, 2)) as descuento_aplicado,
        {{ parse_fecha_flexible('fecha_actualizacion') }} as fecha_actualizacion,
        '2022_2023' as anio_esquema
    from fuente
),

final as (
    select
        orden_id,
        cliente_id,
        sku_producto,
        canal_raw,
        estatus_pago_raw,
        fecha_orden,
        monto_total,
        cantidad,
        direccion_entrega,
        descuento_aplicado,
        fecha_actualizacion,
        anio_esquema
    from transformado
)

select
    orden_id,
    cliente_id,
    sku_producto,
    canal_raw,
    estatus_pago_raw,
    fecha_orden,
    monto_total,
    cantidad,
    direccion_entrega,
    descuento_aplicado,
    fecha_actualizacion,
    anio_esquema
from final

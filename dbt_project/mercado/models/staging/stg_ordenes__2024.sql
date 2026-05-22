with fuente as (
    select
        orden_id,
        cliente_id,
        producto_sku,
        canal_venta,
        estatus_pago,
        fecha_compra,
        monto,
        cantidad_unidades,
        domicilio_entrega,
        descuento_aplicado,
        fecha_modificacion
    from {{ source('raw', 'ordenes_2024') }}
),

transformado as (
    select
        trim(orden_id) as orden_id,
        trim(cliente_id) as cliente_id,
        trim(producto_sku) as sku_producto,
        trim(canal_venta) as canal_raw,
        trim(estatus_pago) as estatus_pago_raw,
        {{ parse_fecha_flexible('fecha_compra') }} as fecha_orden,
        try_cast(trim(monto) as decimal(12, 2)) as monto_total,
        cantidad_unidades::integer as cantidad,
        trim(domicilio_entrega) as direccion_entrega,
        descuento_aplicado::decimal(12, 2) as descuento_aplicado,
        {{ parse_fecha_flexible('fecha_modificacion') }} as fecha_actualizacion,
        '2024' as anio_esquema
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

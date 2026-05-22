with fuente as (
    select
        sku,
        nombre_producto,
        categoria_subcategoria,
        precio_lista,
        peso,
        proveedor,
        descripcion,
        stock_disponible,
        fecha_alta,
        activo
    from {{ source('raw', 'catalogo_productos') }}
),

transformado as (
    select
        trim(sku) as sku,
        trim(nombre_producto) as nombre_producto,
        trim(categoria_subcategoria) as categoria_subcategoria,
        try_cast(
            replace(replace(replace(precio_lista, '$', ''), ',', ''), ' ', '') as decimal(12, 2)
        ) as precio_lista,
        try_cast(regexp_replace(peso, '[^0-9.]', '', 'g') as decimal(10, 2)) as peso_kg,
        trim(proveedor) as proveedor,
        nullif(trim(descripcion), '') as descripcion,
        try_cast(stock_disponible as integer) as stock_disponible,
        {{ parse_fecha_flexible('fecha_alta') }} as fecha_alta,
        trim(activo) = '1' as activo
    from fuente
),

final as (
    select
        sku,
        nombre_producto,
        categoria_subcategoria,
        precio_lista,
        peso_kg,
        proveedor,
        descripcion,
        stock_disponible,
        fecha_alta,
        activo
    from transformado
)

select
    sku,
    nombre_producto,
    categoria_subcategoria,
    precio_lista,
    peso_kg,
    proveedor,
    descripcion,
    stock_disponible,
    fecha_alta,
    activo
from final

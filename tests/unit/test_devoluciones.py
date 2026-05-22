"""Tests de contrato para mercado.cleaners.devoluciones."""

from __future__ import annotations

from mercado.cleaners.devoluciones import clasificar_razon_devolucion

PATRONES_EJEMPLO: dict[str, list[str]] = {
    'DEFECTO': [r'defect', r'roto', r'dañado'],
    'TALLA': [r'talla', r'tamaño'],
}


def test_clasificar_razon_coincide_categoria_happy_path():
    """Primera categoría que coincide gana."""
    assert clasificar_razon_devolucion('Producto defectuoso', PATRONES_EJEMPLO) == 'DEFECTO'


def test_clasificar_razon_case_insensitive_edge_case():
    """La coincidencia es insensible a mayúsculas."""
    assert clasificar_razon_devolucion('TALLA INCORRECTA', PATRONES_EJEMPLO) == 'TALLA'


def test_clasificar_razon_sin_coincidencia_retorna_otro():
    """Sin match retorna OTRO."""
    assert clasificar_razon_devolucion('motivo desconocido', PATRONES_EJEMPLO) == 'OTRO'


def test_clasificar_razon_none_invalido():
    """None retorna OTRO."""
    assert clasificar_razon_devolucion(None, PATRONES_EJEMPLO) == 'OTRO'


def test_clasificar_razon_vacio_invalido():
    """Cadena vacía retorna OTRO."""
    assert clasificar_razon_devolucion('', PATRONES_EJEMPLO) == 'OTRO'


def test_clasificar_razon_primer_match_gana_edge_case():
    """Si varias categorías podrían coincidir, gana la primera en el dict."""
    patrones = {
        'A': [r'problema'],
        'B': [r'problema'],
    }
    assert clasificar_razon_devolucion('tengo un problema', patrones) == 'A'

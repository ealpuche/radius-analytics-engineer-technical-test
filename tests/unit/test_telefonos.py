"""Tests de contrato para mercado.cleaners.telefonos."""

from __future__ import annotations

from mercado.cleaners.telefonos import extraer_telefono


def test_extraer_telefono_con_extension_happy_path():
    """Número con extensión retorna dígitos y extensión separados."""
    assert extraer_telefono('81-3801-8090 ext. 3033') == ('8138018090', '3033')


def test_extraer_telefono_sin_extension_edge_case():
    """Número sin extensión retorna extensión None."""
    assert extraer_telefono('55-1234-5678') == ('5512345678', None)


def test_extraer_telefono_none_invalido():
    """None retorna (None, None)."""
    assert extraer_telefono(None) == (None, None)


def test_extraer_telefono_vacio_invalido():
    """Cadena vacía retorna (None, None)."""
    assert extraer_telefono('') == (None, None)


def test_extraer_telefono_sin_digitos_invalido():
    """Texto sin dígitos retorna (None, None)."""
    assert extraer_telefono('sin telefono') == (None, None)

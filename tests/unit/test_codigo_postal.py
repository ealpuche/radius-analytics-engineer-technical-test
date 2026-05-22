"""Tests de contrato para mercado.normalizers.codigo_postal."""

from __future__ import annotations

from mercado.normalizers.codigo_postal import parse_codigo_postal


def test_parse_codigo_postal_entero_corto_happy_path():
    """Entero corto se rellena a 5 dígitos."""
    assert parse_codigo_postal(6500) == '06500'


def test_parse_codigo_postal_cadena_valida_edge_case():
    """Cadena de 5 dígitos se retorna tal cual."""
    assert parse_codigo_postal('64000') == '64000'


def test_parse_codigo_postal_sentinel_invalido():
    """Sentinel 9999999 retorna None."""
    assert parse_codigo_postal('9999999') is None
    assert parse_codigo_postal(9999999) is None


def test_parse_codigo_postal_abc_invalido():
    """Texto no numérico retorna None."""
    assert parse_codigo_postal('abc') is None


def test_parse_codigo_postal_none_invalido():
    """None retorna None."""
    assert parse_codigo_postal(None) is None


def test_parse_codigo_postal_vacio_invalido():
    """Cadena vacía retorna None."""
    assert parse_codigo_postal('') is None


def test_parse_codigo_postal_mas_de_cinco_digitos_invalido():
    """Más de 5 dígitos (no sentinel) retorna None."""
    assert parse_codigo_postal('123456') is None

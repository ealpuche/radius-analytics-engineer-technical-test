"""Tests de contrato para mercado.normalizers.montos."""

from __future__ import annotations

from mercado.normalizers.montos import parse_peso, parse_precio


# ── parse_precio ──────────────────────────────────────────────────────────────


def test_parse_precio_formato_moneda_happy_path():
    """Precio con símbolo y separadores de miles se parsea."""
    assert parse_precio('$ 15,255.49') == 15255.49


def test_parse_precio_sin_simbolo_edge_case():
    """Precio numérico simple se parsea."""
    assert parse_precio('1250.50') == 1250.5


def test_parse_precio_invalido_retorna_none():
    """Texto no numérico retorna None."""
    assert parse_precio('no es precio') is None


def test_parse_precio_none_invalido():
    """None retorna None."""
    assert parse_precio(None) is None


def test_parse_precio_vacio_invalido():
    """Cadena vacía retorna None."""
    assert parse_precio('') is None


# ── parse_peso ────────────────────────────────────────────────────────────────


def test_parse_peso_con_unidad_happy_path():
    """Peso con unidad kg se parsea."""
    assert parse_peso('2.35 kg') == 2.35


def test_parse_peso_sin_unidad_edge_case():
    """Peso numérico sin unidad se parsea."""
    assert parse_peso('10.5') == 10.5


def test_parse_peso_invalido_retorna_none():
    """Texto no numérico retorna None."""
    assert parse_peso('pesado') is None


def test_parse_peso_none_invalido():
    """None retorna None."""
    assert parse_peso(None) is None


def test_parse_peso_vacio_invalido():
    """Cadena vacía retorna None."""
    assert parse_peso('') is None

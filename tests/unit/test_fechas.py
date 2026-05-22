"""Tests de contrato para mercado.cleaners.fechas."""

from __future__ import annotations

from datetime import date

from mercado.cleaners.fechas import parse_fecha_multiformato


def test_parse_fecha_iso_happy_path():
    """Formato YYYY-MM-DD se parsea correctamente."""
    assert parse_fecha_multiformato('2023-05-14') == date(2023, 5, 14)


def test_parse_fecha_dd_mm_yyyy_edge_case():
    """Formato DD/MM/YYYY se parsea correctamente."""
    assert parse_fecha_multiformato('14/05/2023') == date(2023, 5, 14)


def test_parse_fecha_texto_invalido_retorna_none():
    """Texto no parseable retorna None sin excepción."""
    assert parse_fecha_multiformato('basura') is None


def test_parse_fecha_none_invalido():
    """None retorna None."""
    assert parse_fecha_multiformato(None) is None


def test_parse_fecha_vacio_invalido():
    """Cadena vacía retorna None."""
    assert parse_fecha_multiformato('') is None


def test_parse_fecha_yyyy_mm_dd_slash_edge_case():
    """Formato YYYY/MM/DD se parsea correctamente."""
    assert parse_fecha_multiformato('2023/05/14') == date(2023, 5, 14)


def test_parse_fecha_dd_mm_yyyy_guion_edge_case():
    """Formato DD-MM-YYYY se parsea correctamente."""
    assert parse_fecha_multiformato('14-05-2023') == date(2023, 5, 14)

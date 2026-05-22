"""Tests de contrato para mercado.normalizers.sku."""

from __future__ import annotations

from mercado.normalizers.sku import normalizar_sku


def test_normalizar_sku_guion_bajo_happy_path():
    """sku_NNNN se normaliza a SKU-NNNNN con padding."""
    assert normalizar_sku('sku_3740') == 'SKU-03740'


def test_normalizar_sku_prod_prefijo_edge_case():
    """PROD-NNNNN se normaliza a SKU-NNNNN."""
    assert normalizar_sku('PROD-12345') == 'SKU-12345'


def test_normalizar_sku_vacio_invalido():
    """Cadena vacía retorna None."""
    assert normalizar_sku('') is None


def test_normalizar_sku_none_invalido():
    """None retorna None."""
    assert normalizar_sku(None) is None


def test_normalizar_sku_guion_happy_path():
    """SKU-NNNNN ya canónico se mantiene."""
    assert normalizar_sku('SKU-12345') == 'SKU-12345'


def test_normalizar_sku_solo_digitos_edge_case():
    """Cadena solo numérica se normaliza con padding."""
    assert normalizar_sku('03740') == 'SKU-03740'


def test_normalizar_sku_prefijo_p_edge_case():
    """P-NNNNN se normaliza a SKU-NNNNN."""
    assert normalizar_sku('P-12345') == 'SKU-12345'


def test_normalizar_sku_texto_invalido():
    """Texto sin núcleo numérico retorna None."""
    assert normalizar_sku('sin-sku') is None

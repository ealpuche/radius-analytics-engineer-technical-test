"""Utilidades puras para parseo de precios y pesos."""

from __future__ import annotations

import logging
import re

logger = logging.getLogger(__name__)

_PATRON_NUMERO = re.compile(r'-?\d+(?:\.\d+)?')


def parse_precio(valor: str | None) -> float | None:
    """Parsea un precio con símbolo de moneda y separadores de miles.

    Args:
        valor: Cadena como ``'$ 15,255.49'`` o ``None``.

    Returns:
        Valor numérico en float o ``None`` si no es parseable.
    """
    if valor is None:
        return None

    texto = valor.strip()
    if not texto:
        return None

    texto_limpio = re.sub(r'[$\s]', '', texto)
    texto_limpio = texto_limpio.replace(',', '')

    match = _PATRON_NUMERO.search(texto_limpio)
    if not match:
        logger.debug('Precio no parseable: %r', valor)
        return None

    try:
        return float(match.group())
    except ValueError:
        logger.debug('Precio no parseable: %r', valor)
        return None


def parse_peso(valor: str | None) -> float | None:
    """Parsea un peso con unidad opcional (kg, g, etc.).

    Args:
        valor: Cadena como ``'2.35 kg'`` o ``None``.

    Returns:
        Valor numérico en float o ``None`` si no es parseable.
    """
    if valor is None:
        return None

    texto = valor.strip()
    if not texto:
        return None

    texto_limpio = re.sub(
        r'\s*(?:kg|kilogramos?|g|gramos?|lb|lbs|libras?)\s*$',
        '',
        texto,
        flags=re.IGNORECASE,
    ).strip()

    match = _PATRON_NUMERO.search(texto_limpio)
    if not match:
        logger.debug('Peso no parseable: %r', valor)
        return None

    try:
        return float(match.group())
    except ValueError:
        logger.debug('Peso no parseable: %r', valor)
        return None

"""Utilidades puras para normalización de SKU a formato canónico."""

from __future__ import annotations

import logging
import re

logger = logging.getLogger(__name__)

_PREFIJOS_SKU = re.compile(
    r'^(?:sku[_-]?|prod[_-]?|p[_-]?)',
    re.IGNORECASE,
)


def normalizar_sku(valor: str | None) -> str | None:
    """Normaliza un SKU a formato canónico ``SKU-NNNNN``.

    Acepta variantes como ``sku_3740``, ``SKU-12345``, ``P-12345``,
    ``PROD-12345`` o cadenas solo numéricas. El núcleo numérico se rellena
    con ceros a la izquierda hasta 5 dígitos.

    Args:
        valor: SKU en cualquier formato soportado o ``None``.

    Returns:
        SKU canónico en mayúsculas o ``None`` si el valor es inválido.
    """
    if valor is None:
        return None

    texto = valor.strip()
    if not texto:
        return None

    texto_limpio = _PREFIJOS_SKU.sub('', texto)
    digitos = ''.join(c for c in texto_limpio if c.isdigit())

    if not digitos or len(digitos) > 5:
        logger.debug('SKU inválido: %r', valor)
        return None

    nucleo = digitos.zfill(5)
    return f'SKU-{nucleo}'

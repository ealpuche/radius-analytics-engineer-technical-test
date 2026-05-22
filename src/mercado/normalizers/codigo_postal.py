"""Utilidades puras para normalización de código postal mexicano."""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)

_SENTINEL_CP_INVALIDO = '9999999'


def parse_codigo_postal(valor: str | int | None) -> str | None:
    """Normaliza un código postal a exactamente 5 dígitos.

    Args:
        valor: CP como cadena, entero o ``None``. El sentinel ``9999999``
            se trata como inválido.

    Returns:
        Cadena de 5 dígitos o ``None`` si el valor es inválido.
    """
    if valor is None:
        return None

    texto = str(valor).strip()
    if not texto:
        return None

    if texto == _SENTINEL_CP_INVALIDO:
        return None

    if not texto.isdigit():
        logger.debug('Código postal no numérico: %r', valor)
        return None

    if len(texto) > 5:
        logger.debug('Código postal con más de 5 dígitos: %r', valor)
        return None

    cp = texto.zfill(5)
    if len(cp) != 5:
        logger.debug('Código postal inválido tras normalizar: %r', valor)
        return None

    return cp

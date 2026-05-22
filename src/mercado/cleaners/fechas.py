"""Utilidades puras para parseo de fechas en múltiples formatos."""

from __future__ import annotations

import logging
from datetime import date, datetime

logger = logging.getLogger(__name__)

_FORMATOS_FECHA: tuple[str, ...] = (
    '%Y-%m-%d',
    '%d/%m/%Y',
    '%Y/%m/%d',
    '%d-%m-%Y',
)


def parse_fecha_multiformato(valor: str | None) -> date | None:
    """Parsea una fecha en varios formatos comunes del dataset Mercado.

    Formatos soportados: ``YYYY-MM-DD``, ``DD/MM/YYYY``, ``YYYY/MM/DD``,
    ``DD-MM-YYYY``.

    Args:
        valor: Cadena con la fecha o ``None``.

    Returns:
        Objeto ``date`` si el parseo fue exitoso; ``None`` si el valor es
        vacío, nulo o no reconocible.
    """
    if valor is None:
        return None

    texto = valor.strip()
    if not texto:
        return None

    for formato in _FORMATOS_FECHA:
        try:
            return datetime.strptime(texto, formato).date()
        except ValueError:
            continue

    logger.debug('Fecha no parseable: %r', valor)
    return None

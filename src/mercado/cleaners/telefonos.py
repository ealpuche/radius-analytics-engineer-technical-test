"""Utilidades puras para extracción de teléfono y extensión."""

from __future__ import annotations

import logging
import re

logger = logging.getLogger(__name__)

_PATRON_EXTENSION = re.compile(
    r'\s*(?:ext\.?|extension|x)\s*[:.]?\s*(\d+)\s*$',
    re.IGNORECASE,
)


def extraer_telefono(valor: str | None) -> tuple[str | None, str | None]:
    """Extrae el número telefónico (solo dígitos) y la extensión opcional.

    Args:
        valor: Cadena con teléfono, p. ej. ``'81-3801-8090 ext. 3033'``.

    Returns:
        Tupla ``(numero_digitos, extension)``. Si no hay extensión, el segundo
        elemento es ``None``. Si el valor es inválido o no contiene dígitos,
        retorna ``(None, None)``.
    """
    if valor is None:
        return None, None

    texto = valor.strip()
    if not texto:
        return None, None

    extension: str | None = None
    match_ext = _PATRON_EXTENSION.search(texto)
    if match_ext:
        extension = match_ext.group(1)
        texto = texto[: match_ext.start()]

    digitos = ''.join(c for c in texto if c.isdigit())
    if not digitos:
        logger.debug('Teléfono sin dígitos: %r', valor)
        return None, None

    return digitos, extension

"""Utilidades puras para clasificación de razones de devolución."""

from __future__ import annotations

import logging
import re

logger = logging.getLogger(__name__)

_CATEGORIA_OTRO = 'OTRO'


def clasificar_razon_devolucion(
    texto: str | None,
    patrones: dict[str, list[str]],
) -> str:
    """Clasifica el texto de devolución según patrones regex por categoría.

    La primera categoría cuyo patrón coincida (insensible a mayúsculas) gana.
    Los patrones se reciben como parámetro para no acoplar reglas de negocio.

    Args:
        texto: Descripción libre de la razón de devolución.
        patrones: Mapa ``categoria -> lista de patrones regex``.

    Returns:
        Nombre de la categoría coincidente o ``'OTRO'`` por defecto.
    """
    if texto is None:
        return _CATEGORIA_OTRO

    texto_limpio = texto.strip()
    if not texto_limpio:
        return _CATEGORIA_OTRO

    for categoria, lista_patrones in patrones.items():
        for patron in lista_patrones:
            if re.search(patron, texto_limpio, flags=re.IGNORECASE):
                logger.debug(
                    'Razón clasificada como %s con patrón %r',
                    categoria,
                    patron,
                )
                return categoria

    logger.debug('Razón sin clasificar, asignada a OTRO: %r', texto)
    return _CATEGORIA_OTRO

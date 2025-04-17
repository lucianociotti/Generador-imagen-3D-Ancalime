import re
from typing import Callable, Dict, Any

# Registry de funciones generadoras de formas geométricas
_SHAPES: Dict[str, Callable[[Dict[str, Any]], Any]] = {}

def register_shape(keywords):
    """
    Decorador para registrar una función generadora bajo una lista de palabras clave.
    Cada palabra clave asociada invocará esa función si aparece en el prompt.
    """
    def decorator(fn):
        for kw in keywords:
            _SHAPES[kw.lower()] = fn
        return fn
    return decorator

def find_shape(prompt: str):
    """
    Busca en el registry la primera función cuyo keyword esté en el prompt.
    Devuelve la función generadora o None si no hay match.
    """
    text = prompt.lower()
    for kw, fn in _SHAPES.items():
        if kw in text:
            return fn
    return None

def parse_params(prompt: str) -> Dict[str, Any]:
    """
    Extrae parámetros numéricos del prompt.
    Devuelve un dict con la lista "dims" de números en orden de aparición.
    Por ejemplo, 'cubo 40' → {'dims': [40.0]}
    'cilindro 10 30' → {'dims': [10.0, 30.0]}
    """
    nums = re.findall(r"(\d+\.?\d*)", prompt)
    return {"dims": [float(n) for n in nums]} if nums else {}

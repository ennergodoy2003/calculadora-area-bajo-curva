import math
import numpy as np
import sympy as sp
from .simbolos import x


def _limpiar(valores):
    """Convierte a lista de Python y cambia los valores inválidos (NaN, infinito) por None."""
    return [float(v) if np.isfinite(v) else None for v in valores]


def generar_grafica(f, a, b, funcion_texto):
    """Calcula los puntos y el rango de la gráfica, en unidades enteras."""
    f_num = sp.lambdify(x, f, "numpy")
    margen = max((b - a) * 0.2, 0.5)

    # Rango de x: el intervalo con margen, incluyendo siempre el origen
    x_min = math.floor(min(a - margen, 0))
    x_max = math.ceil(max(b + margen, 0))

    # Puntos del área (entre a y b)
    x_area = np.linspace(a, b, 400)
    y_area = f_num(x_area) * np.ones_like(x_area)

    # Rango de y: toda el área, el 0 y un poco de aire
    validos = y_area[np.isfinite(y_area)]
    y_bajo = float(validos.min()) if validos.size else 0
    y_alto = float(validos.max()) if validos.size else 0
    y_min = math.floor(min(y_bajo, 0) - 0.5)
    y_max = math.ceil(max(y_alto, 0) + 0.5)

    # Puntos de la curva en todo el ancho visible
    x_curva = np.linspace(x_min, x_max, 800)
    y_curva = f_num(x_curva) * np.ones_like(x_curva)

    return {
        "etiqueta": funcion_texto,
        "a": a,
        "b": b,
        "x_min": x_min, "x_max": x_max,
        "y_min": y_min, "y_max": y_max,
        "x_area": _limpiar(x_area),
        "y_area": _limpiar(y_area),
        "x_curva": _limpiar(x_curva),
        "y_curva": _limpiar(y_curva),
    }
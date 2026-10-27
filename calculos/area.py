import sympy as sp
from .simbolos import x


def calcular_area_total(f, a_exacto, b_exacto):
    """Busca dónde f(x) corta el eje x y suma el valor absoluto de cada tramo."""
    raices = sp.solveset(f, x, domain=sp.Interval.open(a_exacto, b_exacto))

    if raices == sp.S.EmptySet:
        # No hay raíces: la función no cruza el eje x en el intervalo
        cortes = []
    elif isinstance(raices, sp.FiniteSet):
        # Raíces encontradas con exactitud
        cortes = sorted([r for r in raices if r.is_real], key=float)
    else:
        # Plan B: SymPy no pudo encontrar las raíces con exactitud
        area = sp.Integral(sp.Abs(f), (x, a_exacto, b_exacto)).evalf()
        return area, None, []

    puntos = [a_exacto] + cortes + [b_exacto]

    area = 0
    tramos = []
    for i in range(len(puntos) - 1):
        valor = sp.integrate(f, (x, puntos[i], puntos[i + 1]))
        area += sp.Abs(valor)
        tramos.append({
            "desde": sp.latex(puntos[i]),
            "hasta": sp.latex(puntos[i + 1]),
            "valor": sp.latex(valor),
            "absoluto": sp.latex(sp.Abs(valor)),
        })

    return sp.simplify(area), cortes, tramos
import sympy as sp
from .simbolos import x
from .area import calcular_area_total
from .grafica import generar_grafica


def resolver_integral(funcion_texto, a, b):
    """Hace todo el cálculo y devuelve un diccionario listo para mostrar en el HTML."""
    f = sp.sympify(funcion_texto)
    a_exacto = sp.nsimplify(a)
    b_exacto = sp.nsimplify(b)

    # Integral definida y procedimiento
    F = sp.integrate(f, x)
    F_a = sp.simplify(F.subs(x, a_exacto))
    F_b = sp.simplify(F.subs(x, b_exacto))
    integral_neta = sp.integrate(f, (x, a_exacto, b_exacto))

    # Área total y gráfica (cada una en su propio módulo)
    area_total, cortes, tramos = calcular_area_total(f, a_exacto, b_exacto)
    grafica = generar_grafica(f, a, b, funcion_texto)

    return {
        "f": sp.latex(f),
        "F": sp.latex(F),
        "a": sp.latex(a_exacto),
        "b": sp.latex(b_exacto),
        "F_a": sp.latex(F_a),
        "F_b": sp.latex(F_b),
        "neta": sp.latex(integral_neta),
        "neta_decimal": f"{float(integral_neta):.4f}",
        "area_total": sp.latex(area_total),
        "area_decimal": f"{float(area_total):.4f}",
        "numerico": cortes is None,
        "hay_cortes": bool(cortes),
        "cortes": ",\\ ".join(sp.latex(c) for c in cortes) if cortes else "",
        "tramos": tramos,
        "son_distintos": abs(float(integral_neta) - float(area_total)) > 1e-9,
        "grafica": grafica,
    }
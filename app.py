from flask import Flask, render_template, request
from calculos import resolver_integral

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def inicio():
    datos = {"funcion": "x**2", "a": 0, "b": 2}
    resultado = None
    error = None

    if request.method == "POST":
        funcion_texto = request.form["funcion"]
        a = float(request.form["a"])
        b = float(request.form["b"])
        datos = {"funcion": funcion_texto, "a": a, "b": b}

        if a >= b:
            error = "El límite inferior (a) debe ser menor que el superior (b)."
        else:
            try:
                resultado = resolver_integral(funcion_texto, a, b)
            except Exception:
                error = "No pude entender la función. Revisá cómo la escribiste (ejemplo: x**2 + 3*x)."

    return render_template("index.html", datos=datos, resultado=resultado, error=error)


if __name__ == "__main__":
    app.run(debug=True)
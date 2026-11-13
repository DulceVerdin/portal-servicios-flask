import math

from flask import Flask, render_template, request

app = Flask(__name__)


def leer_numero(campo, etiqueta, permitir_negativo=False):
    valor = request.form.get(campo, "").strip()

    if not valor:
        raise ValueError(f"El campo {etiqueta} es obligatorio.")

    try:
        numero = float(valor)
    except ValueError:
        raise ValueError(f"Ingresa un número válido para {etiqueta}.") from None

    if not math.isfinite(numero):
        raise ValueError(f"Ingresa un número finito para {etiqueta}.")

    if not permitir_negativo and numero < 0:
        raise ValueError(f"El campo {etiqueta} no puede ser negativo.")

    return numero


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/empresa")
def empresa():
    return render_template("empresa.html")


@app.route("/servicios")
def servicios():
    return render_template("servicios.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


@app.route("/compra", methods=["GET", "POST"])
def compra():
    resultado = None
    error = None
    datos = {}

    if request.method == "POST":
        datos = request.form.to_dict()

        try:
            cantidad = leer_numero("cantidad", "cantidad")
            precio_unitario = leer_numero("precio_unitario", "precio unitario")
            subtotal = cantidad * precio_unitario
            descuento = subtotal * 0.10 if subtotal > 1000 else 0
            total = subtotal - descuento

            resultado = {
                "cantidad": datos.get("cantidad", ""),
                "precio_unitario": datos.get("precio_unitario", ""),
                "subtotal": f"{subtotal:.2f}",
                "descuento": f"{descuento:.2f}",
                "total": f"{total:.2f}",
            }
        except ValueError as exc:
            error = str(exc)

    return render_template(
        "compra.html",
        resultado=resultado,
        error=error,
        datos=datos,
    )


@app.route("/salario", methods=["GET", "POST"])
def salario():
    resultado = None
    error = None
    datos = {}

    if request.method == "POST":
        datos = request.form.to_dict()

        try:
            horas = leer_numero("horas", "horas trabajadas")
            pago_por_hora = leer_numero("pago_por_hora", "pago por hora")
            horas_normales = min(horas, 40)
            horas_extra = max(horas - 40, 0)
            pago_normal = horas_normales * pago_por_hora
            pago_extra = horas_extra * pago_por_hora * 2
            total = pago_normal + pago_extra

            resultado = {
                "horas": datos.get("horas", ""),
                "pago_por_hora": datos.get("pago_por_hora", ""),
                "horas_normales": f"{horas_normales:.2f}",
                "pago_normal": f"{pago_normal:.2f}",
                "horas_extra": f"{horas_extra:.2f}",
                "pago_extra": f"{pago_extra:.2f}",
                "total": f"{total:.2f}",
            }
        except ValueError as exc:
            error = str(exc)

    return render_template(
        "salario.html",
        resultado=resultado,
        error=error,
        datos=datos,
    )


@app.route("/temperatura", methods=["GET", "POST"])
def temperatura():
    resultado = None
    error = None
    datos = {}

    if request.method == "POST":
        datos = request.form.to_dict()

        try:
            celsius = leer_numero("celsius", "grados Celsius", permitir_negativo=True)
            fahrenheit = (celsius * 9 / 5) + 32
            kelvin = celsius + 273.15

            resultado = {
                "celsius": datos.get("celsius", ""),
                "fahrenheit": f"{fahrenheit:.2f}",
                "kelvin": f"{kelvin:.2f}",
            }
        except ValueError as exc:
            error = str(exc)

    return render_template(
        "temperatura.html",
        resultado=resultado,
        error=error,
        datos=datos,
    )


if __name__ == "__main__":
    app.run(debug=True)

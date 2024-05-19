from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    mensaje = None

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        edad = int(request.form.get('edad'))
        tarros_pintura = int(request.form.get('tarros_pintura'))

        total_sin_descuento = tarros_pintura * 9000


        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        descuento_aplicado = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - descuento_aplicado

        mensaje = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'descuento_aplicado': descuento_aplicado,
            'total_con_descuento': total_con_descuento
        }

    return render_template('ejercicio1.html', mensaje=mensaje)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    mensaje = None

    if request.method == 'POST':
        nombre = request.form.get('nombre')
        contrasena = request.form.get('contrasena')

        if nombre == 'juan' and contrasena == 'admin':
            mensaje = f"Bienvenido administrador {nombre}"
        elif nombre == 'pepe' and contrasena == 'user':
            mensaje = f"Bienvenido usuario {nombre}"
        else:
            mensaje = "Usuario o contraseña incorrectos."

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
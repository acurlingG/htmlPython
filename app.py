from flask import Flask, render_template, request


app= Flask(__name__)

@app.route('/')
def formulario():
    return render_template('inicio.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form['nombre']
    edad = request.form['edad']
    return f"<h2>Hola {nombre}, tienes {edad} años. </h2"

if __name__ == '__main__':
    app.run(debug=True)
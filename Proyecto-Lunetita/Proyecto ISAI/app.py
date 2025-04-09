from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/productos', methods=['GET', 'POST'])
def productos():
    return render_template('productos.html')

@app.route('/empleados', methods=['GET', 'POST'])
def empleados():
    return render_template('empleados.html')

@app.route('/proveedores', methods=['GET', 'POST'])
def proveedores():
    return render_template('proveedores.html')

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    return render_template('clientes.html')

@app.route('/pos', methods=['GET', 'POST'])
def pos():
    return render_template('POS.html')

if __name__ == '__main__':
    app.run(debug=True, port=15000)

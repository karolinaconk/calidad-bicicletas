from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos
app.config['DATABASE'] = 'bicicletas_mockup.sql'
app.config['SECRET_KEY'] = '123'

# Función para conectarse a la base de datos
def conectar_bd():
    conexion = sqlite3.connect(app.config['DATABASE'])
    conexion.row_factory = sqlite3.Row
    return conexion

# Ruta principal de la página web
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para mostrar las bicicletas disponibles
@app.route('/bicicletas')
def bicicletas():
    conexion = conectar_bd()
    cursor = conexion.execute('SELECT * FROM bicicletas')
    bicicletas = cursor.fetchall()
    conexion.close()
    return render_template('bicicletas.html', bicicletas=bicicletas)

# Ruta para alquilar una bicicleta
@app.route('/alquilar', methods=['GET', 'POST'])
def alquilar():
    if request.method == 'POST':
        # Lógica para guardar la información del alquiler en la base de datos
        return redirect(url_for('index'))
    else:
        conexion = conectar_bd()
        cursor = conexion.execute('SELECT * FROM bicicletas')
        bicicletas = cursor.fetchall()
        conexion.close()
        return render_template('alquilar.html', bicicletas=bicicletas)

if __name__ == '__main__':
    app.run(debug=True)
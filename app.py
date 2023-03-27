from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'adminBikes'
app.config['MYSQL_DATABASE_PASSWORD'] = '123'
app.config['MYSQL_DATABASE_DB'] = 'centro_comercial_renta_bicicletas'

# Función para conectarse a la base de datos
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host=app.config['MYSQL_DATABASE_HOST'],
            user=app.config['MYSQL_DATABASE_USER'],
            password=app.config['MYSQL_DATABASE_PASSWORD'],
            database=app.config['MYSQL_DATABASE_DB']
        )
        return conexion
    except Exception as e:
        print('Error al conectarse a la base de datos:', e)
        return None

# Ruta principal de la página web
@app.route('/')
def index():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM bicicletas')
    bicicletas = cursor.fetchall()
    conexion.close()
    return render_template('index.html', bicicletas=bicicletas)

# Ruta para mostrar las bicicletas disponibles
@app.route('/bicicletas')
def bicicletas():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM bicicletas')
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
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM bicicletas')
        bicicletas = cursor.fetchall()
        conexion.close()
        return render_template('alquilar.html', bicicletas=bicicletas)

# Ruta para iniciar sesión
@app.route('/iniciar_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        # Lógica para verificar las credenciales del usuario y crear la sesión
        return redirect(url_for('index'))
    else:
        return render_template('iniciar_sesion.html')

# Ruta para registrarse
@app.route('/registrarse', methods=['GET', 'POST'])
def registrarse():
    if request.method == 'POST':
        # Lógica para crear un nuevo usuario en la base de datos
        return redirect(url_for('index'))
    else:
        return render_template('registrarse.html')

# Ruta para cerrar sesión
@app.route('/cerrar_sesion')
def cerrar_sesion():
    # Lógica para cerrar la sesión del usuario
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
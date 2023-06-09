from flask import Flask, render_template, request,session, redirect, url_for
from dicc_bicicletas import lee_diccionario_bicicletas
from transacciones import agregar_transaccion, lee_diccionario_transaccion
from usuarios import agregar_usuario, lee_diccionario_usuarios
from login import verifica_login
import mysql.connector
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.secret_key ='Mantequilla'

# Configuración de la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'adminBikes'
app.config['MYSQL_DATABASE_PASSWORD'] = '123'
app.config['MYSQL_DATABASE_DB'] = 'centro_comercial_renta_bicicletas'

config = {
    'host': '127.0.0.1',
    'user': 'adminBikes',
    'password': '123',
    'db': 'centro_comercial_renta_bicicletas',
}

dicc_bicicletas = lee_diccionario_bicicletas(config)
dicc_usuarios = lee_diccionario_usuarios(config)
dicc_transaccion = lee_diccionario_transaccion(config)

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

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        dicc_usuarios = lee_diccionario_usuarios(config)
        return render_template('login.html')
    if request.method == 'POST':
        dicc_usuarios = lee_diccionario_usuarios(config)
        valor = request.form['login']
        if valor == 'login':
            correo = request.form['email']
            password = request.form['password']
            verifacacion = verifica_login(dicc_usuarios,correo,password)
            if verifacacion == 'correcto':
                session['id']   = dicc_usuarios[correo]['id']
                session['nombre']   = dicc_usuarios[correo]['nombre']
                session['correo_electronico']   = dicc_usuarios[correo]['correo_electronico']
                session['telefono']   = dicc_usuarios[correo]['telefono']
                session['contrasena']   = dicc_usuarios[correo]['contrasena']
                session['identificacion']   = dicc_usuarios[correo]['identificacion']
                session['logged_in']= True
                return redirect('/')
            else:
                return render_template('login.html')

# Ruta principal de la página web
@app.route('/', methods=['GET','POST'])
def index():
    conexion = conectar_bd()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM bicicletas')
    bicicletas = cursor.fetchall()
    conexion.close()
    if request.method == 'GET':
        return render_template('index.html', bicicletas=dicc_bicicletas, transaccion=dicc_transaccion)

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
        guardado = request.form['guardar']
        if guardado == 'Guardar':
                email = request.form['email']
                fecha_alquiler = request.form['fecha_alquiler']
                fecha_devolucion = request.form['fecha_devolucion']
                duracion_alquiler = request.form['duracion_alquiler']
                costo_alquiler = duracion_alquiler*20
                registrado = agregar_transaccion(dicc_usuarios,email,fecha_alquiler,fecha_devolucion,duracion_alquiler,costo_alquiler,config)
                if registrado:
                    return redirect('/')
                else:
                    return render_template('alquilar.html',mensaje='Correo ya registrado')
    else:
        return render_template('alquilar.html', bicicletas=bicicletas)

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        if request.method == 'POST':
            valor = request.form['signup']
            if valor == 'Registrate':
                nombre = request.form['nombre']
                correo = request.form['email']
                phone = request.form['phone']
                identification = request.form['identification']
                password = request.form['password']
                registrado = agregar_usuario(dicc_usuarios,nombre,correo,phone,password,identification,'activo',config)
                if registrado:
                    return render_template('login.html')
                else:
                    return render_template('signup.html',mensaje='Correo ya registrado')

@app.route("/logout", methods=['GET','POST'])
def logout():
    if request.method == 'GET':
        session['logged_in'] = False
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
from passlib.hash import sha256_crypt
import mysql.connector

def lee_diccionario_usuarios(config:dict)->dict:
    diccionario = {}
    try:
        bd = mysql.connector.connect(**config)
        cur = bd.cursor()
        cur.execute("SELECT id, nombre, correo_electronico, telefono,contrasena,identificacion FROM usuarios")
        for id, nombre, correo_electronico, telefono, password, identificacion in cur.fetchall():
            diccionario[correo_electronico] = {
                'nombre' : nombre,
                'correo_electronico' : correo_electronico,
                'telefono' : telefono,
                'contrasena' : password,
                'identificacion' : identificacion
            }
        cur.close()
        bd.close()
    except:
        print(f"No se pudo establecer conexion")
    return diccionario

def agregar_usuario(dicc:dict,nombre:str,correo:str,phone:str,password:str,identification:str,estado:str,config:dict) -> bool:
    registrado = False
    if correo not in dicc:
        try:
            bd = mysql.connector.connect(**config)
            cur = bd.cursor()
            query = 'INSERT INTO usuarios (nombre, correo_electronico, telefono, contrasena ,identificacion) VALUES ("{}","{}","{}","{}","{}")'.format(nombre, correo, phone, password, identification)
            cur.execute(query)
            cur.close()
            bd.commit()
            bd.close()
            registrado = True
        except:
            print(f"No se pudo establecer la conexion")
    return registrado
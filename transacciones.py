from datetime import date
import mysql.connector

def lee_diccionario_transaccion(config:dict)->dict:
    diccionario = {}
    try:
        bd = mysql.connector.connect(**config)
        cur = bd.cursor()
        cur.execute("SELECT * FROM transacciones")
        for id,correo_electronico,fecha_alquiler,fecha_devolucion,duracion_alquiler,costo_alquiler in cur.fetchall():
            diccionario[id] = {
                'id' : id,
                'correo_electronico' : correo_electronico,
                'fecha_alquiler' : fecha_alquiler,
                'fecha_devolucion' : fecha_devolucion,
                'duracion_alquiler' : duracion_alquiler,
                'costo_alquiler' : costo_alquiler,
            }
        cur.close()
        bd.close()
    except:
        print(f"No se pudo establecer conexion")
    return diccionario

def agregar_transaccion(dicc:dict, email:str,fecha_alquiler:date,fecha_devolucion:date,duracion_alquiler:int,costo_alquiler:float,config:dict) -> bool:
    registrado = False
    if email in dicc:
        try:
            bd = mysql.connector.connect(**config)
            cur = bd.cursor()
            query = 'INSERT INTO transacciones (correo_electronico,fecha_alquiler,fecha_devolucion,duracion_alquiler,costo_alquiler) VALUES ("{}","{}","{}","{}","{}")'.format(email,fecha_alquiler,fecha_devolucion,duracion_alquiler,costo_alquiler)
            cur.execute(query)
            cur.close()
            bd.commit()
            bd.close()
            registrado = True
        except:
            print(f"No se pudo establecer la conexion")
    return registrado
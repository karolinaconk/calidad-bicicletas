import mysql.connector


def lee_diccionario_bicicletas(config:dict)->dict:
    diccionario = {}
    try:
        bd = mysql.connector.connect(**config)
        cur = bd.cursor()
        cur.execute("SELECT id,marca,modelo,tamano,imagen FROM bicicletas")
        for id, marca, modelo, tamano, imagen in cur.fetchall():
            diccionario[str(id)] = {
                'id' : id,
                'marca' : marca,
                'modelo' : modelo,
                'tamano' : tamano,
                'imagen' : imagen
            }
        cur.close()
        bd.close()
    except:
        print(f"No se pudo establecer conexion")
    return diccionario

if __name__ == "__main__":
    print('Bicicletas')
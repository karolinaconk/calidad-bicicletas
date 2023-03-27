from passlib.hash import sha256_crypt

def verifica_login(dicc:dict,correo:str,password:str) -> str:
    mensaje = ''
    if correo in dicc:
        password_hash = dicc[correo]['contrasena']
        print(password_hash)
        if password_hash == password:
            correcta = True
        else:
            correcta = False
        
        if correcta:
            mensaje = 'correcto'
        else:
            mensaje = 'Password incorrecto'
    else:
        mensaje = 'Correo no registrado'
    return mensaje

if __name__ == "__main__":
    print('Login')
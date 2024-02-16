import json
from modulo1 import opcion1

datos = {
        "nombre":[],
        "direccion":[],
        "estado": [],
        "telefono": [],
        "consultas": [],
        "reclamaciones": [],
        "sugerencias": [],
        "fidelidad": [],
        "ofrecido": [],
        "servicio": []
        }
    jsonData = json.dumps(datos, indent=4)

    rutaFile = "usuarios.json"
    with open("usuarios.json", 'w') as outfile:
        outfile.write(rutaFile)


print('''Bienvenido
      Favor indique el numero de la opcion a la cual desea ingresar
      1. Usuarios
      2. Servicios
      3. Reportes
      ''')
rtaMenu = input(int())

if rtaMenu ==1:
    opcion1()

    




    
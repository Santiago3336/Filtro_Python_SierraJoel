def crearJson():

    import json

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

CrearUsuarios = crearJson()

def ingresarDatos(ruta_archivo, dato,nuevo_item ):

    import json

    with open("usuarios.json", 'r') as openfile:
        jsonDato = json.load(openfile)
        if dato in jsonDato:
            jsonDato[dato].append(nuevo_item)

    with open(ruta_archivo, 'w') as file:
        json.dump(jsonDato, file, indent=4)

def opcion1():
    print('''Usted ha ingresado a la opcion Usuarios
          A continuacion digite el numero de la opcion a la cual desea ingresar:
          1. Registrar Nuevo Usuario
          2. Ver usuarios segun categoria
          3. Ver informacion de Usuario
          ''')
    rtaOpcion1 = input(int())

    if rtaOpcion1 == 1:

        import json

        ruta_archivo = 'usuarios.json'

        print("ingrese el nombre que desea ingresar")
        nom = input("")
        ingresarDatos(ruta_archivo, nom)


        print("ingrese la direccion ")
        direct = input("")
        with open("rutaFile", 'r') as file:
            jsonDato = json.load(file)
        if nombre in jsonDato:
            jsonDato['direccion'].append(nombre)

        with open("rutaFile", 'w') as outfile:
            json.dump(jsonDato, outfile, indent=4)


        with open("usuarios.json", 'w') as outfile:
             []['nombre'] = (nombre,outfile)

        print("ingrese la direccion")
        direccion = input("")
        with open("usuarios.json", 'w') as outfile:
             []['direccion'] = (direccion,outfile)

        print("ingrese el telefono")
        tel = input(int())
        with open("usuarios.json", 'w') as outfile:
             []['telefono'] = (tel,outfile)

    if rtaOpcion1 == 2:
         
        import json

        with open("usuarios.json", 'r') as openfile:
            datos = (open.json,openfile)

        
        
        
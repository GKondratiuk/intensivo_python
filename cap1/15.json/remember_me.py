'''
from pathlib import Path
import json

master = input("What is your name ?") #guarda lo que el usuario ingrese en una variable
path = Path('username.json') #creamos el archivo json
contents = json.dumps(master) #transforma los datos a json
path.write_text(contents) #vuelca los datos

print(f"Te recordare cuando regreses {master}")

VAMOS A ACTUALIZAR ESTE PROGRAMA, RECUPERAREMOS EL USUARIO GUARDADO
O SI NO EXISTE, CREAREMOS UNO NUEVO 
'''
'''
from pathlib import Path
import json

path = Path('username.json')

if path.exists():
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Bienvenido nuevamente {username}")
else:
    username = input("Cual es tu nombre ?")
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"Te recordare cuando regreses {username}")
'''    
'''
MUCHAS VECES NOS DAREMOS CUENTA QUE EL CODIGO FUNCIONA 
PERO PODRIAMOS MEJORARLO,DIVIDIENDOLO EN UNA SERIE DE FUNCIONES, ESTO SE LLAMA REFACTORIZACION
ESTO HACE QUE NUESTRO CODIGO SEA MAS LIMPIO Y LEGIBLE
'''
'''
from pathlib import Path
import json

def greet_user(): #definimos una funcion 
    path = Path('username.json')

    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Bienvenido nuevamente {username}")
    else:
        username = input("Cual es tu nombre ?")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"Te recordare cuando regreses {username}")
        
greet_user()
'''

'''
GREET_USER:
RECUPERA EL NOMBRE DE USUARIO
O SOLICITA UNO NUEVO SI NO EXISTE
ASI QUE VAMOS A DIVIDIRLO PARA QUE SEA MAS SIMPLE
'''

from pathlib import Path
import json

def get_stored_username(path): #obtenemos el nombre de usuario(si existe)
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None
    
def greet_user(): #saluda al usuario por su nombre
    path = Path('username.json') # crea el archivo
    username = get_stored_username(path) # recupera el nombre de dicha funcion
    if username: # si hay algo guardado en la variable
        print(f"Bienvenido {username}")
    else:
        username = input("Cual es tu nombre ?")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"Te recordare cuando regreses {username}")
    
greet_user()
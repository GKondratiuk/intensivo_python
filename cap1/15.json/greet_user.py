from pathlib import Path
import json

path = Path('username.json')#traemos el archivo a leer
contents = path.read_text() #leemos el archivo
username =json.loads(contents) #lo guardamos en una variable

print(f"Bienvenido nuevamente {username}")
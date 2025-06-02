'''
Ahora escribiremos un programa que utilice json.loads() para
volver a leer la lista en memoria:
'''
from pathlib import Path
import json

path = Path('numbers.json') #seleccionamos el archivo a leer
contents = path.read_text() #seleccionamos una variable a leer
numbers = json.loads(contents) #toma la cadena en json y la devuelve en python

print(numbers) #imprimimos en pantalla

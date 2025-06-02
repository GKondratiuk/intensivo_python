from pathlib import Path #importamos libreria para manipular archivos de texto
import json #importamos json

numbers = [2,3,5,7,11,13] #creamos lsitas de numeros

path = Path('numbers.json') #creamos un archivo .json
contents = json.dumps(numbers) #transforma los datos ingresados en formato json
path.write_text(contents) #escribimos en el archivo
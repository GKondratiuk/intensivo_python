from pathlib import Path
path = Path('invitados.txt')

while True:
    respuesta = input('desea agregar un nombre ? y/n')
    if respuesta == 'n':
        break
    else:
        nombre = input('agrege su nombre... ')
        with path.open(mode='a') as archivo:
            archivo.write(nombre + '\n')
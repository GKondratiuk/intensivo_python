nombre = input('Cual es tu nombre ? ')



from pathlib import Path
path = Path('invitado.txt')
path.write_text(nombre)
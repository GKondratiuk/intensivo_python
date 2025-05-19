'''
6-1. Persona: Use un diccionario para almacenar información sobre una
persona que conozca. Guarde su nombre, apellido, edad y la ciudad en la
que vive. Debería tener claves como nombre, apellido, edad y ciudad.
Imprima toda la información almacenada en su diccionario.
'''

persona = {'nombre':'carlos','apellido':'slash','edad':35,'ciudad':'infierno'}
print(persona)
print(persona['nombre'])
print(persona['apellido'])
print(persona['edad'])
print(persona['ciudad'])

'''
• 6-2. Números favoritos: Use un diccionario para guardar los números
favoritos de distintas personas. Piense en cinco nombres y úselos como claves
en su diccionario. Piense el número favorito de cada persona y guárdelo
como valor en su diccionario. Imprima el nombre y el número favorito de
cada persona. Para que sea más divertido, puede preguntar a sus amigos
para conseguir datos reales para su programa.
'''
numeros = {}

numeros ['tevetedi'] = 17
numeros ['moroko'] = 22
numeros ['pacoco'] = 3
numeros ['kakorra'] = 38
numeros ['willy'] = 88


print(f'El numero favorito de tevetedi es el {numeros["tevetedi"]}')
print(f'El numero favorito de moroko es el {numeros["moroko"]}')
print(f'El numero favorito de pacoco es el {numeros["pacoco"]}')
print(f'El numero favorito de kakorra es el {numeros["kakorra"]}')
print(f'El numero favorito de willy es el {numeros["willy"]}')

'''
• 6-3. Glosario: Puede usar un diccionario de Python para modelar un
diccionario real. Sin embargo, para evitar confusiones, lo llamaremos
"glosario".
• Piense en cinco palabras de programación que haya aprendido en los
capítulos anteriores y úselas como claves en su glosario. Guarde sus
significados como valores.
• Imprima cada palabra con su significado en una salida con formato
limpio. Podría imprimir la palabra seguida de dos puntos y luego la
definición, o la palabra en una línea y la definición sangrada en una
segunda línea. Use el carácter de nueva línea (\n) para insertar una línea
en blanco entre cada par palabra-definición en la salida.
'''

print('\nGLOSARIO')

glosario = {}

glosario ['variables'] = 'cajas donde guardamos un valor'
glosario ['bucle for'] = 'los utilizamos para recorrer objetos, numeros'
glosario ['listas'] = 'sirve para enlistar van entre []'
glosario ['tuplas'] = 'como las listas pero no se pueden modificar, van con ()'
glosario ['diccionarios'] = 'guardan informacion con clave-valor van con {}'

print(f'bucle for: {glosario["bucle for"]}\n listas: {glosario["listas"]}\n tuplas: {glosario["tuplas"]}\n diccionarios: {glosario["diccionarios"]}\n variables: {glosario["variables"]} ')
'''
Un diccionario es similar a una lista, pero nos permite conectar
informaciones. Aprenderemos a crear diccionarios, pasar en bucle
por ellos y usarlos en combinación con listas y sentencias if.
Conocer los diccionarios le permitirá modelar una variedad aun
mayor de situaciones reales.
Podrá crear un
diccionario que represente a una persona y guardar toda la
información que quiera sobre esa persona: nombre, edad, ubicación,
profesión y cualquier otro aspecto personal que pueda describir.
'''

print('************************')
print('**DICCIONARIO SENCILLO**')
print('************************')

#Piense en un juego con aliens de distintos colores que valgan
#distintos puntos. Este sencillo diccionario guarda información sobre
#un alien concreto:
'''
Un diccionario de Python es una colección de pares clave-valor.
En Python, un diccionario va entre llaves
Cada clave se conecta con su valor mediante dos puntos y
varios pares clave-valor se separan entre ellos por comas
'''
alien_0 = {'color':'green','points':5}

print(alien_0['color'])
print(alien_0['points'])

#Ahora podemos acceder al color o a los puntos de alien_0. Si un
#jugador dispara al alien verde, podemos comprobar cuántos puntos
#gana con un código como este:

alien_0 = {'color': 'verde', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

'''
Los diccionarios son estructuras dinámicas. Podemos añadirles
nuevos pares clave-valor en cualquier momento. Para añadir un
nuevo par, daríamos el nombre del diccionario seguido por la nueva
clave entre corchetes junto con el nuevo valor.
'''
print('\nAGREGANDO VALORES')
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

'''
En ocasiones puede resultar conveniente, incluso necesario,
comenzar con un diccionario vacío e ir añadiéndole elementos. Para
empezar a rellenar un diccionario vacío, defina uno con unas llaves
vacías y luego añada cada par clave-valor en su propia línea.
'''
print('\nAGREGANDO VALORES A DICCIONARIO VACIO')
#comenzamos con un diccionario vaci
alien_11 = {}
#agregamos clave -  valor
alien_11['color'] = 'gris'
#agregamos clave -  valor
alien_11['points'] = 10

print(alien_11)

print('\nMODIFICANDO VALORES')

alien_0['color'] = 'amarillo'

print(f'El nuevo color del alien0 es {alien_0['color']}')

print('\n')
print('************************')
print('**AGREGANDO MOVIMIENTO**')
print('************************')

# definimos clave-valor del alien, posicion x, posicion y, velocidad.
alien_0 = {'x_position':0,'y_position':25,'speed':'medium'}
print(f'Original position: {alien_0["x_position"]}')

#movemos el alien hacia la derecha
#determina cuanto se mueve el alien basandose en su velocidad actual

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #debe ser un alien rapido
    x_increment = 3

#la nueva posicion es la antigua mas el incremento

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f'La nueva posicion es: {alien_0["x_position"]}')


print('\n')
print('******************************')
print('**ELIMINAR PARES CLAVE-VALOR**')
print('******************************')

alien_0 = {'color':'green','points':5}
print(alien_0)
#la sentencia del elimina permanentemente los datos de los puntos
del alien_0['points']
print(alien_0)

print('\n')
print('******************************')
print('**DICC. DE OBJETOS SIMILARES**')
print('******************************')

lenguaje_favorito = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}
#Conviene incluir una coma
#también después del último par, así se quedará preparada para
#añadir otro par en la siguiente línea si hace falta.

lenguaje = lenguaje_favorito['sarah'].title() #guardamos su lenguaje favorito en una variable
print(lenguaje)


print('\n')
print('***************************************')
print('**METODO GET() PARA ACCEDER A VALORES**')
print('***************************************')

#Usar claves entre corchetes para recuperar el valor que nos
#interesa en un diccionario puede causar un problema: si la clave que
#pedimos no existe, nos dará error.

#Veamos este ejemplo
#alien_0 = {'color':'green','speed':'slow'}
#print(alien_0['points'])

alien_0 = {'color':'green','speed':'slow'}

valor_punto = alien_0.get('points','no existe ese valor asignado')#el segundo argumento es opcional

print(valor_punto)
'''
una lista dentro de un diccionario o incluso un diccionario dentro de
otro diccionario. La anidación es una característica potente
A veces, necesitamos almacenar múltiples diccionarios en una
lista o una lista de elementos como valor en un diccionario. Esto se
llama "anidación". Podemos anidar diccionarios dentro de una lista,
'''

print('*************************')
print('LISTA CON DICCIONARIOS DENTRO')
print('*************************')
#diccionario de aliens
alien_0 = {'color':'green','points':5} #diccionario
alien_1 = {'color':'yellow','points':10}
alien_2 = {'color':'red','points':15}
#lista de diccionarios
aliens = [alien_0,alien_1,alien_2] #lista de diccionarios

for alien in aliens:
    print(alien)
    
#usamos range() para crear una flota de 30 aliens:
(print('\n crearemos 30 aliens'))  

aliens = []
# crea 30 aliens verdes
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'low'} # por cada alien que crea lo guarda en una variable
    aliens.append(new_alien) #agrega la variable a la lista

#muestra los 5 primeros aliens

for alien in aliens[:5]: #:5 es el rango de la lista que queremos que se nos muestre
    print(alien)
    
print(f'se han creado un total de {len(aliens)} aliens')

#todos estos alienígenas tienen las mismas características, pero
#Python los considera como un objeto separado, lo que nos permite
#modificar cada extraterrestre individualmente.

#convertimos los 3 primeros aliens en amarillo
print('\n CONVIRTIENDO ALIENS')
for alien in aliens[:3]:
    if alien['color'] == 'green':
       alien['color'] = 'yellow'
       alien['speed'] = 'medium'
       alien['points'] = 10

for alien in aliens [:5]:
    print(alien)
print('...')

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens [:3]:
    print(alien)
print('...')


'''
Es habitual guardar un número de diccionarios en una lista
cuando cada diccionario contiene distintos tipos de información
sobre un objeto. Por ejemplo, podemos crear un diccionario para
cada usuario de un sitio web, como hemos hecho en user.py, y
guardar los diccionarios individuales en una lista llamada users.
'''

print('\n*************************')
print('DICCIONARIOS CON LISTAS DENTRO')
print('*************************')

#En vez de colocar un diccionario dentro de una lista, a veces es
#útil poner una lista dentro de un diccionario.

#guardamos la informacion de la pizza que estamos pidiendo 

pizza ={ #diccionario
    'masa':'piedra', #diccionario
    'aditivos': ['hongos','queso extra']#lista
}
#resumen del pedido
print(f'su orden de pizza a la/al {pizza["masa"]}')

for aditivo in pizza['aditivos']:
    print(f'\t + {aditivo}')
    
print('\n LENGUAJES')

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward':['rust','c'],
    'phil':['python','haskell']
}
#yo quiero tomar el nombre y el lenguaje dentro de lenguajes
for nombre,languages in favorite_languages.items():#usamos un bucle para pasar dentro del diccionario
    print(f'\n El lenguaje favorito de {nombre.title()} es ')
    for language in languages:#usamos otro bucle para pasar dentro la lista
        print(f'{language}')
    
'''
*NOTA: No es recomendable anidar demasiadas listas y diccionarios. Si anida
elementos en muchos más niveles que los ejemplos anteriores o trabaja con el
código de otra persona con muchos niveles de anidación, es bastante
probable que exista una forma más sencilla de resolver el problema.
'''

print('\n************************************')
print('DICCIONARIOS CON DICCIONARIOS DENTRO')
print('************************************')
#Podemos anidar un diccionario dentro de otro, pero si lo hacemos
#el código puede complicarse rápidamente.

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'priceton',
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location':'paris',
    },
}

for username, user_info in users.items():
    print(f'\n username: {username}')
    full_name = f'{user_info['first']} {user_info['last']}'
    location = f'{user_info['location']}'
    print(f'\tnombre completo: {full_name.title()} ')
    print(f'\tubicacion: {location.title()}')
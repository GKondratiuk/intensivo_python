'''
El siguiente código pasa en bucle por una lista
de marcas de coche y busca el valor 'bmw'. Siempre que el valor sea
'bmw', se imprimirá con todas las letras mayúsculas en vez de solo la
inicial:
'''

cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

'''
En Python, la comprobación de igualdad distingue entre
mayúsculas y minúsculas, así que dos valores que las usen de
distinta forma no se consideran iguales:
'''

'''
Para descubrir si un valor en particular está ya en una lista,
usaremos la palabra clave in. Tomemos como ejemplo un código que
podríamos escribir para una pizzería.
'''
print('\n Buscamos valor')
toppings =['hongos','salamin','chedar']
print('chedar' in toppings)

'''
piense en una lista de usuarios que tienen prohibido comentar en un
foro. Podemos comprobar si un usuario está vetado antes de dejarle
enviar un comentario:
'''
print('\n Buscamos si el valor NO esta en la lista')

banneados = ['marcos','andrea','laura','jorge','esteban']
user = 'adrian'
if user not in banneados:
    print(f'{user.title()} no se encuentra en la lista de banneados, puede continuar')      
      
      



#4-1. Pizzas: Piense en al menos tres de sus pizzas favoritas. Guarde estos
#nombres en una lista y use un bucle for para imprimir el nombre de cada
#pizza.

pizzas = ['roquefort','calabresa','jamon crudo y parmesano']
for pizza in pizzas:
    print(pizza)

#Modifique su bucle for para imprimir una oración usando el nombre de
#la pizza en vez de solo el nombre. Para cada pizza debería tener al
#menos una línea de salida con una oración simple, como "Me gusta la
#pizza de pepperoni".
print('\nmodificamos:')

pizzas = ['roquefort','calabresa','jamon crudo y parmesano']
for pizza in pizzas:
    print(f'Me gusta la pizza de {pizza.title()}')
    
#Añada una línea al final del programa, fuera del bucle, que indique
#cuánto le gusta la pizza. La salida debería tener tres o más líneas sobre
#sus pizzas favoritas y al final una frase adicional, como "¡Me encanta la
#pizza!

print('\nmodificamos:')

frase = 'No hay anda mas rico que comer pizza'
pizzas = ['roquefort','calabresa','jamon crudo y parmesano']
for pizza in pizzas:
    print(f'Me gusta la pizza de {pizza.title()}')

print(f'{frase}')

#Animales: Piense en al menos tres animales diferentes que tengan una
#característica en común. Guarde los nombres de estos animales en una lista y
#use un bucle for para imprimir el nombre de cada animal.
print('\nmodificamos:')

animales = ['gato','leon','lince']

for animal in animales:
    print(animal)
    
#Modifique su programa para imprimir una oración sobre cada animal,
#como "Un perro sería una excelente mascota".
print('\nmodificamos:')

for animal in animales:
    print(f'{animal} es un felino')


'''
• Añada una línea al final del programa diciendo qué tienen estos
animales en común. Podría imprimir una frase como "¡Cualquiera de
estos animales sería una excelente mascota!".
'''
print('\nmodificamos:')

for animal in animales:
    print(f'{animal} es un felino')

print('Son grandes cazadores')
'''

• 4-12. Más bucles: Todas las versiones de foods.py de esta sección han
evitado usar bucles for al imprimir para ahorrar espacio. Elija una versión de
foods.py y escriba dos bucles para imprimir cada lista de comida.
'''

#4-10. Trozos: Partiendo de uno de los programas que hemos escrito en este
#capítulo, añada varias líneas al final que hagan lo siguiente:
#• Imprimir el mensaje "Estos son los tres primeros elementos de la lista:". A
#continuación, use un trozo para imprimir los tres primeros elementos de la
#lista de ese programa.

bebidas = ['vino','cerveza','cynar','whisky','ron']
print(f'Estos son los primeros elementos de la lista de bebidas {bebidas[0:3]}')

#• Imprimir el mensaje "Estos tres elementos están en el medio de la lista:".
#A continuación, use un trozo para imprimir los tres elementos centrales de
#la lista.

print(f'\n Estos son los elementos centrales de la lista {bebidas [1:5]}')

#• Imprimir el mensaje "Estos son los tres últimos elementos de la lista:". A
#continuación, use un trozo para imprimir los tres últimos elementos de la
#lista.

print(f'\n Estos son los ultimos tres elementos de una lista {bebidas[2:5]}')

#• 4-11. Mis pizzas, sus pizzas: Empiece con el programa del ejercicio 4-
#1. Haga una copia de la lista de pizzas y llámela friend_pizzas. A
#continuación, haga lo siguiente:

mis_pizzas = ['jamon','roquefort','huevo','palmito','salame']
sus_pizzas = mis_pizzas[:]

#• Añada una pizza nueva a la lista original.
mis_pizzas.append('rucula')

#• Añada una pizza diferente a la lista friend_pizzas.
sus_pizzas.append('anana')

#• Compruebe que tiene dos listas separadas. Imprima el mensaje "Mis
#pizzas favoritas son:" y luego use un bucle for para imprimir la primera
#lista. Imprima el mensaje "Las pizzas favoritas de mi amigo son:" y
#después utilice un bucle for para imprimir la segunda lista. Asegúrese de
#que cada pizza se guarda en la lista adecuada.

print(f'\n mis pizzas favoritas son:')
for pizza in mis_pizzas:
    print(pizza)
    
print(f'\n las pizzas favoritas de mi amigo son:')
for pizza in sus_pizzas:
    print(pizza)

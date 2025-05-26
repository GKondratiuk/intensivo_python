'''
Los siguientes ejercicios son un poco más difíciles que los del capítulo 2, pero le
dan la oportunidad de trabajar con listas de todas las formas descritas.
• 3-4. Lista de invitados: Si pudiese invitar a cualquiera, vivo o muerto, a
cenar, ¿a quién invitaría? Haga una lista de al menos tres personas a las que
le gustaría invitar a una cena y úsela para imprimir un mensaje para cada
persona invitándole a cenar.
'''
lista_invitados = ['Kakorra','tevetedi','seba','chino','pacoco']

print(lista_invitados[0])
print(lista_invitados[1])
print(lista_invitados[2])
print(lista_invitados[3])
print(lista_invitados[4])

'''
3-5. Cambiar la lista de invitados: Acaba de enterarse de que uno de
sus invitados no podrá asistir, así que tiene que enviar un nuevo juego de
invitaciones. Tendrá que pensar en otra persona para invitar.
• Empiece con el programa del ejercicio 3-4. Añada una llamada a
print() al final del programa indicando el nombre del invitado que no
puede asistir.
• Modifique la lista sustituyendo el nombre del invitado que no puede venir
por el de otra persona a la que va a invitar en su lugar.
• Imprima un segundo grupo de mensajes de invitación, uno para cada
persona que haya en la lista ahora.
'''

print(f'No podrá venir {lista_invitados.pop()}')#no solo elimina el objeto sino que ademas lo toma, lo recupera
lista_invitados.append('charly')
print(f'entonces invitaremos a "charly" {lista_invitados}')

'''
-6. Más invitados: Acaba de encontrar una mesa más grande, así que
dispone de más espacio. Piense en otros tres invitados más.
• Empiece con el programa del ejercicio 3-4 o 3-5. Añada una llamada a
print() al final para informar a la gente de que ha encontrado una mesa
de comedor más grande.
• Use insert() para añadir un nuevo invitado al principio de la lista.
• Use insert() para añadir un nuevo invitado en mitad de la lista.
• Use append() para añadir un nuevo invitado al final de la lista.
• Imprima un nuevo juego de mensajes de invitación, uno para cada
persona de la lista.
'''

lista_invitados.insert(0,'ema')
lista_invitados.insert(3,'moroko')
lista_invitados.append('lobo')

print(lista_invitados[0])
print(lista_invitados[1])
print(lista_invitados[2])
print(lista_invitados[3])
print(lista_invitados[4])
print(lista_invitados[5])
print(lista_invitados[6])
print(lista_invitados[7])

'''
3-7. Reducir la lista de invitados: Acaba de descubrir que la mesa no
llegará a tiempo para la cena y solo tiene espacio para dos invitados.
• Empiece con el programa de 3-6. Añada una línea que imprima un
mensaje diciendo que solo puede invitar a dos personas a cenar.
'''
print("\nLo siento solo puedo invitar a dos personas\n")

'''
• Use pop() para eliminar invitados de la lista de uno en uno hasta que
solo queden dos. Cada vez que retire un nombre de la lista, imprima un
mensaje para esa persona diciendo que lo siente, pero que no puede
invitarle a cenar.
'''

excluido = lista_invitados.pop()
print(f'Lo siento {excluido}, pero no puedo invitarte a cenar')

excluido = lista_invitados.pop()
print(f'Lo siento {excluido}, pero no puedo invitarte a cenar')

excluido = lista_invitados.pop()
print(f'Lo siento {excluido}, pero no puedo invitarte a cenar')

excluido = lista_invitados.pop()
print(f'Lo siento {excluido}, pero no puedo invitarte a cenar')

excluido = lista_invitados.pop()
print(f'Lo siento {excluido}, pero no puedo invitarte a cenar')

excluido = lista_invitados.pop()
print(f'Lo siento {excluido}, pero no puedo invitarte a cenar')

'''
• Imprima un mensaje para cada una de las dos personas que quedan en
la lista informándoles de que siguen invitados.

'''
print(f"Todavía estas en la lista {lista_invitados[0]}")
print(f'todavia estas en la lista {lista_invitados[1]}')

'''
• Use del para borrar los dos últimos nombres de la lista y que se quede
vacía. Imprima la lista para asegurarse de que realmente tiene una lista
vacía al final del programa.
'''

del lista_invitados[0]
del lista_invitados[0]

print(lista_invitados)# imprime [] es porque la lista está vacía
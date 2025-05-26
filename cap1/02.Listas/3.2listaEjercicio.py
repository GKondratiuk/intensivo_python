
'''
• 3-8. Ver el mundo: Piense en al menos cinco lugares del mundo que le
gustaría visitar.
• Guarde esos lugares en una lista. Asegúrese de no hacerlo en orden
alfabético.
'''
lugares = ['gran bretaña','alemania','nueva zelanda', 'dinamarca', 'luxemburgo']


#• Imprima la lista en su orden original. No se preocupe por el formato,
#simplemente imprímala como una lista de Python en bruto.
print('Lugares')
print(lugares)


#Use sorted() para imprimir la lista en orden alfabético sin modificarla
#realmente.
print('\nLugares en orden alfabetico')
print(sorted(lugares))

#• Compruebe que la lista sigue en su orden original imprimiéndola.
print('\nLugares en orden original')
print(lugares)

#• Use sorted() para imprimir la lista en orden alfabético inverso sin
#cambiar el orden de la lista original.
print('\nLugares en orden alfabetico - inverso')
print(sorted(lugares, reverse=True))

#• Compruebe que la lista sigue en su orden original imprimiéndola otra vez.
print('\nLugares en orden Original')
print(lugares)

#• Use reverse() para cambiar el orden de la lista. Imprímala para
#comprobar que el orden ha cambiado.
print('\nLugares en orden Cambiado')
lugares.reverse()
print(lugares)

#• Use reverse() para cambiar el orden de la lista de nuevo. Imprímala
#para comprobar que ha vuelto al orden original.
print('\nLugares en orden Reverso')
lugares.reverse()
print(lugares)

#• Use sort() para cambiar la lista y guardarla en orden alfabético.
#Imprímala para comprobar que el orden ha cambiado.
print('\nLugares en orden alfabetico')
lugares.sort()
print(lugares)

#• Use sort() para cambiar la lista y guardarla en orden alfabético inverso.
#Imprímala para comprobar que el orden ha cambiado.
print('\nLugares en orden alfabetico - inverso')
lugares.sort(reverse=True)
print(lugares)

#• 3-9. Invitados a la cena: Trabajando con uno de los programas de los
#ejercicios 3-4 a 3-7, utilice len() para imprimir un mensaje indicando el
#número de personas que va a invitar a cenar.
print('\nInvitados')
invitados = ['tevetedi','moroko','kakorra','paococo','charly','el chino']
print(f'El numero de invitados a la fiesta es de {len(invitados)}')

'''
• 3-10. Todas las funciones: Piense en algo que podría guardar en una
lista. Por ejemplo, podría hacer una lista de montañas, ríos, países, ciudades,

'''

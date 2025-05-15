'''
a veces
necesitamos crear listas de elementos que no se puedan alterar. Eso
es justo lo que podemos hacer con las tuplas. Python se refiere a los
valores que no pueden cambiar como inmutables, y una lista
inmutable se denomina "tupla".
Una tupla es muy parecida a una lista, solo que emplea
paréntesis en lugar de corchetes. Una vez definida la tupla, podemos
acceder a los elementos individuales usando sus índices, como
haríamos con una lista.
'''

dimensiones = (200,50)
print(dimensiones[0])
print(dimensiones[1])

#dimensiones[0] = 10 (este codigo intenta cambiar el valor de una tupla)
# esto genera error porque las tuplas no se pueden modificar, la lista si

'''
los valores de una tupla tambien se pueden pasar con un bucle for
'''
print('\n bucle for')
for dimension in dimensiones:
    print(dimension)
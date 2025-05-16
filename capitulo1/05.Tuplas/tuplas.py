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
    
'''
Aunque no se puede modificar una tupla, sí se puede asignar un
nuevo valor a una variable que representa una tupla.
'''

dimensiones = (200,50)
print('\n Dimensiones Originales: ')
for dimension in dimensiones:
    print(dimension)
    
dimensiones = (400,100)
print('\n Dimensiones modificadas')
for dimension in dimensiones:
    print(dimension) #No da error porque reasignar el valor de una variable es valido 
    
'''
En comparación con las listas, las tuplas son estructuras de datos
simples. Utilícelas cuando quiera guardar un conjunto de valores que
no deberían cambiar durante la vida de un programa.
'''
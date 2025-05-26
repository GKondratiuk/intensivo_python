print('votar')
edad = 17
if edad >= 18:
    print('Podes votar')
else:
    print('eres demasiado joven para votar')
    
print('\n Tarifas')

edad = 20
if edad < 4:
    print('Entrada gratuita')
elif edad < 18:
    print('Debe pagar 25 dolares')
else:
    print('paga 40 dolares') 
    
'''
En lugar de determinar un precio y mostrar un mensaje, solo determina el precio
de la entrada. Además de ser más eficiente y consiso, este código revisado es
más fácil de modificar que el del enfoque original.
'''
    
print('\n Tarifas con mejores practicas')

edad = 3

if edad < 4:
    precio = 0
elif edad < 18:
    precio = 25
else:
    precio = 40

print(f'La entrada cuesta ${precio}')


'''
La mayor parte de este código no cambia. El segundo bloque elif
comprueba ahora si una persona tiene menos de 65 años antes de
asignarle el precio completo de la entrada, 40 dólares. Observe que
es preciso cambiar el valor asignado en el bloque else por 20 dólares
porque las únicas personas que entrarían en este bloque tienen 65
años o más.
'''

print('\n Tarifas con mejores practicas')

edad = 65

if edad < 4:
    precio = 0
elif edad < 18:
    precio = 25
elif edad < 65:
    precio = 40
else:
    precio = 20
print(f'La entrada cuesta ${precio}')
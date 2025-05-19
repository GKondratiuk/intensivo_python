

#• 7-1. Coche de alquiler: Escriba un programa que pregunte al usuario qué
#tipo de coche desea alquilar. Imprima un mensaje sobre el coche, como
#"Veamos si tenemos un Subaru para usted".

coche = input('bienvenidos a la tienda alquiler de coches. ¿que coche desea alquilar? ')
print(f'{coche} ? aqui está')

#• 7-2. Mesa en un restaurante: Escriba un programa que pregunte al
#usuario cuántos vienen a cenar. Si la respuesta es más de ocho, imprima un
#mensaje diciendo al usuario que tendrán que esperar mesa. De lo contrario,
#dígale que su mesa está lista.

invitados = int(input('cuantos vienen a cenar ? '))
if invitados > 8:
    print(f'{invitados} ? entonces deberan esperar')
else:
    print('La mesa está lista')
    
'''
• 7-3. Múltiplos de diez: Pida al usuario un número y luego infórmele de si
ese número es múltiplo de 10 o no.
'''

numero = int(input('Coloque un numero '))
if numero % 10 == 0:
    print('es multiplo de 10')
else:
    print('no es multiplo de 10')
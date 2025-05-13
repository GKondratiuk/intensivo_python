'''
• 4-7. Treses: Haga una lista de los múltiplos de 3 comprendidos entre el 3 y
el 30. Use un bucle for para imprimir los números de la lista.
• 4-8. Cubos: Un número elevado a la tercera potencia es un cubo. Por
ejemplo, el cubo de 2 se escribe como 2**3 en Python. Haga una lista de los
10 primeros cubos (es decir, el cubo de cada entero entre 1 y 10) y use un
bucle for para imprimir el valor de cada cubo.
• 4-9. Comprensión de cubos: Use una lista por comprensión de los 10
primeros cubos.

'''

#4-3. Contar hasta veinte: Use un bucle for para imprimir los números del
#1 al 20, ambos incluidos.

for valor in range(1,21):
    print(valor)
    
#• 4-4. Un millón: Haga una lista de números de uno a un millón y luego use
#un bucle for para imprimir los números. (Si la salida tarda mucho, deténgala
#pulsando Control-C o cerrando la ventana de salida).
    
print('\n Millon')

millon =[]
for valor in range(1,101):
    millon.append(valor)
    
print(millon)

#• 4-5. Sumar un millón: Haga una lista de los números del uno al millón y
#use min() y max() para asegurarse de que su lista empieza realmente en uno
#y acaba en un millón. Utilice también la función sum() para ver lo rápido que
#Python puede sumar un millón de números.

print('\n Suma')

suma_millon = []

for valor in range(1,1000001):
    suma_millon.append(valor)

print(f'La suma del millon es: {sum(suma_millon)}')
print(f'El minimo es: {min(suma_millon)}')
print(f'El maximo es: {max(suma_millon)}')

#• 4-6. Números impares: Use el tercer argumento de la función range()
#para hacer una lista de los números impares comprendidos entre 1 y 20.
#Utilice un bucle for para imprimir cada número.
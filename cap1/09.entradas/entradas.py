'''
La función input() pausa el programa y espera a que el usuario
introduzca texto.
#message = input("Tell me something, and I will repeat it back to you: ")
print(message)
'''
'''
Usar int() para aceptar entrada numérica
Podemos resolver este problema con la función int(), que
transforma la entrada en un valor numérico. Esto permite que la
comparación se ejecute con éxito:
>>> age = input("How old are you? ")
How old are you? 21

>>> age = int(age)
>>> age >= 18
True

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
print("\nYou're tall enough to ride!")
else:
print("\nYou'll be able to ride when you're a little older.")
'''

'''
El operador módulo: Lo que hace es dividir un número entre otro y
devolver el resto:

>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
Este operador no nos da el resultado de la división de los dos
números; únicamente nos dice cuál es el resto.

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
print(f"\nThe number {number} is even.")
else:
print(f"\nThe number {number} is odd.")


Los números pares son siempre divisibles entre dos, así que, si el
módulo de un número y dos es cero (aquí, if number % 2 == 0), el
número es par. De lo contrario, es impar.
'''
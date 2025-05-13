'''
Python
ofrece varias herramientas para trabajar eficientemente con listas de
números. Cuando entienda cómo usar estas herramientas con
eficacia, su código funcionará incluso aunque las listas contengan
millones de elementos.
'''
for valor in range(1,5):
    print(valor) #nos arroja los numeros del 1 al 4
    
'''
Si quiere hacer una lista de números, puede convertir los
resultados de range() directamente en una lista usando la función
list(). Al meter una llamada a la función range() en list(), la salida
será una lista de números.
'''
print('\nLista de numeros')
numeros = list(range(1,5))
print(numeros) # nos arroja una lista de numeros del 1 al 4

'''
También podemos usar la función range() para decirle a Python
que se salte números en un rango determinado. Si pasamos un
tercer argumento a la función, Python usa ese valor como tamaño
de paso al generar números.
El siguiente ejemplo hace una lista de números pares entre el 0 y
el 10:
'''
print('\nLista de numeros salteada')

numeros_salteados = list(range(2,11,2)) 
#nos indica que iniciando del numero 2, hasta llegar al 10 salteando de 2 en 2 [2,4,6,8,10]
print(numeros_salteados)

'''
Podemos crear prácticamente cualquier conjunto de números que
queramos usando la función range(). Por ejemplo, piense cómo
podríamos hacer una lista de los 10 primeros números cuadrados (es
decir, el cuadrado de cada entero del 1 al 10). En Python, dos
asteriscos (**) representan exponentes. Así es como pondríamos los
10 primeros números cuadrados en una lista:
'''
'''
print('\nLista de numeros al cuadrado')

cuadrados = []#lista vacia llamada cuadrados

for value in range(1,11): #por cada valor iniciando en 1 hasta llegar al 10
    cuadrado = value**2 #guardá en una variable el valor elevado a la 2
    cuadrados.append(cuadrado) # el numero elevado a la 2 guardalo en la lista

print(cuadrados)
'''
print('\nEste codigo puede mejorarse')

cuadrados = []#lista vacia llamada cuadrados

for value in range(1,11): #por cada valor iniciando en 1 hasta llegar al 10
    cuadrados.append(value**2) #guardar en la lista el valor elevado a la 2

print(cuadrados) #imprimir lista de numeros elevados a la 2
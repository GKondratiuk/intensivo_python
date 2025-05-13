'''
Una lista es una colección de elementos dispuestos en un orden
particular. Podemos crear una lista que incluya las letras del
abecedario, los números del 0 al 9. como una lista suele tener 
varios elementos, conviene ponerles nombres en plural
'''

bicicletas = ['monuntainBike', 'fixie', 'inglesa']
print(bicicletas) #Error
'''
python nos devuelve toda la lista con corchetes y apostrofes completos,
como esto es algo que no queremos mostrar, las listas hay que mostrarlas 
de la siguiente manera:
'''
print('\nerror solucionado\n') #esto es lo que queremos mostrar al usuario, un formato limpio
print(bicicletas[-1])#esto nos muestra el ultimo elemento de la lista y así susecivamente
print(bicicletas[0])#los indices siempre empiezan desde 0
print(bicicletas[1])
print(bicicletas[2])

print("\nA partir de ahora empezaremos a ver los modificadores de las listas\n")
motos = ['Suzuki','Ducati','Kawazaki'] #las tres grandes Japonesas
motos[1] = 'Honda'
print(motos[0]),print(motos[1]),print(motos[2])
#Perdon dicen que son 4

'''

APEND()/ INSERT(X,Y)

'''

print('\nAgregamos un item al final con APPEND\n')

motos.append('Yamaha')#agrega un item al final de la lista 
print(motos[0]),print(motos[1]),print(motos[2]),print(motos[3])

print('\nAgregamos un item donde elijamos con INSERT\n')

motos.insert(1,'Ducati') #Agrega un item
print(motos)

'''

DEL / .POP() / REMOVE()

'''

print('\nEliminamos ducati porque no es nipona con DEL\n')
del motos[1] #Elimina 1 item
print(motos)

'''
a veces necesitaremos tomar el valor del elemento que eliminamos
esto se realiza con .pop()
'''
print('\nUtilizamos POP\n')
primer_moto = motos.pop(0)
print(f"La primer moto en mi vida fue una {primer_moto.title()}")

'''
A veces desconocemos la posicion de indice en la que se encuentra el objeto
entonces podemos pasarlo por valor
'''

print('\nUtilizamos .REMOVE() por valor\n')
print(motos)
motos.remove('Yamaha')#reconoce mayusculas y minusculas
print(motos)


'''

ORDENAR LISTAS DE MANERA PERMANENTE

'''

print("\nORDENAR LISTAS POR ORDEN ALFABETICO PERMANENTEMENTE")
autos = ["bmw","audi","volvo","toyota"]
print(autos)
autos.sort() # ES IMPORTANTE QUE TODO ESTÉ EN MINUSCULA, sino hay que hacer un forEach para que todo quede en minuscula
print(autos)

print("Modo inverso")
autos.sort(reverse=True)
print(autos)


'''

ORDENAR LISTAS DE MANERA TEMPORAL

'''
autos = ['bmw', 'audi', 'volvo', 'toyota', 'subaru', 'peugeot']
print('\nORDENAMOS DE MANERA TEMPORAL')
print(sorted(autos))

print('ORDENAMOS DE MODO INVERSO')
autos.reverse()
print(autos)

'''

LONGITUD DE UNA LISTA 

'''
print('\nPODEMOS VER LA CANTIDA DE OBJETOS EN UNA LISTA')
print(autos)
print(f'Son {len(autos)} objetos')
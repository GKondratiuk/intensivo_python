

#7-8. Bocatería: Haga una lista llamada pedidos_bocadillos y rellénela con
#los nombres de varios bocadillos. A continuación, haga una lista vacía
#llamada bocadillos_terminados. Pase en bucle por la lista de pedidos de
#bocadillos e imprima un mensaje para cada pedido, como "Su bocadillo de
#atún está listo". A medida que se hagan los bocadillos, páselos a la lista de
#terminados. Cuando todos los bocadillos estén hechos, imprima un mensaje
#que los enumere todos.

print("Pedidos Bocadillos")
pedidos_bocadillos = ['pastrami','sanguchito','pastrami','pancho','hummus','pastrami']
bocadillos_terminados = []

while pedidos_bocadillos: # mientras pedidos de bocadillos tenga items
    bocadillo = pedidos_bocadillos.pop() # el item que saca, lo guarda en la variable
    print(f'Su {bocadillo} esta listo')
    bocadillos_terminados.append(bocadillo)

print(f"\naqui tenemos {bocadillos_terminados}")

#• 7-9. Ya no hay pastrami: Usando la lista pedidos_bocadillos del
#ejercicio 7-8, asegúrese de que el bocadillo de 'pastrami' aparezca en la
#lista al menos tres veces. Añada código al principio del programa para
#imprimir un mensaje diciendo que no queda pastrami y use un bucle while
#para eliminar todas las apariciones de 'pastrami' en pedidos_bocadillos.
#Asegúrese de que no pasa ningún bocadillo de pastrami a la lista
#bocadillos_terminados.

print(f'\n FILTRO: no queda pastrami ')
pedidos_bocadillos = ['pastrami','sanguchito','pastrami','pancho','hummus','pastrami']

while 'pastrami'in pedidos_bocadillos:#mientras pedidos de bocadillos exista
    pedidos_bocadillos.remove('pastrami') #remover pastrami de la lista
    
print(f'{pedidos_bocadillos}')
        
'''
• 7-10. Vacaciones de ensueño: Escriba un programa que pregunte a los
usuarios por las vacaciones de sus sueños. Escriba unas instrucciones como
"Si pudieras visitar cualquier lugar del mundo, ¿dónde irías?". Incluya un
bloque de código que imprima el resultado de la encuesta.
'''

print(f'\nVacaciones, donde serian tus vacaciones ?: ')

vacaciones = {}
bandera = True

while bandera == True:
    
    nombre = input(f"Como es tu nombre ?")
    vacaciones[nombre] = input(f"Si puedieras ir de vacaciones a un lugar sonado donde seria ? ")
    respuesta = input(f"hay otra persona para encuestar ? yes/no ")
    if respuesta == 'no':
        bandera = False

for nombre,lugar in vacaciones.items():
    print(f"el es {nombre} y sus vacaciones soniadas serian en {lugar}") 

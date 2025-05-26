'''
Si hay que modificar una lista cuando se trabaja con ella, es
mejor usar un bucle while. Emplear bucles while con listas y
diccionarios nos permite recoger, almacenar y organizar muchas
entradas para examinarlas e informar luego.
'''

print('\n****************************************')
print('PASAR ELEMENTOS DE UNA LISTA A LA OTRA')
print('\n**************************************')


#mueve usuarios de una lista a la otra, desde el ultimo usuario, al primero de la lista, en ese orden
#comenzamos con una lista de usuarios a verificar
#y una lista de usuarios para alojar a los confirmados 

unconfirmed_users = ['alicia','brian','candela']
confirmed_users =[]

#verifica cada usuario hasta que ya no hay usuarios sin confirmar
#cada usuario verificado es movido a la lista de usuarios confirmados

while unconfirmed_users: # mientras existan usuarios sin confirmar
    current_user = unconfirmed_users.pop() #saca un usuario de la lista y lo agrega a una nueva variable
    print(f"Verifiando usuario {current_user.title()}")
    confirmed_users.append(current_user) #agrega el usuario de la variable a la lista
    
print("\nTodos los usuarios han sido confirmados")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


print('\n****************************************')
print('**********MASCOTAS-FILTRAMOS*************')
print('\n**************************************')

pets = ['dog','cat','dog','goldfish','cat','rabit','cat']
print(pets)
#mientras exista gato en animales
while'cat' in pets:
    pets.remove('cat') #remueve los cats de la lista, de uno en uno 

print("Removemos los cats:")
print(pets)


print('\n****************************************')
print('RELLENAR DICCIONARIO CON ENTRADA DEL USUARIO')
print('\n**************************************')
#Bucle que pide al nombre del usuario participante y respuesta

respuestas = {} #diccionario vacio

#configura una bandera para indicar que la encuesta esta activa
encuesta_activa = True

while encuesta_activa: #mientras la encuesta esta activa hacer:
    #pide el nombre y la respuesta de la persona
    name = input("Cual es tu nombre ? ")
    respuesta = input("Cual es tu color favorito ? ")
    #guarda la respuesta en un diccionario 
    respuestas[name] = respuesta #respuesta vinculada al nombre
    
    #averiguar si alguien va a hacer la encuesta 
    repeat = input("Alguien mas va a realizar la encuesta ? yes/no ")
    if repeat == 'no':
        encuesta_activa = False
    
    #Mostramos los resultados
    print('\nMostramos los resultados: ')
    for name, respuesta in respuestas.items():
        print(f"{name} dijo que su color favorito es {respuesta}")


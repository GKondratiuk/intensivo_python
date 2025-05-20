#• 7-4. Ingredientes de pizza: Escriba un bucle que pida al usuario que
#introduzca una serie de ingredientes de pizza y termine escribiendo el valor
#'quit'. Cuando introduzca cada ingrediente, imprima un mensaje diciendo
#que lo añadirá a su pizza.

print('\nIngredientes')

ingredientes = ''
input("que ingredientes agregará a la pizza ? ")
bandera = True
while bandera == True:
    ingredientes = input("desea agregar algo mas ? pulse 'quit' si no quiere nada mas ")
    if ingredientes == 'quit':
        bandera = False
        
#• 7-5. Entradas de cine: Un cine cobra las entradas a distinto precio en
#función de la edad del espectador. Los menores de 3 años entran gratis, los
#niños de entre 3 y 12 años pagan 8 euros y la entrada para mayores de 12
#años cuesta 12 euros. Escriba un bucle para preguntar a los usuarios su edad
#y luego dígales el precio de su entrada.

edad = ''
bandera = True
while bandera == True:
    edad = int(input('Digame su edad: '))
    if edad < 3:
        precio = print('entra gratis')
    elif edad < 13:
        precio = 8
    else:
        precio = 12
    print(f'La persona tiene {edad} entonces {precio}')
    persona = input("va a entrar alguien mas ? y/n ")
    if persona == 'n':
        print('gracias, puede/en ingresar')
        bandera = False
    else:
        continue
    

#• 7-6. Tres salidas: Escriba distintas versiones de los ejercicios 7-4 o 7-5,
#haciendo cada uno de los siguientes como mínimo una vez:
#• Use una prueba condicional en la sentencia while para detener el bucle.
#• Use una variable active para controlar cuánto tiempo se ejecuta el bucle.
#• Use una sentencia break para salir del bucle cuando el usuario
#introduzca el valor 'quit'.



'''
• 7-7. Infinidad: Escriba un bucle que no termine nunca y ejecútelo. (Para
detenerlo, pulse Control-C o cierre la ventana que muestra la salida).
'''
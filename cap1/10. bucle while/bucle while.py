'''
el
bucle while se ejecuta mientras se cumpla una condición.
Podemos usar un bucle while para contar una serie de números.
Por ejemplo, el siguiente bucle cuenta de 1 a 5:
'''
print('\nREPETIR')
numero = 1
while numero < 6:
    print(numero)
    numero +=1
    
print('\nREPETIR HASTA QUE SE DESEE')



'''
mensaje = input('decime algo y repetiré despues de ti... ')
#print(mensaje)

while mensaje != 'quit':
    mensaje = input('decime algo y repetiré despues de ti... ')
    print(mensaje)

Este programa funciona bien, pero imprime la palabra 'quit' como
si fuese un mensaje real. Podemos arreglarlo con una simple prueba
if:
'''

#mensaje =  ''
#while mensaje != 'quit':
#    mensaje = input('decime algo y repetiré despues de ti o pulsa salir para cerrar el programa ')
#    if mensaje != 'quit':
#        print(mensaje)


print('\nREPETIR CON BANDERA')
'''
Esta variable, llamada "bandera",
actúa como una señal para el programa. para continuar o finalizarlo
'''
mensaje = ''
activado = True
while activado == True:
    mensaje = input("Decime algo y repetiré despues de ti hasta que pulses 'quit'... ")
    if mensaje == 'quit':
        activado = False
    else:
        print(mensaje)

print('\nBRACK PARA SALIR DEL BUCLE')

'''
ara salir de un bucle while inmediatamente sin ejecutar ningún
código dentro del bucle, independientemente de los resultados de
cualquier prueba condicional, podemos usar la sentencia break.
'''


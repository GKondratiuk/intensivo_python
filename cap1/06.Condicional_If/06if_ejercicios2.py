
'''
• 5-8. Hola, Admin: Cree una lista de cinco o más nombres de usuario,
incluyendo el nombre 'admin'. Imagine que está escribiendo código que
imprimirá un mensaje para cada usuario cuando inicien sesión en un sitio
web. Pase en bucle por la lista e imprima un saludo para cada usuario:
• Si el nombre de usuario es 'admin', imprima un saludo especial, como
"Hola, admin, ¿quieres ver un informe de estado?".
• De lo contrario, imprima un saludo genérico, como "Hola, Juan, gracias
por volver a entrar".
'''
print('\nhola admin')
usuarios = ['tevetedy','alan','pacoco','dario','kakorra','admin']

for usuario in usuarios:
    if usuario == 'admin':
        print(f'Hola {usuario} lo estabamos esperando, Señor')
    else:
        print(f'Hola, {usuario} bienvenido')
        
'''
• 5-9. Sin usuarios: Añada una prueba if al programa del ejercicio
anterior (hello_admin.py) para asegurarse de que la lista no está vacía.
• Si la lista está vacía, imprima el mensaje "¡Necesitamos encontrar algún
usuario!".
• Borre todos los nombres de usuario de la lista y asegúrese de que se
imprime el mensaje correcto.
'''
print('\nSin usuarios')
usuarios = []

if usuarios:
    for usuario in usuarios:
        if usuario == 'admin':
            print(f'Hola {usuario} lo estabamos esperando, Señor')
        else:
            print(f'Hola, {usuario} bienvenido')
else:
    print('Necesitamos encontrar algun usuario')        
    

'''
• 5-10. Comprobar nombres de usuario: Haga lo siguiente para crear
un programa que simule cómo los sitios web se aseguran de que todos los
usuarios tienen un nombre único.
• Cree una lista con cinco o más nombres de usuario llamada
current_users.
• Cree otra lista de cinco nombres de usuario llamada new_users.
Asegúrese de que uno o dos de los nuevos nombres de usuario estén
también en la lista current_users.
• Pase en bucle por la lista new_users para ver si cada nuevo nombre de
usuario está ya usado. Si lo está, imprima un mensaje diciendo al usuario
que tendrá que introducir otro nombre. Si un nombre no se ha usado
todavía, imprima un mensaje diciendo que el nombre de usuario está
disponible.
• Asegúrese de que su comparación no distingue entre mayúsculas y
minúsculas. Si se ha usado 'Juan', no debería aceptarse 'JUAN'. (Para
hacer esto, necesitará una copia de current_users con la versión en
minúsculas de todos los usuarios existentes).
'''
print('\nUsuarios concurrentes')

usuarios_concurrentes = ['cachi','lobo','leon','bati','charly']
usuarios_nuevos = ['lobo','moroko','pablo','sorgo','bati','jorge']

for usuario_nuevo in usuarios_nuevos:
    if usuario_nuevo in usuarios_concurrentes:
        print(f'el usuario {usuario_nuevo} ya es un usuario habitué')
    else:
        print(f'el usuario {usuario_nuevo} se registró de manera exitosa')    
        
'''
• 5-11. Números ordinales en inglés: Los números ordinales indican su
posición en una lista, como 1o, 2o, etc. En inglés, la mayoría terminan en th,
excepto el 1, el 2 y el 3, que terminan en st, nd y rd, respectivamente.
• Guarde los números del 1 al 9 en una lista.
• Pase en bucle por la lista.
• Use una cadena if-elif-else dentro del bucle para imprimir la
terminación adecuada en inglés de cada número. La salida debería ser
"1st 2nd 3rd 4th 5th 6th 7th 8th 9th", y cada resultado debería
aparecer en una línea separada.
'''

print('\nNumeros')

numeros = [1,2,3,4,5,6,7,8,9]

for numero in numeros:
    if numero == 1:
        print(f'{numero}st')
    elif numero == 2:
        print(f'{numero}nd')
    elif numero == 3:
        print(f'{numero}rd')
    else:
        print(f'{numero}th')
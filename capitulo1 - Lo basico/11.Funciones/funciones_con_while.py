print('\nFUNCION CON BUCLE WHILE INFINITO')
#a tener en cuenta las VARIABLES QUE CONTIENEN FUNCIONES
'''
def get_formatted_name(first_name,last_name):
    #devuelve un nombre completo con un formato adecuado
    full_name = f'{first_name} {last_name}' #creamos una variable que reciba los parametros
    return full_name.title() #la variable devolverá lo que se coloque en los parametros
#esto es un bucle infinito !
while True: #bucle infinito
    print('Please tell me your name:')
    f_name = input('first name: ') #guardamos el primer nombre en una variable
    l_name = input('last name: ') #guardamos el segundo nombre en una variable
    
    formmated_name = get_formatted_name(f_name, l_name) #guardamos la funcion en una variable
    print(f'Hello ! {formmated_name}')# corremos la variable que contiene a la funcion
'''
print('\nFUNCION CON BUCLE WHILE CON BREAK')
    
def obtener_nombre_completo(primer_nombre,segundo_nombre): #funcion con parametros
    nombre_completo = f'{primer_nombre} {segundo_nombre}' #guardamos los parametros en una variable
    return nombre_completo #devolvemos la variable
while True:
    primer_nombre = input("Decime tu nombre o pulsá quit para salir ")
    if primer_nombre == 'quit':
        break
    segundo_nombre = input("Coloque su apellido ")
    
    nombre_completo = obtener_nombre_completo(primer_nombre,segundo_nombre)
    print(nombre_completo)
        
        
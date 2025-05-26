'''
son bloques de código con nombre diseñados para hacer una tarea específica.

algunas funciones cuya misión principal consiste en mostrar información y
otras diseñadas para procesar datos y devolver un valor o un
conjunto de valores. 

Por último, veremos cómo guardar las funciones
en archivos separados, denominados "módulos", para tener
organizados los archivos de programa principales.
'''
print("Definimos una funcion")
#definimos una funcion
def gran_usuario():
    print('Hola a todos') #muestra un saludo
    
gran_usuario() #llamamos a la funcion que muestra un saludo

print("\nDefinimos una funcion con Parametro")
#definimos una funcion con PARAMETRO
def gran_usuario(username):
    print(f'Hola {username}') #muestra un saludo a alguien especifico
    
gran_usuario('javier') #le pasamos un ARGUMENTO a la funcion llamada
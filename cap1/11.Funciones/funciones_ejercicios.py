

#• 8-1. Mensaje: Escriba una función llamada mostrar_mensaje() que
#imprima una oración diciendo a todos lo que está aprendiendo en este
#capítulo. Llame a la función y asegúrese de que el mensaje se muestra
#correctamente.
print('\n Mostramos un mensaje')
def mostrar_mensaje():
    print('este es un mensaje')
    
mostrar_mensaje()

'''
• 8-2. Libro favorito: Escriba una función llamada libro_favorito() que
acepte un parámetro título. La función debería imprimir un mensaje como
"Uno de mis libros favoritos es Alicia en el País de las Maravillas". Llame
a la función, asegurándose de incluir el título de un libro como argumento en
la llamada a la función.
'''
print('\n Mostramos un mensaje con Parametros')
def libro_favorito(titulo):
    print(f'Mi libro favorito es {titulo}')
    
libro_favorito('lobo estepario') #llamamos a la funcion y colocamos el argumento
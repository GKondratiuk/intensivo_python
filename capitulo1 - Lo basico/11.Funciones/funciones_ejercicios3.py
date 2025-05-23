'''
• 8-8. Álbumes de usuarios: Empiece con el programa del ejercicio 8-7.
Escriba un bucle while que permita a los usuarios introducir el artista y el
título de un álbum. Una vez que disponga de esa información, llame a
hacer_album() con la entrada de usuario e imprima el diccionario que se ha
creado. Asegúrese de incluir un valor para salir en el bucle while.
'''
#• 8-6. Nombres de ciudad: Escriba una función llamada ciudad_pais()
#que admita el nombre de una ciudad y su país. La función debería devolver
#una cadena con formato, similar a esta:
#"Santiago, Chile"
#Llame a su función con al menos tres pares ciudad-país e imprima los valores
#devueltos.

def ciudad_pais(ciudad,pais):
    return f'Mi lugar favorito es la ciudad de {ciudad} que esta en {pais}'

lugar = ciudad_pais('Santiago','Chile')
print(lugar)

'''
• 8-7. Álbum: Escriba una función llamada hacer_album() que cree un
diccionario para describir un álbum musical. La función debería aceptar un
nombre de artista y un título de álbum y debería devolver un diccionario con
estas dos informaciones. Use la función para hacer tres diccionarios que
representen distintos álbumes. Imprima cada valor devuelto para comprobar
que los diccionarios están almacenando bien la información.
Use None para añadir un parámetro opcional a hacer_album() que permita
guardar el número de canciones que contiene un álbum. Si la línea de
llamada incluye un valor para el número de canciones, añádalo al
diccionario del álbum. Haga al menos una nueva llamada a la función que
incluya este dato.
'''

print('\nALBUM: ')

def hacer_album():
    banda = {}
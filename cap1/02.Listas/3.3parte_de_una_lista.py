'''
También podemos trabajar con un grupo
específico de elementos en una lista, que en Python denominamos
"trozo" o slice.
'''

jugadores = ['pacoco','carli','willy','charly','borleto','kakorra','moroko']
print(jugadores[0:3])#sekecciona los elementos desde el indice 0 hasta el 2 inclusive

#podemos combinar una lista con un for ej:

# elegir los primeros tres jugadores para tu equipo

for jugador in jugadores[:3]:
    print(jugador.title())
    
    '''
    Los trozos o particiones son muy útiles en diversas situaciones.
Por ejemplo, al crear un juego, podemos añadir el resultado final de
un jugador a una lista cada vez que termine de jugar. A
continuación, podríamos obtener sus tres mejores puntuaciones
organizando la lista en orden decreciente y sacando un trozo que
incluya solo los tres primeros resultados. Cuando se trabaja con
datos, los trozos pueden servir para procesar los datos en secciones
de un tamaño específico. Y, si estamos creando una aplicación web,
podemos emplear trozos para mostrar información en una serie de
páginas con una cantidad de información apropiada en cada una.
    '''
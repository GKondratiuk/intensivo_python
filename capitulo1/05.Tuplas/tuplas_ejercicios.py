#• 4-13. Bufé: Un restaurante de tipo bufé ofrece solo cinco comidas básicas.
#Piense en cinco platos básicos y guárdelos en una tupla.

comidas = ('guisito rico','polenta','pastel de papa','arroz con pollo','mila con fritas')

#• Use un bucle for para imprimir cada comida que ofrece el restaurante.
for comida in comidas:
    print(comida)
    
#• Intente modificar alguno de los elementos y asegúrese de que Python
#rechaza el cambio.

#comidas[0] = 'Guiso de lentejas' # este codigo no da error

#• El restaurante cambia su menú, sustituyendo dos elementos por comidas
#diferentes. Añada una línea que rehaga la tupla y use un bucle for para
#imprimir cada uno de los elementos del menú modificado.

print('\nComidas nuevas del restaurante')
comidas = ('guiso de lenteja','polenta','pastel de papa','arroz con pollo','ravioles')
for comida in comidas:
    print(comida)
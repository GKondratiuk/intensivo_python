print('***************************')
print('***LISTAS SIMPLES***')
print('***************************')

adicionales = ['hongos','pimientos verdes','queso extra']

for adicional in adicionales:
    if adicional == 'pimientos verdes':
        print('no tenemos pimientos verdes')
    else:
        print(f'agregando {adicional}')

print('Disfrute su pizza')

print('\nListas Vacias')

adicionales = []

if adicionales:#si la lista no está vacía ingresa al cilco for
    for adicional in adicionales:
        print(f'agregando {adicional}')
    
    print('Disfrute su pizza')

else:
    print('Estas seguro que qures una pizza sola ?')
    
print('\n')
print('***************************')
print('***MULTIPLES LISTAS***')
print('***************************')

adicionales_disponibles = ['hongos','aceitunas','pimientos verdes','salame','anana','queso extra']
adicionales_pedidos = ['hongos', 'papas fritas','queso extra']

for adicional_pedido in adicionales_pedidos:
    if adicional_pedido in adicionales_disponibles:
        print(f'agregando {adicional_pedido}')
    else:
        print('perdon, no tenemos ese adicional')
        
print('Disfrute su pizza')

print('***************************')
print('***MULTIPLES CONDICIONES***')
print('***************************')

'''
a veces es importante comprobar todas las
condiciones de interés. En esos casos, conviene usar una serie de
sentencias if simples sin bloques elif ni else. Esta técnica tiene
sentido cuando puede darse más de una condición y queremos
actuar sobre todas las condiciones evaluadas como True.
'''

condimentos = ['hongos','extra queso']

if 'hongos' in condimentos:
    print('agregando hongos')
if 'salame' in condimentos:
    print('agregando salame')
if 'extra queso' in condimentos:
    print('agregando extra queso')
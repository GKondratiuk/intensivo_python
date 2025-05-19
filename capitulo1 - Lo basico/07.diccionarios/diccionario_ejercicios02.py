
'''
• 6-4. Glosario 2: Ahora que sabe cómo pasar en bucle por un diccionario,
limpie el código del ejercicio 6-3 sustituyendo las llamadas a print() por un
bucle que pase por las claves y valores del diccionario. Cuando sepa con
seguridad que su bucle funciona, añada a su glosario cinco términos más
relacionados con Python. Cuando vuelva a ejecutar el programa, estas
nuevas palabras y definiciones deberían incluirse automáticamente en la
salida.
'''

glosario = {}

glosario ['variables'] = 'cajas donde guardamos un valor'
glosario ['bucle for'] = 'los utilizamos para recorrer objetos, numeros'
glosario ['listas'] = 'sirve para enlistar van entre []'
glosario ['tuplas'] = 'como las listas pero no se pueden modificar, van con ()'
glosario ['diccionarios'] = 'guardan informacion con clave-valor van con {}'
#valores agregados
glosario ['items()'] = 'podemos ver tanto llaves(kays) como valores(value)'
glosario ['kay()'] = 'podemos ver solo las llaves'
glosario ['value()'] = 'podemos ver solo los valores'
for llave,valor in glosario.items(): #items() agrega tanto kay como value
    print(f'\n{llave} = {valor}')
     
'''
• 6-5. Ríos: Haga un diccionario con tres ríos importantes y el país por el que
discurre cada uno. Un par clave-valor podría ser 'nilo': 'egipto'.
• Use un bucle para imprimir una frase sobre cada río, como "El Nilo
discurre por Egipto".
• Use un bucle para imprimir el nombre de cada río incluido en el
diccionario.
• Use un bucle para imprimir el nombre de cada país incluido en el
diccionario.
'''

print('\nRios')

rios = {
    'nilo':'egipto',
    'parana':'argentina',
    'nieper': 'ucrania'
}

for clave,valor in rios.items():
    print(f'Los rios son tan hermosos, como el rio {clave} que pasa por {valor}')

print('Bucle para rios')

for rio in rios.keys():
    print(f'me encanta el rio {rio}')
    
print('Bucle para paises')

for pais in rios.values():
    print(f'yo se que {pais} tiene al menos un rio')
    

'''
• 6-6. Sondeos: Use el código de favorite_languages.py.
• Haga una lista de personas que deberían hacer la encuesta sobre
lenguajes preferidos. Incluya algunos nombres que estén ya en el
diccionario y otros que no lo estén.
• Pase en bucle por la lista de personas que deberían hacer la encuesta. Si
ya la han hecho, deles las gracias por responder. Si todavía no la han
completado, imprima un mensaje invitándoles a hacerlo
'''

print('\nsondeos')
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

personas = ['fran','sarah','cami','phil','luka']

for persona in personas:
    if persona in favorite_languages:
        lenguage = favorite_languages[persona] #agarra el valor por defecto
        print(f'gracias por hacer la encuesta {persona}, tu lenguaje es {lenguage}')
    else:
        print(f'deberia hacer la encuesta {persona}')
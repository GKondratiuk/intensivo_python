'''
Python nos deja pasar en bucle por un
diccionario. Los diccionarios sirven para guardar información de
distintas maneras, por lo que existen formas diferentes de pasar en
bucle por ellos. Podemos pasar por todos los pares clave-valor de un
diccionario, solo por las claves o solo por los valores.
'''
print('*************************************')
print('BUCLE FOR POR CLAVE-VALOR')
print('*************************************')
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

#por cada clave-valor en user_0 ver items
for key,value in user_0.items():#este metodo es requerido para que devuelva la secuencia de pares clave-valor
    print(f'\nkey: {key}') #imprimir clave
    print(f'Value: {value}') #imprimir valor
    
print('\n Lenguajes favoritos')
    
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
#por cada nombre y lenguaje en lenguajes favoritos 
for name,language in favorite_languages.items():
    print(f'\nname: {name}')
    print(f'language: {language}')
    

'''
El método keys() es útil cuando no hace falta trabajar con todos
los valores de un diccionario. Vamos a pasar en bucle por el
diccionario favorite_languages para imprimir los nombres de todos los
que hicieron la encuesta:
'''  
print('\n*************************************')  
print('BUCLE FOR POR CLAVE')
print('*************************************')
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

#por cada nombre en lenguaje_favorito
for name in favorite_languages.keys():#key solo nos arroja info de la clave, se puede omitir
    print(name.title())
    
print('\n*************************************')
print('BUCLE FOR DICCIONARIOS CON LISTAS')
print('*************************************')
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

friends = ['phil','sarah']

for name in favorite_languages.keys():
    print(f'Hi {name.title()}') #acá pide que muestre la clave,key, nombre
    if name in friends:
        language = favorite_languages[name].title() #acá pide que guarde el valor, value - agarra el valor por defecto
        print(f'\t{name.title(),} veo tu amor por {language}')
    
    if 'erin' not in favorite_languages.keys():
        print('Erin, por favor hacé la encuesta')
        

print('\n*************************************')
print('BUCLE FOR POR CLAVE EN ORDEN PARTICULAR')
print('*************************************')

'''
a veces nos interesa
que el bucle siga un orden diferente.
Una forma de hacerlo es ordenar las claves a medida que se
devuelven en el bucle for. Podemos usar la función sorted() para
obtener una copia de las claves en orden:
'''

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
    
print('\n*************************************')
print('BUCLE POR TODOS LOS VALORES')
print('*************************************')

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values(): # Nos pasa solo los valores
    print(language.title())

print('\nSin repeticiones')
#Para ver cada lenguaje elegido
#sin repeticiones, podemos usar un conjunto. Un "conjunto" es una
#colección en la que cada elemento debe ser único:
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()): #utilizamos SET para que no se repitan valores
    print(language.title())
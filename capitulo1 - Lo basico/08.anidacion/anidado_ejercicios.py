
'''
• 6-7. Personas: Empiece con el programa que ha escrito para el ejercicio
6-1. Cree dos diccionarios nuevos que representen a distintas personas y
guarde los tres diccionarios en una lista llamada personas. Pase en bucle por
la lista. Al hacerlo, imprima todo lo que sabe sobre cada persona.
'''

print('\n*********************************')
print('******PERSONAS - DICCIONARIO*******')
print('*********************************')
#• 6-7. Personas: Empiece con el programa que ha escrito para el ejercicio
#6-1. Cree dos diccionarios nuevos que representen a distintas personas y
#guarde los tres diccionarios en una lista llamada personas. Pase en bucle por
#la lista. Al hacerlo, imprima todo lo que sabe sobre cada persona.

persona_1 = {'nombre':'carlos','apellido':'slash','edad':35,'ciudad':'infierno'}
persona_2 = {'nombre':'willy','apellido':'box','edad':33,'ciudad':'nevermind'}
persona_3 = {'nombre':'pacoco','apellido':'wolf','edad':33,'ciudad':'lordaderon'}

personas = [persona_1,persona_2,persona_3]

for persona in personas:
    print(f'Se buscan ese bastardo {persona}')
    
    
#• 6-8. Mascotas: Cree varios diccionarios, cada uno representando una
#mascota diferente. En cada diccionario, incluya el tipo de animal y el nombre
#del dueño. Guarde estos diccionarios en una lista llamada mascotas. A
#continuación, pase en bucle por la lista y, al hacerlo, imprima todo lo que
#sabe sobre cada mascota.

print('\n***********************************')
print('******MASCOTAS - DICCIONARIO*******')
print('**********************************')

mascota_1 = {'tipo':'gato','dueño':'azul'}
mascota_2 = {'tipo':'lechuza','dueño':'harry'}
mascota_3 = {'tipo':'nutria','dueño':'pacoco'}

mascotas = [mascota_1,mascota_2,mascota_3]

for mascota in mascotas:
    print(f'tenemos esta mascota{mascota}')
    
#• 6-9. Lugares favoritos: Cree un diccionario llamado lugares_favoritos.
#Piense en tres nombres para usar como claves en el diccionario y guarde
#entre uno y tres lugares favoritos para cada persona. Para hacer este
#ejercicio un poco más interesante, pregunte a algunos amigos por sus sitios
#preferidos. Pase en bucle por el diccionario e imprima el nombre y el lugar
#favorito de cada persona.

lugares_favoritos = {
    'willy':'nevermind', 
    'tevetedi':'infierno',
    'pacoco':'azeroth'
    }

for nombre,lugar in lugares_favoritos.items():
    print(f'el es {nombre} y su lugar favorito es {lugar}')
    
print('\n********************************')
print('************PERSONAS**************')
print('******DICCIONARIO CON LISTA*******')
print('*********************************')

#6-10. Números favoritos: Modifique el programa del ejercicio 6-2 para
#que cada persona pueda tener más de un número favorito. Luego, imprima el
#nombre de cada persona junto con su(s) número(s) favorito(s).

numeros = {}

numeros ['tevetedi'] = [17,5]
numeros ['moroko'] = [22,77,1,7,27]
numeros ['pacoco'] = [6,29]
numeros ['kakorra'] = [38,33,12]
numeros ['willy'] = [88,11,3,14]

#para el unico caso hasta el momento que se utiliza un for anidado
for nombre,numeros in numeros.items():
    print(f'El numero favorito de {nombre} es: {numeros}')
    for numero in numeros:
        print(f'{numero}')
    
#• 6-11. Ciudades: Cree un diccionario llamado ciudades. Use los nombres
#de tres ciudades como claves en su diccionario. Cree un diccionario de
#información sobre cada ciudad e incluya el país en el que se encuentra, su
#población aproximada y alguna curiosidad sobre la ciudad. Las claves para
#cada ciudad serían país, población y curiosidad. Imprima el nombre de
#cada ciudad y toda la información que tenga guardada sobre ella.

print('\n**************************************')
print('*****************CIUDADES***************')
print('******DICCIONARIO CON DICCIONARIO*******')
print('****************************************')

ciudades = {
    'san rafael':{'pais':'argentina','poblacion':'30_000','curiosidad':'hermosos embalces'},
    'buenos aires':{'pais':'argentina','poblacion':'1_000_000','curiosidad':'ciudad que nunca duerme'},
    'resistencia':{'pais':'argentina','poblacion':'50_000','curiosidad':'una ciudad de paso'}
    }

for ciudad,datos in ciudades.items():
    print(f'\nla ciudad de: {ciudad}')
    pais = f'{datos['pais']}'
    poblacion = f'{datos['poblacion']}'
    info = f'{datos['curiosidad']}'
    print(f'\testá en {pais}')
    print(f'\tcuenta con una poblacion de {poblacion}')
    print(f'\tes curioso que para mi sea / tenga {info}')
    
'''
• 6-12. Extensiones: Ahora estamos trabajando con ejemplos lo
suficientemente complejos como para ser ampliados de distintas maneras.
Elija uno de los programas de ejemplo de este capítulo y amplíelo añadiendo
claves y valores nuevos, cambiando el contexto del programa o mejorando el
formato de la salida.
'''


print('\n RETORNAR DICCIONARIO')

def constriur_persona(first_name,last_name):
    person = {'first':first_name,'last':last_name} #guardamos los parametros con formato diccionario
    return person

person = constriur_persona('oliver','atom')
print(person)

print('\n RETORNAR DICCIONARIO CON PARAMETRO OPCIONAL')

def build_person(first_name, last_name, age=None):
#"""Devuelve un diccionario de información sobre una persona."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
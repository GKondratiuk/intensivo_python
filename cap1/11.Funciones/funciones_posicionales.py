#Cuando llamamos a una función, Python debe asociar cada
#argumento de la llamada con un parámetro de la definición. La
#forma más fácil de hacerlo se basa en el orden de los argumentos
#proporcionados. Los valores asociados así se denominan
#"argumentos posicionales".
print('\n FUNCIONES EN BASE AL ORDEN DE LOS ARGUMENTOS')

def describir_animal(animal,nombre):
    print(f'Mi mascota es un/a {animal}')
    print(f'Su nombre es {nombre}')
    print(f'mi {animal} se llama {nombre}')
    
describir_animal('gato','chimuelo')
describir_animal('chimuelo','gato')

print('\n FUNCIONES EN BASE A PALABRA CLAVE')
#Los argumentos de palabra clave nos evitan tener que
#preocuparnos por el orden correcto de los argumentos

def describir_animal(animal,nombre):
    print(f'Mi mascota es un/a {animal}')
    print(f'Su nombre es {nombre}')
    print(f'mi {animal} se llama {nombre}')

describir_animal(nombre='chimuelo',animal='gato') #es una forma mas larga de pasar los argumentos pero evitaremos confuciones

print('\n VALORES PREDETERMINADOS')
#Usar valores predeterminados permite
#simplificar las llamadas a funciones y aclarar de qué forma se suelen
#utilizar nuestras funciones.

def describir_animal(animal,nombre='chimuelo'):
    print(f'Mi mascota es un/a {animal}')
    print(f'Su nombre es {nombre}')
    print(f'mi {animal} se llama {nombre}')
    
describir_animal('gato')#definimos solo un argumento, el otro ya esta predeterminado
#para describir un nombre que no sea chimuelo deberemos utilizar la funcion de la siguiente manera
describir_animal(nombre='esteban',animal='gato') #palabras claves

print('\n LLAMADAS A FUNCIONES EQUIVALENTES')

'''
a menudo tendrá varias formas equivalentes de llamar a una función.
Considere la siguiente definición para describe_pet() con un valor
predeterminado:
def describe_pet(pet_name, animal_type='dog'):

# Un perro llamado Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# Un hámster llamado Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
'''


    
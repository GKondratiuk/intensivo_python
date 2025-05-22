'''
Una función no siempre tiene por qué mostrar su salida
directamente. En vez de eso, puede procesar datos y devolver un
valor o un conjunto de valores.
'''

def nombre_completo(nombre,apellido):
    full_name = f'{nombre} {apellido}' # la variable toma los valores, siempre hay que crearla
    return full_name

warcraft = nombre_completo('Groom','Hellscream') #variable que toma el valor de la funcion. Crearla siempre
print(warcraft)

print('\n ARGUMENTO OPCIONAL')
#A veces, tiene sentido hacer que un argumento sea opcional para
#que la gente que usa la función pueda decidir si incluir información
#adicional o no.
#Ejemplos: nombres completos, primer, segundo o apellido

def nombre_completo(primer_nombre,segundo_nombre,tercer_nombre): # imprmie nombre completo
    full_name = f'{primer_nombre} {segundo_nombre} {tercer_nombre}'
    return full_name

musico = nombre_completo('Johan','Sebastian','Bach')
print(musico) # imprime nombre completo


def nombre_completo(primer_nombre,tercer_nombre,segundo_nombre=''): # imprmie nombre completo
    if segundo_nombre: # si existe segundo nombre, si hay segundo nombre
        full_name = f'{primer_nombre} {segundo_nombre} {tercer_nombre}'
        return full_name
    else:
        full_name = f'{primer_nombre} {tercer_nombre}'
        return full_name
        

musico = nombre_completo('Johan','Bach')
print(musico) # imprime nombre completo o sin segundo nombre
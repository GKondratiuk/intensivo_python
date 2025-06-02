'''
Python utiliza objetos especiales llamados "excepciones" para
administrar los errores que surjan durante la ejecución de un
programa.
Esto hace que el programa no se detenga abruptamente.
por ejemplo en el caso de intentar dividir por cero
para controlar esto utilizaremos los codigos try-except
'''
try:
    print(5/0)

except ZeroDivisionError:
    print('No se puede dividir por 0')
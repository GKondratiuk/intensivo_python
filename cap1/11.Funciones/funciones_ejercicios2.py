

#• 8-3. Camiseta: Escriba una función llamada hacer_camiseta() que acepte
#una talla y un texto para un mensaje que habría que imprimir en la camiseta.
#La función debería imprimir una frase resumiendo la talla de la camiseta y el
#mensaje impreso.
#Llame a la función una vez con argumentos posicionales para hacer una
#camiseta. Llame a la función por segunda vez usando argumentos de palabra
#clave.

print(f'\n FUNCION CON PRAM. OPCIONALES')
def hacer_camiseta(talla,mensaje):
    print(f'esta es una camiseta {talla}')
    print(f'Con el logo de {mensaje}')
    
hacer_camiseta('XL','HERMETICA')

print(f'\n FUNCION CON CLAVE')

hacer_camiseta(mensaje= 'LOGOS',talla='S') 

#• 8-4. Camisetas grandes: Modifique la función hacer_camiseta () para
#que las camisetas sean grandes por defecto con un mensaje que diga "Me
#encanta Python". Haga una camiseta grande y una mediana con el mensaje
#predeterminado y una de cualquier talla con un mensaje diferente.

print(f'\n FUNCION CON PRAM. x DEFECTO')

def hacer_camisetas(talla='GRANDE',mensaje='I LOVE PYTHON'):
    print(f'esta es una camiseta {talla}')
    print(f'Con el logo de {mensaje}')
    
hacer_camisetas()

'''
PRUÉBELO
• 8-5. Ciudades: Escriba una función llamada describir_ciudad() que
acepte el nombre de una ciudad y su país. La función debería imprimir una
oración simple, como "Reikiavik está en Islandia". Dé al parámetro del país
un valor predeterminado. Llame a la función para tres ciudades diferentes,
con al menos una que no esté en el país predeterminado.
'''

print(f'\n CIUDADES')

def describir_ciudad(nombre,pais='Argentina'):
    print(f'la ciudad de {nombre} esta en {pais}')
    
describir_ciudad('Rosario')
describir_ciudad('San Rafael')
describir_ciudad('Munich','Alemania')
    
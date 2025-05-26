


'''
• 5-1. Pruebas condicionales: Escriba una serie de pruebas condicionales.
Imprima una frase describiendo cada prueba y su predicción para el
resultado. Su código debería tener un aspecto similar a esto:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

• Examine los resultados y asegúrese de comprender por qué cada línea se
evalúa como True o False.

• Cree al menos 10 pruebas y haga que 5, como mínimo, se evalúen como
True y otras 5 como False.
'''
print('Verdadero o falso:')
objeto = 'pelota'
edad = 18
print(objeto == 'pelota')#verdadero porque el valor de la variable coincide con la variable
print(objeto == 'auto') #falso
print(objeto != 'Pelota')#Verdadero porque reconoce mayusculas
print(edad == 18) #verdadero
print(edad == '18') #falso porque esto es una cadena, y va variable contiene un INT 

#Pruebas con el método lower().
print('\n Metodo lower')

motos_mayus = []
motos = ['suzuki','honda','yamaha']
for moto in motos:
    if moto == 'suzuki':
        print(f'Mi moto favorita es {moto.title()}')
    elif moto == 'yamaha':
        print(f'la peor moto es {moto.lower()}')
    moto_mayus = moto.upper()
    motos_mayus.append(moto_mayus)

print(motos_mayus)

#• Pruebas numéricas que impliquen igualdad y desigualdad, mayor que y
#menor que, mayor o igual que y menor o igual que.

print('\n mayor, igual, menor')
a = 20
b = 15

if a > b:
    print(f'{a} es mayor que {b}')
    
if b > a:
    print(f'{b} es mayor que {a}')

a == b

if a > b or a < b:
    print('esto se va a imprimir siempre')

if a < b and  b < a:
    print('esto TAMBIEN se imprime siempre')

print('\nprobamos si un elemento esta en la lista o no')
#• Prueba para comprobar si un elemento está en una lista.
for moto in motos:
    if moto == 'suzuki':
        print(f'{moto} esta en la lista')

if 'suzuki' in motos:
    print('ya te dijimos que esta')
#• Prueba para comprobar si un elemento no está en una lista.
prohibidos = ['Marcos','Javier','Ezequiel']

if 'Maxi' not in prohibidos:
    print('maxi pasa')

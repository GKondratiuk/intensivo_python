'''
A menudo, conviene empezar con una lista existente y crear una
totalmente nueva basada en ella. Veamos cómo hacerlo copiando
una lista. Analizaremos una situación en la que copiar una lista es
útil.
Para copiar una lista, podemos hacer un trozo que incluya toda la
lista original omitiendo el primer índice y el segundo ([:]). Esto dice
a Python que haga un trozo que empiece en el primer elemento y
termine en el último, creando una copia de toda la lista.
Por ejemplo, imagine que tenemos una lista de nuestra comida
favorita y queremos hacer otra con la que le gusta a un amigo. A
este amigo le gusta todo lo que hay en nuestra lista, así que
podemos crear la suya copiando la nuestra:
'''
# copiamo una lista
my_food = ['pizza','asado','milanesas','papas']
friend_food = my_food[:] 
#lo que hacen los [:] es que se copien los elementos de la lista
# si utilizamos la sintaxis friend_food = my_food hace 1 lista igual a la otra y eso es otra cosa

print('mis comidas favoritas son:')
print(my_food)
print('Las comidas favofitas de mi amigo son: ')
print(friend_food)

my_food.append('falafel')
friend_food.append('chipa')

print('me agregue una nueva comida:')
print(my_food)
print('a mi amigo tambien')
print(friend_food)
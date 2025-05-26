#creamos un perro
class Dog: #las clases siempre van en mayusculas, creamos una clase perro
    def __init__(self,name,age): #metodo init
        self.name = name #self brinda acceso a los atributos
        self.age = age 
        #metodo sit
    def sit(self):#self para que tenga acceso a los atributos
        print(f'{self.name} ahora está sentado')
        #metodo roll over
    def roll_over(self):#self para que tenga acceso a los atributos
        print(f'{self.name} hace una pirueta')

my_dog = Dog('willy',6) #creamos un nuevo perro, instanciamos 

print(f"Mi perro se llama {my_dog.name} y tiene {my_dog.age} años de edad")

my_dog.sit() #mi perro puede sentarse por el método de la clase
my_dog.roll_over()
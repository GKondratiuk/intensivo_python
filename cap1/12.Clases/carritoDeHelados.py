class Restaurante: #  clase restaurante
    
    def __init__(self,nombre_restaurante,tipo_cocina): #metodo init
        
        self.nombre_restaurante = nombre_restaurante #nombre restaurante se vincula a este restaurante
        self.tipo_cocina = tipo_cocina
        
        #creamos un nuevo metodo
    def describir_restaurante(self): #self porque va a recibir los atributos de ''esta'' clase
        print(f"Bienvenidos a {self.nombre_restaurante.title()}") #va a recibir el nombre de #este restaurante y esta cocina
        print(f"típica cocina {self.tipo_cocina.title()}")
        #creamos otro metodo
    def abrir_restaurante(self):
        print('El restaurante se encuentra abierto')
        




class CarritoDeHelados(Restaurante): #creacion de clase hija
    def __init__(self,nombre_restaurante,tipo_cocina): # metodo init con parametros
        super().__init__(nombre_restaurante,tipo_cocina) #herencia
        self.sabores = ['menta','limon'] #atributo nuevo de la clase hija
        
    def mostrar_sabores(self): #creamos los metodos de la clase hija
        for sabor in self.sabores:
            print(f'{sabor}')


mi_carrito = CarritoDeHelados('Giorgio','Carrito de helados')
#mi_carrito.sabores = ['menta']
mi_carrito.mostrar_sabores()
            
            
            
        
    
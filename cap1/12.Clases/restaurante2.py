class Restaurante: #  clase restaurante
    
    def __init__(self,nombre_restaurante,tipo_cocina): #metodo init y sus parametros(argumentos)
        
        self.nombre_restaurante = nombre_restaurante #nombre restaurante se vincula a este restaurante
        self.tipo_cocina = tipo_cocina #atributo
        self.numero_servido = 1 #atributo
        
        #creamos un nuevo metodo
    def describir_restaurante(self): #self porque va a recibir los atributos de ''esta'' clase
        print(f"Bienvenidos a {self.nombre_restaurante.title()}") #va a recibir el nombre de #este restaurante y esta cocina
        print(f"típica cocina {self.tipo_cocina.title()}")
        #creamos otro metodo
    def abrir_restaurante(self):
        print('El restaurante se encuentra abierto')
        
    def establecer_numero_servido(self,numero_servido): #creamos metodo para aumentar el numero de clientes servidos
        self.numero_servido = numero_servido 
        
    def incrementar_numero_servido(self,numero_servido): #nuevo metodo
        self.numero_servido += numero_servido  #incrementa el numero de servidos
        
#instanciamos

restaurante = Restaurante('restaurante criollo','cocina criolla')

print(f"El numero de clientes a los que hemos servido es de {restaurante.numero_servido}")

restaurante.establecer_numero_servido(5) #modificamos el numero de clientes servidos
print(f"El nuevo numero de clientes a los que hemos servido es de {restaurante.numero_servido}")

restaurante.incrementar_numero_servido(10)

print(f"Los dias lunes el total de clientes servidos puede ser {restaurante.numero_servido}")
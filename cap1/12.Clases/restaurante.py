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
        

#instanciamos un restaurante

restaurante_criollo = Restaurante('restaurante criollo','cocina criolla') #creamos un nuevo restaurante

print(f"Esto es {restaurante_criollo.nombre_restaurante}, hacemos {restaurante_criollo.tipo_cocina}")

restaurante_criollo.describir_restaurante() #llamamos al método 

restaurante_criollo.abrir_restaurante() #llamamos al otro metodo

print("\n***************************************")
print("CREAMOS 3 INSTANCIAS MAS DE RESTAURANTES")
print("Y LLAMAMOS A 1 DE SUS METODOS")
print("***************************************")

restaurante_arabe = Restaurante('restaurante arabe','cocina arabe')
restaurante_arabe.describir_restaurante()
print("***************************************")

restaurante_italiano = Restaurante('restaurante italiano','cocina italiana')
restaurante_italiano.describir_restaurante()
print("***************************************")

restaurante_peruano = Restaurante('restaurante peruano','cocina peruana')
restaurante_peruano.describir_restaurante()
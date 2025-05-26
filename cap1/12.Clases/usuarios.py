#creamos una nueva clase
class Usuario: #creamos el metodo init
    def __init__(self,nombre,apellido,password,mail): # colocamos sus atributos
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.mail = mail
        #creamos los metodos
    def describir_usuario(self): #siempre llamamos desde self
        print(f"Usuario:{self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Contraseña: {self.password}")
        print(f"Email: {self.mail}")
    
    def saludar_usuario(self):
        print(f"Hola {self.nombre} te estamos saludando")
        
#instanciamos nuevos usuarios

usuario_uno = Usuario('willy','box','1234','willy@mail.com')
usuario_uno.describir_usuario()
usuario_uno.saludar_usuario()
print("\n***************************************")
print("CREAMOS MAS INSTANCIAS DE USUARIOS")
print("***************************************")
            
usuario_dos = Usuario('carlos','slash','calleFalsa','cslash@mail.com')
usuario_dos.describir_usuario()
usuario_dos.saludar_usuario()

print("\n***************************************")
print("CREAMOS 3 INSTANCIAS MAS DE RESTAURANTES")
print("Y LLAMAMOS A 1 DE SUS METODOS")
print("***************************************")

usuario_tres = Usuario('Pacoco','Castro','qwerty','pcastro@mail.com')
usuario_tres.describir_usuario()
usuario_tres.saludar_usuario()
        
'''
9-4. Número servido: Empiece con el programa del ejercicio 9-1. Añada
un atributo llamado número_servido con un valor predeterminado de 0. Cree
una instancia llamada restaurante a partir de esta clase. Imprima el número
de clientes a los que ha servido el restaurante, cambie ese valor y vuelva a
imprimirlo.
Añada un método llamado establecer_número_servido() que le permita
configurar el número de clientes a los que se ha servido. Llámelo con un
número nuevo y vuelva a imprimir el valor.
Añada un método llamado incrementar_número_servido() que le permita
incrementar el número de clientes atendidos. Llámelo con cualquier número
que pueda representar a cuántos clientes se ha servido en un día laborable
normal.
'''       
    
    
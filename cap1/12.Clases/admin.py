class Usuario: #creamos el metodo init
    def __init__(self,nombre,apellido,password,mail): # colocamos sus parametros
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.mail = mail
        self.intentos_inicio = 0
        
        #creamos los metodos
    def describir_usuario(self): #siempre llamamos desde self
        print(f"Usuario:{self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Contraseña: {self.password}")
        print(f"Email: {self.mail}")
    
    def saludar_usuario(self):
        print(f"Hola {self.nombre} te estamos saludando")
    
    def incrementar_intentos_inicio(self):
        self.intentos_inicio += 1
        print(f'intentos de inicio = {self.intentos_inicio}')
    
    def restablecer_intentos_inicio(self):
        self.intentos_inicio = 0
        

class Admin(Usuario): #hija que hereda
    def __init__(self,nombre,apellido,password,mail): #parametros 
        super().__init__(nombre,apellido,password,mail)
        self.privilegios = []
    
    def mostrar_privilegios(self):
        print('sus privilegios como admin son:')
        for privilegio in self.privilegios:
            print(privilegio)
        
willy = Admin('willy','box','1234','wbox@mail.com')

willy.privilegios = [
    'ver contraseñas',
    'bannear gente',
    'kickear gente',
]

willy.mostrar_privilegios()
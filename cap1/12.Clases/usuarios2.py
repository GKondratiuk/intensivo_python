#creamos una nueva clase
class Usuario: #creamos el metodo init
    def __init__(self,nombre,apellido,password,mail): # colocamos sus atributos
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
        
usuario_uno = Usuario('willy','box',1234,'wbox@mail.com')

usuario_uno.saludar_usuario()
usuario_uno.incrementar_intentos_inicio()
usuario_uno.incrementar_intentos_inicio()
usuario_uno.incrementar_intentos_inicio()
usuario_uno.restablecer_intentos_inicio()
usuario_uno.incrementar_intentos_inicio()
        

'''
9-5. Intentos de inicio de sesión: Añada un atributo intentos_inicio a
la
clase
Usuario
del
ejercicio
9-3.
Escriba
un
método
llamado
incrementar_intentos_inicio() que aumente el valor de intentos_inicio en
1. Escriba otro método llamado restablecer_intentos_inicio() que
restablezca el valor de intentos_inicio a 0.
Haga una instancia de la clase Usuario y llame varias veces a
incrementar_intentos_inicio(). Imprima el valor de intentos_inicio para
asegurarse de que se ha incrementado correctamente y luego llame a
restablecer_intentos_inicio(). Vuelva a imprimir intentos_inicio para
asegurarse de que se ha restablecido a 0.
'''
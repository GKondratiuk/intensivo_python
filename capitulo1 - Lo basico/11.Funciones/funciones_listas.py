'''
Supongamos que tenemos una lista de usuarios y queremos
imprimir un mensaje para saludar a cada uno. El siguiente ejemplo
envía una lista de nombres a una función llamada greet_users(), que
saluda a cada persona de la lista individualmente:
'''

def greet_users(names):
#"""Imprime un saludo sencillo para cada usuario de la lista."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

'''
Piense en una empresa que crea modelos en impresión 3D de los
diseños que envían los usuarios. Los diseños que hay que imprimir
se guardan en una lista y, una vez impresos, pasan a una lista
aparte. El siguiente código hace esto sin usar funciones:
'''

# Empieza con unos diseños que hay que imprimir.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula la impresión de cada diseño hasta que no queda ninguno.
# Mueve cada diseño a completed_models después de la impresión.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Muestra todos los modelos completados.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    

def print_models(unprinted_designs, completed_models):
#Simula imprimir cada diseño, hasta que no queda ninguno.
#Mueve cada diseño a completed_models después de la impresión.
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
#Muestra todos los modelos que se han imprimido.
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

'''
PRUÉBELO
• 8-9. Mensajes: Haga una lista con una serie de mensajes de texto cortos.
Pásela a una función llamada mostrar_mensajes() que imprima cada
mensaje.
• 8-10. Enviar mensajes: Empiece con una copia del programa del
ejercicio 8-9. Escriba una función llamada enviar_mensajes() que imprima
cada mensaje de texto y lo mueva a una nueva lista denominada
mensajes_enviados a medida que imprime. Después de llamar a la función,
imprima ambas listas para asegurarse de que los mensajes se han movido
correctamente.
• 8-11. Mensajes archivados: A partir del trabajo realizado para el
ejercicio 8-10, llame a la función enviar_mensajes() con una copia de la
lista de mensajes. Después, imprima ambas listas para confirmar que la lista
original conserva sus mensajes.
'''
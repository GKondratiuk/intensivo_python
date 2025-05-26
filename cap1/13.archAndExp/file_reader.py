from pathlib import Path #importamos clase 

path = Path('pi_digits.txt') #creamos un objeto que representa al archivo de texto y le asignamos variable, aca se especifican als rutas
contents = path.read_text() #metodo que utilizamos para leer los contenidos 

lines = contents.splitlines() #splitline devuelve una lista con todas las lineas del archivo
pi_string = ''

for line in lines:
    pi_string += line.lstrip()
    
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the firs millon digits of pi !")
else:
    print("Your birthday does not appear in the firs million digits of pi.")
    
    print(f"{pi_string[:1000000]}...")
    print(len(pi_string))
    
    '''
leído de un archivo, podemos analizar su contenido de cualquier
forma que imaginemos.
PRUÉBELO
• 10-1. Aprender Python: Abra un archivo nuevo en su editor de texto y
escriba unas líneas resumiendo lo que ha aprendido sobre Python hasta
ahora. Empiece cada línea con la frase "En Python se puede...". Guarde el
archivo como aprender_python.txt en el mismo directorio que los ejercicios
de este capítulo. Escriba un programa que lea el archivo e imprima dos veces
lo que ha escrito: una vez leyendo el archivo completo y otra pasando en
bucle por el objeto del archivo.
• 10-2. Aprender C: Puede usar el método replace() para sustituir cualquier
palabra de una cadena por otra diferente. Aquí tiene un ejemplo rápido para
cambiar 'perro' por 'gato' en una oración:
>>> message = "Me encantan los perros."
>>> message.replace('perro', 'gato')
'Me encantan los gatos.'
Lea cada línea del archivo que acaba de crear, aprender_python.txt, y cambie
la palabra Python por el nombre de otro lenguaje, como C. Imprima en la
pantalla las líneas modificadas.
• 10-3. Un código más sencillo: El programa file_reader_py en esta
sección utiliza una variable temporal, lines, para mostrar el funcionamiento
de splitlines(). Puede saltarse la parte de la variable temporal y pasar un
bucle directamente por la lista que devuelve splitlines():
for line in contents.splitlines():
    
    '''
filename = 'aprender_python.txt' #agregamos el archivo a una variable

with open(filename) as f: #abrimos el archivo y le ponemos un alias
    contents = f.read() #le colocamos el metodo read() y lo colocamos en una variable

print(contents)

#Lo pasamos por un bucle for lo que nos permite recorrer cada dato del archivo 
#para despues podes trabajar con el
print('\n esto pasa por un for')
with open(filename) as f: #abrimos el archivo y le colocamos un alias
    lines = f.readlines() #guardamos su contenido en una variable
    for line in lines:
        print(line)
        
# utilizamos remplace para remplazar partes del texto
print('\n Reemplazamos por java')
with open(filename) as f:
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        print(line.replace('python','java'))
    
    
    

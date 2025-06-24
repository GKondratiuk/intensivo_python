from django.db import models
# Create your models here.
#creamos una clase topic que hereda de models
class Topic(models.Model): #un tema sobre lo que esta aprendiendo el usuario
    text = models.CharField(max_length=200) #atributo text - crea caja de texto
    date_added = models.DateTimeField(auto_now_add=True)#atributo registra fecha y hora
    
    def __str__(self): #devuelve una representacion del modelo como cadena
        return self.text # devuelve el texto
# para ver todos los tipos de campos que podemos utilizar en un modelo podemos consultar
#en la pagina oficial de django "referencia de campos de modelo"

#Para activar nuestros modelos deberemos pedirle a django que incluya nuestra app al proyecto
#desde el archivo settings.py en el directorio principal del proyecto "learning log"

class Entry(models.Model):#hereda de la clase model
    "Algo especifico aprendido sobre algun tema"
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) #topic como instancia de la clave foranea
    #termino que se utiliza para referenciar asociacion entre datos 
    #y que cuando uno de estos datos sea borrado, se borraran tambien todos sus datos asociados en cascada 
    text = models.TextField()#campo de entrada
    date_added = models.DateTimeField(auto_now_add=True)#registra el momento que se realiza la entrada
    
    class Meta:#metodo para referirse a varias entrada como 'entries
        verbose_name_plural = 'entries'
        
    def __str__(self):
        "Devuelve una cadena simple que representa la entrada"
        return f"{self.text[:50]}..." #metodo para mostrar solo los primeros 50 caracteres de las entradas 
    
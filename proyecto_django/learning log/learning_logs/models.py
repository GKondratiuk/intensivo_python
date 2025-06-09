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
#desde el archivo settings.py en el directorio principal del proyecto
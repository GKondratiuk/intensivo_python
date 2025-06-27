from django.db import models

# Create your models here.
#defino modelo pizzas por medio de una clase 

class Pizza(models.Model):
    name = models.CharField(max_length=70) #ctrl + space(muestra los atributos disponibles)
    
    def __str__(self):
        return self.name #retornamos el nombre
    
class Ingrediente(models.Model):
    pizza = models.ForeignKey(Pizza,on_delete=models.CASCADE) #clave foranea para pizza
    name = models.TextField()
    
    def __str__(self):
        return f'{self.name[:50]}...'#retornamos el nombre con una limitacion 
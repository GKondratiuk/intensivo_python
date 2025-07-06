from django.db import models
#Estas clases se van a convertir en nuestras bases de datos
#Cada vez que se realiza un cambio hay que migrar con makemigrations, migrate
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    Project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False) #si el proyecto está finalizado o no 
    
    def __str__(self):
        return self.title + ' - ' + self.Project.name
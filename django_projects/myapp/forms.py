#Creamos nuestro formulario a partir de este archivo, despues lo importamos en views.py
from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", 
    max_length=200, widget=forms.TextInput(attrs={'class': 'input'})) #agrega estilo desde css
    description = forms.CharField(label="descripcion de la tarea",widget=forms.Textarea
    (attrs={'class': 'input'})) # todos reciben datos
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200,
    widget=forms.TextInput(attrs={'class':'input'}))
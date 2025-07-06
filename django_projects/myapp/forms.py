#Creamos nuestro formulario a partir de este archivo, despues lo importamos en views.py
from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label="descripcion de la tarea",widget=forms.Textarea)
    
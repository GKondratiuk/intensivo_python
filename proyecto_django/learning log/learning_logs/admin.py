from django.contrib import admin
from .models import Topic #de la carpeta models importamos Topic
from .models import Entry #Registramos el modelo Entry tambien para poder manejarlo como admin.
#todo estos cambios seran visualiados desde la agina admin

admin.site.register(Topic)#esto le dice a django que gestione nuestro modelo a travez del sitio admin
#ingresamos a http:localhost:8000/admin , ingresamos con nombre de usuario y contrasenia para 
#poder administrar el sitio
# Register your models here.
admin.site.register(Entry)
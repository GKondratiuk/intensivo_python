from django.urls import path #importacion necesaria para urls
from . import views

app_name = 'pizzas' #ayuda a django a distinguir de todas las urls
urlpatterns = [ #lista de paginas individuales que va a tener nuestra app 
    path('',views.index,name='index')
    #esto es : desde la url principal se mostrara el index de nombre index
]
'''
este es el paso 1 B - Con este paso completamos la definicion de las urls, despues de aca hay que ir al 
archivo views.py para el paso 2, escritura de las vistas
'''
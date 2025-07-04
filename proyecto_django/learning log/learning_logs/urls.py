#Definimos patrones de URL para learning_logs
from django.urls import path #Importacion necesaria para asignar urls
from . import views

app_name = 'learning_logs' #ayuda a django a distinguir entre todos los archivos urls
urlpatterns = [#lista de paginas individuales que se pueden solicitar a la app 
    #pagina de inicio
    path('',views.index,name='index'),#3 parametros, la vista la escribimos desde views.py
    #cuando definimos este codigo django buscara el archivo iindex en view, la crearemos desde alli
    #pagina que muestra todos lo temas
    path('topics/',views.topics,name='topics'),
    #pagina de detalles sobre un tema individual
    path('topics/<int:topic_id>/',views.topic,name='topic') #esta pagina espera una id
]

'''pagina que muestra todos los temas
Este es el paso 1-B, Seguimos definiendo URLS despues de aqui hay que ir al archivo views.py para 
definir la estructura de las vistas
'''
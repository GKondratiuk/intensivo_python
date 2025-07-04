from django.shortcuts import render
from .models import Topic # importamos topic desde models
# Create your views here.
def index(request):
    #pagina de inicio para learning logs
    return render(request, 'learning_logs/index.html')
#ahora debemos crear la carpeta 'templates' en la app y dentro de ella otra carpeta con el nombre de la app
#y dentro de esa carpeta una archivo llamado index.html.nos vemos alli 

def topics(request):#topics necesita el parametro request que recibe del servidor
    #muestra todos los temas
    topics = Topic.objects.order_by('date_added') #peticion a la base de datos
    context = {'topics':topics}#definimos de que manera mostraremos la informacion
    return render(request, 'learning_logs/topics.html',context) #retornamos

def topic(request,topic_id):
    #muetra un tema concreto y todas sus entradas 
    topic = Topic.objects.get(id=topic_id)#de todos los objetos de topic dame la id
    entries = topic.entry_set.order_by('-date_added') #ordenar las entradas por fecha
    context = {'topic':topic,'entries':entries}
    return render(request, 'learing_logs/topic.html',context) #devolvemos

'''
Este es el paso 2 desde aqui renderizamos, creamos las vistas y creamos la carpeta templates desde la app.
nos vemos alli aora continuar con el paso 3
'''
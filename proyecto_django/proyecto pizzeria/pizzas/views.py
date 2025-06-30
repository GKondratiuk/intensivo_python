from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pizzas/index.html') #renderizamos la vista del menu principal 

'''
hasta aqui el paso 2 
para empezar con el paso 3 debemos crear la carpeta 'templates' dentro de la app con otra carpeta 
con el mismo nombre del proyecto y dentro de lla un archivo index.html. quedaria de la siguiente manera
templates/pizzas/index.html
'''
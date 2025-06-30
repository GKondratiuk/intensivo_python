"""
URL configuration for learning_log project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# aca configuramos las URLs necesarias para el proyecto, despues de incluir las urls desde la app aqui,
#hay que crear el archivo urls.py desde la app 
from django.contrib import admin # importa modulo admin
from django.urls import path, include # importa funcion para crear las rutas, incluimos include

urlpatterns = [
    path('admin/', admin.site.urls),#define las url del sitio admin
    #pagina de inicio
    path('',include('learning_logs.urls')), #agregamos learning logs
]
'''
este es el paso 1-A - ASIGNAR URLS
Despues de incluir la URLs aqui, debemos crear un archivo urls.py en la app del proyecto.
'''
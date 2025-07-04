from django.http import HttpResponse
from .models import Project,Task
from django.shortcuts import render, get_object_or_404 #para que no caiga el servidor

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects = list(Project.objects.values()) #recuperamos la lista de proyectos desde models y de la bd
    return render(request, "projects.html")

def tasks(request):
    #task = Task.objects.get(title=title)
    return render(request, 'tasks.html')

def hello(request,username):
    return HttpResponse("<h1> Hello %s </h1>" %username) #guarda y devuelve username
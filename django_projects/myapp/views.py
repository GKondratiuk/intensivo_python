from django.http import HttpResponse
from .models import Project,Task
from django.shortcuts import render,redirect, get_object_or_404 #para que no caiga el servidor
from .forms import CreateNewTask, CreateNewProject #importamos el formulario
#estas vistas van a estar cosntantemente interactuando con nuestro html
# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html',{
        'title': title
    })

def about(request):
    username = 'Guille'
    return render(request, 'about.html',{
        'username': username #podemos pasarle funciones al html
    })

def projects(request):
    #projects = list(Project.objects.values()) #recuperamos la lista de proyectos desde models y de la bd
    projects = Project.objects.all()
    return render(request, "projects/projects.html",{
        'projects': projects 
    })

def tasks(request):
    #task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html',{
        'tasks': tasks
    })

def hello(request,username):
    return HttpResponse("<h1> Hello %s </h1>" %username) #guarda y devuelve username

def create_task(request): #request
    if request.method == 'GET':
        #show interface
        return render(request,'tasks/create_task.html', {
        'form': CreateNewTask() 
    }) #1. creamos el html. 2. nos venimos aqui. 3-nos vamos a urls.
    else:
          Task.objects.create(title=request.POST['title'], 
          description=request.POST['description'], Project_id=2) #guardamos info del formulario relacionado al proyecto con id 2. a la base de datos 
          return redirect('tasks')
      
def create_project(request):
        if request.method == 'GET':
            return render(request,'projects/create_project.html', {
                'form': CreateNewProject()
            })
        else:
            Project.objects.create(name=request.POST["name"])
            redirect('projects')

    
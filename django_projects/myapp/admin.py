from django.contrib import admin
from .models import Project, Task #importamos desde models

# Register your models here.
admin.site.register(Project) #traemos la clase project
admin.site.register(Task)
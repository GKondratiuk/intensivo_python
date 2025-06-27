from django.contrib import admin
from .models import Pizza
from .models import Ingrediente
# Register your models here.
admin.site.register(Pizza)
admin.site.register(Ingrediente)
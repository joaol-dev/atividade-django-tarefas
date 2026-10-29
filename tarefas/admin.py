# Register your models here.

from django.contrib import admin
from .models import Categoria, Tarefa

admin.site.register(Categoria)
admin.site.register(Tarefa)

from django.contrib.auth.models import User
User.objects.values_list("username", "is_staff", "is_superuser")
# todos/admin.py
#this can interact with our data if we register the model
from django.contrib import admin
# Register your models here.
from .models import Todo

admin.site.register(Todo)

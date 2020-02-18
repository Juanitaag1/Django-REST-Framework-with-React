#from django.shortcuts import render

# Create your views here.
# todos/views.py
#41
from rest_framework import generics
#42 from tutorial
from .models import Todo
from .serializers import TodoSerializer


class ListTodo(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

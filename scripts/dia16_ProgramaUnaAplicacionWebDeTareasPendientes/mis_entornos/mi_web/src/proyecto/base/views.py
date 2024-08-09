from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from . models import Tarea

# Create your views here.

# ListView es un tipo de página que visualiza una lista de objetos

class ListaPendientes(ListView): 
    model = Tarea

class DetalleTarea(DetailView):
    model = Tarea
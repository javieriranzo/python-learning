from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Tarea

# Create your views here.

# ListView es un tipo de página que visualiza una lista de objetos

class ListaPendientes(ListView): 
    model = Tarea
    context_object_name = 'lista_tareas'
    # Si se quiere cambiar el nombre de la template se tiene que utilizar
    # template_name = 'base/nombre_template

class DetalleTarea(DetailView):
    model = Tarea
    context_object_name = 'detalle_tarea'
    # Si se quiere cambiar el nombre de la template se tiene que utilizar
    # template_name = 'base/nombre_template

class CrearTarea(CreateView): 
    model = Tarea
    # Este atributo es para que cree los campos para todos los campos del model Tarea. Si solo se quisiese campos específicos hay que pasarlos en modo lista
    fields = '__all__'
    # Cuando finalice la tarea con éxito, vuelve al home
    success_url = reverse_lazy('tareas') 
    # Si se quiere cambiar el nombre de la template se tiene que utilizar
    # template_name = 'base/nombre_template

class EditarTarea(UpdateView):
    model = Tarea
    # Este atributo es para que cree los campos para todos los campos del model Tarea. Si solo se quisiese campos específicos hay que pasarlos en modo lista
    fields = '__all__'
    # Cuando finalice la tarea con éxito, vuelve al home
    success_url = reverse_lazy('tareas')
    # Si se quiere cambiar el nombre de la template se tiene que utilizar
    # template_name = 'base/nombre_template

class EliminarTarea(DeleteView):
    model = Tarea
    context_object_name = 'lista_tareas'
    # Cuando finalice la tarea con éxito, vuelve al home
    success_url = reverse_lazy('tareas')

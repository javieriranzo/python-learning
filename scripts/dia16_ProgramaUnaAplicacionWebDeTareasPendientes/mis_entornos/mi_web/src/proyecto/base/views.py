from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from . models import Tarea

# Create your views here.

# ListView es un tipo de página que visualiza una lista de objetos

class Logueo(LoginView):
    template_name = 'base/login.html'
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tareas')
    
class PaginaRegistro(FormView): 
    template_name = 'base/registro_usuario.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tareas')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)
    
    def get(self, *args, **kwargs): 
        if self.request.user.is_authenticated:
            return redirect('tareas')
        return super(PaginaRegistro, self).get(*args, **kwargs)


class ListaPendientes(LoginRequiredMixin, ListView): # Se añade LoginRequiredMixin para que un usuario sin registrar pueda acceder a la funcion
    model = Tarea
    context_object_name = 'lista_tareas'
    # Si se quiere cambiar el nombre de la template se tiene que utilizar
    # template_name = 'base/nombre_template
    
    # Recibir solo las tareas creadas por un usuario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Para ver las tareas del usuario que está registrado en ese momento
        context['lista_tareas'] = context['lista_tareas'].filter(usuario = self.request.user)
        # Para ver solo las tareas no completas
        context['count'] = context['lista_tareas'].filter(completo = False)

        # Mostrar tareas buscadas en la caja de texto
        valor_buscado = self.request.GET.get('area_buscar') or ''
        if valor_buscado: 
            context['lista_tareas'] = context['lista_tareas'].filter(titulo__icontains=valor_buscado)
        context['valor_buscado'] = valor_buscado
        return context

class DetalleTarea(LoginRequiredMixin, DetailView): # Se añade LoginRequiredMixin para que un usuario sin registrar pueda acceder a la funcion
    model = Tarea
    context_object_name = 'detalle_tarea'
    # Si se quiere cambiar el nombre de la template se tiene que utilizar
    # template_name = 'base/nombre_template

class CrearTarea(LoginRequiredMixin, CreateView): # Se añade LoginRequiredMixin para que un usuario sin registrar pueda acceder a la funcion
    model = Tarea
    # Este atributo es para que cree los campos para todos los campos del model Tarea. Si solo se quisiese campos específicos hay que pasarlos en modo lista
    fields = ['titulo', 'descripcion', 'completo']
    # Cuando finalice la tarea con éxito, vuelve al home
    success_url = reverse_lazy('tareas') 
    # Si se quiere cambiar el nombre de la template se tiene que utilizar
    # template_name = 'base/nombre_template

    # Cuando se cree una tarea, no será necesario indicar el autor de la tarea, se asignará como autor el usuario registrado
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super(CrearTarea, self).form_valid(form)

class EditarTarea(LoginRequiredMixin, UpdateView): # Se añade LoginRequiredMixin para que un usuario sin registrar pueda acceder a la funcion
    model = Tarea
    # Este atributo es para que cree los campos para todos los campos del model Tarea. Si solo se quisiese campos específicos hay que pasarlos en modo lista
    fields = ['titulo', 'descripcion', 'completo']
    # Cuando finalice la tarea con éxito, vuelve al home
    success_url = reverse_lazy('tareas')
    # Si se quiere cambiar el nombre de la template se tiene que utilizar
    # template_name = 'base/nombre_template

class EliminarTarea(LoginRequiredMixin, DeleteView): # Se añade LoginRequiredMixin para que un usuario sin registrar pueda acceder a la funcion
    model = Tarea
    context_object_name = 'lista_tareas'
    # Cuando finalice la tarea con éxito, vuelve al home
    success_url = reverse_lazy('tareas')

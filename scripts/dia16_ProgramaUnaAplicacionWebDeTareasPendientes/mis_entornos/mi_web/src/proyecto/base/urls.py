from django.urls import path
from . views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', Logueo.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('registro_usuario/', PaginaRegistro.as_view(), name='registro_usuario'),
    path('', ListaPendientes.as_view(), name='tareas'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='detalle_tarea'),
    path('crear_tarea/', CrearTarea.as_view(), name='crear_tarea'),
    path('editar_tarea/<int:pk>', EditarTarea.as_view(), name='editar_tarea'),
    path('eliminar_tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar_tarea')
]
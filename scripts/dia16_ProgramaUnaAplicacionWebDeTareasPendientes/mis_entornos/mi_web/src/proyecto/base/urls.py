from django.urls import path
from . views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea

urlpatterns = [
    path('', ListaPendientes.as_view(), name='tareas'),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name='detalle_tarea'),
    path('crear_tarea/', CrearTarea.as_view(), name='crear_tarea'),
    path('editar_tarea/<int:pk>', EditarTarea.as_view(), name='editar_tarea'),
    path('eliminar_tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar_tarea'),
]
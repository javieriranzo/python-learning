from django.urls import path
from ._import views

urlpatterns = [
    path('', views.listaPendientes, name='pendientes')
]
from django.urls import path
from . import views

urlpatterns = [

    path(
        '',
        views.listar_destinos,
        name='listar_destinos'
    ),

    path(
        'nuevo/',
        views.añadir_destino,
        name='añadir_destino'
    ),

    path(
        'editar/<int:pk>/',
        views.modificar_destino,
        name='modificar_destino'
    ),

    path(
        'eliminar/<int:pk>/',
        views.eliminar_destino,
        name='eliminar_destino'
    ),
]
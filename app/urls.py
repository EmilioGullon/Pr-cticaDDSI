# En app/urls.py
from django.urls import path
from .views import listar_empleados, agregar_empleado, enlace_principal, listas, agregar

urlpatterns = [
    #path('home/', home, name='home'),
    #path('contacto/', contacto, name='contacto'),
    #path('galeria/', galeria, name='galeria'),
    #path('home/<str:username>', home, name='home'),
    path('listare/', listar_empleados, name='listar_empleados'),
    path('agregare/', agregar_empleado, name='agregar_empleado'),
    path('listas/', listas,name='listas'),
    path('agregar/', agregar,name='agregar'),
    path('', enlace_principal, name='enlace_principal'),
]

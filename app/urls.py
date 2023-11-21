# En app/urls.py
from django.urls import path
from .views import home,contacto, galeria, listar_empleados, agregar_empleado, agregar_socio

urlpatterns = [
    path('home/', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('home/<str:username>', home, name='home'),
    path('listare/', listar_empleados, name='listar_empleados'),
    path('agregare/', agregar_empleado, name='agregar_empleado'),
    path('agregars/', agregar_socio, name='agregar_socio'),

]

# En app/urls.py
from django.urls import path
from .views import home,contacto, galeria, listar_empleados, agregar_empleado

urlpatterns = [
    path('home/', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('home/<str:username>', home, name='home'),
    path('listar/', listar_empleados, name='listar_empleados'),
    path('agregar/', agregar_empleado, name='agregar_empleado'),

]

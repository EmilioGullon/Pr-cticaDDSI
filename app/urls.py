# En app/urls.py
from django.urls import path
from .views import home,contacto, galeria, listar_empleados, agregar_empleado, agregar_socio, listar_socios, agregar_anuncio, listar_anuncios

urlpatterns = [
    path('home/', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('home/<str:username>', home, name='home'),
    path('listare/', listar_empleados, name='listar_empleados'),
    path('agregare/', agregar_empleado, name='agregar_empleado'),
    path('agregars/', agregar_socio, name='agregar_socio'),
    path('listars/', listar_socios, name='listar_socios'),
    path('agregara/', agregar_anuncio, name='agregar_anuncio'),
    path('listara/', listar_anuncios, name='listar_anuncios'),

]

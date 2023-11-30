# En app/urls.py
from django.urls import path
from .views import register,desloguearse,empleados,home,listar_empleados, agregar_empleado, enlace_principal, listas, agregar, login_view

urlpatterns = [
    path('', home, name='home'),
    path('empleados/', empleados, name='empleados'),
    path('desloguearse/', desloguearse, name='desloguearse'),
    path('register/', register, name='register'),
    #path('home/', home, name='home'),
    #path('contacto/', contacto, name='contacto'),
    #path('galeria/', galeria, name='galeria'),
    #path('home/<str:username>', home, name='home'),
    #path('listare/', listar_empleados, name='listar_empleados'),
    #path('agregare/', agregar_empleado, name='agregar_empleado'),
    #path('listas/', listas,name='listas'),
    #path('agregar/', agregar,name='agregar'),
    #path('', enlace_principal, name='enlace_principal'),
    #path('login/', login_view, name='login_url'),
]

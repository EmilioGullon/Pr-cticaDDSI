from django.urls import path
from .views import index, almacenes, productos, listar_almacenes, crear_almacen, crear_producto

urlpatterns = [
    path('', index, name='index'),
    path('almacenes/', almacenes, name='almacenes'),
    path('productos/', productos, name='productos'),
    path('agregar_almacen/', crear_almacen, name='agregar_almacen'),
    path('listar_almacenes/', listar_almacenes, name='listar_almacenes'),
    path('agregar_producto/', crear_producto, name='agregar_producto'),

]
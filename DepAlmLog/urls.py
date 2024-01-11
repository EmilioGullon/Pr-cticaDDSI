from django.urls import path
from .views import index, almacenes, productos, listar_almacenes, crear_almacen, crear_producto, eliminar_almacen, buscar_producto, eliminar_producto, producto_a_almacen, contenido_almacen

urlpatterns = [
    path('', index, name='index'),
    path('almacenes/', almacenes, name='almacenes'),
    path('productos/', productos, name='productos'),
    path('agregar_almacen/', crear_almacen, name='agregar_almacen'),
    path('listar_almacenes/', listar_almacenes, name='listar_almacenes'),
    path('agregar_producto/', crear_producto, name='agregar_producto'),
    path('eliminar_almacen/<str:Alm>/', eliminar_almacen, name='eliminar_almacen'),
    path('buscar_producto/', buscar_producto, name='buscar_producto'),
    path('eliminar_producto/<int:Prod>/', eliminar_producto, name='eliminar_producto'),
    path('producto_a_almacen/', producto_a_almacen, name='producto_a_almacen'),
    path('contenido_almacen/<str:Alm>', contenido_almacen, name='contenido_almacen')
]
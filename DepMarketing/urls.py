from django.urls import path
from .views import ListaMarketing,agregar_socio, eliminar_socio, buscar_socio, modificar_socio, mostrar_socio, buscar_anuncio, mostrar_anuncio, agregar_anuncio, eliminar_anuncio, modificar_anuncio, anunciar_producto

urlpatterns = [
    path('', ListaMarketing.as_view(), name= 'ListaMarketing'),
    path('agregar_socio', agregar_socio, name = 'agregar_socio'),
    path('eliminar_socio/<str:DNIS>/', eliminar_socio, name='eliminar_socio'),
    path('buscar_socio', buscar_socio, name='buscar_socio'),
    path('mostrar_socio/<str:DNIS>/', mostrar_socio, name='mostrar_socio'),
    path('modificar_socio/<str:DNIS>/', modificar_socio, name='modificar_socio'),
    path('buscar_anuncio', buscar_anuncio, name='buscar_anuncio'),
    path('mostrar_anuncio/<str:CodigoA>/', mostrar_anuncio, name='mostrar_anuncio'),
    path('modificar_anuncio/<str:CodigoA>/', modificar_anuncio, name='modificar_anuncio'),
    path('agregar_anuncio', agregar_anuncio, name = 'agregar_anuncio'),
    path('eliminar_anuncio/<str:CodigoA>/', eliminar_anuncio, name='eliminar_anuncio'),
    path('anunciar_producto', anunciar_producto, name='anunciar_producto')
]
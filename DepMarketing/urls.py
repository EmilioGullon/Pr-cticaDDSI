from django.urls import path
from .views import ListaMarketing,agregar_socio, eliminar_socio, buscar_socio, mostrar_socio, agregar_anuncio, eliminar_anuncio

urlpatterns = [
    path('', ListaMarketing.as_view(), name= 'ListaMarketing'),
    path('agregar_socio', agregar_socio, name = 'agregar_socio'),
    path('eliminar_socio/<str:DNIS>/', eliminar_socio, name='eliminar_socio'),
    path('buscar_socio', buscar_socio, name='buscar_socio'),
    path('mostrar_socio/<str:DNIS>/', mostrar_socio, name='mostrar_socio'),
    path('agregar_anuncio', agregar_anuncio, name = 'agregar_anuncio'),
    path('eliminar_anuncio/<str:CodigoA>/', eliminar_anuncio, name='eliminar_anuncio')
]
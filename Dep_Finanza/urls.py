from django.urls import path
from .views import ListaMovimientos,agregar_gasto, eliminar_gasto, agregar_ingreso

urlpatterns = [
    path('', ListaMovimientos.as_view(), name= 'ListaMovimientos'),
    path('agregar_gasto', agregar_gasto, name = 'agregar_gasto'),
    path('eliminar_gasto/<str:Num_factura>/', eliminar_gasto, name='eliminar_gasto'),
    path('agregar_ingreso', agregar_ingreso, name = 'agregar_ingreso')
]
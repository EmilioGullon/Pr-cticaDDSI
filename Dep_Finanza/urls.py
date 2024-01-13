from django.urls import path
from .views import ListaMovimientos,agregar_gasto, eliminar_gasto, agregar_ingreso, eliminar_ingreso
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListaMovimientos.as_view()), name= 'ListaMovimientos'),
    path('agregar_gasto', login_required(agregar_gasto), name = 'agregar_gasto'),
    path('eliminar_gasto/<str:Num_factura>/', login_required(eliminar_gasto), name='eliminar_gasto'),
    path('agregar_ingreso', login_required(agregar_ingreso), name = 'agregar_ingreso'),
    path('eliminar_ingreso/<str:Ref_pago>/', login_required(eliminar_ingreso), name='eliminar_ingreso')
]
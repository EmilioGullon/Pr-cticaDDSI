from django.urls import path
from .views import ListaMovimientos,agregar_gasto_nomina, agregar_gasto_productos, eliminar_gasto_nomina, eliminar_gasto_productos, agregar_ingreso, eliminar_ingreso, modificar_gasto_nomina, modificar_gasto_productos, modificar_ingreso
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(ListaMovimientos.as_view()), name= 'ListaMovimientos'),
    path('agregar_gasto_nomina/', login_required(agregar_gasto_nomina), name = 'agregar_gasto_nomina'),
    path('agregar_gasto_productos/', login_required(agregar_gasto_productos), name = 'agregar_gasto_productos'),
    path('eliminar_gasto_nomina/<str:Num_factura>/', login_required(eliminar_gasto_nomina), name='eliminar_gasto_nomina'),
    path('eliminar_gasto_productos/<str:Num_factura>/', login_required(eliminar_gasto_productos), name='eliminar_gasto_productos'),
    path('agregar_ingreso/', login_required(agregar_ingreso), name = 'agregar_ingreso'),
    path('eliminar_ingreso/<str:Ref_pago>/', login_required(eliminar_ingreso), name='eliminar_ingreso'),
    path('modificar_gasto_nomina/<str:Num_factura>/', login_required(modificar_gasto_nomina), name='modificar_gasto_nomina'),
    path('modificar_gasto_productos/<str:Num_factura>/', login_required(modificar_gasto_productos), name='modificar_gasto_productos'),
    path('modificar_ingreso/<str:Ref_pago>/', login_required(modificar_ingreso), name='modificar_ingreso'),
]
from django.urls import path
from .views import ListaRRHH,agregar_empleado, eliminar_empleado, agregar_nomina, eliminar_nomina

urlpatterns = [
    path('', ListaRRHH.as_view(), name= 'ListaRRHH'),
    #path('lista_empleados', ListaEmpleados.as_view(), name='ListaEmpleados'),
    path('agregar_empleado', agregar_empleado, name = 'agregar_empleado'),
    path('eliminar_empleado/<str:DNIE>/', eliminar_empleado, name='eliminar_empleado'),
    path('agregar_nomina', agregar_nomina, name = 'agregar_nomina'),
    path('eliminar_nomina/<str:Nomina>/', eliminar_nomina, name='eliminar_nomina')
]
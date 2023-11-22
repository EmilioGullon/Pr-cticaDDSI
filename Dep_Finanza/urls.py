from django.urls import path
from .views import ListaMovimientos

urlpatterns = [
    path('', ListaMovimientos.as_view(), name= 'ListaMovimientos'),
]
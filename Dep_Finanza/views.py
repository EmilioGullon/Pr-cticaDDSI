from django.shortcuts import render,redirect
from django.views.generic import ListView
from app.models import Ingreso,Gasto
from itertools import chain
# Create your views here.

class ListaMovimientos(ListView):
    template_name = 'finanza/lista_movimientos.html'
    context_object_name = 'movimientos'

    def get_queryset(self):
        # Obtiene todos los gastos e ingresos y los combina en una lista
        gastos = Gasto.objects.all()
        ingresos = Ingreso.objects.all()
        movimientos = sorted(
            chain(gastos, ingresos),
            key=lambda movimiento: movimiento.Num_factura if isinstance(movimiento, Gasto) else movimiento.Ref_pago,
            reverse=True
        )
        return movimientos
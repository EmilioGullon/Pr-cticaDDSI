from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from app.models import Ingreso,Gasto, GastoN, GastoP, Nomina_tiene
from itertools import chain
# Create your views here.


class ListaMovimientos(ListView):
    template_name = 'finanza/lista_movimientos.html'
    context_object_name = 'movimientos'

    def get_queryset(self):
        gastosN = GastoN.objects.all()
        #gastosP = GastoP.objects.all()        
        movimientos = list(gastosN) #+ list(gastosP)
        gastos = sorted(movimientos, key=lambda movimiento: movimiento.Num_factura)
        ingresos = Ingreso.objects.order_by('Ref_pago')
        return {'gastos': gastos, 'ingresos': ingresos}

def agregar_gasto(request):
    if request.method == 'POST':
        num_fact = request.POST['num']
        nombre = request.POST['nombre']
        gasto = request.POST['gasto']
        cant = request.POST['cant']

        try:
            if gasto == 'N':
                GastoN.objects.create(Num_factura=num_fact, Receptor=nombre,  CantG=cant)
            else:
                GastoP.objects.create(Num_factura=num_fact, Receptor=nombre,  CantG=cant)                
            
            return redirect('ListaMovimientos')
        except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar empleado: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'finanza/agregar_gasto.html')

    return render(request, 'finanza/agregar_gasto.html')

def agregar_gasto_nomina(nom):
    try:
        GastoN.objects.create(Num_factura="N"+nom.Nomina, Receptor=nom.DNIE.NombreE,  CantG=nom.Bruto, Nomina_tiene=nom)
    except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar empleado: {e}")

def eliminar_gasto(request, Num_factura):
    gasto = get_object_or_404(Gasto, Num_factura=Num_factura)
    gasto.delete()
    return redirect('ListaMovimientos')

def agregar_ingreso(request):
    if request.method == 'POST':
        num_fact = request.POST['num']
        nombre = request.POST['nombre']
        gasto = request.POST['gasto']
        cant = request.POST['cant']

        try:
            Ingreso.objects.create(Ref_pago=num_fact, Emisor=nombre, TipoI=gasto,  CantI=cant)
            return redirect('ListaMovimientos')
        except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar empleado: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'finanza/agregar_ingreso.html')

    return render(request, 'finanza/agregar_ingreso.html')


def eliminar_ingreso(request, Ref_pago):
    gasto = get_object_or_404(Ingreso, Ref_pago=Ref_pago)
    gasto.delete()
    return redirect('ListaMovimientos')

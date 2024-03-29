from django.shortcuts import render,redirect, get_object_or_404
from django.db import transaction
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from app.models import Ingreso, Gasto, GastoN, GastoP, Nomina_tiene, Producto, contiene, Almacen, Producto
from itertools import chain
from .forms import CrearGastoN, CrearGastoP, CrearIngreso, ModificarGastoN, ModificarGastoP, ModificarIngreso
# Create your views here.


class ListaMovimientos(ListView):
    template_name = 'finanza/lista_movimientos.html'
    context_object_name = 'movimientos'

    def get_queryset(self):
        gastosN = GastoN.objects.all()
        gastosP = GastoP.objects.all()        
        #movimientos = list(gastosP) #+ list(gastosN)
        #gastos = sorted(movimientos, key=lambda movimiento: movimiento.Num_factura)
        ingresos = Ingreso.objects.order_by('Ref_pago')
        return {'gastosN': gastosN, 'gastosP': gastosP, 'ingresos': ingresos}

def agregar_gasto_nomina(request):
    if request.method == 'POST':
        form = CrearGastoN(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            nomina = Nomina_tiene.objects.get(Nomina=gasto.Nomina_tiene.Nomina)
            gasto.CantG = nomina.Bruto + nomina.Impuesto
            gasto.save()
            return redirect('ListaMovimientos')
    else:
        form = CrearGastoN()

    return render(request, 'finanza/agregar_gasto_nomina.html', {'form': form})

def agregar_gasto_productos(request):
    if request.method == 'POST':
        form = CrearGastoP(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            producto = Producto.objects.get(Prod=gasto.Producto.Prod)
            gasto.CantG = producto.Precio*3/4 * gasto.CantidadC
            gasto.save()
            try:
                trasladar = contiene(
                Prod = gasto.Producto,
                Alm = gasto.Almacen,
                CantidadC = gasto.CantidadC)
                trasladar.save()
            except Exception as e:
                conexion = contiene.objects.get(Prod=gasto.Producto, Alm=gasto.Almacen)
                conexion.CantidadC += gasto.CantidadC
                conexion.save()
            return redirect('ListaMovimientos')
    else:
        form = CrearGastoP()

    return render(request, 'finanza/agregar_gasto_productos.html', {'form': form})

def eliminar_gasto_nomina(request, Num_factura):
    gasto = get_object_or_404(GastoN, Num_factura=Num_factura)
    gasto.delete()
    return redirect('ListaMovimientos')

def eliminar_gasto_productos(request, Num_factura):
    gasto = get_object_or_404(GastoP, Num_factura=Num_factura)
    gasto.delete()
    return redirect('ListaMovimientos')

def agregar_ingreso(request):
    if request.method == 'POST':
        form = CrearIngreso(request.POST)
        if form.is_valid():
            gasto = form.save()
            return redirect('ListaMovimientos')
    else:
        form = CrearIngreso()

    return render(request, 'finanza/agregar_ingreso.html', {'form': form})


def eliminar_ingreso(request, Ref_pago):
    gasto = get_object_or_404(Ingreso, Ref_pago=Ref_pago)
    gasto.delete()
    return redirect('ListaMovimientos')

def modificar_gasto_nomina(request, Num_factura):
    gasto = get_object_or_404(GastoN, Num_factura=Num_factura)

    if request.method == 'POST':
        form = ModificarGastoN(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('ListaMovimientos')
    else:
        form = ModificarGastoN(instance=gasto)

    return render(request, 'finanza/modificar_gasto.html', {'form': form, 'gasto': gasto})

def modificar_gasto_productos(request, Num_factura):
    gasto = get_object_or_404(GastoP, Num_factura=Num_factura)
    producto_anterior = get_object_or_404(Producto, Prod=gasto.Producto.Prod)
    alm_anterior = get_object_or_404(Almacen, Alm=gasto.Almacen.Alm)
    cant_anterior = gasto.CantidadC

    if request.method == 'POST':
        form = ModificarGastoP(request.POST, instance=gasto)
        if form.is_valid():
            cambio = form.save(commit=False)
            producto = Producto.objects.get(Prod=gasto.Producto.Prod)
            cambio.CantG = producto.Precio*3/4 * gasto.CantidadC
            trasladar = contiene(
                Prod = cambio.Producto,
                Alm = cambio.Almacen,
                CantidadC = cambio.CantidadC)
            trasladar_anterior = get_object_or_404(contiene, Prod=producto_anterior, Alm=alm_anterior)
            try:
                with transaction.atomic():
                    trasladar.save()
                    trasladar_anterior.CantidadC-=cant_anterior
                    trasladar_anterior.save()
                    cambio.save()
            except Exception as e:
                try:
                    with transaction.atomic():
                        conexion = contiene.objects.get(Prod=gasto.Producto, Alm=gasto.Almacen)
                        conexion.CantidadC += gasto.CantidadC
                        conexion.save()
                        conexion_anterior = get_object_or_404(contiene, Prod=producto_anterior, Alm=alm_anterior)
                        conexion_anterior.CantidadC-=cant_anterior
                        conexion_anterior.save()
                        cambio.save()
                except:
                    print("Error")
            return redirect('ListaMovimientos')
    else:
        form = ModificarGastoP(instance=gasto)

    return render(request, 'finanza/modificar_gasto.html', {'form': form, 'gasto': gasto})

def modificar_ingreso(request, Ref_pago):
    ingreso = get_object_or_404(Ingreso, Ref_pago=Ref_pago)

    if request.method == 'POST':
        form = ModificarGastoP(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            return redirect('ListaMovimientos')
    else:
        form = ModificarGastoP(instance=ingreso)

    return render(request, 'finanza/modificar_ingreso.html', {'form': form, 'ingreso': ingreso})

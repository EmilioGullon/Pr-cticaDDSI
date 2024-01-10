from django.shortcuts import render, redirect, get_object_or_404
from app.models import Almacen, Producto
from .forms import CrearAlmacen, CrearProducto
from django.views import View

# Create your views here.

def index(request):
    return render(request, 'almlog/index.html')

def almacenes(request):
    return render(request, 'almlog/almacenes.html')

def productos(request):
    return render(request, 'almlog/productos.html')

def listar_almacenes(request):
    almacenes = Almacen.objects.all()
    return render(request, 'almlog/listar_almacenes.html', {
        'almacenes': almacenes
    })

def crear_almacen(request):
    if request.method == 'POST':
        form = CrearAlmacen(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/almacenamiento_logistica/listar_almacenes')
    else:
        form = CrearAlmacen()

    return render(request, 'almlog/agregar_almacen.html', {'form': form})

def crear_producto(request):
    if request.method == 'POST':
        form = CrearProducto(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/almacenamiento_logistica/productos')
    else:
        form = CrearProducto()

    return render(request, 'almlog/agregar_producto.html', {'form': form})

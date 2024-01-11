from django.shortcuts import render, redirect, get_object_or_404
from app.models import Almacen, Producto, contiene
from .forms import CrearAlmacen, CrearProducto, BuscarProducto, ProductoAAlmacen
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

def eliminar_almacen(request, Alm):
    almacen = get_object_or_404(Almacen, Alm=Alm)
    almacen.delete()
    return redirect('/almacenamiento_logistica/listar_almacenes')

def crear_producto(request):
    if request.method == 'POST':
        form = CrearProducto(request.POST)
        if form.is_valid():
            producto = form.save()
            nombre = producto.NombreP
            return redirect('/almacenamiento_logistica/buscar_producto/?consulta={}'.format(nombre))
    else:
        form = CrearProducto()

    return render(request, 'almlog/agregar_producto.html', {'form': form})

def buscar_producto(request):
    if request.method == 'GET':
        form = BuscarProducto(request.GET)
        if form.is_valid():
            consulta = form.cleaned_data['consulta']
            resultados = Producto.objects.filter(NombreP__icontains=consulta)
        else:
            resultados = Producto.objects.all()
    else:
        form = BuscarProducto()
        resultados = Producto.objects.all()

    return render(request, 'almlog/buscar_producto.html', {'form': form, 'resultados': resultados})

def eliminar_producto(request, Prod):
    producto = get_object_or_404(Producto, Prod=Prod)
    nombre = producto.NombreP
    producto.delete()
    return redirect('/almacenamiento_logistica/buscar_producto/?consult={}'.format(nombre))

def producto_a_almacen(request):
    if request.method == 'POST':
        form = ProductoAAlmacen(request.POST)
        if form.is_valid():
            contenido = form.save()
            #almacen = contenido.Alm
            #return redirect('/almacenamiento_logistica/#contenido_almacen/{}'.format(almacen.Alm))
            return redirect('/almacenamiento_logistica/almacenes')
    else:
        form = ProductoAAlmacen()

    return render(request, 'almlog/producto_a_almacen.html', {'form': form})

def contenido_almacen(request, Alm):
    productos = contiene.objects.filter(Alm=Alm)
    almacen = Almacen.objects.get(Alm=Alm)
    return render(request, 'almlog/contenido_almacen.html', {
        'productos': productos,
        'almacen': almacen
    })
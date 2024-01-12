from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from app.models import Almacen, Producto, contiene, Anuncio
from .forms import CrearAlmacen, CrearProducto, BuscarProducto, ProductoA_EnAlmacen, ModificarProducto, ModificarAlmacen, ModificarCantidad, SeleccionarAnuncio

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

def producto_a_en_almacen(request):
    if request.method == 'POST':
        form = ProductoA_EnAlmacen(request.POST)
        if form.is_valid():
            contenido = form.save()
            #almacen = contenido.Alm
            #return redirect('/almacenamiento_logistica/#contenido_almacen/{}'.format(almacen.Alm))
            return redirect('/almacenamiento_logistica/almacenes')
    else:
        form = ProductoA_EnAlmacen()

    return render(request, 'almlog/producto_a_en_almacen.html', {'form': form})

def contenido_almacen(request, Alm):
    productos = contiene.objects.filter(Alm=Alm)
    almacen = Almacen.objects.get(Alm=Alm)
    return render(request, 'almlog/contenido_almacen.html', {
        'productos': productos,
        'almacen': almacen
    })

def ubicacion_producto(request, Prod):
    almacenes = contiene.objects.filter(Prod=Prod)
    producto = Producto.objects.get(Prod=Prod)
    return render(request, 'almlog/ubicacion_producto.html', {
        'producto': producto,
        'almacenes': almacenes
    })

def modificar_producto(request, Prod):
    producto = get_object_or_404(Producto, Prod=Prod)

    if request.method == 'POST':
        form = ModificarProducto(request.POST, instance=producto)
        if form.is_valid():
            nuevo = form.save()
            nombre = nuevo.NombreP
            return redirect('/almacenamiento_logistica/buscar_producto/?consult={}'.format(nombre))
    else:
        form = ModificarProducto(instance=producto)

    return render(request, 'almlog/modificar_producto.html', {'form': form})

def modificar_almacen(request, Alm):
    almacen = get_object_or_404(Almacen, Alm=Alm)

    if request.method == 'POST':
        form = ModificarAlmacen(request.POST, instance=almacen)
        if form.is_valid():
            form.save()
            return redirect('/almacenamiento_logistica/listar_almacenes')
    else:
        form = ModificarAlmacen(instance=almacen)

    return render(request, 'almlog/modificar_almacen.html', {'form': form})

def modificar_contiene_almacen(request, Alm, Prod):
    contenedor = get_object_or_404(contiene, Alm=Alm, Prod=Prod)

    if request.method == 'POST':
        form = ModificarCantidad(request.POST, instance=contenedor)
        if form.is_valid():
            nuevo = form.save()
            codigo = nuevo.Alm.Alm
            return redirect('/almacenamiento_logistica/contenido_almacen/{}'.format(codigo))
    else:
        form = ModificarCantidad(instance=contenedor)

    return render(request, 'almlog/modificar_contiene.html', {'form': form})

def modificar_contiene_producto(request, Prod, Alm):
    contenedor = get_object_or_404(contiene, Prod=Prod, Alm=Alm)

    if request.method == 'POST':
        form = ModificarCantidad(request.POST, instance=contenedor)
        if form.is_valid():
            nuevo = form.save()
            codigo = nuevo.Prod.Prod
            return redirect('/almacenamiento_logistica/ubicacion_producto/{}'.format(codigo))
    else:
        form = ModificarCantidad(instance=contenedor)

    return render(request, 'almlog/modificar_contiene.html', {'form': form})

def producto_a_anuncio(request, Prod):
    producto = Producto.objects.get(Prod=Prod)
    anuncios = Anuncio.objects.all()

    if request.method == 'GET':
        form = SeleccionarAnuncio(request.GET)
        if form.is_valid():
            eleccion = form.cleaned_data['eleccion']
            try:
                anuncio = Anuncio.objects.get(CodigoA=eleccion)
                anuncio.Productos.add(producto)
            except Exception as e:
                mensaje_error = f"Error: no existe ningún anuncio con este código."
    else:
        form = SeleccionarAnuncio()

    return render(request, 'almlog/producto_a_anuncio.html', {
        'producto': producto,
        'anuncios': anuncios,
        'form': form,
        'mensaje_error': mensaje_error
    })
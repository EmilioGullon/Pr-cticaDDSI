from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from app.models import Socio, Anuncio, Producto
from itertools import chain
# Create your views here.

class ListaMarketing(ListView):
    template_name = 'marketing_clientes/lista_marketing.html'
    context_object_name = 'marketing'

    def get_queryset(self):
        socios = Socio.objects.order_by('NombreS')
        anuncios = Anuncio.objects.order_by('CodigoA')
        return {'socios': socios, 'anuncios': anuncios}
    

def agregar_socio(request):
    if request.method == 'POST':
        dni = request.POST['dni']
        nombre = request.POST['nombre']
        apellido1 = request.POST['Primero']
        apellido2 = request.POST['Segundo']
        telefono = request.POST['Telefono']
        email = request.POST['E-mail']
        try:
            Socio.objects.create(DNIS=dni, NombreS=nombre, Apellido1S=apellido1, Apellido2S=apellido2, TelefonoS=telefono, E_mailS=email)
            return redirect('ListaMarketing')
        except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar socio: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'marketing_clientes/agregar_socio.html')

    return render(request, 'marketing_clientes/agregar_socio.html')

def listar_socios(request):
    socios = Socio.objects.all()
    return render(request, 'marketing_clientes/lista_marketing.html', {'socios': socios})

def agregar_anuncio(request):
    if request.method == 'POST':
        codigo = request.POST['codigo']
        tipo = request.POST['tipo']
        desc = request.POST['descripcion']
        loc = request.POST['localizacion']
        producto = request.POST['producto']
        try:
            nuevo_anuncio = Anuncio.objects.create(CodigoA=codigo, TipoA=tipo, DescripcionA=desc, LocalizacionA=loc)
            producto = get_object_or_404(Producto, Prod=producto)
            nuevo_anuncio.Producto.add(producto)
            return redirect('ListaMarketing')
        
        except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar anuncio: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'marketing_clientes/agregar_anuncio.html')

    return render(request, 'marketing_clientes/agregar_anuncio.html')

def listar_anuncios(request):
    anuncios = Anuncio.objects.all()
    return render(request, 'marketing_clientes/lista_marketing.html', {'anuncios': anuncios})

def eliminar_socio(request, DNIS):
    socio = get_object_or_404(Socio, DNIS=DNIS)
    socio.delete()
    return redirect('ListaMarketing')

def eliminar_anuncio(request, CodigoA):
    anuncio = get_object_or_404(Anuncio, CodigoA=CodigoA)
    anuncio.delete()
    return redirect('ListaMarketing')

def buscar_socio(request, DNIS):
    socio = get_object_or_404(Socio, DNIS=DNIS)
    return render(request, 'marketing_clientes/socios_anuncio.html', {'socio' : socio})

def buscar_anuncio(request, CodigoA):
    anuncio = get_object_or_404(Anuncio, CodigoA=CodigoA)
    return render(request, 'marketing_clientes/datos_anuncio.html', {'anuncio' : anuncio})

def modificar_socio(request, DNIS, nuevos_datos):
    socio = get_object_or_404(Socio, DNIS=DNIS)
    for atributo, nuevo_valor in nuevos_datos.items():
        setattr(socio, atributo, nuevo_valor)
    socio.save()
    return redirect('ListaMarketing')
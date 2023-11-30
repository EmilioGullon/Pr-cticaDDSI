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
        producto = request.POST['producto']
        try:
            producto = get_object_or_404(Producto, Prod=producto)
            if(producto):
                nuevo_socio = Socio.objects.create(DNIS=dni, NombreS=nombre, Apellido1S=apellido1, Apellido2S=apellido2, TelefonoS=telefono, E_mailS=email)
                nuevo_socio.Producto.add(producto)

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
            producto = get_object_or_404(Producto, Prod=producto)
            if(producto):
                nuevo_anuncio = Anuncio.objects.create(CodigoA=codigo, TipoA=tipo, DescripcionA=desc, LocalizacionA=loc)
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

def buscar_socio(request):
    if request.method == 'POST':
        dnis = request.POST.get('dni')
        try:
            socio = Socio.objects.get(DNIS=dnis)
            # Redirige a la página de detalle del socio
            return redirect('mostrar_socio', DNIS=socio.DNIS)
        except Socio.DoesNotExist:
            print("No se encontró ningún socio con el DNI proporcionado.")
            return redirect('ListaMarketing')
    else:
        # Manejar el caso en que no se haya enviado un formulario
        return render(request, 'ListaMarketing')

def mostrar_socio(request, DNIS):
    socio = get_object_or_404(Socio, DNIS=DNIS)
    return render(request, 'marketing_clientes/mostrar_socio.html', {'socio': socio})

def buscar_anuncio(request):
    if request.method == 'POST':
        codigoa = request.POST.get('codigo')
        try:
            anuncio = Anuncio.objects.get(CodigoA=codigoa)
            # Redirige a la página de detalle del socio
            return redirect('mostrar_anuncio', CodigoA=anuncio.CodigoA)
        except Anuncio.DoesNotExist:
            print("No se encontró ningún anuncio con el código proporcionado.")
            return redirect('ListaMarketing')
    else:
        # Manejar el caso en que no se haya enviado un formulario
        return render(request, 'ListaMarketing')

def mostrar_anuncio(request, CodigoA):
    anuncio = get_object_or_404(Anuncio, CodigoA=CodigoA)
    return render(request, 'marketing_clientes/mostrar_anuncio.html', {'anuncio': anuncio})

def modificar_socio(request, DNIS):
    
    sociomod = get_object_or_404(Socio, DNIS=DNIS)

    if request.method == 'POST':
        nombren = request.POST.get('nombre', '')
        primeran = request.POST.get('Primero', '')
        segundoan = request.POST.get('Segundo', '')
        telefonon = request.POST.get('Telefono', '')
        emailn = request.POST.get('E-mail', '')
        
        try:
            if(nombren):
                sociomod.NombreS = nombren
            
            if(primeran):
                sociomod.Apellido1S = primeran
            
            if(segundoan):
                sociomod.Apellido2S = segundoan
            
            if(telefonon):
                sociomod.TelefonoS = telefonon
            
            if(emailn):
                sociomod.E_mailS = emailn

            sociomod.save()

            return render(request, 'marketing_clientes/mostrar_socio.html', {'socio': sociomod})

        except Exception as e:
        
            # Manejar el error aquí, si es necesario
            print(f"Error al modificar socio: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'marketing_clientes/mostrar_socio.html')
    

    return render(request, 'marketing_clientes/modificar_socio.html', {'socio': sociomod})

def modificar_anuncio(request, CodigoA):
    
    anunciomod = get_object_or_404(Anuncio, CodigoA=CodigoA)

    if request.method == 'POST':
        tipon = request.POST.get('tipo', '')
        descn = request.POST.get('descripcion', '')
        codigon = request.POST.get('codigo', '')
        locn = request.POST.get('localizacion', '')
        
        try:
            if(tipon):
                anunciomod.TipoA = tipon
            
            if(descn):
                anunciomod.DescripcionA = descn
            
            if(codigon):
                anunciomod.CodigoA = codigon
            
            if(locn):
                anunciomod.LocalizacionA = locn

            anunciomod.save()

            return render(request, 'marketing_clientes/mostrar_anuncio.html', {'anuncio': anunciomod})

        except Exception as e:
        
            # Manejar el error aquí, si es necesario
            print(f"Error al modificar anuncio: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'marketing_clientes/mostrar_anuncio.html')
    

    return render(request, 'marketing_clientes/modificar_anuncio.html', {'anuncio': anunciomod})
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from app.models import Socio, Anuncio, Producto, compra, Almacen, contiene, Ingreso, produce
from itertools import chain
from .forms import SeleccionarProducto, ComprarProd
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
        #producto = request.POST['producto']
        try:
            #producto = get_object_or_404(Producto, Prod=producto)
            #if(producto):
            nuevo_socio = Socio.objects.create(DNIS=dni, NombreS=nombre, Apellido1S=apellido1, Apellido2S=apellido2, TelefonoS=telefono, E_mailS=email)
            #nuevo_socio.Producto.add(producto)

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

        try:     
            Anuncio.objects.create(CodigoA=codigo, TipoA=tipo, DescripcionA=desc, LocalizacionA=loc)
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
        #codigon = request.POST.get('codigo', '')
        locn = request.POST.get('localizacion', '')
        
        try:
            if(tipon):
                anunciomod.TipoA = tipon
            
            if(descn):
                anunciomod.DescripcionA = descn
            
            #if(codigon):
            #    anunciomod.CodigoA = codigon
            
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

def anuncio_de_producto(request, CodigoA):
    anuncio = Anuncio.objects.get(CodigoA=CodigoA)

    if request.method == 'GET':
        form = SeleccionarProducto(request.GET)
        if form.is_valid():
            eleccion = form.cleaned_data['eleccion']
            try:
                producto = Producto.objects.get(Prod=eleccion)
                anuncio.Productos.add(producto)
            except Exception as e:
                f"Error: no existe ningún producto con este código."
    else:
        form = SeleccionarProducto()

    return render(request, 'marketing_clientes/anuncio_de_producto.html', {
        'anuncio': anuncio,
        'form': form,
    })

def eliminar_el_producto(request, CodigoA, Prod):
    producto = Producto.objects.get(Prod=Prod)
    anuncio = Anuncio.objects.get(CodigoA=CodigoA)
    anuncio.Productos.remove(producto)
    return redirect('/marketing_clientes/insertar_producto/{}'.format(anuncio.CodigoA))

def socio_comprar(request, DNIS):
    socio = Socio.objects.get(DNIS=DNIS)
    
    if request.method == 'POST':
        form = ComprarProd(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.DNIS = socio
            try:
                stock = contiene.objects.get(Alm=comp.Alm, Prod=comp.Prod)
                producto = Producto.objects.get(Prod=comp.Prod.Prod)
                stock.CantidadC = stock.CantidadC - comp.CantidadC
                stock.save()
                comp.save()
                ingresos = Ingreso.objects.all()
                if ingresos.exists():
                    mayor_cod_ingreso = Ingreso.objects.order_by('-Ref_pago').first()
                    ingreso = Ingreso(Ref_pago=mayor_cod_ingreso.Ref_pago+1, 
                                      Emisor=socio.DNIS, TipoI='Compra', 
                                      CantI=comp.CantidadC*producto.Precio)
                    ingreso.save()
                    conexion = produce(Ref_pago=ingreso, Compra=comp)
                    conexion.save()
                else:
                    ingreso = Ingreso(Ref_pago=0, 
                                      Emisor=socio.DNIS, TipoI='Compra', 
                                      CantI=comp.CantidadC*producto.Precio)
                    ingreso.save()
                    conexion = produce(Ref_pago=ingreso, Compra=comp)
                    conexion.save()
            except Exception as e:
                f"Error"
            return redirect('/marketing_clientes/compra_socio/{}' .format(DNIS))
    else:
        form = ComprarProd()

    return render(request, 'marketing_clientes/compra_socio.html', {'form': form, 'socio': socio})
from django.shortcuts import render, redirect
from .models import Empleado, Socio

# Create your views here.
def home(request, username):
    context = {'username': username}
    return render(request, 'app/home.html', context)

def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):
    return render(request, 'app/galeria.html')

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'app/listar_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        dni = request.POST['dni']
        nombre = request.POST['nombre']
        apellido1 = request.POST['Primero']
        apellido2 = request.POST['Segundo']
        telefono = request.POST['Telefono'] 
        try:
            Empleado.objects.create(DNIE=dni, NombreE=nombre, Apellido1E=apellido1, Apellido2E=apellido2, TelefonoE=telefono)
            return redirect('listar_empleados')
        except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar empleado: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'app/agregar_empleado.html')

    return render(request, 'app/agregar_empleado.html')

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
            return redirect('listar_socios')
        except Exception as s:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar socio: {s}")
            # Renderizar la misma página en caso de error
            return render(request, 'app/agregar_socio.html')

    return render(request, 'app/agregar_socio.html')

def listar_socios(request):
    socios = Socio.objects.all()
    return render(request, 'app/listar_socios.html', {'socios': socios})
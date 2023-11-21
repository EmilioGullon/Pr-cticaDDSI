from django.shortcuts import render, redirect
from .models import Empleado

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
        DNIE = request.POST['dni']
        NombreE = request.POST['nombre']
        Apellido1E = request.POST['Primero']
        Apellido2E = request.POST['Segundo']
        TelefonoE = request.POST['Telefono'] 
        try:
            Empleado.objects.create(nombre=NombreE, apellido1=Apellido1E, apellido2=Apellido2E, telefono=TelefonoE)
            return redirect('listar_empleados')
        except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar empleado: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'app/agregar_empleado.html')

    return render(request, 'app/agregar_empleado.html')
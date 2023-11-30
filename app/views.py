from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Empleado
from .forms import CustomUserCreationForm

# Create your views here.i
def home(request):
    return render(request, 'app/home.html')

@login_required
def empleados(request):
    return render(request, 'app/empleados.html')

def desloguearse(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

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

def enlace_principal(request):
    return render(request, 'enlace_principal.html')

def listas(request):
    return render(request, 'listas.html')

def agregar(request):
    return render(request, 'agregar.html')

def login_view(request):
#8;9?+W)3k}-5Txv
#CC*H5R'hQYxNaNA
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

        else:
            # Si el nombre de usuario y la contraseña no coinciden, devuelve un mensaje de error.
            return render(request, 'app/login.html', {'error_message': 'Nombre de usuario y/o contraseña incorrectos'})

    else:
        return render(request, 'app/login.html')
    
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }    
    
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
    
        if user_creation_form.is_valid():  
            user = user_creation_form.save()
            
            #user = authenticate(request ,username = user_creation_form.cleaned_data.get('username'), password = user_creation_form.cleaned_data.get('password'))
        
            login(request, user)
            return redirect('home')
    
    return render(request, 'registration/register.html', data)
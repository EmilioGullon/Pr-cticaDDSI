from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from app.models import Empleado,Nomina_tiene
from itertools import chain
# Create your views here.

class ListaEmpleados(ListView):
    template_name = 'rrhh/lista_empleados.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        empleados = Empleado.objects.order_by('DNI')
        return {'empleados': empleados}
    
class ListaNominas(ListView):
    template_name = 'rrhh/lista_nominas_empleado.html'
    context_object_name = 'nominas'

    def get_queryset(self):
        nominas = Nomina_tiene.objects.order_by('#Nomina')
        return {'nominas': nominas}
    

def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido1 = request.POST['apellido1']
        apellido2 = request.POST['apellido2']
        dni = request.POST['dni']
        tlf = request.POST['tlf']

        try:
            Empleado.objects.create(DNIE=dni, NombreE=nombre, Apellido1E=apellido1, Apellido2E=apellido2, TelefonoE=tlf)
            return redirect('ListaEmpleados')
        except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar empleado: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'finanza/agregar_empleado.html')

    return render(request, 'finanza/agregar_empleado.html')


def eliminar_empleado(request, DNI):
    empleado = get_object_or_404(Empleado, DNIE=DNI)
    empleado.delete()
    return redirect('ListaEmpleados')

def agregar_nomina(request):
    if request.method == 'POST':
        num_nomina = request.POST['num_nomina']
        bruto = request.POST['bruto']
        impuestos = request.POST['impuestos']
        dni = request.POST['dni']
        empleado = request.POST['impuestos']

        try:
            Nomina_tiene.objects.create(Nomina=num_nomina, Bruto=bruto, Impuesto=impuestos, DNIE=dni, Empleado=empleado)
            return redirect('ListaNominas')
        except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar nómina: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'rrhh/agregar_nomina.html')

    return render(request, 'rrhh/agregar_nomina.html')


def eliminar_nomina(request, Num_nomina):
    nomina = get_object_or_404(Nomina_tiene, Num_nomina=Num_nomina)
    nomina.delete()
    return redirect('ListaNominas')
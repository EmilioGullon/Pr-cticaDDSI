from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView
from app.models import Empleado,Nomina_tiene
from Dep_Finanza.views import agregar_gasto_nomina
from itertools import chain
from .forms import CrearNomina
# Create your views here.

class ListaEmpleados(ListView):
    template_name = 'rrhh/lista_empleados.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        empleados = Empleado.objects.order_by('DNIE')
        nominas = Nomina_tiene.objects.order_by('Nomina')
        return {'empleados': empleados, 'nominas': nominas}
    
class ListaRRHH(ListView):
    template_name = 'rrhh/lista_rrhh.html'
    context_object_name = 'rrhh'

    def get_queryset(self):
        empleados = Empleado.objects.order_by('DNIE')
        nominas = Nomina_tiene.objects.order_by('Nomina')
        return {'empleados': empleados, 'nominas': nominas}
    

def agregar_empleado(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido1 = request.POST['apellido1']
        apellido2 = request.POST['apellido2']
        dni = request.POST['dni']
        tlf = request.POST['tlf']

        try:
            Empleado.objects.create(DNIE=dni, NombreE=nombre, Apellido1E=apellido1, Apellido2E=apellido2, TelefonoE=tlf)
            return redirect('ListaRRHH')
        except Exception as e:
            # Manejar el error aquí, si es necesario
            print(f"Error al agregar empleado: {e}")
            # Renderizar la misma página en caso de error
            return render(request, 'rrhh/agregar_empleado.html')

    return render(request, 'rrhh/agregar_empleado.html')


def eliminar_empleado(request, DNIE):
    empleado = get_object_or_404(Empleado, DNIE=DNIE)
    empleado.delete()
    return redirect('ListaRRHH')

#def agregar_nomina(request):
#    if request.method == 'POST':
#        num_nomina = request.POST['num_nomina']
#        bruto = request.POST['bruto']
 #       impuestos = request.POST['impuestos']
  #      dni = request.POST['dni']
#
 #       try:
  #          empleado = get_object_or_404(Empleado, DNIE=dni)
   #         nom = Nomina_tiene.objects.create(Nomina=num_nomina, Bruto=bruto, Impuesto=impuestos, DNIE=empleado)
    #        agregar_gasto_nomina(nom)
     #       return redirect('ListaRRHH')
      #  except Exception as e:
       #     # Manejar el error aquí, si es necesario
        #    print(f"Error al agregar nómina: {e}")
         #   # Renderizar la misma página en caso de error
          #  return render(request, 'rrhh/agregar_nomina.html')

    #return render(request, 'rrhh/agregar_nomina.html')


def agregar_nomina(request):
    if request.method == 'POST':
        form = CrearNomina(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListaRRHH')
    else:
        form = CrearNomina()

    return render(request, 'rrhh/agregar_nomina.html', {'form': form})

def eliminar_nomina(request, Nomina):
    nomina = get_object_or_404(Nomina_tiene, Nomina=Nomina)
    nomina.delete()
    return redirect('ListaRRHH')
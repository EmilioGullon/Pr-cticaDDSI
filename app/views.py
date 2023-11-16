from django.shortcuts import render

# Create your views here.
def home(request, username):
    context = {'username': username}
    return render(request, 'app/home.html', context)

def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):
    return render(request, 'app/galeria.html')
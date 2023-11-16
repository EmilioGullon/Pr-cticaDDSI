# En app/urls.py
from django.urls import path
from .views import home,contacto, galeria

urlpatterns = [
    path('home/', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('galeria/', galeria, name='galeria'),
    path('home/<str:username>', home, name='home'),

]

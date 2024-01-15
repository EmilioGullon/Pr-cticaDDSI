from django import forms
from app.models import compra

class SeleccionarProducto(forms.Form):
    eleccion = forms.CharField(max_length=100, required=False, label='Código del producto')

class ComprarProd(forms.ModelForm):
    class Meta:
        model = compra
        fields = ['DNIS', 'Prod', 'CantidadC', 'FechaC']
        labels = {
            'DNIS': 'DNI del socio',
            'Prod': 'Código del producto',
            'CantidadC': 'Cantidad del producto',
            'FechaC' : 'Fecha de la compra'
        }
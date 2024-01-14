from django import forms

class SeleccionarProducto(forms.Form):
    eleccion = forms.CharField(max_length=100, required=False, label='Código del producto')
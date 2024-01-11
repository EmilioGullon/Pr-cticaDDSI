from django import forms
from app.models import Almacen, Producto, contiene

class CrearAlmacen(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['Alm', 'NombreA', 'Direccion', 'Provincia']
        labels = {
            'Alm': 'Código',
            'NombreA': 'Nombre',
            'Direccion': 'Dirección',
            'Provincia': 'Provincia',
        }

class CrearProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['Prod', 'NombreP', 'DescripcionP', 'Precio']
        labels = {
            'Prod': 'Código',
            'NombreP': 'Nombre',
            'DescripcionP': 'Descripción',
            'Precio': 'Precio',
        }
        widgets = {
            'DescripcionP': forms.Textarea(attrs={'class': 'descripcion-input'}),
        }

class BuscarProducto(forms.Form):
    consulta = forms.CharField(max_length=100, required=False, label='Buscar')

class ProductoA_EnAlmacen(forms.ModelForm):
    class Meta:
        model = contiene
        fields = ['Prod', 'Alm', 'CantidadC']
        labels = {
            'Alm': 'Código del almacén',
            'Prod': 'Código del producto',
            'CantidadC': 'Cantidad del producto',
        }
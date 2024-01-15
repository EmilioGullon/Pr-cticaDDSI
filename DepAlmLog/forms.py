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

class ModificarProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['NombreP', 'DescripcionP', 'Precio']
        labels = {
            'NombreP': 'Nuevo nombre',
            'DescripcionP': 'Nueva descripción',
            'Precio': 'Nuevo precio',
        }

    def clean_Precio(self):
        precio = self.cleaned_data['Precio']
        if precio <= 0:
            raise forms.ValidationError('El precio debe ser un número mayor que 0.')
        return precio
    
class ModificarAlmacen(forms.ModelForm):
    class Meta:
        model = Almacen
        fields = ['NombreA', 'Direccion', 'Provincia']
        labels = {
            'NombreA': 'Nuevo nombre',
            'Direccion': 'Nueva dirección',
            'Provincia': 'Nueva provincia',
        }

class SeleccionarAnuncio(forms.Form):
    eleccion = forms.CharField(max_length=100, required=False, label='Código del anuncio')
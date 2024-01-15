from django import forms
from app.models import GastoN, GastoP, Ingreso

class CrearGastoN(forms.ModelForm):
    class Meta:
        model = GastoN
        fields = ['Num_factura', 'Receptor', 'CantG', 'Fecha', 'Nomina_tiene']
        labels = {
            'Num_factura': 'Nº Factura',
            'Receptor': 'Nombre del remitente',
            'CantG': 'Cantidad',
            'Fecha': 'Fecha',
            'Nomina_tiene': 'Código de la nómina',
        }

class CrearGastoP(forms.ModelForm):
    class Meta:
        model = GastoP
        fields = ['Num_factura', 'Receptor', 'Fecha', 'Producto', 'CantidadC', 'Almacen']
        labels = {
            'Num_factura': 'Nº Factura',
            'Receptor': 'Nombre del remitente',
            'Fecha': 'Fecha',
            'Producto': 'Código del producto',
            'CantidadC': 'Número de productos',
            'Almacen': 'Almacén para los productos'
        }

class CrearIngreso(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['Ref_pago', 'Emisor', 'TipoI', 'CantI' ]
        labels = {
            'Ref_pago': 'Nº Factura',
            'Emisor': 'Nombre del remitente',
            'TipoI': 'Fecha',
            'CantI': 'Cantidad'
        }

class ModificarGastoN(forms.ModelForm):
    class Meta:
        model = GastoN
        fields = ['Receptor', 'CantG', 'Fecha', 'Nomina_tiene']
        labels = {
            'Receptor': 'Nuevo remitente',
            'CantG': 'Nueva cantidad',
            'Fecha': 'Nueva fecha',
            'Nomina_tiene': 'Nueva nómina',
        }

class ModificarGastoP(forms.ModelForm):
    class Meta:
        model = GastoP
        fields = ['Receptor', 'Fecha', 'Producto', 'CantidadC', 'Almacen']
        labels = {
            'Receptor': 'Nuevo remitente',
            'Fecha': 'Nueva fecha',
            'Producto': 'Nuevo producto',
            'CantidadC': 'Nuevo nº productos',
            'Almacen': 'Nuevo almacén'
        }

class ModificarIngreso(forms.ModelForm):
    class Meta:
        model = Ingreso
        fields = ['Emisor', 'TipoI', 'CantI' ]
        labels = {
            'Emisor': 'Nuevo remitente',
            'TipoI': 'Nueva fecha',
            'CantI': 'Nueva cantidad'
        }
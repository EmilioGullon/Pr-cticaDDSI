from django import forms
from app.models import Nomina_tiene

class CrearNomina(forms.ModelForm):
    class Meta:
        model = Nomina_tiene
        fields = ['Nomina', 'Bruto', 'Impuesto', 'DNIE']
        labels = {
            'Nomina': 'Código',
            'Bruto': 'Bruto',
            'Impuesto': 'Impuesto',
            'DNIE': 'DNI',
        }
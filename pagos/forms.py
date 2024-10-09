from django import forms
from .models import Pago

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = ['cronogramaAlumno', 'referencia_pago', 'valor_pagado']


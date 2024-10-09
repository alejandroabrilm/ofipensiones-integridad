from django import forms
from .models import CronogramaAlumno

class CronogramaForm(forms.ModelForm):
    class Meta:
        model = CronogramaAlumno
        fields = '__all__'

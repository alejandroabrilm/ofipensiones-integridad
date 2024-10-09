from django.db import models
from instituciones.models import Institucion

class Curso(models.Model):
    grado = models.CharField(max_length=5)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, null=True)
    anio = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        institucion_nombre = self.institucion.nombre if self.institucion else "Sin Institución"
        return f'{self.grado} - {institucion_nombre}'

from django.db import models

from cursos.models import Curso

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    documentoIdentidad = models.CharField(max_length=20, primary_key=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre if self.nombre else "Sin Nombre"

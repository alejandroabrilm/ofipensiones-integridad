from django.db import models

from cursos.models import Curso

class Alumno(models.Model):
    nombre = models.CharField(max_length=255)
    documentoIdentidad = models.IntegerField(primary_key=True)
    curso = models.ManyToManyField(Curso)

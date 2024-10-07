from django.db import models

class Curso(models.Model):
    grado = models.CharField(max_length=5)
    grupo = models.CharField(max_length=5)
    jornada = models.CharField(max_length=15)

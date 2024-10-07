from django.db import models

from alumnos.models import Alumno

class CronogramaAlumno(models.Model):
    CONCEPTOS=(
        ('Matricula','Matricula'),
        ('Pension','Pension'),
        ('Otro Pago','Otro Pago')
    )
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, default=None)
    concepto = models.CharField(max_length=9, choices=CONCEPTOS)
    mes = models.CharField(max_length=10)
    valor = models.DecimalField

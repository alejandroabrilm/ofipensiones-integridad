from django.db import models
from cronogramasAlumnos.models import CronogramaAlumno

class Pago(models.Model):
    cronogramaAlumno = models.ForeignKey(CronogramaAlumno, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    referencia_pago = models.CharField(max_length=255)
    valor_pagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Pago {self.referencia_pago} - {self.cronogramaAlumno.alumno.nombre}'
    
    def save(self, *args, **kwargs):
        # Al realizar un pago, marcar como pagado en el cronograma
        cronograma = self.cronogramaAlumno
        cronograma.pagado = True
        cronograma.save()
        super().save(*args, **kwargs)

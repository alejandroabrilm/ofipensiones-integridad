from django.db import models

from alumnos.models import Alumno

class CronogramaAlumno(models.Model):
    CONCEPTOS=(
        ('matricula','Matricula'),
        ('pension','Pension'),
        ('otros','Otro Pago')
    )
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    concepto = models.CharField(max_length=20, choices=CONCEPTOS)
    mes = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2, null = True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.concepto} - {self.mes} - {self.alumno.nombre}'
    
    @property
    def esta_pendiente(self):
        return not self.pagado

from django.db import models

class Institucion(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email_contacto = models.EmailField()

    def __str__(self):
        return self.nombre if self.nombre else "Sin Nombre"

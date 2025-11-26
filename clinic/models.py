from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    peso_kg = models.FloatField()
    nombre_duenio = models.CharField(max_length=100)
    telefono_duenio = models.CharField(max_length=50)
    email_duenio = models.EmailField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

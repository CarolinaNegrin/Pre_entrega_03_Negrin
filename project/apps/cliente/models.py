from django.db import models

# Create your models here.

class Ciudad(models.Model):
    nombre = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nacimiento = models.DateField(null=True)
    contacto = models.CharField(max_length=25)
    ciudad_id = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True, blank=True)
    domicilio = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
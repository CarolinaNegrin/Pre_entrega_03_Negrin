from django.db import models

# Create your models here.

class Ciudad:
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Domicilio:
    ciudad = models.ForeignKey(Ciudad,on_delete=models.SET_NULL, null=True, blank=True)
    barrio = models.CharField(max_length=25)
    calle = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.ciudad}, {self.barrio}, {self.calle}"

class Cliente:
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    nacimiento = models.DateField(null=True)
    contacto = models.CharField(max_length=25)
    domicilio = models.ForeignKey(Domicilio,on_delete=models.SET_NULL, null=True, blank=True)
    numero = models.CharField(max_length=25)
    def __str__(self):
        return f"{self.apellido}, {self.nombre}"
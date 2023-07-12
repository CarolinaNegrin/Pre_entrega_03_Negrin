from django.db import models
from cliente.models import Cliente
from producto.models import Producto
# Create your models here.

class Vender (models.Model):
    carrito = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Producto: {self.carrito.nombre}, Cliente: {self.cliente}, Total ${self.carrito.precio}"
    
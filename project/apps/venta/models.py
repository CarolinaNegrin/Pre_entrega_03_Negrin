from django.db import models
from cliente.models import Cliente
from producto.models import Producto
# Create your models here.

class vender (models.Model):
    carrito = Producto
    ...
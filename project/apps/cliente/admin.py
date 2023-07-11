from django.contrib import admin
from django.db import models
from .models import Cliente, Domicilio, Ciudad
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Domicilio)
admin.site.register(Ciudad)
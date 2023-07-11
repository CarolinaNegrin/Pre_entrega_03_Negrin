from django.contrib import admin
from django.db import models
from .models import Cliente, Ciudad
# Register your models here.

admin.site.register(Cliente)

admin.site.register(Ciudad)
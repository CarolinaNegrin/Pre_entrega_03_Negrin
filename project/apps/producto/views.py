from django.shortcuts import render
from .models import Producto
from datetime import date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import ProductoForm
# Create your views here.

def home_productos(request):
    productos_registros = Producto.objects.all()
    contexto = {"productos": productos_registros}
    return render(request, "producto/index.html", contexto)

def registrar_producto (request: HttpRequest) -> HttpResponse:
    form = ProductoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("producto:home_productos")
    else:  # request.method == "GET"
        form = ProductoForm()
    return render(request, "producto/nuevoproducto.html", {"form": form})
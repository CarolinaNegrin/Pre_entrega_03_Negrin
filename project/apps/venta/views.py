from django.shortcuts import render
from .models import Vender
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import VentaForm
# Create your views here.

def home (request):
    ventas_registradas = Vender.objects.all()
    contexto = {"ventas": ventas_registradas}
    return render(request, "venta/index.html", contexto)

def NuevaVenta (request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("venta:home")
    else:  # request.method == "GET"
        form = VentaForm()

    return render(request, "venta/nuevaventa.html", {"form": form})
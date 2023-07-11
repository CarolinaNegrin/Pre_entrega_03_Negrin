from django.shortcuts import render
from .models import Cliente, Ciudad
from datetime import date
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .forms import ClienteForm


# Create your views here.
def home(request):
    clientes_registros = Cliente.objects.all()
    contexto = {"clientes": clientes_registros}
    return render(request, "cliente/index.html", contexto)

def crear_cliente(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:home")
    else:  # request.method == "GET"
        form = ClienteForm()

    return render(request, "cliente/nuevocliente.html", {"form": form})


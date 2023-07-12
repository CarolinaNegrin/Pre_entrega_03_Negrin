from django import forms

from .models import Vender


class VentaForm(forms.ModelForm):
    class Meta:
        model = Vender
        fields = ["carrito", "cliente"]
    
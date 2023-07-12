from django.urls import path
from .views import home, NuevaVenta

app_name = 'venta'

urlpatterns = [
    path('', home, name='home'),
    path('nuevaventa/', NuevaVenta, name='nuevaventa')
   
]
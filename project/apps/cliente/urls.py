from django.urls import path
from .views import home, crear_cliente

app_name = 'cliente'

urlpatterns = [
    path('', home, name='home'),
    path('nuevocliente/', crear_cliente, name='nuevocliente'),
   
]
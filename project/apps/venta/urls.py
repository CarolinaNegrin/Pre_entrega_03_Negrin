from django.urls import path
from .views import home

app_name = 'venta'

urlpatterns = [
    path('', home, name='home'),

   
]
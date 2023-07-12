from django.urls import path
from .views import home_productos, registrar_producto
app_name = 'producto'

urlpatterns = [
    path('home/', home_productos, name='home'),
    path('nuevoproducto', registrar_producto, name='nuevoproducto'),
   
]
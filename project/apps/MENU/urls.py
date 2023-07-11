from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

from .views import index

app_name = "HOME"

urlpatterns = [
    path("", index, name="index"),

]

urlpatterns += staticfiles_urlpatterns()
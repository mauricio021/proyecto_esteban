from django.urls import path
from . import views

app_name = "cliente"

urlpatterns = [
    path('', views.home, name="index"),
    path("crear_clientes", views.crear_clientes,),
    path("busqueda/", views.busqueda),
    path("crear/", views.crear)
]


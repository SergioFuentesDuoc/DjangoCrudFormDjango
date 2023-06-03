from django.urls import path
from .views import home, form_vehiculo, form_mod_vehiculo,listar_mod_vehiculo

urlpatterns = [
    path('', home, name="home"),
    path('form_vehiculo', form_vehiculo, name="form_vehiculo"),
    path('form_mod_vehiculo<id>', form_mod_vehiculo, name="form_mod_vehiculo"),
    path('listar_mod_vehiculo', listar_mod_vehiculo, name="listar_mod_vehiculo"),
]

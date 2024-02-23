from django.contrib import admin
from django.urls import path
from Adso.views import *
from django.urls import path
import os
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo', saludo),
    path('edad/<int:ano>', calcular_edad),
    path('msg_saludo', msg_saludo),
    path('accounts/',include('django.contrib.auth.urls')),
    path('crud/',crud),
    path('registro/',registro),
    path('logueo2/', logueo2),
  

    #//////RUTAS DEL CRUD DE CREACIÓN Y LOGIN    ////
    path('crear/', crear_usuario),
    path('logueo/', logueo),
    path('valida_logueo/', valida_logueo)    
    #//////////////////// -->



]

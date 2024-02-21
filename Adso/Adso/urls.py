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
    # FORMA 1
    path('crear/', crear_usuario),
    path('accounts/',include('django.contrib.auth.urls')),
    path('registro/',registro)

    
    # FORMA 2
    # path('registro/', registro),
    



]

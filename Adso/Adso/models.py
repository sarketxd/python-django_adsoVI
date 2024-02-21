from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=7)

class Articulos(models.Model):
    nombre = models.CharField(max_length=30)
    seccion = models.CharField(max_length=30)
    precio = models.CharField(max_length=7)

class Pedidos(models.Model):
    nombre = models.CharField(max_length=30)  # Agrega max_length aquí
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=7)  # Agrega max_length aquí

class Usuario(models.Model):
    nombre = models.CharField(max_length=50, db_collation='utf8mb4_general_ci', blank=True, null=True)
    apellidos = models.CharField(max_length=100, db_collation='utf8mb4_general_ci', blank=True, null=True)
    password = models.CharField(max_length=254)

    class Meta:
        #managed = False
        db_table = 'usuario'
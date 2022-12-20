from django.db import models

# Create your models here.
class jugadores(models.Model):
    nombre = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    puesto = models.CharField(max_length=20)
    camiseta = models.IntegerField()


class goles(models.Model):
    nombre = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    goles = models.IntegerField()

class partidos(models.Model):
    rival = models.CharField(max_length=50)
    instancia = models.CharField(max_length=50)
    resultado = models.CharField(max_length=25)
    

class tecnicos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rol = models.CharField(max_length=25)
    
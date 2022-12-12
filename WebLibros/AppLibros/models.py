from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CienciaFiccion(models.Model):
    titulo = models.CharField(max_length=255)
    autor  = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=2000)
    publicacion = models.DateField()
    url_portada = models.CharField(max_length=255)
    publicacion_en_foro = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return f"{self.titulo}, {self.autor}"

class Terror(models.Model):
    titulo = models.CharField(max_length=255)
    autor  = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=2000)
    publicacion = models.DateField()
    url_portada = models.CharField(max_length=255)
    publicacion_en_foro = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return f"{self.titulo}, {self.autor}"

class Distopia(models.Model):
    titulo = models.CharField(max_length=255)
    autor  = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=2000)
    publicacion = models.DateField()
    url_portada = models.CharField(max_length=255)
    publicacion_en_foro = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return f"{self.titulo}, {self.autor}"

class Fantasia(models.Model):
    titulo = models.CharField(max_length=255)
    autor  = models.CharField(max_length=40)
    sinopsis = models.CharField(max_length=2000)
    publicacion = models.DateField()
    url_portada = models.CharField(max_length=255)
    publicacion_en_foro = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return f"{self.titulo}, {self.autor}"


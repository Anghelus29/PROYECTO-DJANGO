from django.db import models
from .validators import validation_paginas
from .validators import validation_edad



class Autores(models.Model):
    nombre = models.CharField(max_length=50)
    nacimiento = models.DateField(max_length=50)
    edad = models.IntegerField(validators=[validation_edad,])
    cantidad_libros = models.IntegerField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id_autor=models.ForeignKey(Autores, on_delete=models.CASCADE)
    nombre = models.TextField()
    paginas = models.IntegerField(validators=[validation_paginas,])
    editorial = models.CharField(max_length=70)
    created= models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.TextField()
    horario_atencion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Biblioteca_libro(models.Model):
    disponible = models.CharField(max_length=2)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    def __str__(self):
        return self.disponible
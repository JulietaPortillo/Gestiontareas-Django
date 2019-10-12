from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    estado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Comunidad(models.Model):
    Nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre

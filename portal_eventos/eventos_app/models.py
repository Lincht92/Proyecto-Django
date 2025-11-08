from django.db import models
from django.contrib.auth.models import User

#Para interactura con el ORM
class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=200)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eventos')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

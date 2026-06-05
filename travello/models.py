from django.db import models

class DestinosTuristicos(models.Model):
    nombreCiudad = models.CharField(max_length=100)
    descripcionCiudad = models.TextField()
    imagenCiudad = models.ImageField(upload_to='fotos_destinos/')
    precioTour = models.IntegerField()
    ofertaTour = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreCiudad
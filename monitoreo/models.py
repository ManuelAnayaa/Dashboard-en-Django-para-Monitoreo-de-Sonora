from django.db import models

class DatoSensor(models.Model):
    municipio = models.CharField(max_length=100)
    tipo_dato = models.CharField(max_length=50)  # Ejemplo: temperatura, humedad
    valor = models.FloatField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.municipio} - {self.tipo_dato}: {self.valor}"

    class Meta:
        ordering = ['-fecha_registro']
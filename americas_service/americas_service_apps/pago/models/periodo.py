from django.db import models


class Periodo(models.Model):

    estado = models.BooleanField(default=True)
    fecha = models.DateField()

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

    def __str__(self):
        return '%s' % (self.fecha)

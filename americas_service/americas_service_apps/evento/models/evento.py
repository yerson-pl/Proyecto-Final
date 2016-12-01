from django.db import models


class Evento(models.Model):

    nombre = models.CharField(max_length=200)
    # descripcion = models.TextField(max_length=500, null=True, blank=True)
    fecha = models.DateField()
    hora = models.TimeField()

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return '%s' % (self.nombre)


class TimeStampModel(models.Model):

    creacion = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "TimeStampModel"
        verbose_name_plural = "TimeStampModels"

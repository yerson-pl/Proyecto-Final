from django.db import models
from americas_service_apps.asociacion.models.socio_lote import SocioLote
from .cuota import Cuota


class CuotaSocio(models.Model):

    socio = models.OneToOneField(SocioLote)
    cuota = models.ManyToManyField(Cuota)

    class Meta:
        verbose_name = "CuotaSocio"
        verbose_name_plural = "CuotaSocios"

    def __str__(self):
        return '%s %s' % (self.socio, self.cuota)

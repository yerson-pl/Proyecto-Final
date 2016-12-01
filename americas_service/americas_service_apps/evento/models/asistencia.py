from django.db import models

from americas_service_apps.asociacion.models.socio_lote import SocioLote
from .evento import Evento, TimeStampModel


class Asistencia(TimeStampModel):

    evento = models.ForeignKey(Evento)
    socio_lote = models.ForeignKey(SocioLote)
    dni_representante = models.CharField(max_length=8, null=True, blank=True)
    estado = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Asistencia"
        verbose_name_plural = "Asistencias"
        permissions = (
            ('list_asistencia', 'Can list categoria'),
            ('get_asistencia', 'Can get asistencia'),
        )

    def __str__(self):
        return self.dni_representante

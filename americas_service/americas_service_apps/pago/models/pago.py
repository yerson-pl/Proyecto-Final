from django.db import models
from americas_service_apps.evento.models.evento import Evento
from .periodo import Periodo


class Pago(models.Model):

    inasistencia = models.ForeignKey(Evento)
    periodo = models.ForeignKey(Periodo)
    fecha = models.DateTimeField()
    imagen = models.ImageField()
    monto = models.DecimalField(decimal_places=2, max_digits=5)
    num_recibo = models.CharField(max_length=50)
    validacion = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return '%s' % (self.fecha)

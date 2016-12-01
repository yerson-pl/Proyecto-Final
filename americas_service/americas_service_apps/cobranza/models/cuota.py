from django.db import models
from .rubro_cobranza import RubroCobranza
# from americas_service_apps.asociacion.models.InformacionLote import InformacionLote
from americas_service_apps.asociacion.models.lote import Lote


class Cuota(models.Model):

    lote = models.OneToOneField(Lote)
    rubro_cobranza = models.ForeignKey(RubroCobranza)
    # valor = models.DecimalField(
    #     decimal_places=2, max_digits=5, default=0.0)
    # area_lote = models.DecimalField(
    #    decimal_places=2, max_digits=5, default=0.0)
    cuota = models.DecimalField(
        decimal_places=2, max_digits=10, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.importe = self.rubro_cobranza.importe
        self.area_lote = self.lote.area_lote
        self.cuota = self.area_lote * self.importe
        return super(Cuota, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Cuota"
        verbose_name_plural = "Cuotas"

    def __str__(self):
        # return('{0}'.format(self.valor))
        return '%s %s' % (self.lote, self.cuota)

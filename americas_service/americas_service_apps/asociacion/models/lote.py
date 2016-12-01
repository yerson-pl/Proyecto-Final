from uuid import uuid4
# from datetime import datetime, timedelta
from django.db import models
from .manzana import Manzana
from django.utils.translation import ugettext_lazy as _
# models
# from .ArregloLote import ArregloLote


class Lote(models.Model):
    """
    Clase para crear la tabla Lote
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    manzana = models.ForeignKey(Manzana, null=False, blank=False)

    # iteracion_lote = models.ForeignKey(
    #     'self', related_name='asociacion', null=True, blank=True)
    # item = models.IntegerField(default=1, null=False, blank=False)
    lote = models.CharField(
        _('ingrese lote'), unique=True, max_length=3, null=False, blank=False)
    area_lote = models.DecimalField(
        _('area total'), null=False, blank=False,
        decimal_places=2, max_digits=5, default=0.0)
    # area_total = models.DecimalField(
    #     _('area total'), null=False, blank=False,
    #     decimal_places=2, max_digits=5, default=0.0)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"

    def __str__(self):
        return 'Mz-%s L-%s' % (self.manzana, self.lote)

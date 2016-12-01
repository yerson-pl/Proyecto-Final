
from uuid import uuid4
# from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext_lazy as _
# models
# from .ArregloManzana import ArregloManzana


class Manzana(models.Model):
    """
    Clase para crear la tabla Manzana
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # manzana = models.ForeignKey(
    #     'self', related_name='iteracion_manzana', null=True, blank=True)
    # item = models.IntegerField(default=1, null=False, blank=False)
    # manzana_id = models.AutoField(primary_key=True)
    manzana = models.CharField(_('ingrese manzana'), unique=True,
                               max_length=3, null=False, blank=False)
    # numero_lotes = models.PositiveSmallIntegerField(
    #     _('numero lotes'), default=1, blank=False, null=False)
    # arreglo_manzana = models.ForeignKey(ArregloManzana)

    class Meta:
        verbose_name = "Manzana"
        verbose_name_plural = "Manzanas"

    def __str__(self):
        return '%s' % (self.manzana)

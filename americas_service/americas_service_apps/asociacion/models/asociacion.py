from uuid import uuid4
# from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from .cuenta_banco import CuentaBanco
# from django.utils.text import capfirst, get_text_list


class Asociacion(models.Model):

    """
    Modelo Asociacion, corresponde a la tabla asosciacion
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    ruc = models.CharField(_('ruc'), unique=True, max_length=11, null=False)
    nombre = models.CharField(_('nombre asociacion'),
                              max_length=100, null=False)
    denominacion = models.CharField(
        _('denominacion asociacion'), max_length=150, null=True)
    cuenta_banco = models.OneToOneField(CuentaBanco,
                                        related_name='asociaciones')
    website = models.URLField(null=True, blank=True)
    logo = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    update_at = models.DateTimeField(
        _('update at'), auto_now=True)

    class Meta:
        verbose_name = _('asociacion')
        verbose_name_plural = _('asociaciones')

    def __str__(self):
        return self.ruc

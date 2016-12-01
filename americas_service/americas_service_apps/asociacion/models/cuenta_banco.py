# from uuid import uuid4
# from datetime import datetime
from django.db import models
# from .Banco import Banco
# from .TipoCuenta import TipoCuenta
# from americas_service_apps.asociacion.choices.enums import BANCO_CHOICES
# from americas_service_apps.asociacion.choices.enums import TIPO_CUENTA_CHOICES
# from django.utils.translation import ugettext_lazy as _
# from django.utils.text import capfirst, get_text_list


class CuentaBanco(models.Model):

    # id = models.UUIDField(primary_key=True, default=uuid4, editable=False)

    # entidad_bancaria = models.CharField(max_length=100, choices=BANCO_CHOICES)
    # entidad_bancaria = models.ForeignKey(Banco)
    entidad_bancaria = models.CharField(
        max_length=50, unique=True, blank=False, null=False)
    # tipo_cuenta = models.CharField(max_length=50, choices=TIPO_CUENTA_CHOICES)
    # tipo_cuenta = models.ForeignKey(TipoCuenta)
    tipo_cuenta = models.CharField(max_length=50, blank=False, null=False)
    numero_cuenta = models.CharField(
        max_length=50, unique=True, null=False, blank=False)

    class Meta:
        verbose_name = "Cuenta de banco"
        verbose_name_plural = "Cuentas de bancos"

    def __str__(self):
        return '%s - (%s)' % (self.entidad_bancaria, self.numero_cuenta)

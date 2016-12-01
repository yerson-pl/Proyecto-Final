from django.db import models
from americas_service_apps.cobranza.models.cuota_socio import CuotaSocio
from americas_service_apps.asociacion.models.cuenta_banco import CuentaBanco


class ValidarPago(models.Model):

    cuota_socio = models.ForeignKey(CuotaSocio)
    cuenta_banco = models.OneToOneField(CuentaBanco)
    importe_deposito = models.DecimalField(
        decimal_places=2, max_digits=5, null=False, blank=False)
    fecha_deposito = models.DateField()
    numero_operacion = models.CharField(max_length=50, null=False, blank=False)
    imagen_voucher = models.ImageField(blank=True)

    class Meta:
        verbose_name = "ValidarPago"
        verbose_name_plural = "ValidarPagos"

    def __str__(self):
        return '%s %s' % (self.cuenta_banco, self.cuenta_banco)

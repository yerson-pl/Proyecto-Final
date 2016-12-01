from django.db import models
# from americas_service_apps.utils.choices.Global import SELECT_SN_CHOICES
from .concepto_cobranza import ConceptoCobranza
# from .Mora import Mora


class RubroCobranza(models.Model):

    concepto = models.ForeignKey(ConceptoCobranza)
    rubro_cobranza = models.CharField(
        max_length=100, unique=True, null=False, blank=False)
    importe = models.DecimalField(
        decimal_places=2, max_digits=5, null=False, blank=False)
    con_mora = models.BooleanField(default=False)
    mora = models.DecimalField(
        decimal_places=2, max_digits=5, null=True, blank=True, default=0.0)
    detalle = models.TextField(max_length=500, null=True, blank=True)
    fecha_inicio = models.DateField(null=False, blank=False)
    dias = models.IntegerField(null=False, blank=False)

    class Meta:
        verbose_name = "Rubro de cobranza"
        verbose_name_plural = "Rubros de cobranza"

    def __str__(self):
        return 'Concepto - %s, Rubro %s, Importe S/ - %s, Mora - S/ %s' % (
            self.concepto.concepto_cobranza,
            self.rubro_cobranza,
            self.importe,
            self.mora)

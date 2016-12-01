from django.db import models
from americas_service_apps.cobranza.models.rubro_cobranza import RubroCobranza


class Debe(models.Model):

    codigo_deb = models.AutoField(primary_key=True)
    glosa_debe = models.OneToOneField(RubroCobranza)

    class Meta:
        verbose_name = "DEBE"
        verbose_name_plural = "DEBE"

    def __str__(self):
        return '%s' % (self.glosa_debe)

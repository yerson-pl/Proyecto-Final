from django.db import models


class Categoria(models.Model):

    nombre = models.CharField(max_length=300)
    detalle = models.TextField(max_length=600)
    importe_total = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return '%s %s' % (self.nombre, self.importe_total)

from django.db import models


class Haber(models.Model):

    class Meta:
        verbose_name = "HABER"
        verbose_name_plural = "HABER"

    def __str__(self):
        pass

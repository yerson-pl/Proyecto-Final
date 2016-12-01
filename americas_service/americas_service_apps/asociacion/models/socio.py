from django.db import models
from americas_service_apps.auths.models.person import Person
from americas_service_apps.auths.choices.enums import ESTADO_CIVIL_CHOICES
from americas_service_apps.auths.choices.enums import SELECT_SN_CHOICES
# from americas_service_apps.socio.models.Email import Email


class Socio(models.Model):

    persona = models.OneToOneField(Person)
    estado_civil = models.CharField(
        max_length=20, choices=ESTADO_CIVIL_CHOICES, null=False, blank=False)
    conyuge = models.OneToOneField(
        'self', related_name='socio', null=True, blank=True)
    domicilio = models.CharField(max_length=300, null=True, blank=True)
    procedencia = models.CharField(max_length=50, null=True, blank=True)
    celular = models.CharField(max_length=30, null=True, blank=True)
    telefono = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    # email = models.OneToOneField(Email, null=False, blank=False)
    residencia_juliaca = models.CharField(
        max_length=2, choices=SELECT_SN_CHOICES)
    is_adventista = models.CharField(
        max_length=2, choices=SELECT_SN_CHOICES)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def __str__(self):
        return '%s %s - (%s)' % (
            self.persona.first_name,
            self.persona.last_name,
            self.persona.documento_identidad)

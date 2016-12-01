from django.contrib import admin

from .models.pago import Pago
from .models.periodo import Periodo
from .models.validar_pago import ValidarPago

admin.site.register(Pago)
admin.site.register(Periodo)
admin.site.register(ValidarPago)

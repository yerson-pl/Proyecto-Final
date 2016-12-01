from django.contrib import admin
from .models.asistencia import Asistencia
from .models.evento import Evento
from .models.inasistencia import Inasistencia
# Register your models here.

admin.site.register(Asistencia)
admin.site.register(Evento)
admin.site.register(Inasistencia)

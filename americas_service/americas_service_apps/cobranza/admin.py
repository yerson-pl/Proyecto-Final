from django.contrib import admin
# from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .models.rubro_cobranza import RubroCobranza
from .models.concepto_cobranza import ConceptoCobranza
# from .models.Debe import Debe
from .models.cuota import Cuota
from .models.cuota_socio import CuotaSocio
from .models.categoria import Categoria
# from .models.ValidarPago import ValidarPago

admin.site.register(RubroCobranza)
admin.site.register(ConceptoCobranza)
# admin.site.register(Debe)
admin.site.register(Cuota)
admin.site.register(CuotaSocio)
# admin.site.register(ValidarPago)
admin.site.register(Categoria)

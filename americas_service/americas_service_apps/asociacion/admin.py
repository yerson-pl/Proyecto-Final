from django.contrib import admin
# from django.contrib.contenttypes.models import ContentType

# Register your models here.
from .models.asociacion import Asociacion
from .models.lote import Lote
from .models.manzana import Manzana
from .models.cuenta_banco import CuentaBanco
# from .models.InformacionLote import InformacionLote
from .models.socio import Socio
from .models.socio_lote import SocioLote
# from .models.Banco import Banco
# from .models.TipoCuenta import TipoCuenta

# admin.site.register(ContentType)


class AsociacionAdmin(admin.ModelAdmin):

    list_display = ('ruc', 'nombre', 'denominacion', 'cuenta_banco', 'website')


class LoteInline(admin.TabularInline):
    model = Lote
    extra = 1


class ManzanaAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['manzana']}), ]
    inlines = [LoteInline]


admin.site.register(Asociacion, AsociacionAdmin)
admin.site.register(Lote)
admin.site.register(Manzana, ManzanaAdmin)
# admin.site.register(ManzanaLote)
admin.site.register(CuentaBanco)
# admin.site.register(RelacionManzanaLote, RelacionManzanaLoteAdmin)
# admin.site.register(RelacionManzanaLote)
# admin.site.register(InformacionLote)
admin.site.register(Socio)
admin.site.register(SocioLote)
# admin.site.register(Banco)
# admin.site.register(TipoCuenta)

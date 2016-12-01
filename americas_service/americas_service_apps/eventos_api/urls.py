from django.conf.urls import url, include
from rest_framework import routers

from .views.inasistencia import InasistenciaViewSet
from .views.evento import EventoViewSet
from .views.asistencia import AsistenciaViewSet

router = routers.DefaultRouter()

router.register(r'inasistencias', InasistenciaViewSet)
router.register(r'eventos', EventoViewSet, 'evento-view')
router.register(r'asistencias', AsistenciaViewSet, 'asistencia-view')

urlpatterns = [
    url(r'^', include(router.urls)),
]
